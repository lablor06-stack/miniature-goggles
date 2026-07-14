# S04 — Turtle Soup Daily (sweep di estremi n-day, swing)

**Famiglia:** Reversal swing multi-day · **Riferimenti research:** 07§4 (Connors-Raschke), 06, 10

---

## 1. Concetto e razionale

Versione swing dello sweep-reversal: il falso breakout di un **massimo/minimo a 20 giorni**
(o dell'estremo della settimana precedente) intrappola i breakout trader e i CTA trend-following
di breve. Regole storicamente pubblicate (Street Smarts, 1995 — uno dei pochi setup del corpus
con backtest pubblici storici, E2). Adattamento IFTS: conferma di struttura intraday (MSS M15)
invece del fade cieco, holding 1–4 giorni... ma **il perimetro v1 del sistema è intraday-only
(flat 15:50)**, quindi S04 è valutata *come candidata* nella sua forma swing E nella variante
intraday (chiusura giornaliera del pezzo residuo).

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ (meglio ES: meno rumore) |
| **Timeframe** | Riferimenti: Daily · Setup: H1/M15 · Esecuzione: M15 |
| **Bias** | Contro l'espansione che fa il nuovo estremo n-day; idealmente pro-bias del range settimanale (fade del bordo) |
| **Contesto** | Nuovo 20-day high/low (o PWH/PWL) violato di poco e rigettato; mercato in range di medio periodo (non in trend impulsivo daily) |
| **Sessione** | Trigger solo in KZ (il daily extreme viene spesso preso in NY AM) |

## 3. Filtri

1. Il breakout deve violare l'estremo di ≤ 0.5×ADR (violazioni profonde = vero breakout).
2. Il daily NON deve essere in trend impulsivo (≥ 3 daily BOS consecutivi nella direzione
   del breakout = NT: non si fa turtle soup dentro un treno).
3. Distanza dal EQ del range multi-day ≥ 1×ADR (spazio per il mean-revert).
4. No settimane di earnings-cluster mega-cap per NQ.

## 4. Sequenza di ingresso (short su falso massimo)

1. Il daily segna nuovo 20-day high / viola PWH.
2. Intraday (KZ): sweep P6 sul livello + **MSS ribassista M15** con displacement.
3. Ingresso limit sul FVG/OB M15 del displacement (premium del range intraday).
4. Un solo tentativo per evento (l'evento è raro e "one-shot").

## 5. Conferme

- SMT sul nuovo estremo (ES fa HH, NQ no) — su questo setup è la conferma principe (+1).
- Excess/coda evidente sul daily (+½) · CVD divergente, se disponibile (+½).

## 6. Stop

Sopra il massimo dello sweep + P16 (su M15 la distanza è tipicamente 0.3–0.6×ADR: size
ridotta di conseguenza — il rischio % resta P11).

## 7. Target

- TP1: EQ del range intraday / primo pool interno daily — 1/2 + BE.
- TP2: EQ del range daily multi-day (il baricentro da cui il breakout è partito).
- (Variante swing, fuori perimetro v1: runner multi-day verso il lato opposto del range con
  stop a BE — documentata per completezza e per la valutazione in matrice.)

## 8. Invalidazione

- Pre-entry: accettazione sopra l'estremo (2 close H1) = breakout vero → NT definitivo.
- Post-entry: nuovo HH intraday sopra lo sweep = stop (non si media).
- Time-stop: se dopo 2 ore il prezzo non ha raggiunto TP1, uscita a mercato (il fade che non
  parte subito degrada).

## 9. Esempio pratico (ES)

- 20-day high 6288.75 (e PWH 6290.00 adiacente: pool composito).
- Martedì 09:52: high 6293.50 (violazione 4.75 pt ≈ 0.35×ADR ✓), NQ resta sotto il suo PWH
  (SMT ✓). Close M15 6285.25 = sweep ✓.
- 10:10: MSS M15 (close sotto swing 6279.50 con body 2.2× ✓), FVG M15 6281.75–6285.50.
- Short limit 6283.50 (CE), stop 6294.25 (high +3 tick) = 10.75 pt.
- TP1 6266 (EQ intraday, 1.6R) 1/2+BE · TP2 6249.50 (EQ range daily, 3.2R) raggiunto il
  giorno dopo — nella variante v1 intraday si chiude 15:50 a 6259 (~+2.3R medio).

## 10. Errori frequenti

1. Fade del breakout **senza** sweep+MSS (il turtle soup originale "cieco" ha edge decaduto:
   serve la conferma).
2. Farlo in trend daily impulsivo (filtro 2 ignorato = i disastri peggiori del setup).
3. Stop "stretto" sotto il livello invece che sopra lo sweep (viene preso dal secondo test).
4. Aspettarsi frequenza: è un setup da 2–5 occasioni/mese.
5. Trascurare il rollover: l'estremo n-day va letto sulla serie corretta.

## 11. Note quantitative attese

- **Frequenza:** 2–5/mese per strumento (bassa).
- **Profilo:** WR 45–55%, avg win 2R (intraday) / 3R+ (swing) → expectancy +0.4/+0.8R.
- **Robustezza:** buona sul concetto (E2 storica); la versione moderna dipende dalla qualità
  della conferma.
- **Limite strutturale per la Fase 3:** frequenza troppo bassa per essere primaria; overlap
  concettuale totale con S01 (stesso meccanismo, ancora daily) → naturale candidata a
  *filtro/contesto* più che a strategia autonoma.
