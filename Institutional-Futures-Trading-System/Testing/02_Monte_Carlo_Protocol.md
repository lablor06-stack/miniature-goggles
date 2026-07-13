# 02 — Protocollo Monte Carlo

> Scopo: trasformare una serie limitata di trade in **distribuzioni** di esiti possibili, per
> dimensionare rischio e aspettative psicologiche. Implementato in
> `Statistics/Tools/monte_carlo.py` (stdlib-only, seed riproducibile).

## 1. Metodo

**Bootstrap i.i.d. (resampling con reimmissione)** della serie di R osservati:
- Input: serie R (da journal, n ≥ 30; sotto: il tool avvisa che gli intervalli sono ampi).
- Per ciascuna delle N=10.000 simulazioni: campiona `horizon` trade (default 100) con
  reimmissione e calcola: R totale, MaxDD, max losing streak, % settimane negative proxy.
- Output: percentili P5/P25/P50/P75/P95 di ogni grandezza + probabilità di eventi soglia
  (DD > X R, serie > k perdite, orizzonte in perdita).

**Variante a blocchi (block bootstrap, default block=5):** ricampiona blocchi consecutivi
per preservare eventuale autocorrelazione/clustering dei risultati (giornate correlate).
Si riportano ENTRAMBE le versioni; se divergono molto, il clustering è reale e conta la
versione a blocchi (più conservativa di norma).

## 2. Domande a cui risponde (e le decisioni collegate)

| Domanda | Output | Decisione alimentata |
|---|---|---|
| Qual è il DD "normale" del sistema? | P50-P75 MaxDD | Aspettative psicologiche (Manual/03) |
| Qual è il DD di allarme? | P95 MaxDD | Kill-switch (Core Model §10) e R17 |
| Quante perdite consecutive aspettarsi? | P95 losing streak | Dimensionamento P11 (Manual/02 §2.3) |
| Probabilità di trimestre negativo con questa expectancy? | P(R_tot < 0 su 60 trade) | Buffer di capitale/prop |
| La size 0.25-0.50% è giustificata? | P(DD% > limite prop) | Vol.5 §2 |

## 3. Probabilità di rovina (definizione operativa)

Non usiamo la formula classica (assume bet fisse e i.i.d.): la stimiamo per simulazione come
`P( equity% tocca −X% entro H trade )` con X = limite operativo (es. trailing prop o −10R
mensile) — output diretto del tool con `--ruin-level`.

## 4. Limiti dichiarati del metodo

1. Il bootstrap assume che il futuro campioni dallo stesso processo del passato: **regime
   change non modellato** → i percentili sono condizionati al regime osservato.
2. Con n piccolo la coda è sottostimata (i disastri rari non sono nel campione) → si integra
   uno **stress sintetico**: `--inject-tail` aggiunge al pool un evento −3R con probabilità
   1% (gap/slippage catastrofico) — default ON, disattivabile.
3. I R del journal includono già slippage reale (S3-S4) o sintetico (S2) — non aggiungere due volte.

## 5. Cadenza

- Alla fine di S2 (baseline), mensile in S3-S4 (Manual/04 §5), e a ogni 50 trade nuovi.
- Ogni run salvata con: data, n, seed, percentili chiave → confronto nel tempo (il
  peggioramento della distribuzione È il segnale di decadimento dell'edge, prima ancora
  del P&L).
