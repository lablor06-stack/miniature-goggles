# 07 — Liquidità: Pool, Sweep, Interna/Esterna, EQH/EQL, Inducement

> Se la struttura è la sintassi, la liquidità è la **semantica**: spiega *perché* il prezzo va
> dove va. La tesi centrale del sistema — il prezzo si muove da pool a pool — vive qui.

---

## 1. Teoria

### 1.1 Tassonomia dei pool (gerarchia IFTS, dal più pesante al più leggero)

| Rank | Pool | Perché pesa |
|---|---|---|
| 1 | **PWH/PWL** (settimana prec.) | Riferimento di ogni desk multi-day; stop swing + breakout order |
| 2 | **PDH/PDL** (giorno prec.) | Il riferimento intraday universale |
| 3 | **Estremi di sessione** (Asia H/L, London H/L, ONH/ONL) | Stop dei trader di sessione; primo carburante NY |
| 4 | **EQH/EQL** (P3: entro 0.10×ATR14) | Liquidità "ingegnerizzata": doppi massimi/minimi da manuale attirano sia stop sia breakout |
| 5 | **Swing esterni recenti** | Stop strutturali |
| 6 | **Numeri tondi** (x000/x500 su NQ, x00/x50 su ES) | Clustering cognitivo (E1, Osler) |
| 7 | Swing interni, wick prominenti | Micro-pool per il timing d'ingresso |

**Liquidità esterna** = pool oltre gli estremi del dealing range. **Liquidità interna** =
inefficienze *dentro* il range (FVG, OB non mitigati). Ciclo canonico:
**esterna → (MSS) → interna → esterna opposta.** Il sistema entra dopo il raid dell'esterna,
usa l'interna come stazioni intermedie di gestione, e targhetta l'esterna opposta.

### 1.2 Anatomia dello sweep (P6)

Sweep valido = **wick oltre il pool + close di ritorno sotto/sopra il livello entro 3 barre.**

Tre esiti dopo la violazione di un pool, mutuamente esclusivi e diagnostici:

1. **Sweep-and-reverse:** ritorno immediato → era liquidity grab; se segue MSS → Setup A.
2. **Sweep-and-go (espansione):** accettazione oltre (close multipli, value migra) → era
   repricing; il livello violato diventa supporto/resistenza per Setup B.
3. **Grind-through:** violazione lenta senza displacement né rejection → nessuna informazione,
   nessun trade (il caso più frequente nel lunch).

Qualificatori di qualità dello sweep (usati per il grading):
- **Profondità:** 0.1–0.5 × ATR14 oltre il pool = ideale (cattura stop, non repricing);
  oltre 1 × ATR = sospetta espansione.
- **Velocità di ritorno:** entro 1-3 barre (LTF) = rigetto vero; excess/coda visibile.
- **Pool multipli:** raid che prende *in un colpo* PDL + London low + EQL = massima qualità
  (più carburante consumato, meno benzina sotto).
- **Tempo:** dentro KZ (il meccanismo richiede partecipazione — `01_Microstructure` §5/6).

### 1.3 Inducement (IDM)

Pool *interno* creato dal primo pullback dopo un impulso: gli ingressi anticipati vi
parcheggiano stop che verranno spazzati prima del movimento vero. Uso IFTS (conservativo): dopo
un MSS, se esiste un IDM ovvio tra il prezzo e la zona d'ingresso (FVG/OB), **attendere il suo
sweep** prima di considerare l'ingresso maturo — riduce gli stop-out "di un tick".

### 1.4 Draw on Liquidity (DOL)

Il pool opposto più probabile come destinazione. Selezione IFTS (deterministica, non a
sentimento): il pool di rank più alto NON ancora preso **nella direzione del bias HTF**, entro
1.5 × ADR dalla posizione corrente. Se non esiste → niente narrativa → NT (no-trade).

---

## 2. Vantaggi

- Dà al sistema **target oggettivi** (il DOL) e quindi R:R calcolabili *prima* dell'ingresso —
  requisito P12 (R:R ≥ 2) verificabile ex-ante.
- Lo sweep è l'evento **più leggibile** del vocabolario: wick+ritorno si vede uguale su ogni
  chart, senza parametri estetici.
- La gerarchia dei pool struttura il pre-market: la mappa dei livelli è una checklist, non
  un'opinione.

## 3. Svantaggi e limiti

