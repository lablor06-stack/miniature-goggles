# CHANGELOG — Institutional Futures Trading System

Formato: [SemVer](https://semver.org/lang/it/). Le modifiche ai parametri canonici P1–P17
richiedono bump minor + nota di validazione (vedi `Documentation/00_Conventions_and_Specs.md` §4).

## [3.0.0] — 2026-07 · Decision Support System (state-driven; logica segnali invariata)

Da indicatore object-driven a sistema di supporto decisionale: il grafico comunica lo STATO
del ciclo di vita del trade e la prossima azione, non gli oggetti. Design completo in
`Documentation/07_Decision_Support_System.md`.

### Aggiunto
- **Macchina a stati finiti (9 stati, uno alla volta):** Idle → Waiting Liquidity →
  Liquidity Taken → Waiting MSS → Structure Confirmed → Waiting Retracement → Entry Ready →
  Trade Active → Trade Closed; direzione d'ipotesi derivata da trade/setup/raid/bias.
- **Confidence Engine pesato 0-100** (bias 20 · KZ 10 · sweep 15 · MSS 20 · SMT 10 · P/D 10
  · VWAP 5 · FVG 5 · RR 5) — mostrato solo il totale; scomposizione in Debug.
- **Execution Panel**: header merged DIREZIONE+CONFIDENZA con campitura direzionale,
  Status, Next (evento richiesto), Entry/Stop/Target. Righe fisse, zero flicker.
- **Trade tracker UI** con esito visivo (TARGET HIT / STOPPED / SESSION END): completa il
  ciclo e riporta il grafico pulito; adotta anche i trigger Setup B (E/S/T derivati dai
  valori già calcolati). Non tocca statistiche né journal.
- **Modalità Debug** (progressive disclosure): stato interno, pesi, memorie, voti regime.

### Cambiato
- Visibilità guidata dallo stato in Execution: pool → sweep → zona d'ingresso (solo stati
  5-6) → solo E/S/T in trade → chart pulito dopo l'uscita. OB boxes, EQ line, label di zona
  e pannello on-chart rimossi da Execution (il panel narra); tutto resta in Analysis.
- Modalità: Execution / Analysis / Debug (Analysis assorbe la vecchia Standard).
- MSS disegnato in Execution solo se avanza la narrativa attiva (sweep alle spalle).

### Invariato (compatibilità)
- Tutte le condizioni di segnale, detection e calcoli; le 7 alertcondition e i payload
  dinamici; statistiche RQ; zero repaint. `aState` viene azzerato al passaggio di consegne
  al tracker (bookkeeping visivo dichiarato).

## [2.1.0] — 2026-07 · Visual experience redesign (logica invariata)

Ridisegno completo del layer visivo del Master; Logic Layer identico a 2.0.0 (segnali,
alert, statistiche, calcoli VWAP/SMT/zone/liquidità intoccati). Design system in
`Documentation/06_UI_Design_System.md`.

