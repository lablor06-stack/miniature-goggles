# 01 — Definizioni Formali delle Metriche

> Definizioni univoche e implementate 1:1 in `Statistics/Tools/kpi_calculator.py`.
> Convenzione: R = risultato del trade in unità di rischio iniziale; serie = sequenza
> cronologica di R; equity(k) = Σ R(1..k).

## 1. Metriche per-trade e aggregate

| Metrica | Definizione | Note |
|---|---|---|
| **Win rate (WR)** | n(R > 0) / n(R ≠ escl.) | I BE (R = 0 ± 0.05) sono esclusi dal WR e riportati a parte come be_rate |
| **Avg win / Avg loss** | media(R⁺) / |media(R⁻)| | Anche mediane (dist. asimmetriche) |
| **Payoff ratio** | avg win / avg loss | |
| **Expectancy** | media(R) su tutti i trade | Con IC bootstrap 95% |
| **Profit Factor (PF)** | Σ R⁺ / |Σ R⁻| | ∞ se zero perdite (riportato "inf") |
| **Std dev (R)** | dev. standard campionaria di R | |
| **SQN** | √n × media(R) / std(R) | Van Tharp; confrontabile tra sistemi |
| **MAE/MFE efficiency** | % winner con MAE < 0.5R; MFE capture = mediana(R/MFE) **sui soli winner** (sui perdenti degenererebbe a 0 per costruzione) | Qualità di ingressi/uscite |

## 2. Metriche di percorso (equity curve)

| Metrica | Definizione |
|---|---|
| **Max Drawdown (R)** | max_k [ max_{j≤k} equity(j) − equity(k) ] |
| **Max DD duration** | n. trade tra il picco e il pieno recupero più lungo |
| **Ulcer Index (R)** | √( media( DD(k)² ) ) sulla serie dei drawdown |
| **Recovery factor** | equity finale / MaxDD |

## 3. Metriche annualizzate (solo su dati live/SIM con date reali)

- **Periodicità di calcolo: settimanale** (il trade singolo non è i.i.d. giornaliero; la
  settimana è l'unità naturale del sistema). Rendimento settimanale in R → serie w(i).
- **Sharpe (settimanale, annualizzato):** media(w)/std(w) × √52. Risk-free omesso (i R sono
  già rendimenti in eccesso sul margine, il cash sul conto matura a parte).
- **Sortino:** media(w)/std(w⁻) × √52, dove std⁻ usa solo settimane negative (downside
  deviation rispetto a 0).
- **Nota d'onestà:** Sharpe/Sortino su < 26 settimane sono decorativi; il tool li marca
  `low_n` sotto questa soglia.

## 4. Metriche di processo (dal journal)

| Metrica | Definizione |
|---|---|
| Compliance rate | n(rule_break = none) / n trade |
| Grade accuracy | n(grade confermato in review) / n | (campo review, manuale) |
| Missed-trade gap | expectancy(missed=1) − expectancy(eseguiti) | se > 0 il filtro umano toglie valore |
| Tilt frequency | giorni con tilt=1 / giorni operativi | |

## 5. Stratificazioni standard (ogni metrica × ogni taglio)

`setup (A/B/C) · grade · killzone · day_type · direction · symbol · sweep_grade · smt ·
of_confirm · quintili pd_position · fasce vwap_sigma · day of week`

Regole: n del sottogruppo sempre visibile; nessun taglio sotto n=15 viene stampato
(anti-apofenia); vedi `00_Backtesting_Plan.md` §8 per la molteplicità.

## 6. Convenzioni di arrotondamento e edge case

- R arrotondati a 2 decimali; percentuali a 1.
- Trade `missed=1` esclusi da tutte le metriche di risultato (riportati solo nel gap §4).
- Righe `setup=NT` escluse dai KPI di risultato, contate nei KPI di processo.
- Serie con n < 10: il tool stampa solo n, somma R e rifiuta il resto (`insufficient sample`).
