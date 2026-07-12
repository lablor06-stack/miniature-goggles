# 00 — Sintesi della Ricerca (leggere dopo i documenti 01-12)

> Questo documento risponde a tre domande: **(1)** che cosa, di tutto il corpus studiato,
> regge uno scrutinio quantitativo? **(2)** come si compone in un unico modello coerente?
> **(3)** quali vincoli di progettazione ne derivano per le strategie (Fase 2-3)?

---

## 1. Il quadro unificato

I quattro corpi di conoscenza studiati **descrivono lo stesso fenomeno da quattro angoli**:

| Corpus | Angolo | Contributo al sistema |
|---|---|---|
| **Microstruttura** (01) | *Meccanica* — chi esegue cosa, e perché le cascate esistono | Il "perché" fisico di sweep e displacement; le finestre di partecipazione |
| **AMT / Profile** (02-03) | *Fisica del valore* — accettazione/rifiuto, balance/imbalance | Il regime: quale playbook è autorizzato oggi |
| **ICT/SMC** (06-10) | *Linguaggio operativo* — sigle precise per eventi ricorrenti | La grammatica esecutiva: dove entrare, dove invalidare |
| **Tempo** (11) + **VWAP/OF/SMT** (04-05-12) | *Filtri e conferme* | Quando il meccanismo è attivo; conferme ortogonali |

**Il modello unificato in una frase:** *nei momenti di massima partecipazione (KZ), il prezzo
rivisita liquidità dormiente (pool); se la violazione non è repricing informativo, la cascata
viene assorbita (sweep) e l'iniziativa si manifesta con displacement (MSS) verso la liquidità
opposta (DOL); le zone lasciate dal displacement (FVG/OB/Breaker) sono i punti di ingresso a
rischio definito, e la posizione nel range (P/D) ne stabilisce la legittimità geometrica.*

Ogni parola di questa frase è un modulo del Pine e una riga delle checklist. Nient'altro è
necessario; tutto il resto (VWAP, profile, SMT, order flow) è contesto e conferma.

---

## 2. Che cosa regge lo scrutinio (bilancio di evidenza)

### Pilastri E1 (su cui il sistema può poggiare il peso)

1. **Stagionalità intraday di volume/volatilità** (U-shape; concentrazione a open/news/close).
2. **Clustering degli stop** oltre estremi visibili e numeri tondi + **cascate con overshoot
   e ritorno** in assenza di news (Osler; meccanica del matching).
3. **VWAP come benchmark di esecuzione** istituzionale (flusso reale ancorato al livello).
4. **Futures = luogo della price discovery** per l'equity USA (ES/NQ sono il posto giusto).
5. **Mean-reversion intraday dopo overshoot** vs **persistenza in imbalance**: entrambi i
   regimi esistono; nessuno domina incondizionatamente → serve il classificatore di regime.

### Concetti E2-E3 (operabili con misurazione in-house obbligatoria)

- Sweep-and-reverse come setup (P6) · MSS con displacement come trigger di inversione ·
  zone di displacement (FVG/OB/Breaker) come punti di reazione · SMT a estremi correlati ·
  IB/day-type framework · nPOC magnet · profilo settimanale (prior debole).

### Folklore E4 (bandito dalle regole; al più linguaggio)

- "Ogni high/low viene sempre preso", "il FVG si riempie sempre", ratio di Fibonacci come
  numeri magici, "gli algo bancari cacciano i tuoi stop ogni giorno", DOM come intenzione,
  qualunque claim con "sempre/mai" senza orizzonte.

### Il debito statistico dichiarato

Il sistema è onesto sul suo punto debole: **i tassi di successo dei suoi eventi (sweep, MSS,
zone) non hanno letteratura pubblica** — hanno meccanismo plausibile (E1 adiacente) e
definizioni testabili. Il debito si ripaga con la strumentazione integrata: il modulo
Statistics del Pine e il journal accumulano l'evidenza E2 *personale* dal giorno 1. Questa è
una feature di prodotto, non una scusa: nessun venditore serio può promettere win-rate; può
promettere **misurabilità**.

---

## 3. Le Research Questions ufficiali (RQ)

Aperte deliberatamente; pipeline in `Testing/00` §7; molte sono contate in automatico dal Pine.

