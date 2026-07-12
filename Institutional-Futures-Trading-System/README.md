# IFTS — Institutional Futures Trading System

**Versione:** 1.0.0 · **Data:** Luglio 2026 · **Mercati:** ES / NQ (CME) · **Stack:** Pine Script v6 + Python 3

> Sistema di trading discrezionale-sistematizzato per futures su indici americani, costruito con
> standard da desk istituzionale: ricerca documentata, strategie confrontate quantitativamente,
> manuale operativo, indicatore Pine Script v6 completamente modulare, piano di backtesting con
> Monte Carlo e walk-forward, tooling Python per l'analisi delle performance.

---

## 1. Cos'è questo progetto

IFTS è un **framework operativo completo** per il trading intraday e swing su **ES (E-mini S&P 500)**
e **NQ (E-mini Nasdaq-100)**. Non è "un indicatore con delle frecce": è la codifica end-to-end di un
processo decisionale — dalla teoria (ICT/Smart Money Concepts, Auction Market Theory, Volume Profile,
Order Flow) fino all'esecuzione, alla misurazione e al miglioramento continuo.

Il progetto è stato costruito **come se fosse destinato alla due-diligence di una prop firm o di un
hedge fund**: ogni scelta è motivata, ogni claim è classificato per livello di evidenza, ogni regola
è scritta in modo testabile e falsificabile.

### Principi di progettazione

1. **Falsificabilità** — ogni regola è definita in modo abbastanza preciso da poter essere backtestata.
   Se una regola non è testabile, è opinione, non sistema.
2. **Onestà statistica** — distinguiamo esplicitamente tra: (a) evidenza accademica/peer-reviewed,
   (b) evidenza empirica interna riproducibile, (c) folklore di trading da validare. Nessun claim
   di win-rate viene presentato senza fonte o pipeline di verifica.
3. **Modularità** — ogni concetto (struttura, liquidità, zone, VWAP, sessioni, SMT…) è un modulo
   indipendente sia nella documentazione sia nel codice, attivabile/disattivabile singolarmente.
4. **Ridondanza minima** — un concetto vive in un solo posto ed è referenziato ovunque serva.
5. **Processo > previsione** — il sistema gestisce rischio e aspettativa matematica; non pretende
   di prevedere il mercato.

---

## 2. Struttura del repository

```
Institutional-Futures-Trading-System/
├── README.md                    ← questo file (mappa del progetto)
├── CHANGELOG.md                 ← storico versioni
├── LICENSE.md                   ← licenza proprietaria
│
├── Research/                    ← FASE 1 — studio approfondito (13 documenti)
│   ├── 00_Research_Synthesis.md         ← sintesi: cosa regge, cosa no, gerarchia di evidenza
│   ├── 01_Market_Microstructure_Futures.md
│   ├── 02_Auction_Market_Theory.md
│   ├── 03_Volume_Profile_Market_Profile.md
│   ├── 04_VWAP_Anchored_VWAP.md
│   ├── 05_Order_Flow_CVD_Delta_Footprint_DOM.md
│   ├── 06_Swing_Structure_BOS_CHOCH_MSS.md
│   ├── 07_Liquidity_Sweeps_Internal_External.md
│   ├── 08_Order_Blocks_Breaker_Mitigation.md
│   ├── 09_FVG_IFVG.md
│   ├── 10_Premium_Discount_Equilibrium_Fibonacci.md
│   ├── 11_Sessions_Kill_Zones.md
│   └── 12_SMT_Divergence.md
│
├── Documentation/               ← architettura, convenzioni, glossario, review
│   ├── 00_Conventions_and_Specs.md      ← ⚠ LEGGERE PER PRIMO: parametri canonici del sistema
│   ├── 01_System_Architecture.md
│   ├── 02_Glossary.md
│   ├── 03_Red_Team_Review.md            ← FASE 7 — critica sistematica + correzioni
│   └── 04_Optimization_Report.md        ← FASE 8 — ottimizzazioni applicate
│
├── Strategy/                    ← FASI 2-3 — strategie e selezione
│   ├── Strategies/S01..S10_*.md         ← 10 strategie complete
│   ├── 20_Comparison_Matrix.md          ← matrice comparativa multi-criterio
│   └── 21_IFTS_Core_Model.md            ← strategia definitiva (sintesi delle migliori)
│
├── Manual/                      ← FASE 4 — manuale operativo
│   ├── 00_Philosophy_and_Rules.md
│   ├── 01_Playbook_Checklists.md        ← pre-market, ingresso, gestione, uscita
│   ├── 02_Risk_and_Money_Management.md
│   ├── 03_Psychology_and_Errors.md
│   ├── 04_KPI_and_Review_Routines.md    ← KPI, diario, routine G/S/M
│   └── 05_Prop_Firm_Adaptation.md
│
├── Pine/                        ← FASE 5 — codice Pine Script v6
│   ├── README.md                        ← installazione, architettura codice, limiti piattaforma
│   ├── Indicators/
│   │   └── IFTS_Master.pine             ← indicatore flagship, tutti i moduli integrati
│   └── Modules/                         ← moduli standalone (à-la-carte)
│       ├── IFTS_Structure.pine          ← swing, BOS, CHoCH, MSS, EQH/EQL, sweep
│       ├── IFTS_Zones.pine              ← OB, Breaker, Mitigation, FVG, IFVG
│       ├── IFTS_VWAP_Suite.pine         ← VWAP sessione + bande, AVWAP multipli
│       ├── IFTS_Sessions_KZ.pine        ← sessioni, kill zone, livelli chiave, OR
│       ├── IFTS_PremiumDiscount.pine    ← range dealing, equilibrium, OTE
│       └── IFTS_SMT.pine                ← divergenze SMT ES/NQ/YM
│
├── Testing/                     ← FASE 6 — validazione
│   ├── 00_Backtesting_Plan.md           ← protocollo completo (in/out-of-sample, WFA)
│   ├── 01_Metrics_Definitions.md        ← definizioni formali di ogni metrica
│   ├── 02_Monte_Carlo_Protocol.md
│   └── 03_Robustness_Sensitivity.md
│
├── Journal/                     ← diario operativo
│   ├── Journal_Template.md              ← template trade-per-trade
│   ├── journal_schema.csv               ← schema dati per i tool Python
│   └── Daily_Weekly_Review_Template.md
│
├── Statistics/                  ← misurazione
│   ├── 00_KPI_Definitions.md
│   └── Tools/
│       ├── kpi_calculator.py            ← calcola tutti i KPI dal journal CSV
│       ├── monte_carlo.py               ← simulazione Monte Carlo (bootstrap)
│       └── sample_trades.csv            ← dataset di esempio per testare i tool
│
├── Examples/                    ← trade walkthrough completi
│   ├── EX01_Sweep_Reversal_Long.md
│   ├── EX02_Continuation_Short.md
│   └── EX03_No_Trade_Day.md
│
└── Images/                      ← diagrammi SVG (architettura, setup, sessioni)
```

