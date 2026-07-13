# EX02 — Setup B Short: Trend Day ribassista, ricarico su Breaker (walkthrough)

> Il complementare di EX01: la giornata in cui il reversal è VIETATO e il denaro è nel
> seguire il flusso. NQ, regole Setup B (Core Model §4).

## 1. Pre-market (07:55 ET)

- **Calendario:** CPI 08:30 ⚠ → protocollo news attivo (Manual/01 §2.4): nessun ordine
  pendente fino a 08:45; la KZ operativa parte a 08:45.
- **HTF:** daily ha rotto HL settimanale mercoledì; H4 in LH/LL. **Bias: SHORT.**
- **Narrativa:** *"CPI decide. Scenario primario: sorpresa hawkish → gap/drive sotto la VA
  di ieri → trend day short → Setup B sui ricarichi (breaker/IFVG). Alternativo: CPI in
  linea → rotazione, torna il playbook A. NT: primo movimento post-CPI, sempre."*

## 2. Sviluppo — la dichiarazione del regime (08:30–10:30)

- CPI 08:30: sopra le attese. NQ da 22540 a 22390 in 6 minuti. **Non si opera il primo
  movimento** (filtro A2/news: il repricing non è un raid ✓ Research/01 §6).
- 09:30 open 22350, **sotto l'intero range di ieri** (gapVote −1). Nessun rientro nei
  primi 15' → accettazione ✓.
- 10:18: close M5 22288 sotto IB low con displacement (ibVote −1).
- VWAP: prezzo sotto dal 09:30, VWAP inclinato giù (vwapVote −1).
- **10:30: regime = TREND ▼ (3 voti)** → Setup A long VIETATO (A7); Setup B short attivo
  (B1 ✓, B2 bias H4 short ✓).

## 3. Il ricarico (11:05)

- Il pullback 10:40-11:00 attraversa al rialzo un bearish FVG M5 (22310–22336)... NO:
  lo *rispetta*. Attenzione didattica: il pullback consegna DENTRO la zona flip creata
  dalla rottura delle 10:18: l'ex swing-supporto 22322 (OB bullish fallito) è ora
  **breaker bearish 22308–22330**.
- 11:05: il pullback tocca 22326 (dentro il breaker), mini-sweep dello swing M1 22318,
  poi close M5 22297 sotto il bordo (B4 trigger ✓).
- **Checklist B:** B1 ✓ · B2 ✓ · B3 breaker, discount del leg? Il pullback è al 42% del
  leg 22390→22288 ✓ · B4 ✓ · B5 DOL: low overnight 22180 → (22297−22180)/(22334−22297)
  = 3.2R ✓ · B6 orario 11:05 ✓ (pre-lunch).
- Grade: VWAP first-touch coincidente (il pullback ha toccato anche il VWAP) +1;
  correlato ES concorde +0.5 → **A** → 0.35%.
- Ordine: short 22297 · stop 22334 (sopra breaker + 4 tick, 37 pt) · TP1 22262 (nuovo
  low marginale) · runner verso 22180.

## 4. Gestione

- TP1 11:38 → ½ chiuso, BE ✓. Runner con trail sopra swing M5.
- 12:00-13:00 lunch: la posizione si GESTISCE (trail), non si aggiunge ✓R2.
- 14:10: accelerazione a 22195; 14:25 swing M5 22216 violato → out.
- **Risultato: ½×0.95R + ½×2.7R ≈ +1.8R.**
- 15:10: nuova zona? Sì (IFVG 14:40) ma trade #3 della giornata sarebbe il limite P15 —
  preso? NO: alle 15:00 il playbook C impone target corti e il DOL residuo è < 2R → NT.
  (La disciplina sull'ULTIMA ora è dove i trend day restituiscono i profitti.)

## 5. Note didattiche

1. **Il regime prima del segnale (V3):** lo stesso grafico alle 10:00 mostrava "sweep del
   low di ieri" — un occhio da Setup A ci avrebbe visto un long. Il classificatore
   (3 voti) ha detto: espansione, non raid. La distinzione sweep/accettazione È il sistema.
2. **CPI:** il primo movimento post-release non si fade e non si insegue: si *lascia
   dichiarare* (l'edge del giorno news è nel ricarico, non nella reazione).
3. Lo stop del B vive oltre la zona flip (chi è intrappolato lì difende quel livello:
   se passa, la tesi è morta), non "N punti" arbitrari.
4. Il trend day paga col runner (½ posizione = 2.7R): chiudere tutto a TP1 avrebbe
   dimezzato l'expectancy del setup (errore E9/E8).
