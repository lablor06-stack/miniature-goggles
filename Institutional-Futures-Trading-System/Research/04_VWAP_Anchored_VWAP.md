# 04 — VWAP & Anchored VWAP

> Il VWAP è l'unico livello del sistema di cui è **documentato** l'uso istituzionale diretto:
> è il benchmark standard di esecuzione (E1). Questo lo rende qualitativamente diverso da ogni
> altro riferimento: non "funziona perché lo guardano i trader", funziona perché **misura il
> prezzo medio pagato dai partecipanti** nel periodo ancorato.

---

## 1. Teoria

### 1.1 Definizione

`VWAP_t = Σ(P_i × V_i) / Σ(V_i)` per i = inizio ancoraggio … t, con P tipicamente hlc3.

- **Session VWAP:** ancorato all'apertura del trading day CME (18:00 ET). Variante RTH-only
  (ancora 09:30) per la lettura del flusso cash — il sistema le traccia entrambe, con la
  session come primaria e la RTH come secondaria.
- **Bande:** ±1σ, ±2σ dove σ è la deviazione standard *pesata per volume* del prezzo attorno
  al VWAP (non ATR, non stdev semplice — coerente con la definizione).
- **AVWAP:** stesso calcolo, ancoraggio a un evento scelto: open settimanale/mensile, swing
  high/low rilevante (origine del dealing range), giorno di news, MSS maggiore.

### 1.2 Perché è rilevante (meccanismo)

1. **Benchmark di esecuzione:** i desk vengono valutati contro il VWAP (E1: Berkowitz, Logue &
   Noser 1988; Madhavan 2002). Un buy program "in ritardo" sul VWAP tende ad accelerare gli
   acquisti quando il prezzo torna sotto/al VWAP → domanda reale su quel livello.
2. **Inventory reference:** il VWAP di un periodo è il prezzo medio dell'inventory accumulata
   in quel periodo. AVWAP da uno swing low = prezzo medio dei compratori da quel minimo: la sua
   perdita significa che *l'intera posizione media è in perdita* → cambio di regime psicologico
   e di flusso (stop-out dei ritardatari).
3. **Focal point:** è su ogni terminale istituzionale → coordinamento.

### 1.3 Letture operative

| Situazione | Lettura | Uso nel sistema |
|---|---|---|
| Prezzo sopra VWAP in salita, VWAP inclinato | Long inventory in controllo | Filtro direzione Setup B long |
| Prezzo oscilla attraverso VWAP piatto | Balance | Regime range → Setup A agli estremi |
| Primo pullback al VWAP dopo displacement | Punto di ricarico algo | Confluenza d'ingresso B |
| Estensione a ±2σ con delta in esaurimento | Eccesso statistico di sessione | Contesto per fade (solo con trigger di struttura) |
| AVWAP dallo swing d'origine del trend perso con displacement | L'inventory del trend è underwater | Conferma di MSS maggiore |
| Compressione prezzo tra VWAP session e AVWAP HTF (pinch) | Decisione imminente | Alert di attenzione, no trade dentro il pinch |

---

## 2. Vantaggi

