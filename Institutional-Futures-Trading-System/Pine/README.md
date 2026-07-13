# Pine/ — Codice Pine Script v6

## 1. Contenuto

| File | Ruolo | Righe ~ |
|---|---|---|
| `Indicators/IFTS_Master.pine` | **Flagship**: tutti i moduli integrati, Signal Engine A/B, dashboard, alert, statistiche | ~1300 |
| `Modules/IFTS_Structure.pine` | Standalone: swing, BOS/CHoCH/MSS, displacement | compatto |
| `Modules/IFTS_Zones.pine` | Standalone: FVG/IFVG, OB/Breaker/Mitigation | compatto |
| `Modules/IFTS_VWAP_Suite.pine` | Standalone: VWAP sessione+bande σ, AVWAP multipli | compatto |
| `Modules/IFTS_Sessions_KZ.pine` | Standalone: sessioni, kill zone, key opens, livelli | compatto |
| `Modules/IFTS_PremiumDiscount.pine` | Standalone: dealing range, EQ, P/D, OTE | compatto |
| `Modules/IFTS_SMT.pine` | Standalone: SMT con filtro di correlazione | compatto |

**Perché Master autonomo + moduli autonomi (niente library):** motivato in
`Documentation/01_System_Architecture.md` §3.1 — deploy senza frizione (nessuna dipendenza da
librerie pubblicate), limiti-oggetti separati per modulo, duplicazione limitata alle primitive
e dichiarata. La library condivisa è roadmap v2.

## 2. Installazione

1. TradingView → Pine Editor → New blank indicator.
2. Incollare il contenuto del file `.pine` → Save → Add to chart.
3. Simboli di riferimento: `CME_MINI:ES1!` / `CME_MINI:NQ1!` (o contratto specifico).
4. Timeframe raccomandati: **M1–M5** (esecuzione), **M15** (setup). Il Master funziona su
   qualunque TF ≤ H1; sopra H1 i moduli intraday (sessioni/KZ) si disattivano da soli.
5. Impostare nel gruppo *Liquidity* il buffer tick (P16): 2 per ES, 4 per NQ.

## 3. Architettura del Master (ordine di valutazione)

```
INPUTS → PRIMITIVES (ATR, body, clock NY) → SWINGS (P1/P2) → STRUCTURE (BOS/CHoCH/MSS)
→ LIQUIDITY (pools, EQH/EQL, sweeps P6) → ZONES (FVG/IFVG, OB/BRK/MIT) → RANGE (P/D, EQ, OTE)
→ VWAP/AVWAP → SMT → BIAS HTF → REGIME → SIGNAL ENGINE (Setup A/B) → STATS → DASHBOARD → ALERTS
```

Ogni engine scrive solo nei propri array; il Signal Engine legge tutti e non scrive in nessuno.
Ogni modulo ha il proprio flag `enable`: **spento = zero calcoli non-primitivi e zero oggetti**
(le richieste `request.security` dei moduli spenti non partono, grazie a `dynamic_requests`).

## 4. Scelte tecniche (e loro motivi)

| Scelta | Motivo |
|---|---|
| Eventi solo su `barstate.isconfirmed` | Zero repaint logico: ciò che appare a chiusura barra non cambia più |
| Pivot con lag dichiarato (P1=3, P2=8) | Il lag è il prezzo della riproducibilità (Research 06 §1.1); i trigger operativi usano i *close di rottura*, che non repaintano |
| `lookahead_off` su ogni `request.security` | Nessun bias di futuro |
| Timezone `America/New_York` esplicita ovunque | Kill zone corrette con DST automatico (errore classico eliminato) |
| Oggetti gestiti in array con cap FIFO | Rispetto dei limiti piattaforma (500/tipo) e performance costante |
| Livelli PDH/PDL/PWH/PWL da `security` con `[1]` | Valori del periodo *chiuso*: stabili, non repaintano |
| Nessun "delta/CVD" nel Master | TradingView non fornisce bid/ask tick storico affidabile: non si finge (Research 05 §1.3) |
| Statistiche on-chart (FVG fill, sweep→MSS, finestra degli estremi) | Alimentano RQ-2/7/9 senza software aggiuntivo; NON sono un backtest (ADR-5) |

## 5. Limiti dichiarati (leggere prima di lamentarsi 🙂)

- I pivot confermano N barre dopo: gli swing "si vedono" con ritardo strutturale.
- Le statistiche coprono solo le barre caricate dal chart (~20k barre): campione locale.
- Il classificatore di regime è un'euristica di assistenza — la decisione resta al trader
  (ADR-1); il valore proxy della "value area" usa i quartili del range del giorno precedente
  quando il volume profile non è disponibile via Pine.
- Su simboli senza volume (indici cash) il VWAP si disattiva con avviso in dashboard.

## 6. Convenzioni di codice

Header di modulo standard:

```pine
// ─────────────────────────────────────────────────────────────────────────────
// MODULE N — NAME
// Purpose : ...
// Inputs  : prefix `xx...`   Enable: `xxOn`
// Emits   : events/series consumed by Signal Engine
// ─────────────────────────────────────────────────────────────────────────────
```

Naming: `camelCase` variabili, `f_` prefisso funzioni, `SCREAMING_SNAKE` costanti, prefissi
di modulo per input. Nessun numero magico nel corpo: tutto da input o costante nominata.
I default degli input replicano i parametri canonici P1–P17.

## 7. Checklist di compilazione/aggiornamento

- [ ] Compila senza warning su ES1! M5
- [ ] Nessun oggetto oltre i cap con 20k barre caricate
- [ ] Alert: ogni `alertcondition` presente nel menu Create Alert
- [ ] DST check: KZ NY AM inizia alle 08:30 ET sia in inverno sia in estate
- [ ] Su simbolo senza volume: nessun errore runtime
- [ ] Su TF H4+: moduli sessione auto-off senza errori
