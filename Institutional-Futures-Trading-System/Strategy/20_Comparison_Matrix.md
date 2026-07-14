# 20 — Matrice Comparativa delle Strategie

> Metodo: valutazione multi-criterio pesata + analisi di ridondanza (overlap) + copertura di
> regime. La selezione NON premia la strategia "migliore in assoluto" ma il **portafoglio di
> setup minimo che copre i regimi con la minima ridondanza** — è un problema di costruzione
> di portafoglio, non di gara.

---

## 1. Criteri e pesi

| Criterio | Peso | Perché questo peso |
|---|---|---|
| **C1 — Solidità del razionale** (evidenza E1-E3 del meccanismo) | 20% | Un edge senza meccanismo muore in silenzio e non si può diagnosticare |
| **C2 — Expectancy attesa per trade** (profilo WR×RR) | 18% | Il motore economico |
| **C3 — Frequenza** (occasioni/settimana) | 12% | Senza campione non c'è né reddito né statistica |
| **C4 — Testabilità/oggettività delle regole** | 15% | Vincolo V8; ciò che non si misura non si migliora |
| **C5 — Robustezza parametrica** (sensibilità a P1-P17) | 12% | Anti-overfitting |
| **C6 — Geometria del rischio** (compatibilità con V6/V7, qualità stop) | 10% | Determina la sopravvivenza nei drawdown |
| **C7 — Complessità cognitiva in esecuzione** (inversa) | 8% | L'esecutore è umano: la complessità si paga in errori |
| **C8 — Dipendenza da input esterni** (dati/piattaforme; inversa) | 5% | Vendibilità e portabilità |

Scala 1–5 per criterio. Punteggio = Σ(voto × peso).

> **Nota di metodo (Red Team M2):** i voti C2/C3 derivano da stime a priori (Fase 2), non da
> backtest — un bias ottimistico *comune* non altera l'ordinamento relativo (tutte le
> candidate usano lo stesso metro), ma i livelli assoluti restano ipotesi: la rete di
> sicurezza sui livelli è nelle soglie pre-registrate di `Testing/00` §5.

## 2. Matrice dei punteggi

| Strategia | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | **Totale** |
|---|---|---|---|---|---|---|---|---|---|
| **S01 Sweep Reversal** | 5 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | **4.24** |
| **S02 Silver Bullet** | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | **4.17** |
| **S03 PO3 Intraday** | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 5 | **3.71** |
| **S04 Turtle Soup Daily** | 5 | 4 | 1 | 4 | 4 | 4 | 4 | 5 | **3.79** |
| **S05 ORB + Profile** | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | **3.81** |
| **S06 VWAP 2σ Reversion** | 4 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | **3.16** |
| **S07 VA Rotation 80%** | 3 | 2 | 2 | 3 | 3 | 2 | 4 | 4 | **2.71** |
| **S08 SMT HTF Reversal** | 4 | 5 | 1 | 4 | 4 | 5 | 3 | 4 | **3.81** |
| **S09 Trend Continuation** | 4 | 5 | 3 | 4 | 4 | 4 | 3 | 5 | **4.09** |
| **S10 London AVWAP** | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 5 | **3.55** |

### Note di voto (i giudizi non ovvi)

- **S01 C1=5:** unico setup il cui meccanismo poggia direttamente sui tre pilastri E1
  (clustering stop, cascata-e-ritorno, finestre di partecipazione).
- **S06 C2=2:** expectancy unitaria strutturalmente bassa (target al VWAP) + coda negativa
  nel regime-switch: il balance che diventa trend colpisce proprio quando si è a mercato.
- **S07 C6=2:** conflitto cronico con V7 (R:R < 2 con stop strutturale) — emerso già
  nell'esempio del suo stesso documento.
- **S08 C2=5 ma C3=1:** la miglior expectancy unitaria del lotto, su 2-4 eventi/mese.
- **S09 C2=5:** i runner nei trend day producono la coda destra della distribuzione — è
  l'unico setup con avg win potenziale > 3R.
- **S04 C3=1:** 2-5 eventi/mese, e la variante swing è fuori perimetro v1.

## 3. Analisi di ridondanza (overlap concettuale)

| Coppia | Overlap | Diagnosi |
|---|---|---|
| S01 ↔ S02 | **Alto** | Stessa narrativa (sweep→MSS→DOL), timing diverso: S02 è la *seconda entrata* di S01 |
| S01 ↔ S03 | **Alto** | Stesso evento (raid) con ancore diverse (pool vs open): S03 = S01 + filtro bias daily + riferimento open |
| S01 ↔ S04 | **Alto** | Stesso meccanismo su orizzonte diverso (daily): S04 = S01 con pool di rank 1 |
| S01 ↔ S08 | **Alto** | S08 = S01 grade A+ (SMT obbligatoria invece che opzionale) |
| S09 ↔ S10 | **Medio-alto** | Entrambe continuation su zone flip; differiscono solo nel regime detector |
| S05 ↔ S09 | **Medio** | S05 è spesso la *prima entrata* di un trend day che S09 cavalca |
| S06 ↔ S07 | **Medio** | Entrambe mean-reversion in balance verso un riferimento di valore |
| S01 ↔ S09 | **Zero (complementari)** | Regimi mutuamente esclusivi: la coppia copre l'intraday |

