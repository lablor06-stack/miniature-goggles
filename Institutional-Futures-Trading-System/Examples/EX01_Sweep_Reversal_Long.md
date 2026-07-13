# EX01 — Setup A Long: Sweep di PDL in NY AM (walkthrough completo)

> Esempio didattico end-to-end: ogni passo cita la checklist/regola applicata.
> Prezzi coerenti con ES; la dinamica è il *pattern canonico* del sistema.

## 1. Pre-market (07:55 ET) — Manual/01 §1

- **Calendario:** nessuna release tier-1 (solo consumer credit 15:00, tier-3). Perimetro:
  NY AM piena. ✓R4
- **HTF:** daily in uptrend (HH 6248.50 / HL 6198), H4 concorde. **Bias: LONG.**
- **Dealing range M15:** 6212.00 (PDL, swing esterno) → 6248.50 (PDH). EQ = 6230.25.
  Prezzo pre-market 6221 = discount (34%). ✓V6 per long
- **Mappa liquidità:** sotto → PDL 6212.00 (rank 2) + London low 6216.75 (rank 3) =
  cluster sell-side. Sopra → PDH 6248.50 (rank 2), nPOC 6244.
- **Narrativa scritta:** *"Veniamo da chiusura debole dentro range. Scenario primario:
  raid del cluster 6212-6217 in NY AM → reversal verso PDH/nPOC (Setup A long). Alternativo:
  accettazione sotto 6212 → Setup B short verso 6198. NT se: apertura direttamente sopra
  6240 (DOL già speso)."*
- **ADR 42 pt, notte ha usato il 31%** → benzina ✓. Stato personale 8/10 ✓. Size per grade
  calcolate ✓.

## 2. Sviluppo (09:30–09:45)

- 09:30 open 6219.75, dentro il range di ieri → prior *rotation* ✓ (il classificatore
  della dashboard mostra ROTATION).
- 09:38: spinta ribassista impulsiva: low **6209.50** — viola PDL (6212.00) di 2.5 pt
  (≈0.3×ATR ✓ profondità ideale) E il London low: **sweep multi-pool** (+1 grade).
- La barra M5 delle 09:40 chiude **6215.25**, sopra il PDL → ritorno in 2 barre ✓ P6.
- **SMT check:** NQ nello stesso momento NON ha violato il suo PDL (LL mancato) →
  divergenza bullish, correlazione rendimenti 0.81 ✓ (+1 grade).
- 09:44: candela M5 con body 9.25 pt vs media 4.1 (2.26× ≥ 1.5 ✓ P4) chiude 6222.50
  sopra lo swing interno 6221.50 → **MSS ▲**. Il movimento lascia **FVG 6214.50–6218.25**
  (3.75 pt ≥ 0.25×ATR ✓ P5).

## 3. Checklist di ingresso (09:45) — Manual/01 §2.1

```
A1 KZ NY AM attiva ✓ · A2 no news ±15' ✓ · A3 sweep PDL+LDN.L rank 2 ✓
A4 MSS con displacement 2.26×, FVG lasciato ✓ · A5 CE 6216.38 in discount (10%) ✓, in OTE ✓
A6 DOL = PDH 6248.50 → stop 6209.00 → R:R = (6248.5-6216.5)/(6216.5-6209.0) = 4.27 ≥ 2 ✓
A7 regime ROTATION, nessun trend contrario ✓
GRADE: SMT +1 · multi-pool +1 · OF n.d. · weekly no · VWAP reclaim in MSS +0.5 → 2.5 = A+ → 0.50%
ORDINE: limit 6216.50 · stop 6209.00 (7.5 pt) · TP1 6230.25 (EQ) · TP2 6248.00 · runner
```
Conto 100k → rischio $500 → 1 ES (7.5×$50=$375; il secondo contratto sforerebbe →
arrotondamento per difetto R8: 1 ES + 2 MES = $450). *Regola dei 10 secondi* ✓.

## 4. Gestione — Manual/01 §3

- 09:51 fill 6216.50 (il prezzo consegna al CE, non serve inseguire ✓E2 evitato).
- MAE: 6214.25 (−0.30R) — dentro il gap, mai vicino allo stop.
- 10:12 **TP1 6230.25** → chiuso ⅓, stop a BE+1 tick (6216.75) ✓R10.
- 10:56 **TP2 6248.00** (front-run del PDH di 2 tick ✓) → chiuso ⅓.
- Runner: trail sotto swing M5. 11:22 swing 6244.75 violato → out.
- **Risultato ponderato: +2.41R** · MFE 4.6R · capture 52% ✓ in banda.

## 5. Post-trade (11:30) — Manual/01 §4

Riga CSV completa (sweep_grade 4, smt bull, pd_position 10, vwap_sigma −1.2 all'entry).
Replay 60'': sequenza conforme, `rule_break none`. Emozione 8/10.

## 6. Perché questo trade è "il sistema" (note didattiche)

1. L'ingresso NON è stato al minimo (6209.50) — il sistema non compra minimi: compra il
   *ritorno confermato* dopo che i minimi hanno fatto il loro lavoro (raccogliere stop).
2. Ogni condizione era binaria e verificabile PRIMA dell'ordine: nessuna "sensazione".
3. Il R:R ex-ante (4.27) è ciò che paga i falsi segnali di una settimana: il singolo
   trade non deve "avere ragione", deve essere ben pagato quando ce l'ha.
4. Il trade era A+ per confluenze *ortogonali* (cross-market + multi-pool + flusso VWAP),
   non per 3 zone sovrapposte contate 3 volte.