---

## 3. Percorso di lettura consigliato

| Chi sei | Percorso |
|---|---|
| **Trader operativo** | `Documentation/00_Conventions` → `Strategy/21_IFTS_Core_Model` → `Manual/` → `Pine/README` → `Examples/` |
| **Risk manager / due diligence** | `Research/00_Research_Synthesis` → `Strategy/20_Comparison_Matrix` → `Testing/` → `Documentation/03_Red_Team_Review` |
| **Sviluppatore** | `Documentation/01_System_Architecture` → `Pine/README` → `Pine/Indicators/IFTS_Master.pine` |
| **Studio completo** | Ordine numerico: Research → Strategy → Manual → Pine → Testing |

---

## 4. Il sistema in una pagina

**Tesi centrale.** Nei futures su indici il prezzo si muove tra pool di liquidità (stop clusterizzati
sopra/sotto massimi e minimi di riferimento) e aree di valore (volume). I momenti di massima
inefficienza — e quindi di massimo vantaggio per un trader direzionale — si concentrano in finestre
temporali precise (kill zone) quando il mercato *rivisita un pool di liquidità, lo assorbe e inverte
con displacement*. Il sistema opera solo in quel contesto, in direzione del bias di timeframe
superiore, con rischio fisso e target su liquidità opposta.

**Il modello operativo (IFTS Core Model, dettagli in `Strategy/21`):**

1. **Contesto** (H4/H1): bias direzionale da struttura esterna + posizione nel range (premium/discount).
2. **Narrativa** (M15): quale pool di liquidità è stato preso? Quale è il target opposto (draw on liquidity)?
3. **Timing**: solo kill zone London / NY AM (+ finestra PM regolamentata).
4. **Innesco** (M1–M5): sweep di liquidità → Market Structure Shift con displacement → zona di ingresso
   (FVG/OB/Breaker) in premium/discount corretto.
5. **Conferme opzionali**: SMT ES/NQ, reazione a VWAP/AVWAP, contesto Volume Profile.
6. **Rischio**: 0.25–0.50% per trade, stop strutturale, R:R minimo 2:1, gestione a regole fisse.
7. **Misurazione**: ogni trade nel journal → KPI settimanali → Monte Carlo trimestrale.

---

## 5. Avvertenze e limiti (leggere prima dell'uso)

- **Nessuna garanzia di profitto.** Il trading di futures comporta rischio di perdita superiore al
  capitale depositato. Questo materiale è ricerca/formazione, non consulenza finanziaria.
- **I numeri vanno guadagnati.** Le statistiche citate in `Research/` sono classificate per livello
  di evidenza; i tassi di successo del modello vanno validati con la pipeline in `Testing/` sui
  **propri** dati ed esecuzione prima di rischiare capitale reale.
- **Il codice Pine è un supporto decisionale**, non un sistema automatico: disegna, misura e
  allerta; la decisione resta al trader secondo il manuale.

---

## 6. Stato del progetto

| Fase | Contenuto | Stato |
|---|---|---|
| 1 | Ricerca (13 documenti) | ✅ Completa |
| 2 | 10 strategie | ✅ Completa |
| 3 | Matrice + strategia definitiva | ✅ Completa |
| 4 | Manuale operativo | ✅ Completo |
| 5 | Pine Script v6 (master + 6 moduli) | ✅ Completo |
| 6 | Piano backtesting + tool Python | ✅ Completo (tool testati) |
| 7 | Red team review | ✅ Completa (correzioni applicate) |
| 8 | Ottimizzazione | ✅ Completa |
| 9 | Struttura finale | ✅ Completa |

*Convenzione linguistica: documentazione in italiano (audience primaria); codice e identificatori in
inglese (standard industriale, portabilità); termini tecnici di dominio mantenuti in inglese.*
