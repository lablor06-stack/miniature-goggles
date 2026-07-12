# CHANGELOG — Institutional Futures Trading System

Formato: [SemVer](https://semver.org/lang/it/). Le modifiche ai parametri canonici P1–P17
richiedono bump minor + nota di validazione (vedi `Documentation/00_Conventions_and_Specs.md` §4).

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
