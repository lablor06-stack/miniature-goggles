# 01 — Microstruttura dei Futures su Indici (ES/NQ)

> Documento fondativo: tutto ciò che nel sistema chiamiamo "liquidità", "sweep", "manipolazione"
> ha una spiegazione **meccanica** nella microstruttura. Capirla sostituisce la narrativa
> cospirativa ("loro") con meccanismi testabili — ed è il prerequisito per fidarsi delle regole
> nei momenti di stress.

---

## 1. Teoria

### 1.1 Il matching engine CME Globex

- ES e NQ girano su **CME Globex**, order book centralizzato con matching **FIFO
  (price-time priority)**: a parità di prezzo vince chi è in coda da più tempo.
- Tipi di ordine rilevanti: **limit** (fornisce liquidità, visibile nel book), **market**
  (consuma liquidità), **stop** (dormiente: alla violazione del trigger diventa **market**
  o limit), **iceberg** (mostra solo una frazione della size reale).
- Il book mostra tipicamente 10 livelli per lato (DOM). La size visibile è una frazione
  dell'intenzione reale: iceberg, ordini sintetici e re-quoting HFT rendono il DOM
  un'indicazione parziale.

### 1.2 Chi opera (tassonomia dei partecipanti)

| Partecipante | Comportamento | Impronta sul prezzo |
|---|---|---|
| **Market maker / HFT** | Quota bid/ask, inventario ~flat a fine giornata; ~50%+ del volume | Mean-reversion a micro-scala, assorbimento |
| **Execution desk istituzionali** | Algos VWAP/TWAP/POV per lavorare ordini grandi in ore | Pressione persistente ma "gentile", ancoraggio al VWAP |
| **CTA / vol-target / risk-parity** | Flussi sistematici legati a trend e volatilità | Accelerazioni in coda ai movimenti, ribilanciamenti a fine giornata |
| **Opzioni / dealer gamma** | Hedging dinamico delta | Pinning in gamma positiva, amplificazione in gamma negativa |
| **Retail / piccoli speculativi** | Stop visibili, ingressi su breakout | Cluster di stop su estremi e numeri tondi |

### 1.3 Perché esistono i "pool di liquidità" (meccanica, non metafora)

1. Gli **stop si concentrano** dove è razionale metterli: oltre massimi/minimi visibili, oltre
   estremi di sessione, oltre numeri tondi. È un equilibrio di coordinamento: tutti vedono gli
   stessi grafici.
2. Uno stop violato **diventa un ordine a mercato**: la violazione di un cluster produce una
   **cascata** — sequenza di market order nella stessa direzione che consuma il book.
3. Per un desk che deve **riempire size**, l'unico posto dove c'è controparte concentrata è
   proprio lì: comprare "dentro" la cascata di vendite degli stop sotto un minimo è il modo più
   economico di accumulare senza muovere il prezzo contro sé stessi.
4. Se dopo la cascata **non arriva informazione nuova**, il prezzo torna nel range: la cascata
   era liquidità, non repricing. Questo è lo **sweep-and-reverse** su cui il sistema costruisce
   il Setup A.

### 1.4 Price discovery e gerarchia dei mercati

- I futures su indici **guidano** la price discovery rispetto al cash e agli ETF (E1, Hasbrouck
  2003): ES si muove per primo, SPY segue. Per questo si opera il future, e per questo le
  divergenze ES/NQ (SMT) hanno senso: due aste parallele sullo stesso macro-flusso.
- Aste di apertura/chiusura equity (09:30/16:00 ET) e **MOC imbalance** (~15:50) creano flussi
  meccanici ricorrenti → parte della stagionalità intraday.

### 1.5 Rollover e serie continue

Ogni trimestre il volume migra al contratto successivo in ~2-3 giorni. Implicazioni: livelli di
lungo periodo vanno verificati sulla serie back-adjusted; il giorno di roll la profondità del book
è anomala su entrambi i contratti.

---

## 2. Vantaggi (del fondare il sistema sulla microstruttura)

- Trasforma i concetti ICT da "segreti degli insider" a **meccanismi verificabili** (stop
  cascade, inventory management, execution algos): si può ragionare su *quando* il meccanismo è
  attivo invece di applicare pattern ovunque.
- Fornisce **criteri di invalidazione oggettivi**: se dopo uno sweep il prezzo *accetta* oltre il
  livello (close multipli, value che migra), la spiegazione "era una cascata di stop senza
  informazione" è falsificata → si sta con l'espansione, non contro.
- Ancora il sistema ai **flussi ricorrenti e datati** (aste, MOC, news alle 08:30/10:00/14:00,
  settlement), che sono la parte più stabile dell'edge temporale.

## 3. Svantaggi e limiti

