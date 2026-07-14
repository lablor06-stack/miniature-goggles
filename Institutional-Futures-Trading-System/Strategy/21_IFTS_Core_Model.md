# 21 — IFTS Core Model (Strategia Definitiva)

> Sintesi della Fase 3: **due motori regime-esclusivi + un playbook pomeridiano ridotto**,
> un solo vocabolario di trigger, un solo schema di rischio. Ogni regola qui è normativa:
> il Manuale la proceduralizza, il Pine la disegna/allerta, il Journal la misura.
> Parametri canonici P1–P17 in `Documentation/00_Conventions_and_Specs.md`.

---

## 0. Il modello in una frase

**Nelle kill zone, opera il lato giusto del raid:** se il mercato prende liquidità e la
rigetta (sweep→MSS), fai il reversal verso il pool opposto (Setup A); se prende liquidità e
la accetta (breakout con accettazione), ricarica col flusso sulle zone flip (Setup B); se non
fa né l'uno né l'altro, non esiste trade.

---

## 1. Stack decisionale comune (vale per A, B, C)

```
LIVELLO 0 — CALENDARIO   news tier-1? half-day? roll? → perimetro orario del giorno
LIVELLO 1 — BIAS HTF     struttura esterna D/H4 + posizione nel dealing range HTF
LIVELLO 2 — MAPPA        pool (rank, `07`§1.1) sopra/sotto + zone HTF + VA/POC/nPOC + key opens
LIVELLO 3 — REGIME       classificazione progressiva della giornata (§2)
LIVELLO 4 — NARRATIVA    quale pool è stato/verrà preso? quale DOL? (ipotesi scritta pre-market)
LIVELLO 5 — TRIGGER      solo in KZ: sequenza A o B (§3-4)
LIVELLO 6 — RISCHIO      grade → size; R:R ≥ 2 ex-ante; stop strutturale
LIVELLO 7 — GESTIONE     regole fisse (§6); flat 15:50
LIVELLO 8 — MISURA       journal completo entro fine giornata
```

## 2. Classificatore di regime (aggiornamento continuo, decisioni alle 09:45 / 10:30)

| Segnale (pesato al momento della lettura) | Voto verso |
|---|---|
| Open dentro VA ieri + overnight nel range di ieri | **Rotation** (→ A) |
| Open fuori VA con accettazione (nessun rientro >15') | **Trend** (→ B) |
| IB extension con displacement entro 10:30 | **Trend** (+1) |
| Rientro in VA dopo tentativo fuori | **Rotation** (+1) |
| Pullback M5 < 50% dei leg + VWAP monotono | **Trend** (+1) |
| Range Asia+London > 80% ADR già speso | **Esaurimento** (→ cautela/NT) |
| Range totale < 40% ADR a mezzogiorno + alternanza CHoCH interni | **Chop** (→ NT) |

Regole di mutua esclusione: **Trend dichiarato (≥3 voti) spegne il Setup A** per quel lato;
**Rotation con raid compiuto spegne il Setup B** fino a nuova accettazione. In dubbio: NT.

## 3. SETUP A — Sweep Reversal (motore primario)

**Ereditato da:** S01 (corpo) + S03 (narrativa AMD, key opens) + S04 (scala weekly) +
S08 (grading SMT) + S02 (seconda finestra).

### 3.1 Condizioni necessarie (tutte)

- **A1.** KZ attiva (London 02–05 / NY AM 08:30–11 / seconda finestra 10–11).
- **A2.** Nessuna release tier-1 entro ±15' (post-release: ok dal +15').
- **A3.** Sweep P6 di un pool rank ≥ 4 (wick oltre + close di ritorno ≤ 3 barre M5).
- **A4.** MSS su M1–M5: close oltre l'ultimo swing interno CONTRO la direzione del raid,
  con displacement P4, che lascia FVG (≥P5) e/o breaker.
- **A5.** Ingresso disponibile in zona (CE del FVG / bordo breaker / OB) nella metà
  favorevole del dealing range M15 (V6) e in OTE del leg (P7, tolleranza).
- **A6.** DOL identificato con R:R ≥ 2.0 dallo stop strutturale (V7).
- **A7.** Regime ≠ Trend contrario dichiarato.

