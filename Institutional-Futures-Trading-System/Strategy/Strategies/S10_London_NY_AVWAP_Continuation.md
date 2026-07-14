# S10 — London → NY Continuation su AVWAP

**Famiglia:** Continuation cross-sessione · **Riferimenti research:** 04, 11

---

## 1. Concetto e razionale

Quando London produce un'espansione direzionale genuina (sweep dell'Asia + displacement che
*accetta*, non rientra), NY AM continua quella direzione più spesso di quanto la inverta —
a condizione che il pullback pre-NY tenga il **prezzo medio dell'iniziativa londinese**,
misurato dall'AVWAP ancorato all'estremo di origine del movimento London. Il setup compra il
primo test dell'AVWAP-London nella finestra 08:30–10:30.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ |
| **Timeframe** | Ancora: estremo London (M15) · Esecuzione: M5 |
| **Bias** | Direzione dell'espansione London; deve concordare con bias H4 |
| **Contesto** | London ha rotto il range Asia con accettazione (2+ close M15 oltre) e chiuso la sua sessione nel terzo estremo del proprio range |
| **Sessione** | Ingresso 08:30–10:30 (deroga alla regola "post-raid": qui il raid È stato London) |

## 3. Filtri

1. **Accettazione London** (non sweep-and-reverse: quello è contesto per S01 opposto!) —
   discriminante: close di sessione London oltre il livello rotto.
2. Bias H4 concorde.
3. Release 08:30: se in agenda, ingresso solo post +15' e solo se la release non ha negato
   il movimento (prezzo ancora oltre l'AVWAP).
4. Distanza dal DOL ≥ 2R residui (il movimento non deve aver già speso l'ADR: London range
   ≤ 60% ADR).

## 4. Sequenza di ingresso (long)

1. AVWAP ancorato al low d'origine dell'espansione London (l'estremo pre-displacement).
2. Pullback NY (il classico "NY reversal della prima mezz'ora") che consegna sull'AVWAP
   ± 0.1×ATR, idealmente dentro un FVG/OB M15 del movimento London (zona composita).
3. Trigger: sweep P6 di uno swing M5 nel pullback + close M5 sopra l'AVWAP.
4. One-shot; se l'AVWAP è perso con accettazione il setup muore (e spesso arma S01 opposto).

## 5. Conferme

- Zona composita AVWAP+FVG London (+1) · midnight open sotto il prezzo (pullback = ritorno
  al "fair" giornaliero) (+½) · session VWAP reclaim simultaneo (+½).

## 6. Stop

Sotto lo swing del pullback − P16; il pullback NY su questo pattern non dovrebbe superare
il 50% del leg London → cap stop 0.3×ADR.

## 7. Target

- TP1: high di London — 1/2 + BE (liquidità ovvia).
- TP2: DOL daily oltre London high (PDH/PWH) — trail M5 sul residuo, flat 15:50.

## 8. Invalidazione

- Pre-entry: NY apre e accetta sotto l'AVWAP (2 close M15) = continuation negata → NT
  (valutare S01 short se c'è pool sopra).
- Post-entry: close M15 sotto AVWAP = uscita concettuale.
- 10:30 senza fill → cancella (la finestra della continuation è la prima ora).

## 9. Esempio pratico (ES)

- Asia 6224–6236. London: sweep 6221.50, poi displacement fino 6254 con 3 close M15 sopra
  Asia high ✓; chiusura sessione London 6251 (terzo superiore ✓). Range London 32 pt ≈ 55%
  ADR ✓. Bias H4 long ✓.
- AVWAP dal low 6221.50 → alle 09:00 passa ~6240.
- 09:36: pullback NY a 6239.50 dentro FVG M15 6237–6242.50 (composita ✓); sweep dello swing
  M5 6240.25 → low 6238, close M5 6243.75 sopra AVWAP ✓.
- Long 6243.75, stop 6235.75 (swing − 2 tick) = 8 pt. TP1 6254 (London high, 1.3R) 1/2+BE ·
  TP2: runner verso PDH 6262.75 → out 6261 (2.2R). ~+1.7R ponderato.

## 10. Errori frequenti

1. Confondere l'espansione London *accettata* con lo sweep londinese *rigettato* (S01
   materiale): è la distinzione close-di-sessione — sbagliarla inverte il trade.
2. Ancorare l'AVWAP a metà movimento (l'ancora è l'estremo d'origine, algoritmico).
3. Entrare al tocco dell'AVWAP senza trigger (il primo tocco spesso viene bucato di qualche
   tick: serve lo sweep+close).
4. Tenerlo oltre il DOL "perché il trend è forte" (il PM ha le sue regole).
5. Usarlo nei giorni di news 08:30 senza il protocollo (filtro 3).

## 11. Note quantitative attese

- **Frequenza:** 2–4/settimana (serve una London direzionale genuina).
- **Profilo:** WR 45–55%, avg win 1.8R → expectancy +0.3/+0.5R.
- **Robustezza:** media: due punti sensibili (definizione di "accettazione London",
  comportamento sulle news 08:30).
- **Nota per la matrice:** concettualmente è "Setup B con ancora di sessione" — forte
  overlap con S09 (stessa famiglia flip/ricarico) ma con regime detector diverso
  (cross-sessione vs day-type). Candidata a fondersi in un unico playbook continuation.
