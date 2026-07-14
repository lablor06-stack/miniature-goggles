# 00 — Convenzioni e Specifiche Canoniche

> **Questo documento è la fonte unica di verità (single source of truth) per tutti i parametri,
> orari, soglie e definizioni numeriche del sistema.** Ricerca, strategie, manuale e codice Pine
> DEVONO usare questi valori. Se un valore va cambiato, si cambia QUI e si propagano i riferimenti.

---

## 1. Strumenti e specifiche contrattuali

| Parametro | ES (E-mini S&P 500) | NQ (E-mini Nasdaq-100) | MES (Micro) | MNQ (Micro) |
|---|---|---|---|---|
| Exchange | CME (Globex) | CME (Globex) | CME | CME |
| Tick size | 0.25 punti | 0.25 punti | 0.25 punti | 0.25 punti |
| Tick value | $12.50 | $5.00 | $1.25 | $0.50 |
| Valore punto | $50 | $20 | $5 | $2 |
| Simboli TradingView | `CME_MINI:ES1!` | `CME_MINI:NQ1!` | `CME_MINI:MES1!` | `CME_MINI:MNQ1!` |
| Scadenze | Mar/Giu/Set/Dic (H,M,U,Z) | idem | idem | idem |
| Rollover operativo | ~8 giorni prima della scadenza (seguire il volume) | idem | idem | idem |

**Nota rollover:** per backtesting usare serie continue back-adjusted; per livelli di lungo periodo
(settimanali/mensili) verificare sempre che il livello non cada in un gap di rollover.

**Correlati per SMT:** ES ↔ NQ (primario), YM (`CBOT_MINI:YM1!`) come tie-breaker.

---

## 2. Fuso orario e orari canonici

**Tutti gli orari del sistema sono in ET (America/New_York), con DST automatico.**
Nel codice Pine: `"America/New_York"` esplicito in ogni chiamata `time()`/`timestamp()`.

| Evento | Orario ET | Note |
|---|---|---|
| Apertura Globex | 18:00 (dom–gio) | Inizio trading day CME |
| Sessione Asia | 20:00 – 00:00 | Definizione operativa IFTS |
| Sessione London | 02:00 – 05:00 | Coincide con London Kill Zone |
| Pre-market NY | 07:00 – 09:30 | News window (08:30!) |
| **RTH (cash)** | **09:30 – 16:00** | Regular Trading Hours equity |
| Initial Balance | 09:30 – 10:30 | Prima ora RTH |
| NY Lunch | 12:00 – 13:00 | NO-TRADE di default |
| Chiusura cash / settlement | 16:00 | MOC imbalance 15:50+ |
| Halt manutenzione | 17:00 – 18:00 | Mercato chiuso |

### Kill Zone (finestre operative autorizzate)

| Kill Zone | Orario ET | Uso nel sistema |
|---|---|---|
| Asia KZ | 20:00 – 00:00 | Solo osservazione/range building. Non si opera. |
| **London KZ** | **02:00 – 05:00** | Operativa (Setup A/B) — opzionale per chi è in fuso EU |
| **NY AM KZ** | **08:30 – 11:00** | **Finestra primaria del sistema** |
| NY Lunch | 12:00 – 13:00 | Vietata |
| NY PM KZ | 13:30 – 16:00 | Operativa con size ridotta (playbook PM) |

**Macro/Silver Bullet windows** (finestre di precisione, sottoinsiemi delle KZ):
03:00–04:00 · 10:00–11:00 · 14:00–15:00 ET.

### Livelli temporali di riferimento (key opens)

- **True Day Open:** 00:00 ET · **Daily Open (Globex):** 18:00 ET · **RTH Open:** 09:30 ET
- **Weekly Open:** domenica 18:00 ET · **Monthly Open:** primo giorno utile 18:00 ET

---

## 3. Gerarchia dei timeframe

| Ruolo | Timeframe | Funzione |
|---|---|---|
| **Bias / HTF** | Daily, H4 | Struttura esterna, range dealing, draw on liquidity settimanale |
| **Contesto / MTF** | H1, M15 | Narrativa di sessione, pool di liquidità, PD array rilevanti |
| **Esecuzione / LTF** | M5, M1 | Sweep, MSS, ingresso su FVG/OB |

Regola di coerenza: **si esegue su LTF solo nella direzione concordata da HTF+MTF.**
Il conflitto HTF↔MTF è un filtro di no-trade, non un'opinione da arbitrare al volo.

---

## 4. Parametri canonici del sistema (usati in docs + Pine)

