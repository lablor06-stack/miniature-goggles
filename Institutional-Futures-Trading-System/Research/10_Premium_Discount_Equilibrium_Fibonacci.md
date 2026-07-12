# 10 — Premium/Discount, Equilibrium, Fibonacci, OTE

> Premium/Discount è prima di tutto un **framework di posizionamento del rischio**, non uno
> strumento predittivo: comprare nella metà bassa del range significa stop più vicino
> all'invalidazione vera e target più lontano. Questa riformulazione — geometria, non magia —
> è la posizione ufficiale del sistema e va difesa in due-diligence.

---

## 1. Teoria

### 1.1 Dealing range e partizione

- **Dealing range:** dall'ultimo swing esterno low all'ultimo swing esterno high (post-sweep
  quando lo sweep ha ridefinito l'estremo). Convenzione: wick inclusi.
- **Equilibrium (EQ):** 50% del range. **Premium:** sopra EQ. **Discount:** sotto EQ.
- Regola cardine: **long solo in discount, short solo in premium** (rispetto al range del TF
  di setup, M15). Operare "nella metà sbagliata" degrada il setup di un grade e dimezza la size
  — o lo vieta, se anche il bias HTF è contrario.

### 1.2 Perché EQ conta (razionale difendibile)

1. **Schelling point:** il 50% è l'unico livello che ogni partecipante calcola uguale, senza
   parametri → coordinamento spontaneo (stesso motivo dei numeri tondi, E1 per clustering).
2. **Baricentro dell'inventory:** in un range, il prezzo medio scambiato ≈ EQ (per profili
   simmetrici coincide col POC): sopra, i seller di range sono in profitto e ricaricano;
   sotto, i buyer.
3. **Risk-geometry:** dal discount, lo stop (sotto il low) è vicino e il target (liquidità in
   premium/oltre) è lontano → R:R strutturalmente favorevole. Questo vale *anche se EQ non
   avesse alcun potere predittivo* — ed è il motivo per cui la regola è robusta.

### 1.3 Fibonacci e OTE

- **OTE (Optimal Trade Entry):** retracement 62–79% del leg di displacement (P7). Overlay
  ICT sul classico "golden pocket".
- Posizione IFTS sui ratio: l'evidenza accademica sui livelli di Fibonacci come livelli
  *speciali* è debole/negativa (E4 per la "magia dei ratio"). MA: (a) l'effetto focal-point
  esiste (tutti li plottano); (b) la zona 62-79% descrive semplicemente un **pullback profondo
  che non ha rotto la struttura** — concetto solido a prescindere dai numeri; (c) l'OTE
  compatta il rischio (stop oltre lo 0.79→origine è vicino).
- **Uso autorizzato:** fib SOLO sul leg di displacement post-MSS (dal punto d'origine allo
  swing prodotto), SOLO per raffinare l'ingresso dentro zone già valide (FVG/OB dentro OTE =
  confluenza). Fib "a tappeto" su ogni swing: vietato.

### 1.4 Frattalità dei range

Il P/D si valuta su tre scale, in ordine di precedenza: dealing range HTF (D/H4 — il bias),
range del setup (M15 — la regola cardine), range intraday (sessione — il timing). Conflitto
tra scale = riduzione grade o NT. Il **midnight open** (00:00 ET) funge da EQ-proxy intraday
nel modello ICT: sopra = premium giornaliero per gli short, sotto = discount per i long
(uso: tie-breaker di timing, non regola primaria).

---

## 2. Vantaggi

- **Regola anti-chasing strutturale:** vietando i long in premium, il sistema non insegue mai
  l'estensione — l'errore retail più costoso in assoluto sparisce *per costruzione*.
- Costo cognitivo zero (un livello, il 50%) e nessun parametro da ottimizzare → non
  overfittabile.
- Migliora meccanicamente la distribuzione dei R:R realizzati (geometria, §1.2.3).
- Si compone bene: P/D è ortogonale a liquidità/struttura/tempo → le confluenze sono
  informative.

## 3. Svantaggi e limiti