### 3.2 Grading (determina la size, P11)

| Conferma | Punti |
|---|---|
| SMT al raid (filtro correlazione OK) | +1 |
| Sweep multi-pool (≥2 pool in un colpo) | +1 |
| Order-flow absorption (se disponibile) | +1 |
| Raid oltre estremo weekly (scala S04) | +1 |
| VWAP reclaim/rigetto concorde durante MSS | +0.5 |
| Zona composita (FVG⊂OB/breaker) | +0.5 |

**Grade:** B = 0 punti (solo condizioni necessarie) → 0.25% · A = 1–2 → 0.35% · A+ = ≥2.5 → 0.50%.

> **Nota anti-overfitting (Red Team M1/M4):** i pesi del grading sono convenzioni ragionate,
> non stime — per questo determinano SOLO la size, mai la validità del trade. Il journal
> registra ogni componente separatamente (RQ-2/5/10): dopo n≥100 i pesi si ristimano dai
> dati con procedura R19. Le confluenze devono essere **ortogonali** (fonti informative
> diverse): zone sovrapposte della stessa famiglia contano una volta sola (composite +0.5).

### 3.3 Esecuzione

- Limit al CE del FVG di displacement (o bordo zona); validità fino a fine KZ.
- Stop: oltre l'estremo dello sweep ± P16. Mai dentro la zona.
- Se il ritracciamento non arriva: trade mancato. Se un IDM ovvio sta tra prezzo e zona:
  attendere il suo sweep (07§1.3).
- Seconda finestra (10–11): stessa narrativa, primo FVG utile della finestra (eredità S02),
  UNA sola volta.

### 3.4 Varianti

- **A-London:** identico in London KZ; target = liquidità di Asia/PD; size max 0.35%
  (liquidità minore).
- **A-Weekly (ex S04):** pool di rank 1-2 (PWH/PWL, 20-day) → grading +1, gestione identica,
  runner autorizzato fino a DOL daily.

## 4. SETUP B — Continuation (motore secondario)

**Ereditato da:** S09 (corpo) + S05 (innesco ORB fuori-value) + S10 (ancora AVWAP London).

### 4.1 Condizioni necessarie

- **B1.** Regime Trend dichiarato (≥3 voti §2) **oppure** innesco precoce: open fuori VA +
  break dell'OR con displacement e retest tenuto (eredità S05) **oppure** London accettata
  + tenuta AVWAP-London (eredità S10).
- **B2.** Bias H4 concorde con la direzione del flusso.
- **B3.** Pullback che consegna su zona flip qualificata: breaker > IFVG > OB+FVG di
  continuazione (ordine di preferenza da 08§9.2); zona nel discount del *leg corrente*.
- **B4.** Trigger: mini-sweep M1 di uno swing interno dentro/alla zona + close M5 a favore.
- **B5.** DOL residuo ≥ 2R (misura: 2×IB, estremo weekly, nPOC).
- **B6.** Orario: 10:00–15:00 (mai in apertura; il regime va prima dimostrato), no lunch
  entry 12–13.

### 4.2 Grading

VWAP first-touch coincidente (+1) · correlato concorde (+0.5) · zona composita (+0.5) ·
delta pro-trend in contrazione sul pullback (+0.5, se disponibile).
B = 0.25% · A = 0.35% · A+ = 0.50%.

### 4.3 Esecuzione

Limit al bordo zona o market al close del trigger B4; stop sotto zona/swing del pullback
− P16 (il più stretto strutturale); max 3 ingressi/giorno (P15), mai due sulla stessa zona.

## 5. SETUP C — PM Playbook (13:30–15:00, ridotto)

- Replica di A (raid del lunch-range/AM extreme) o B (continuazione post-lunch del trend AM)
  **con size dimezzata rispetto al grade** e target massimo = liquidità AM (niente runner
  oltre, eccetto trend day conclamato).
- Nei giorni FOMC: SOLO post 14:30, solo Setup A sul primo raid post-annuncio, size 0.25%.
- Flat tassativo 15:50 (MOC).

## 6. Gestione della posizione (comune, regole fisse)