| RQ | Domanda | Dove si misura |
|---|---|---|
| RQ-1 | L'MSS qualificato (sweep+displacement) ha follow-through > CHoCH semplice? | Pine Statistics + journal |
| RQ-2 | Il grading dello sweep (profondità/velocità/pool/KZ) predice l'esito? | journal (`sweep_grade`) |
| RQ-3 | I nPOC agiscono da magnete entro N giorni più del caso? | studio dedicato (Testing RQ) |
| RQ-4 | L'expectancy dei setup varia con la σ-position VWAP all'ingresso? | journal (`vwap_sigma`) |
| RQ-5 | La conferma order-flow (quando disponibile) aumenta l'expectancy? | journal (`of_confirm`) |
| RQ-6 | OB qualificato > OB generico? Breaker > Mitigation? Body-only vs full-wick? | Pine Statistics (reazione ≥1R) |
| RQ-7 | Fill-rate e reazione dei FVG per TF/KZ; il CE reagisce più del bordo? | Pine Statistics |
| RQ-8 | Expectancy vs percentile P/D all'ingresso? | journal (`pd_position`) |
| RQ-9 | Quando si forma l'estremo del giorno (distribuzione per finestra)? | Pine Statistics |
| RQ-10 | L'SMT (con filtro correlazione) aumenta l'expectancy del Setup A? | journal (`smt`) |

---

## 4. Vincoli di progettazione derivati (input vincolanti per la Fase 2)

Dalla ricerca discendono **otto vincoli**; ogni strategia della Fase 2 sarà valutata anche
sulla conformità a questi:

| # | Vincolo | Fonte |
|---|---|---|
| V1 | **Tempo come condizione necessaria:** ingressi solo in KZ; flat 15:50; no lunch/notte | 11 (E1) |
| V2 | **News-guard:** nessun ingresso a ridosso di release tier-1; sweep in news-window non conta | 01, 11 (E1) |
| V3 | **Regime prima del segnale:** classificare balance/imbalance prima di scegliere il playbook; mai fade in trend day conclamato, mai chasing in balance | 02-03 (E1/E2) |
| V4 | **Trigger solo da eventi qualificati:** MSS (inversione) e BOS interno pro-bias (continuazione); tutto il resto è contesto | 06 (anti-rumore/anti-overfit) |
| V5 | **Liquidità come narrativa:** niente sweep di pool rank≥4 → niente reversal; niente DOL raggiungibile → niente trade | 07 |
| V6 | **Geometria P/D:** long in discount, short in premium (range M15), subordinata al bias HTF | 10 |
| V7 | **R:R ≥ 2 verificato ex-ante** (stop strutturale P16, target DOL) | 07, 10 |
| V8 | **Ogni regola testabile e loggabile:** se non può stare in una colonna del journal, non può stare nel sistema | tutta la ricerca |

---

## 5. Conflitti risolti durante lo studio (decisioni prese)

1. **RTH vs ETH per il valore** → RTH per profilo/valore, ETH per estremi di liquidità (03 §1.1).
2. **Fibonacci** → ammesso solo come OTE sul leg di displacement, mai come motivo (10 §1.3).
3. **Order flow nel codice** → escluso (dati non disponibili con qualità uniforme in Pine);
   resta upgrade discrezionale documentato (05 §1.3) — decisione ribadita in Red Team Review.
4. **SMT razionale** → difesa come divergenza di forza relativa a estremi, non come lead-lag
   (12 §1.4).
5. **Struttura** → definizione algoritmica unica (P1/P2, close-only, displacement P4);
   la "struttura a occhio" ICT-style è esclusa dal sistema (06 §3).
6. **DOM** → contesto formativo, mai input di regole (01, 05).

## 6. Ciò che il sistema sceglie di NON usare (e perché)

| Escluso | Motivo |
|---|---|
| Indicatori di momentum classici (RSI/MACD/Stoch) come filtri | Ridondanti rispetto a struttura+displacement; aggiungono parametri ottimizzabili (overfit surface) senza informazione nuova |
| Pattern candlestick nominali (engulfing, doji…) | Sottoinsiemi non necessari del displacement; lessico duplicato |
| Time-fib, Gann, cicli | Nessun meccanismo plausibile; E4 |
| Profilo volume come trigger | Granularità dati TradingView insufficiente; resta contesto |
| Overnight holding | Fuori dal perimetro di rischio v1 (gap risk, margini, prop-firm rules) |

*(Ogni esclusione riduce la superficie di overfitting e il costo cognitivo — il valore di un
sistema sta anche in ciò che lascia fuori.)*

---

## 7. Handoff alla Fase 2

Le 10 strategie candidate copriranno deliberatamente **famiglie diverse** (reversal da sweep,
continuation, opening range, mean-reversion VWAP, value-rotation, SMT-led, PM plays…) così che
la matrice comparativa (Fase 3) confronti *approcci*, non varianti dello stesso trade. I
vincoli V1-V8 sono il filtro d'ammissione; le RQ definiscono i dati da raccogliere dal primo
giorno di operatività.
