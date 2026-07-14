# 05 — Order Flow: Delta, CVD, Footprint, DOM

> L'order flow è il microscopio: mostra *chi sta aggredendo* e *chi sta assorbendo* al livello.
> Nel sistema IFTS è una **confluenza discrezionale di grado superiore** (non codificata come
> trigger) perché i dati necessari a farne regole meccaniche affidabili non sono disponibili
> con qualità uniforme su tutte le piattaforme dell'utente finale.

---

## 1. Teoria

### 1.1 Grandezze

- **Delta (per barra):** volume eseguito *at ask* (aggressione buy) − volume *at bid*
  (aggressione sell). Misura l'iniziativa dei market order.
- **CVD (Cumulative Volume Delta):** somma cumulata del delta. La *forma* del CVD rispetto al
  prezzo è più informativa del valore assoluto.
- **Footprint:** matrice prezzo × (bid vol, ask vol) dentro ogni barra. Pattern chiave:
  **imbalance diagonale** (aggressione che vince ≥3:1 sul livello adiacente), **stacked
  imbalances** (3+ consecutivi = iniziativa vera), **unfinished auction** (estremo di barra
  senza scambio bilaterale → tende a essere rivisitato).
- **DOM (book):** liquidità passiva dichiarata. Affidabilità bassa (spoofing, iceberg);
  eccezione: **iceberg rilevati** (ricariche ripetute allo stesso prezzo mentre il prezzo non
  passa) = assorbimento reale osservabile.

### 1.2 I due segnali che contano (e il loro razionale)

1. **Assorbimento agli estremi:** durante uno sweep, delta fortemente negativo (aggressione
   sell) ma prezzo che *non scende più* → i sell market stanno riempiendo limit buy
   istituzionali. È la conferma order-flow del Setup A. Sul CVD appare come:
   **prezzo LL, CVD LL molto più profondo** (sproporzione) oppure **prezzo LL, CVD HL**
   (divergenza classica).
2. **Esaurimento:** delta della stessa direzione del trend che si contrae progressivamente
   mentre il prezzo avanza a fatica verso un livello → iniziativa finita.

### 1.3 Vincolo di piattaforma (dichiarato)

TradingView non espone tick-by-tick bid/ask storico per i futures CME su tutti i piani; il
delta "vero" richiede piattaforme dedicate (Sierra Chart, ATAS, Exocharts, NinjaTrader con
dati L1/L2). In Pine si può costruire solo un **proxy**: up/down volume da timeframe inferiore
(`request.security_lower_tf`), che classifica il volume per direzione della candela LTF, non
per lato di esecuzione. Il proxy è utile in divergenza macroscopica, inaffidabile nel dettaglio.
**Decisione IFTS:** l'order flow resta strumento discrezionale su piattaforma dedicata per chi
ce l'ha; il Pine non finge di avere dati che non ha (niente "delta" fasullo nel master —
motivazione completa in `Documentation/03_Red_Team_Review.md`).

---

## 2. Vantaggi

- Unico strumento che distingue **aggressione da assorbimento** in tempo reale: il grafico
  candele mostra *che* il prezzo ha tenuto, il footprint mostra *come*.
- Riduce drasticamente i falsi positivi del Setup A quando disponibile: sweep + assorbimento
  visibile è una classe di trade diversa da sweep solo-prezzo.
- L'evidenza meccanica (stop cascade, iceberg) è osservabile direttamente → feedback formativo
  potentissimo per il trader.

## 3. Svantaggi e limiti

- **Costo e complessità:** dati e piattaforme dedicate; curva di apprendimento lunga (mesi).
- **Rumore:** a granularità fine quasi ogni barra contiene "pattern"; senza livelli di contesto
  (da struttura/liquidità) il footprint produce overtrading.
- **Non backtestabile facilmente:** l'assorbimento è pattern-recognition su dati bid/ask storici
  pesanti; la validazione richiede tooling fuori scope v1.
- Il DOM è manipolabile e va trattato come teatro con eccezioni (iceberg ricorrenti).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| L'order flow imbalance ha potere predittivo a brevissimo termine sul mid-price | Letteratura microstruttura (Cont, Kukanov & Stoikov 2014, *The price impact of order book events*) | **E1** (orizzonti brevi) |
| Il delta/CVD aggregato a barre conserva parte di quel segnale a orizzonte intraday | Estensione plausibile, decadimento rapido | **E3** |
| Divergenze prezzo/CVD agli estremi precedono reversal più spesso del caso | Consenso practitioner order-flow; test pubblici scarsi | **E3** |
| Spoofing/layering esistono e distorcono il DOM | Casi giudiziari documentati (es. flash crash 2010, procedimenti CFTC/DOJ) | **E1** |
| "Il DOM mostra dove andrà il prezzo" | No: la liquidità dichiarata non è impegno | **E4** |

## 5. Contesti favorevoli

- Ai **livelli attesi** (pool esterni, PD array HTF) durante kill zone: il segnale
  assorbimento/esaurimento ha il massimo valore informativo esattamente dove il sistema
  già vuole operare.
- Regimi liquidi e ordinati (book spesso): le impronte sono leggibili.

## 6. Contesti sfavorevoli

- News tier-1 e primi secondi post-release: flusso troppo veloce, letture inaffidabili.
- Notte/festivi: delta sottile, pattern casuali.
- Lettura *senza* livello: footprint "in mezzo al range" = rumore con qualunque esito.

## 7. Errori comuni

1. Usare l'order flow come sistema a sé (senza mappa di livelli) → overtrading da stimoli.
2. Fidarsi del delta grezzo di piattaforme che lo stimano dal tick rule senza bid/ask reale.
3. Leggere ogni divergenza CVD come reversal: in trend forte il CVD diverge per ore (i limit
   assorbono E il prezzo continua — assorbimento non implica inversione senza struttura).
4. Confondere il delta della barra (iniziativa) con il risultato (dove ha chiuso la barra):
   delta positivo + close debole = assorbimento dei buyer, segnale opposto all'ingenuo.
5. Guardare il DOM per decidere il trigger.

## 8. Miglioramenti proposti (IFTS)

- **Ruolo formalizzato:** l'order flow è *upgrade discrezionale* del grade (A → A+) nella
  matrice di confluenza, mai condizione necessaria → il sistema resta operabile da chi non ha
  la piattaforma dedicata, e il journal registra il campo `of_confirm` (sì/no/n.d.) per
  misurare *quanto* l'upgrade paga (research question RQ-5).
- **Checklist di lettura in 3 punti** (Manual/01): al livello, chiedersi solo: (1) chi
  aggredisce? (2) il prezzo risponde? (3) c'è ricarica passiva (iceberg)? — evita l'analisi
  infinita.
- Nel Pine: nessun falso delta; la dashboard espone un **campo manuale** di conferma OF che il
  trader spunta mentalmente (documentato), mantenendo il journal coerente.

## 9. Implicazioni per il sistema

1. Setup A con conferma OF disponibile e positiva = grade A+ (size 0.50%); senza dati OF il
   setup resta valido a grade A (0.25–0.35%).
2. Nessuna regola meccanica del sistema dipende dall'order flow → robustezza rispetto alla
   dotazione tecnologica dell'utente.
3. La formazione order-flow è nel percorso di crescita del trader (Manual/04, routine mensile),
   non nel prerequisito di partenza.
