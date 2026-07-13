# CHANGELOG — Institutional Futures Trading System

Formato: [SemVer](https://semver.org/lang/it/). Le modifiche ai parametri canonici P1–P17
richiedono bump minor + nota di validazione (vedi `Documentation/00_Conventions_and_Specs.md` §4).

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