**Conclusione dell'analisi:** il lotto contiene in realtà **tre famiglie**:
1. **Reversal da liquidità** (S01, S02, S03, S04, S08) — cinque vestiti dello stesso corpo;
2. **Continuation in imbalance** (S05, S09, S10) — tre rilevatori dello stesso regime;
3. **Mean-reversion al valore** (S06, S07) — la famiglia più debole sotto i vincoli IFTS.

## 4. Copertura di regime

| Regime di giornata | Frequenza stimata | Coperto da |
|---|---|---|
| Balance / rotazione con raid mattutino | ~45-55% | Famiglia 1 (Setup A) |
| Trend day / iniziativa | ~15-25% | Famiglia 2 (Setup B) |
| Balance stretto senza raid utile | ~15-25% | **Nessuno → NT by design** |
| News-driven / caotico | ~10% | **Nessuno → NT by design** |

La scelta di lasciare due regimi scoperti è deliberata: sono i regimi in cui nessun setup del
lotto ha meccanismo (il "non fare nulla" è la posizione a expectancy massima).

## 5. Decisioni

### Eliminate (con motivo)

| Strategia | Decisione | Motivo |
|---|---|---|
| **S07 VA Rotation** | ❌ Eliminata | Punteggio minimo (2.71); conflitto cronico con V7; il suo contenuto informativo (accettazione in VA) sopravvive come *filtro di regime* |
| **S06 VWAP 2σ** | ❌ Eliminata come strategia | Expectancy debole + coda negativa da regime-switch; le bande σ sopravvivono come *contesto* (σ-position nel journal e dashboard) |
| **S04 Turtle Soup** | ❌ Assorbita | È S01 quando il pool è di rank 1 (estremo n-day/PWH): diventa la variante "A-Weekly" del modello, non un setup separato |
| **S08 SMT Reversal** | ❌ Assorbita | È S01 a grade massimo: l'SMT resta la conferma che promuove ad A+ |
| **S02 Silver Bullet** | ✅ Assorbita *con ruolo* | Diventa la **seconda finestra d'ingresso** del modello (entry tardiva della stessa narrativa) |
| **S03 PO3** | ✅ Assorbita *con ruolo* | Fornisce al modello il **layer narrativo** (AMD) e il riferimento midnight/RTH open |
| **S10 London AVWAP** | ✅ Assorbita *con ruolo* | Fornisce al playbook continuation l'**ancora AVWAP** e il caso cross-sessione |
| **S05 ORB** | ✅ Promossa (integrata) | Unico rilevatore *precoce* di trend day con supporto E2: diventa il **modulo d'innesco del Setup B** |
| **S01 Sweep Reversal** | ✅ **Promossa: spina dorsale del Setup A** | Miglior punteggio, meccanismo E1, geometria eccellente |
| **S09 Trend Continuation** | ✅ **Promossa: spina dorsale del Setup B** | Complementare esatto di S01; miglior coda destra |

> **Perché il lotto contiene candidate "destinate" a perdere (Red Team D1):** un processo di
> selezione documentato richiede bocciature reali. S06/S07 non sono strawman: sono le
> migliori versioni difendibili delle loro famiglie, e perdono per ragioni *strutturali*
> (conflitto con V7, coda di regime) che il documento di ciascuna già evidenzia. Un lotto
> di sole promosse sarebbe survivorship bias applicato a sé stessi.

### Il razionale di sintesi

Non si "sceglie la migliore": si costruisce il **sistema a due motori + un playbook ridotto**:

- **Setup A (Reversal):** S01 come corpo; S03 fornisce la narrativa AMD e i key opens; S04 la
  scala weekly; S08/SMT il grading; S02 la seconda finestra. → *Un solo modello con varianti,
  un solo campione statistico.*
- **Setup B (Continuation):** S09 come corpo; S05 come innesco precoce (ORB fuori-value);
  S10 come ancora AVWAP cross-sessione. → *Un solo modello di ricarico pro-flusso.*
- **Setup C (PM):** la replica ridotta di A/B nella finestra 13:30–15:00 (già prevista nei
  singoli documenti) con size dimezzata.
- **Mean-reversion pura:** esclusa dal sistema v1. Rientra eventualmente in v2 SOLO se i dati
  del journal (σ-position, RQ-4) dimostreranno un edge residuo non catturato da A/B.

**Vantaggi misurabili della consolidazione:** un unico vocabolario di trigger (sweep P6 +
MSS/BOS), campioni statistici cumulabili (n cresce 3× più in fretta che con 10 sistemi),
zero segnali contraddittori simultanei (A e B sono regime-esclusivi), carico cognitivo
compatibile con esecuzione umana (2 modelli + 1 variante).

→ La specifica completa del modello risultante è in `21_IFTS_Core_Model.md`.