- Senza dati **MBO (market-by-order)** non si può *provare* sul singolo evento chi ha fatto cosa;
  a livello retail si osservano solo le impronte (wick, delta, volume). Il sistema deve quindi
  ragionare per **probabilità di meccanismo**, non per certezza.
- Le dinamiche HFT (sub-millisecondo) **non sono sfruttabili** a latenza umana: ogni parte del
  sistema che pretendesse di "leggere il book" in tempo reale sarebbe teatro. Il DOM si usa per
  contesto (dove sono gli iceberg evidenti), mai per trigger.
- La microstruttura cambia con il regime (vol alta → book sottile → cascate più lunghe): i
  parametri fissi (es. profondità sweep) vanno normalizzati per ATR — il sistema lo fa (P3–P6).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Volume e volatilità intraday a "U" (concentrazione a open/close) | Wood, McInish & Ord (1985); Admati & Pfleiderer (1988) | **E1** |
| Gli stop si clusterizzano oltre estremi e numeri tondi; le cascate di stop producono overshoot e reversione | Osler (2003, 2005) su FX — meccanismo generale del matching, trasferibile ai futures | **E1** (FX) / **E3** (transfer ES) |
| I futures guidano la price discovery sull'equity index | Hasbrouck (2003) | **E1** |
| L'impatto prezzo degli ordini è concavo nella size; i big order vengono splittati (→ impronte persistenti tipo VWAP-algo) | Kyle (1985) teoria; letteratura empirica su meta-orders (Almgren et al.) | **E1** |
| Flussi MOC/settlement creano pattern ricorrenti 15:50–16:00 | Letteratura su closing auctions; osservabile nei dati | **E1/E2** |
| "Gli algo delle banche cacciano i TUOI stop" (versione forte, intenzionale, quotidiana) | Nessuna evidenza; lo spoofing è perseguito (casi DOJ) ma episodico | **E4** |

**Take quantitativo:** ciò che è solido è (a) *dove* si concentra la liquidità dormiente,
(b) *che* la sua esecuzione produce overshoot-e-ritorno in assenza di news, (c) *quando* la
partecipazione si concentra. Il sistema usa esattamente e solamente questi tre pilastri.

## 5. Contesti favorevoli

- Giornate a liquidità normale, calendario noto, book profondo: i meccanismi di cascata/ritorno
  funzionano "da manuale".
- Estremi **visibili e multipli** (PDH/PDL + estremo di sessione coincidenti): più stop, cascata
  più leggibile.
- Finestre ad alta partecipazione (kill zone): la controparte istituzionale che "usa" la cascata
  è presente.

## 6. Contesti sfavorevoli

- **News tier-1 in uscita** (CPI, NFP, FOMC): la violazione di un livello È repricing informativo,
  non caccia di stop → lo sweep-fade fallisce sistematicamente. Regola: no-trade ±X min (Manual).
- **Rollover week**, half-days, vigilie di festività: book sottile, cascate senza controparte,
  pattern inaffidabili.
- **Regime gamma-negativa violenta** (vol esplosiva): i dealer amplificano invece di smorzare;
  gli overshoot non tornano.

## 7. Errori comuni

1. Leggere il DOM come intenzione reale (spoofing/iceberg lo rendono teatrale).
2. Attribuire a manipolazione ciò che è flusso meccanico noto (MOC, roll, hedging gamma).
3. Ignorare il calendario delle news e chiamare "sweep" un breakaway informativo.
4. Operare il contratto in roll o livelli calcolati sulla serie sbagliata.
5. Pretendere di scalare l'edge microstrutturale a latenza umana (fare l'HFT a mano).

## 8. Miglioramenti proposti (IFTS)

- **Event-window discipline:** il sistema marca le finestre news e le esclude (Manual/checklist);
  gli sweep vengono misurati separatamente dentro/fuori le finestre → statistica pulita.
- **Normalizzazione ATR** di tutte le soglie (P3–P6) per robustezza cross-regime.
- **Misura in-house della meccanica sweep:** il modulo Statistics del Pine conta profondità,
  durata e follow-through degli sweep per strumento/TF → sostituisce il folklore con numeri
  propri (pipeline in `Testing/`).

## 9. Implicazioni per il sistema

1. Il Setup A (sweep-reversal) è la monetizzazione diretta della cascata di stop senza
   informazione → richiede: pool visibile, KZ attiva, no news, ritorno rapido (P6).
2. Il Setup B (continuation) è la monetizzazione dell'*accettazione*: quando la violazione è
   repricing, si va con il flusso al pullback.
3. Il tempo è un filtro di primo ordine, non un contorno: fuori dalle finestre di partecipazione
   il meccanismo che giustifica il trade non esiste.