- I pool sono **presunti**: non vediamo gli stop reali (solo MBO li mostrerebbe). L'inferenza
  "estremo visibile ⇒ stop" è robusta in aggregato (E1 su FX) ma fallibile sul singolo evento.
- **Ambiguità multi-pool:** quando sopra ci sono 4 pool ravvicinati, quale è IL target? La
  regola del rank + 1.5×ADR riduce ma non elimina la discrezionalità.
- Il lato psicologico: aspettare lo sweep significa *non* comprare il minimo "che si vede" —
  molti trade mancati per un tick. È un costo strutturale accettato (il sistema paga selettività
  per qualità).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Stop clusterizzati oltre estremi visibili e numeri tondi; le cascate producono reversal a breve in assenza di news | Osler (2003, 2005) — FX, dati ordini reali | **E1** (FX) / **E3** (indici, transfer) |
| Falsi breakout di massimi/minimi n-day: edge storico documentato del fade | Connors & Raschke, *Street Smarts* (1995, Turtle Soup) — regole pubblicate, backtestabili | **E2** storico (edge da riverificare oggi) |
| Doppi massimi/minimi (EQH/EQL) vengono violati prima di un'inversione più spesso che tenere | Ipotesi ICT centrale; misurabile con P3 | **E3 → RQ-2** (modulo Statistics) |
| "Ogni old high/low viene SEMPRE preso" | Falso: orizzonte indefinito rende il claim non falsificabile | **E4** come formulato; utilizzabile solo con orizzonte (es. % di PDH/PDL presi entro la settimana — misurabile) |
| Il primo movimento post-open spesso inverte (Judas) | Vedi `11_Sessions` §4 | **E3** |

## 5. Contesti favorevoli

- **Pre-NY con overnight compresso** dentro il range di ieri: pool freschi e vicini su entrambi
  i lati, raid mattutino quasi garantito da un lato → il pane del Setup A.
- Bias HTF chiaro + pool contro-bias appena preso = ingresso pro-bias con carburante davanti.
- EQH/EQL formati in Asia/London e presi in NY AM.

## 6. Contesti sfavorevoli

- **Trend day:** i pool contro-trend vengono presi *e accettati* (sweep-and-go); il fade
  sistematico dei raid in trend day è il modo più rapido di violare lo stop giornaliero.
- News tier-1: la violazione è repricing (vedi `01` §6).
- Pool troppo lontani (> 1.5×ADR): narrativa "a target impossibile" → NT.
- Venerdì pomeriggio / vigilie: i pool restano lì fino a lunedì.

## 7. Errori comuni

1. Vedere "liquidity grab" in ogni wick: senza pool di rank ≥ 4 e senza KZ non è un segnale.
2. Entrare sul tocco del pool *prima* dello sweep confermato (anticipare il meccanismo).
3. Ignorare il lato opposto: preso il PDL, il target è il pool sopra — ma se sopra non c'è
   nulla entro l'ADR, il trade non ha benzina.
4. Contare come sweep le violazioni con accettazione (esito 2) e farsi male in fade.
5. Muovere il DOL intra-trade per avidità ("adesso punto al PWH") senza regola.

## 8. Miglioramenti proposti (IFTS)

- **Definizione P6 testabile** (wick + ritorno ≤ 3 barre) al posto del "si vede che è un grab"
  — rende lo sweep un *evento* loggabile e contabile.
- **Grading dello sweep** (profondità/velocità/pool multipli/KZ) con punteggio 0-4 nella
  dashboard → il journal misurerà la relazione grade↔esito (RQ-2).
- **Regola DOL deterministica** (rank + direzione bias + 1.5×ADR) — sostituisce la narrativa
  libera con una selezione riproducibile.
- **IDM-wait opzionale** (§1.3) per gli ingressi su zona.

## 9. Implicazioni per il sistema

1. Il Setup A è definito *dalla* liquidità: niente sweep di pool rank ≥ 4 → niente trade,
   qualunque cosa "sembri" fare il grafico.
2. La mappa dei pool è il primo output del pre-market (Manual/01) e il modulo Liquidity del
   Pine la disegna e la aggiorna (stato: intatto / sweep / accettato).
3. Target del sistema = DOL; stop del sistema = oltre lo sweep (il punto dove la tesi
   "era un raid" è falsificata). La geometria del trade discende tutta da qui.
