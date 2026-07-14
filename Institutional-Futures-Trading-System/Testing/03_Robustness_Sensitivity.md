# 03 — Robustness & Sensitivity Analysis

> Un sistema è robusto se l'edge sopravvive a perturbazioni ragionevoli di parametri, costi
> e condizioni. Un edge che vive solo a P4=1.50 e muore a 1.40 non è un edge: è un artefatto.

## 1. Sensitivity dei parametri canonici (griglia pre-registrata)

Su S1 (event study automatizzabile) e su un sottocampione S2, si perturba UN parametro alla
volta attorno al default, tenendo gli altri fissi:

| Parametro | Default | Griglia | Metrica osservata | Criterio di robustezza |
|---|---|---|---|---|
| P1 swing int | 3 | 2/3/4/5 | base rate MSS follow-through | monotona o piatta, no picco isolato |
| P2 swing ext | 8 | 6/8/10/12 | stabilità dealing range (n. ridisegni/die) | variazione < 30% |
| P4 displacement | 1.5 | 1.2/1.35/1.5/1.75/2.0 | n. eventi & follow-through | trade-off regolare frequenza/qualità |
| P5 FVG min | 0.25 | 0.15/0.25/0.35/0.5 | fill rate & react rate | curve lisce |
| P6 sweep window | 3 | 2/3/4/5 | % sweep vs accettazioni | nessun salto |
| P3 EQ tolerance | 0.10 | 0.05/0.10/0.15 | n. pool EQH/EQL | lineare |
| armWindow | 12 | 8/12/16/20 | % setup A armati validi | plateau |

**Regola decisionale:** se la metrica mostra un massimo isolato ("spike") sul default →
sospetto overfitting → si adotta il valore al centro del plateau più vicino, si documenta
nel CHANGELOG. Il default DEVE stare su un plateau.

## 2. Stress dei costi

Expectancy ricalcolata con slippage crescente: 0 / 1 / 2 / 3 tick per lato (ES; doppio NQ).
Criterio: il sistema deve restare ≥ +0.15R a 2 tick/lato. Se l'edge muore a 1 tick, è un
edge di microstruttura non catturabile a mano → si scarta il componente.

## 3. Robustezza temporale e di regime

- **Split per anno** (2024/2025/2026) e per **regime VIX** (terzili): l'expectancy deve
  restare positiva in ≥ 2/3 dei blocchi e mai catastrofica nel terzo.
- **Split per semestre di kill zone** (inverno/estate — DST e liquidità EU): confronto
  London vs NY performance.
- **Degradation test:** metriche su rolling 50 trade — trend al ribasso persistente =
  decadimento (procedure Manual/04 §7).

## 4. Robustezza cross-instrument

Il modello è specificato per ES/NQ. Test: stessi parametri (ATR-normalizzati by design) su
YM e RTY **senza ritocchi**. Aspettativa: expectancy positiva ma inferiore (liquidità e
pool meno puliti). Se NEGATIVA forte: indizio che l'edge su ES/NQ è più fragile di quanto
sembri → approfondire prima del live.

## 5. Ablation study (il test più importante)

Si rimuove UN componente alla volta dal Setup A (su S2 replay):

| Variante | Cosa misura |
|---|---|
| A senza filtro KZ | Il valore del tempo |
| A senza requisito sweep | Il valore della liquidità |
| A senza displacement | Il valore della qualificazione MSS |
| A senza vincolo P/D | Il valore della geometria |
| A senza R:R ≥ 2 | Il valore della selezione dei target |

Se una rimozione NON peggiora le metriche su n adeguato → quel componente è zavorra →
va in revisione (Fase 7 lo prevede). Se le peggiora tutte → il sistema è additivo come
progettato. Questo studio distingue un framework da una liturgia.

## 6. Sanity check contro il caso

- **Test di permutazione:** expectancy del Setup A confrontata con 1.000 pseudo-setup a
  orari/altezze casuali con stessa gestione (stesso TP/SL/time-stop) sulle stesse giornate.
  L'edge reale deve battere il 95° percentile del caso.
- **Benchmark ingenuo:** buy-and-hold intraday RTH e ORB semplice sulle stesse giornate —
  il sistema deve battere entrambi risk-adjusted, altrimenti la complessità non è pagata.