| Fase | Regola |
|---|---|
| **TP1** | A: EQ del range / primo pool interno · B: nuovo estremo marginale — chiusura 1/3 (A) o 1/2 (B), stop a BE+1 tick |
| **TP2** | A: DOL della narrativa — chiusura 1/3 · B: —"— o 2×IB |
| **Runner** | Trail su swing M5 confermati (P17); upgrade a M15 se trend day dichiarato |
| **Time-stop** | A: 90' senza TP1 → riduzione 1/2 · B: MSS M15 contrario → flat immediato |
| **Fine giornata** | Flat 15:50 sempre |
| **Eccezione flash-news** | Uscita discrezionale ammessa e loggata come `exit_news` |

Vietato sempre: mediare, allargare lo stop, rimuovere il TP, re-entry oltre 2 tentativi/lato,
trade fuori KZ, size oltre il grade.

## 7. Rischio (sintesi; dettagli Manual/02)

P11 (0.25/0.35/0.50% per grade) · P13 stop giornaliero −2R o −1% · P14 settimanale −4R ·
P15 max 3 trade/giorno · dopo 2 stop consecutivi: stop operativo di sessione.

## 8. Mappatura Modello → Pine → Journal (contratto di coerenza)

| Regola | Modulo Pine | Campo journal |
|---|---|---|
| KZ (A1/B6) | Sessions & KZ (`kzActive`) | `killzone` |
| Sweep P6 (A3) | Liquidity Engine (`sweepEvent`, grade) | `sweep_grade` |
| MSS+displacement (A4) | Structure Engine (`mssEvent`) | `trigger_type` |
| FVG/CE/IFVG (A5/B3) | Zone Engine (`fvgArray`, stato) | `entry_zone` |
| Breaker/OB (B3) | Zone Engine (`obArray`, flip) | `entry_zone` |
| P/D + OTE (A5) | Range Engine (`pdPosition`) | `pd_position` |
| Bias HTF (L1/B2) | Trend Filter (HTF request) | `bias_htf` |
| SMT grading | SMT Engine (+corr filter) | `smt` |
| VWAP/AVWAP conferme | VWAP Suite (`sigmaPos`) | `vwap_sigma` |
| Regime §2 | Dashboard (euristica day-type) | `day_type` |
| Segnale composito A/B | Signal Engine (alert `IFTS A/B`) | `setup` + `grade` |
| Esiti/statistiche | Statistics module | `result_r`, MAE/MFE |

## 9. Che cosa NON è il modello (per il red team e la due-diligence)

- Non è una previsione del mercato: è un **filtro di asimmetrie** con gestione a regole.
- Non promette win-rate: promette **misurabilità** (ogni condizione è binaria e loggata).
- Non è automatizzabile as-is (i livelli 0-4 richiedono giudizio umano proceduralizzato);
  l'automazione parziale è roadmap post-validazione (300+ trade).
- I numeri attesi (§10) sono **ipotesi da validare** con la pipeline `Testing/`, non claims.

## 10. Profilo atteso aggregato (ipotesi di lavoro, da validare)

| Metrica | Atteso | Fonte dell'ipotesi |
|---|---|---|
| Trade/settimana | 3–6 (A: 2-4, B: 1-3, C: 0-2) | Frequenze S01/S09/S05 filtrate |
| WR | 42–55% | Profili citati nei singoli setup |
| Avg win / avg loss | ≥ 2.0R / ~0.95R (time-stop riduce full-loss) | Struttura TP/trailing |
| Expectancy | +0.35/+0.6R per trade | Derivata; da verificare (Testing §5) |
| Max DD atteso (Monte Carlo preliminare) | 6–10R su 100 trade al P95 | `Statistics/Tools/monte_carlo.py` |
| Ore-schermo/giorno | 2.5–4.5 | KZ coperte |

**Kill-switch di modello:** se dopo 100 trade reali l'expectancy è < +0.1R o il MaxDD reale
supera il P95 Monte Carlo, il sistema va in revisione (non in "ottimizzazione dei parametri":
prima si verifica l'esecuzione contro le checklist, poi si riapre la ricerca).