- **Dipende dalla scelta del range:** swing esterni diversi ⇒ EQ diversi. Mitigazione: P2
  fisso (pivot 8) e regola post-sweep — la selezione è algoritmica nel Pine, identica per
  tutti.
- In trend forte il prezzo staziona in premium per giorni (ogni pullback "è caro"): il P/D
  *da solo* farebbe perdere l'intero trend → per questo è subordinato al bias HTF (in trend up
  si comprano i discount *dei range interni*, non si shorta il premium).
- L'OTE ha evidenza debole: usato solo come raffinamento, mai come motivo del trade.
- Falso senso di precisione: 61.8% vs 65% è rumore; si lavora a *zone* (P7 è una fascia).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Clustering di ordini su livelli "calcolabili da tutti" (tondi, 50%) | Osler (2003) per round numbers; focal point theory (Schelling) | **E1/E3** |
| Ritracciamenti profondi (>50%) senza rottura strutturale hanno follow-through migliore dei breakout inseguiti | Coerente con mean-reversion + trend persistence; testabile | **E3 → RQ-8** |
| Potere predittivo specifico dei ratio di Fibonacci vs livelli casuali | Studi pubblici: nessuna significatività robusta | **E4** (per questo: solo raffinamento) |
| Miglioramento del R:R realizzato imponendo P/D discipline | Conseguenza geometrica quasi-tautologica; quantificabile nel journal | **E2 da produrre** (campo `pd_position` nel journal) |

## 5. Contesti favorevoli

- Range conclamato (balance multi-sessione): P/D al massimo del potere — fade degli estremi
  con EQ come primo target.
- Post-MSS: il nuovo dealing range è fresco, EQ significativo, OTE del displacement = ingresso
  ideale Setup A.
- Bias HTF up + prezzo in discount del range M15 + sweep di un pool = allineamento completo
  (il "textbook" del sistema).

## 6. Contesti sfavorevoli

- Trend day / range extension: il range di riferimento si sta ridefinendo — EQ del range morto
  è un livello morto. Segnale: accettazione oltre l'estremo (close multipli fuori).
- Post-news: range pre-news non vincolante.
- Range troppo stretto (< 1.5×ATR): P/D dentro il rumore → non informativo (regime CHOP).

## 7. Errori comuni

1. Fib su ogni swing minore e trade "perché siamo al 61.8%" (numerologia).
2. Ancorare il range a wick di notte illiquida senza rilevanza (il range è degli swing
   *esterni*, P2).
3. Short "perché siamo in premium" contro bias HTF rialzista (il P/D è un filtro, non un
   segnale).
4. Ridisegnare il range intra-trade per giustificare l'aggiunta di size.
5. Pretendere il tocco esatto dell'OTE e perdere il trade per 2 tick (si lavora a zona, con
   la zona d'ingresso — FVG/OB — come riferimento primario).

## 8. Miglioramenti proposti (IFTS)

- **Selezione algoritmica del dealing range** (P2 + post-sweep rule) nel Pine: l'EQ non è
  più un'opinione — è disegnato uguale per chiunque apra il chart.
- **Campo journal `pd_position`** (percentile 0-100 della posizione nel range all'ingresso)
  → dopo 100 trade, curva expectancy vs percentile (RQ-8): dato proprietario di calibrazione.
- **Fib a lista chiusa:** solo 0.5 (EQ del leg), zona OTE 0.62-0.79, e 1.0 — niente ventagli,
  estensioni multiple, time-fib: riduzione del rumore visivo e decisionale.
- **Midnight open come tie-breaker documentato** (non regola primaria) — uso più onesto di un
  concetto E3.

## 9. Implicazioni per il sistema

1. La regola cardine (long-discount/short-premium sul range M15, subordinata al bias HTF) è
   una **condizione di validità** di ogni setup — appare in ogni checklist e nel Signal Engine.
2. EQ è il primo target parziale naturale nei trade range-to-range; il DOL resta il target
   finale.
3. Nel Pine: modulo PremiumDiscount = dealing range auto + EQ + fascia OTE opzionale +
   etichetta P/D in dashboard + percentile per il journal.
