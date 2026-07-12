# S06 — VWAP 2σ Mean Reversion (giorni balance)

**Famiglia:** Mean-reversion statistica di sessione · **Riferimenti research:** 02, 04

---

## 1. Concetto e razionale

Nei giorni classificati *balance* (apertura in valore, IB contenuto, rotazioni), le estensioni
alla banda 2σ del VWAP di sessione sono eccessi statistici rispetto al consenso di prezzo
della giornata: il flusso di esecuzione (algo benchmarkati al VWAP) e il market making
riportano il prezzo verso la media. Si fade l'estensione SOLO con trigger di struttura e SOLO
nel regime giusto — la versione "fade sempre la 2σ" è esplicitamente rigettata (04§7.1).

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES (preferito: mean-reversion più pulita), NQ con size ridotta |
| **Timeframe** | Regime: M15+profilo · Esecuzione: M5 |
| **Bias** | Neutro/rotazionale: si opera *verso il VWAP*, in entrambe le direzioni |
| **Contesto** | Day-type = balance (open in-value, IB ≤ ADR×0.4, nessuna accettazione fuori IB) |
| **Sessione** | 10:30–12:00 e 13:30–15:00 (dopo che il balance è *dimostrato*, mai in apertura) |

## 3. Filtri (il setup È i suoi filtri)

1. **Classificazione balance attiva** alle 10:30: prezzo dentro IB, IB dentro/attorno VA ieri.
2. Nessuna release tier-1 residua in agenda.
3. σ-position ≥ |2.0| E prezzo a ridosso di un riferimento statico (VAH/VAL, PDH/PDL, EQ del
   range multi-day) — la banda da sola non basta.
4. VIX/vol regime non esplosivo (no giorni |gap| > 1×ADR).

## 4. Sequenza di ingresso (short da +2σ)

1. Prezzo tocca/eccede +2σ dentro la fascia oraria, su riferimento statico.
2. **Trigger:** sweep P6 di uno swing interno M5 sopra la banda + close M5 di ritorno sotto
   la banda (mini-MSS M1 accettato come anticipo).
3. Ingresso a mercato al close del trigger o limit al retest della banda.
4. Max 2 tentativi/giorno totali sul setup (non per lato).

## 5. Conferme

- Delta/CVD in esaurimento sull'estensione (se disponibile) (+1) · coincidenza con EQH/pool
  (+½) · NQ/ES non confermano l'estensione (SMT) (+½).

## 6. Stop

Oltre l'estremo dell'estensione + P16; cap 0.25×ADR (se serve di più, il movimento non è
"un'estensione in balance" ma qualcos'altro → NT).

## 7. Target

- TP1: banda 1σ — 1/2 + BE (il "pagatore" del setup).
- TP2: VWAP (il target naturale della tesi).
- NO runner oltre il VWAP: la tesi finisce lì per definizione (chi vuole il lato opposto
  deve ri-triggerare il setup speculare).

## 8. Invalidazione

- Regime: accettazione fuori IB (2 close M15) in qualunque momento = il giorno non è più
  balance → setup OFF per il resto della giornata.
- Post-entry: close M5 oltre lo sweep = stop.
- Time-stop 45': la reversione che non parte non è una reversione.

## 9. Esempio pratico (ES, giorno balance)

- 10:30: open in-value ✓, IB 6238–6252 (14 pt = 0.33×ADR ✓). VA ieri 6234–6255.
- 11:20: estensione a 6259.75 = +2.1σ, a ridosso di VAH-extension/PDH 6260.50 ✓.
- Sweep M5 dello swing 6258.25 → high 6260.25, close 6256.50 sotto banda (trigger ✓).
- Short 6256.50, stop 6261.25 (+P16) = 4.75 pt. TP1 6250.75 (1σ, 1.2R) 1/2+BE ·
  TP2 6246.25 (VWAP, 2.2R) fill 12:05. ~+1.7R ponderato.

## 10. Errori frequenti

1. Fade della 2σ in trend day (il classificatore di regime non è opzionale: È il setup).
2. Fade "nudo" a metà strada senza riferimento statico.
3. Target avidi oltre il VWAP (la tesi non lo prevede).
4. Rischio troppo largo per "dare spazio" (cap 0.25×ADR: qui la size è tutto).
5. Operarlo in apertura (il balance non è ancora dimostrato prima delle 10:30).

## 11. Note quantitative attese

- **Frequenza:** 2–4/settimana (i balance day sono ~50-60% ma il tocco 2σ+riferimento no).
- **Profilo:** WR alto atteso 55–65%, avg win ~1.3R → expectancy +0.2/+0.4R (profilo
  "tanti piccoli", opposto a S01/S03).
- **Robustezza:** dipende interamente dal classificatore di regime; le bande sono
  deterministiche.
- **Nota per la matrice:** expectancy unitaria bassa + rischio di coda in regime-switch
  (il balance che diventa trend a metà trade) → candidata a ruolo secondario/da valutare
  contro il costo di complessità.
