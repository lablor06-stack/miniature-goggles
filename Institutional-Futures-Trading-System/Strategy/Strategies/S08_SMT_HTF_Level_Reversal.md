# S08 — SMT Divergence Reversal su livello HTF

**Famiglia:** Reversal cross-market · **Riferimenti research:** 12, 07, 06

---

## 1. Concetto e razionale

Reversal costruito *attorno* alla divergenza SMT come segnale principale (non come semplice
conferma): a un livello HTF pesante (PWH/PWL, estremo di dealing range daily, nPOC lontano),
uno solo dei due indici correlati fa il nuovo estremo. La mancata conferma su pool di rank
alto, in KZ, con MSS sul proprio strumento = trade contro l'estremo non confermato.
È S01 con l'ordine dei fattori invertito: qui il *livello HTF + SMT* è il cuore, lo sweep
intraday è il contorno.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | Si opera lo strumento **più debole/forte** (quello che NON ha confermato guida la direzione; si trada quello col setup tecnico migliore) |
| **Timeframe** | Livello: Daily/Weekly · Divergenza: M15 pivot · Esecuzione: M5 |
| **Bias** | Contro l'estremo non confermato (reversal), idealmente pro-bias del range HTF superiore |
| **Contesto** | Livello HTF rank 1-2 (`07`§1.1) raggiunto; correlazione rolling ≥ 0.7 |
| **Sessione** | London KZ o NY AM KZ |

## 3. Filtri

1. **Correlazione regime** ≥ 0.7 (rolling 20 su M15) — obbligatorio (12§1.2).
2. Pivot confermati P1 su *entrambi* gli strumenti, finestra ±5 barre.
3. Niente earnings mega-cap in settimana per la gamba NQ.
4. Il livello deve essere il primo test (no terzo/quarto tocco: il pool è già consumato).

## 4. Sequenza di ingresso (short su SMT bearish a PWH)

1. ES viola il PWH (nuovo HH), NQ non conferma (LH) — pivot confermati.
2. Sullo strumento scelto: sweep P6 sul proprio livello + MSS M5 ribassista con displacement.
3. Ingresso limit su FVG/OB M5 del displacement (premium).
4. One-shot per livello.

## 5. Conferme

- Tie-break YM concorde (2-su-3) (+1) · excess/coda daily al livello (+½) ·
  σ-position > +1.5 (+½).

## 6. Stop

Sopra l'estremo dello sweep sul proprio strumento + P16.

## 7. Target

- TP1: EQ del range intraday — 1/3 + BE.
- TP2: liquidità interna daily (ultimo swing low M15/H1 rilevante) — 1/3.
- Runner: DOL daily opposto con trail M15 (i reversal da livello weekly hanno spazio);
  flat 15:50 (v1).

## 8. Invalidazione

- Pre-entry: il "ritardatario" conferma (NQ fa HH anche lui) = divergenza annullata → NT.
- Pre-entry: accettazione sopra il livello (2 close M15) → NT.
- Post-entry: stop; nessun re-entry sullo stesso livello.

## 9. Esempio pratico

- PWH ES 6291.50; NQ PWH 22710.
- Mercoledì 10:05: ES 6295.75 (HH ✓ oltre PWH), NQ high 22688 → LH ✓ (pivot M15 confermati
  10:35, finestra ±5 ✓). Correlazione rolling 0.84 ✓.
- Si sceglie di shortare NQ (il debole). Sweep locale: NQ ha spazzato il suo swing M15
  22665 nel movimento; MSS M5 alle 10:50 (close 22641 sotto swing con body 2.4× ✓),
  FVG M5 22652–22666.
- Short 22659 (CE), stop 22694 (high 22688 + 4 tick +margine sweep) = 35 pt.
- TP1 22608 (EQ intraday, 1.5R) · TP2 22540 (swing H1, 3.4R) → +2.2R ponderato.

## 10. Errori frequenti

1. SMT su wick non confermati (repaint mentale — l'errore n.1 del concetto).
2. Ignorare il regime settoriale: la "divergenza" nei giorni di rotazione è fondamentale,
   non tecnica (filtro 1).
3. Livelli minori (swing interni): l'SMT lì è rumore.
4. Tradare lo strumento sbagliato (quello senza setup tecnico pulito).
5. Vedere l'SMT e saltare la conferma di struttura ("ha diverso, entro"): senza MSS non c'è
   trigger.

## 11. Note quantitative attese

- **Frequenza:** 2–4/mese (bassa: livelli HTF + divergenza + KZ).
- **Profilo:** WR atteso 50–60% (la selettività paga), avg win 2.2R → expectancy +0.5/+0.8R
  sui pochi eventi.
- **Robustezza:** buona CON il filtro correlazione; fragile senza.
- **Nota per la matrice:** expectancy unitaria eccellente ma frequenza da "condimento";
  overlap forte con S01 (quando l'SMT c'è, S01 la usa già come conferma) → candidata
  all'assorbimento in S01 come variante di grade massimo.