### Aggiunto
- **Modalità EXECUTION (nuovo default):** solo liquidità decisiva (PDH/PDL/Asia H/L),
  1 FVG + 1 OB per lato (champion rendering: gli array restano pieni per l'engine),
  VWAP nudo, evento strutturale corrente, pannello setup unico con E/S/T. ~15-25 oggetti.
- **Visibilità adattiva sul ciclo del trade:** liquidità → SWEEP → MSS+zone → pannello
  E/S/T (le zone si ritirano) → chart pulito a fine trade.
- Palette istituzionale a 5 colori semantici (verde/rosso/grigio/bianco-VWAP/giallo-liquidità);
  zone flip distinte dal bordo tratteggiato, non da un colore in più.
- Pannello setup professionale multiriga (SIDE · grade · RR · E/S/T) al posto di label sparse.

### Cambiato
- Dashboard ridisegnata: borderless, 9 righe fisse (Bias · Regime · P-D · VWAP σ · SMT ·
  Setup · Grade · RR) + statistiche solo in Analysis; rimossi Session/News/sweep/struct.
- Liquidità consumata e zone morte: **eliminate all'istante** (niente fading); i ghost di
  Analysis rimossi; il marker giallo `SWEEP` resta l'unica traccia dell'evento.
- Bande VWAP solo in Analysis; key opens/AVWAP/RTH-VWAP nascosti in Execution.
- OTE disegnata solo a setup armato e rimossa al fill (oltre che a stop/target/scadenza).
- Etichette −80%: solo SWEEP, MSS, pannello setup, 4 pool primari, SMT.
- Input `newsOk` rimosso (riga dashboard eliminata); modalità "Focus" sostituita da
  "Execution".

### Corretto
- La memoria interna dei pool swept ora ha lo stesso orizzonte TTL in ogni modalità: in
  v2.0 i ghost di Analysis allungavano di fatto la memoria del filtro SMT near-pool — la
  logica non deve dipendere dalla modalità di visualizzazione.

## [2.0.0] — 2026-07 · Audit "daily-driver" (nessuna feature nuova)

Riscrittura completa di `IFTS_Master.pine` orientata a pulizia, velocità e uso quotidiano.
Report integrale: `Documentation/05_v2_Audit_Report.md`.

### Aggiunto
- **Display-priority system** a 3 modalità (Focus / Standard / Analysis): gli elementi a
  bassa priorità si nascondono da soli; i ghost degli oggetti ritirati esistono solo in
  Analysis.
- **Smart visualization**: FVG riempiti, blocchi invalidati e liquidità consumata vengono
  rimossi dal grafico e dalla memoria (pool accepted subito; swept dopo TTL configurabile).
- Input riorganizzati in 12 gruppi (General → Advanced), tooltip su ogni impostazione.

### Cambiato (breaking)
- **Alert: da 17 a 7** condizioni azionabili (setup A/B, sweep qualificato in KZ, apertura
  KZ, any-setup) + payload dinamici per webhook; gli alert granulari v1 rimossi.
- Dashboard: aggiornamento solo a chiusura barra, chiavi statiche scritte una sola volta
  (v1 ricostruiva l'intera tabella a ogni tick).
- Sotto `minRr` il Setup A non si arma più (v1 lo armava con flag di invalidità).
- Input rinominati (prefissi di gruppo); `statsOn` → modalità Analysis; `sigUsePm` rimosso.

### Corretto
- Divisione intera latente nel voto VWAP del classificatore di regime (cast float esplicito).
- Flip-flop infinito delle zone invertite: ora un solo flip per vita della zona; statistiche
  fill/inversione conteggiate solo sul FVG originario.
- Doppia rimozione potenziale nello stesso passaggio del lifecycle zone (corruzione array).
- Funzione annidata nella dashboard (non supportata da Pine) → estratta a scope globale.
- Codice morto rimosso (variabili SMT/MSS inutilizzate, tuple dummy).
- Moduli standalone allineati: Zones con lifecycle v2 (rimozione zone morte), Structure con
  choch opzionali (default off).

## [1.0.0] — 2026-07

## [1.0.0] — 2026-07

### Aggiunto
- **Research/**: 13 documenti di studio (microstruttura, AMT, Volume/Market Profile, VWAP/AVWAP,
  order flow, struttura, liquidità, zone, FVG/IFVG, premium/discount, sessioni, SMT) + sintesi
  con gerarchia di evidenza E1–E4.
- **Strategy/**: 10 strategie candidate complete, matrice comparativa multi-criterio pesata,
  strategia definitiva IFTS Core Model (Setup A/B/C).
- **Manual/**: filosofia e regole, checklist operative (pre-market/ingresso/gestione/uscita),
  risk & money management, psicologia ed errori, KPI e routine, adattamento prop firm.
- **Pine/**: `IFTS_Master.pine` (Pine v6, tutti i moduli integrati e toggleabili) + 6 moduli
  standalone (Structure, Zones, VWAP Suite, Sessions/KZ, Premium/Discount, SMT).
- **Testing/**: piano di backtesting (IS/OOS, walk-forward), definizioni metriche, protocollo
  Monte Carlo, robustness & sensitivity.
- **Statistics/Tools/**: `kpi_calculator.py` e `monte_carlo.py` (stdlib-only, testati su
  `sample_trades.csv`).
- **Journal/**, **Examples/**, **Images/** (diagrammi SVG).

### Processo
- Red Team Review (Fase 7) completata: correzioni C1–C12 applicate e documentate in
  `Documentation/03_Red_Team_Review.md`.
- Ottimizzazione (Fase 8) documentata in `Documentation/04_Optimization_Report.md`.