- **Razionale E1** (unico nel toolkit) + calcolo deterministico, zero parametri discrezionali
  (dato l'ancoraggio).
- Auto-adattivo al volume: nelle ore morte si muove poco, nelle kill zone incorpora
  l'informazione in fretta.
- Le bande σ forniscono una **misura di estensione di sessione** normalizzata e confrontabile
  tra giornate (a differenza dei punti fissi).
- L'AVWAP trasforma un principio vago ("i livelli importanti") in una **famiglia parametrica
  disciplinata**: si ancora a eventi definiti, non a piacere.

## 3. Svantaggi e limiti

- **Lag strutturale:** media cumulativa → tardo pomeriggio si muove pochissimo; le letture di
  fine giornata vanno fatte con le bande, non col VWAP stesso.
- La scelta dell'ancora AVWAP reintroduce discrezionalità → serve la lista chiusa di ancore
  autorizzate (fatta: §1.1; enforcement nella checklist).
- In trend day forte il "fade della 2σ" perde sistematicamente: le bande diventano canale di
  tendenza, non elastico. Serve il day-type filter.
- Su Globex notturno il volume è scarso: il session VWAP delle 03:00 è dominato da poche ore
  sottili (per questo il sistema legge il London contro AVWAP settimanale/naked levels, non
  contro la sola session).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| VWAP è il benchmark di esecuzione standard; gli algo VWAP/POV rappresentano quota rilevante del flusso istituzionale | Berkowitz et al. (1988); Madhavan (2002); survey sui transaction cost | **E1** |
| Reversione verso VWAP dopo estensioni in giornate balance | Coerente con letteratura mean-reversion intraday; replicabile | **E2** (da produrre con la pipeline) |
| Prima visita al VWAP dopo impulso = continuazione più probabile del breakdown | Folklore practitioner strutturato (Brian Shannon) con logica inventory | **E3** |
| AVWAP da eventi (earnings/news/swing) come supporto/resistenza | Shannon (practitioner, sistematizzato); nessun paper dedicato | **E3** |
| "Il VWAP viene sempre ritestato in giornata" | Falso come regola; vero solo in % misurabile | **E4** come assoluto |

## 5. Contesti favorevoli

- Giornate balance/rotazionali: VWAP piatto = asse della rotazione (fade degli estremi σ con
  trigger).
- Trend day *ordinato*: pullback al VWAP/1σ = zona Setup B ad alta qualità.
- AVWAP da swing d'origine di un movimento su HTF: riferimento di bias eccellente per giorni.
- Conflitto/convergenza fra VWAP session e AVWAP settimanale: mappa dei "muri" di inventory.

## 6. Contesti sfavorevoli

- Post-gap enorme: il VWAP di sessione parte "vergine" e per ore non rappresenta nessuna
  inventory significativa.
- Bassa liquidità (notte, festivi): media dominata da rumore.
- News tier-1 imminenti: l'inventory pre-news non vincola il prezzo post-news.

## 7. Errori comuni

1. Fade automatico della banda 2σ senza chiedersi *che giornata è* (nei trend day è suicida).
2. Ancorare l'AVWAP a eventi arbitrari finché non "supporta" il proprio bias (cherry-picking) —
   l'antidoto è la lista chiusa di ancore.
3. Usare bande ATR o stdev non pesata e chiamarle "bande VWAP".
4. Confondere il VWAP con un supporto "magico": è un riferimento di *flusso*; senza contesto
   (trend/balance) non implica nulla.
5. Ignorare la differenza session/RTH quando si ragiona sul flusso cash.

## 8. Miglioramenti proposti (IFTS)

- **Lista chiusa di ancore AVWAP** (5): weekly open, monthly open, ultimo swing esterno H/L del
  dealing range, ultimo MSS maggiore HTF, ultimo evento news tier-1. Qualunque altra ancora è
  vietata → riproducibilità.
- **Doppio VWAP (session + RTH)** con priorità dichiarata, per evitare letture miste.
- **σ-position in dashboard:** la posizione corrente in unità σ (es. +1.4σ) è un dato di
  contesto sintetico e confrontabile → registrato nel journal per analisi successive
  (es. expectancy dei Setup A aperti oltre ±1.5σ).
- Bande calcolate correttamente volume-weighted nel Pine (molte implementazioni pubbliche sono
  sbagliate su questo punto).

## 9. Implicazioni per il sistema

1. VWAP/AVWAP sono **filtri e confluenze, mai trigger**: aumentano/riducono il grade del setup
   (A+, A, B) secondo la matrice di confluenza del Core Model.
2. La σ-position entra tra i campi del journal → dopo 100+ trade dirà se pagare di più i setup
   "in estensione" o "a valore" (research question RQ-4).
3. Nel Pine: modulo `VWAP Suite` con session/RTH VWAP + bande 1-2σ + max 3 AVWAP simultanei
   dalla lista autorizzata (2 automatici: weekly, monthly; 1 manuale a click/timestamp).