| # | Parametro | Valore default | Definizione operativa |
|---|---|---|---|
| P1 | Swing interno (pivot) | 3/3 barre | `pivothigh/low(3,3)` — struttura interna LTF |
| P2 | Swing esterno (pivot) | 8/8 barre | struttura esterna / range dealing |
| P3 | Tolleranza EQH/EQL | 0.10 × ATR(14) | due estremi "uguali" se distano ≤ soglia |
| P4 | Displacement | body ≥ 1.5 × media(body, 20) | candela di rottura con corpo dominante |
| P5 | FVG minimo | 0.25 × ATR(14) | gap più piccoli = rumore, ignorati |
| P6 | Sweep valido | wick oltre il livello + close di ritorno entro 3 barre | definizione testabile di "raid" |
| P7 | Zona OTE | 62% – 79% del leg | retracement ottimale nel leg di displacement |
| P8 | Equilibrium | 50% del dealing range esterno | soglia premium/discount |
| P9 | Mitigazione zona | tocco = mitigata; close oltre = invalidata/flip | ciclo di vita OB/FVG |
| P10 | ATR di riferimento | ATR(14) sul TF corrente | normalizzatore universale |
| P11 | Rischio per trade | 0.25% (base) – 0.50% (A+) | % dell'equity, mai nozionale |
| P12 | R:R minimo | 2.0 | sotto 2R il trade non si prende |
| P13 | Stop giornaliero | −2R oppure −1.0% equity | il primo che scatta chiude la giornata |
| P14 | Stop settimanale | −4R | chiude la settimana |
| P15 | Max trade/giorno | 3 (max 2 nella stessa KZ) | anti-overtrading |
| P16 | Buffer stop | 2 tick ES / 4 tick NQ oltre il livello strutturale | anti-spike |
| P17 | Trailing HTF | swing M5 dopo TP1 | vedi gestione, Manual/02 |

**Regola di modifica:** ogni cambiamento a P1–P17 richiede: (a) motivazione scritta,
(b) re-test su dati out-of-sample, (c) bump di versione nel CHANGELOG.

---

## 5. Convenzioni di misura

- **R (unità di rischio):** perdita monetaria a stop pieno del trade. Tutti i risultati si esprimono
  in R, mai in $ o punti, per confrontabilità.
- **Espressione livelli:** i prezzi ES/NQ si citano sempre al quarto di punto (es. 5843.25).
- **Win rate, PF, expectancy:** definizioni formali in `Testing/01_Metrics_Definitions.md`.
- **Campione minimo:** nessuna conclusione statistica con n < 30 trade per setup; confidenza
  operativa da n ≥ 100.

---

## 6. Gerarchia di evidenza (usata in tutta la Research)

| Livello | Etichetta | Significato |
|---|---|---|
| **E1** | Evidenza accademica | Peer-reviewed o dataset pubblici replicabili |
| **E2** | Evidenza empirica interna | Backtest riproducibile con la pipeline `Testing/` |
| **E3** | Consenso di practitioner | Ampiamente usato dai desk, meccanismo plausibile, non verificato |
| **E4** | Folklore | Claim retail non verificato — da trattare come ipotesi |

Ogni claim nei documenti di ricerca porta l'etichetta del suo livello. **Nessuna regola del sistema
può basarsi solo su E4.**

---

## 7. Convenzioni di codice (Pine Script v6)

- `//@version=6`, indentazione 4 spazi, nomi `camelCase` per variabili, `SCREAMING_SNAKE` per costanti,
  prefisso di modulo per gli input (`msShowBos`, `fvgMinAtr`…).
- Ogni modulo: blocco di input con `group` dedicato + flag `enable` → **zero calcoli e zero disegni
  quando disattivo** (v6 valuta `and` in modo lazy: sfruttarlo).
- Oggetti grafici gestiti tramite array con cap esplicito (FIFO delete) — mai affidarsi al garbage
  collector della piattaforma per la semantica.
- `barstate.isconfirmed` per ogni segnale/alert: **nessun repaint logico**. Dove un elemento è
  intrinsecamente repaint-prone (pivot), il lag di conferma è dichiarato nel commento e nel tooltip.
- `request.security()` sempre con `lookahead=barmerge.lookahead_off`; HTF via
  `dynamic_requests=true` solo se il modulo è attivo.
- Commenti in inglese; header di modulo standardizzato (vedi `Pine/README.md`).

---

## 8. Naming dei setup (usato ovunque)

| Codice | Nome | Descrizione breve |
|---|---|---|
| **A** | Sweep Reversal | Sweep di liquidità esterna → MSS → entry su PD array (modello primario) |
| **B** | Continuation | Trend day: pullback su Breaker/IFVG/OB in direzione del bias |
| **C** | PM Fade/Continuation | Playbook pomeridiano regolamentato (13:30–15:00) |
| **NT** | No-Trade | Giornata esclusa da filtri (news, range, conflitto TF) |
