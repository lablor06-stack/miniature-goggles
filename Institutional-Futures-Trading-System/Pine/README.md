# Pine/ — Codice Pine Script v6

## 1. Contenuto

| File | Ruolo |
|---|---|
| `Indicators/IFTS_Master.pine` | **Flagship v2.0.0**: tutti gli engine integrati, display-priority a 3 modalità, Signal Engine A/B, dashboard, 7 alert azionabili, statistiche RQ |
| `Modules/IFTS_Structure.pine` | Standalone: swing, BOS/CHoCH/MSS, displacement |
| `Modules/IFTS_Zones.pine` | Standalone: FVG/IFVG, OB/Breaker/Mitigation (lifecycle v2: zone morte rimosse) |
| `Modules/IFTS_VWAP_Suite.pine` | Standalone: VWAP sessione + bande vw-σ, RTH VWAP, AVWAP |
| `Modules/IFTS_Sessions_KZ.pine` | Standalone: sessioni ET, kill zone, key opens, PDH/PDL/PWH/PWL, IB |
| `Modules/IFTS_PremiumDiscount.pine` | Standalone: dealing range, EQ, P/D, OTE |
| `Modules/IFTS_SMT.pine` | Standalone: SMT con filtro correlazione **sui rendimenti** |

**Perché Master autonomo + moduli autonomi (niente library):** deploy senza frizione, limiti
oggetti separati, duplicazione limitata alle primitive e dichiarata
(`Documentation/01_System_Architecture.md` §3.1). Library condivisa = roadmap v3.

## 2. Installazione

1. TradingView → Pine Editor → New blank indicator → incolla → Save → Add to chart.
2. Simboli: `CME_MINI:ES1!` / `CME_MINI:NQ1!`. TF raccomandati: **M1–M5** (esecuzione),
   M15 (setup). Sopra H1 i moduli di sessione si disattivano da soli.
3. Advanced → *Stop buffer*: 2 tick per ES, 4 per NQ (P16).
4. Scegli la **Display mode** in General (sotto).

## 3. Display modes (v2.1 — il cuore della UX)

| Modalità | Per chi | Cosa mostra |
|---|---|---|
| **Execution** *(default)* | Decidere adesso | Solo le 6 risposte (bias·liquidità·setup·entry·stop·target): pool primari PDH/PDL/Asia, **1 FVG + 1 OB per lato** (champion), VWAP nudo, evento strutturale corrente, pannello setup E/S/T. ~15-25 oggetti |
| **Standard** | Operatività con contesto | + tutti i pool, BOS, testo zone, key opens, AVWAP |
| **Analysis** | Studio e review | + choch, struttura esterna completa, bande VWAP ±σ, blocco statistiche RQ |

**Champion rendering (Execution):** gli array delle zone restano pieni per il Signal Engine
(logica identica); viene *disegnata* solo la migliore per slot — FVG più recente attiva e
OB più vicino al prezzo, per lato. Una zona migliore sostituisce la precedente sul grafico.

**Smart visualization (tutte le modalità):** liquidità consumata e zone morte vengono
**eliminate all'istante** (niente fading, niente ghost). Il marker giallo `SWEEP` è l'unica
traccia del raid; la memoria interna del pool swept dura `Performance → Swept pool memory`
(serve al filtro SMT), invisibile.

**Visibilità adattiva (Execution):** idle → liquidità+VWAP · sweep → marker · MSS → zone
champion · setup armato → SOLO pannello e linee E/S/T (le zone si ritirano) · fine trade →
chart pulito.

## 4. Architettura (ordine di valutazione)

```
INPUTS → DISPLAY-PRIORITY → PRIMITIVES/CLOCK → SWINGS → STRUCTURE → LIQUIDITY → ZONES
→ RANGE → VWAP → SMT → BIAS/REGIME → SIGNAL ENGINE (A/B fattorizzato) → STATS → DASHBOARD
→ ALERTS → PLOTS
```

Ogni engine scrive solo nel proprio stato; il Signal Engine legge tutto, non scrive nulla.
Modulo spento ⇒ zero disegni, zero `request.security`, zero logica non-primitiva.

## 5. Alert (ridisegnati in v2: 7, tutti azionabili)

| Alert | Condizioni combinate | Uso |
|---|---|---|
| Setup A LONG / SHORT armed | KZ + sweep P6 (rank) + MSS + zona FVG + gate P/D + R:R ≥ min | "Vieni a eseguire" |
| Setup B LONG / SHORT trigger | regime trend + bias HTF + zona flip inedita + trigger + DOL | idem, continuation |
| Qualified sweep in KZ | sweep + rank ≤ soglia + dentro KZ + cooldown 5 barre | Pre-avviso: davanti allo schermo prima del possibile MSS |
| Kill zone opened | inizio London / NY AM | Sveglia di sessione (payload dinamico se attivato in Alerts) |
| Any setup (A or B) | unione dei 4 | Un solo alert per il telefono |

Il canale `alert()` dinamico (attivabile nel gruppo Alerts) allega entry/stop/target/grade/RR
— pronto per webhook. **Rimossi rispetto a v1** (restano come informazione on-chart o
grading, non come alert): FVG nuovi, BOS/choch, zone touch, flip, SMT isolata, cross VWAP.

## 6. Scelte tecniche

| Scelta | Motivo |
|---|---|
| Eventi solo su `barstate.isconfirmed` | Zero repaint logico |
| Dashboard aggiornata solo a chiusura barra (chiavi scritte una volta) | Elimina il costo per-tick (v1: ~40 chiamate API/tick) |
| Oggetti `extend.right` + lifecycle con rimozione | Zero manutenzione per-barra; il chart si pulisce da solo |
| `lookahead_off` ovunque; livelli datati da periodi chiusi `[1]` | Nessun bias di futuro |
| `America/New_York` esplicita in ogni `time()` | Kill zone DST-safe |
| Correlazione SMT **sui rendimenti** | Sui livelli è spuriamente ≈1 (fix C1, Red Team) |
| Un flip per vita della zona | Niente flip-flop né doppi conteggi statistici |
| Funzioni senza side-effect su globali | Stato condiviso solo via array/oggetti/ritorni |
| Nessun delta/CVD sintetico | TradingView non ha bid/ask tick storico affidabile: non si finge |

## 7. Limiti dichiarati

- **Il Signal Engine non è il sistema completo:** implementa i livelli 5-6 dello stack;
  calendario, bias, mappa e narrativa restano al trader (Manuale). Un alert senza pre-market
  alle spalle è un input, non un ordine.
- I pivot confermano N barre dopo (lag strutturale, prezzo della riproducibilità).
- Statistiche = campione delle barre caricate dal chart; il proxy "open fuori valore" usa il
  range del giorno prima (VA vera non disponibile in Pine).
- Gate P/D del Signal Engine sul dealing range del TF corrente (il modello lo definisce M15).
- Pool PDH/PDL creati alla chiusura della prima barra della nuova sessione (1 barra di lag).
- L'attesa dell'inducement (Core Model §3.3) resta procedura umana.
- Setup B parte a IB completa (10:30), più conservativo della finestra 10:00 del modello.
- Le finestre in barre (Advanced) cambiano significato col TF — vedere i tooltip.
- Su simboli senza volume il VWAP si disattiva senza errori.

## 8. Migrazione (breaking changes)

**v1 → v2.0:** input riorganizzati in 12 gruppi (reimpostare le personalizzazioni; i default
replicano P1-P17); i 17 alert v1 sostituiti dai 7 attuali (lista §5); `statsOn` → modalità
Analysis; `sigUsePm` rimosso (il PM è playbook manuale Setup C).

**v2.0 → v2.1 (solo visuale, logica intoccata):** modalità "Focus" sostituita da
"**Execution**" (nuovo default); ghost rimossi ovunque (eliminazione immediata); `newsOk`
rimosso con la relativa riga dashboard; dashboard ridotta a 9 righe fisse (+stats in
Analysis); palette a 5 colori (VWAP bianco, liquidità giallo tenue, flip = bordo
tratteggiato); bande VWAP solo in Analysis. Alert e semantica dei segnali invariati: gli
alert esistenti continuano a funzionare senza ricrearli.

## 9. Checklist di compilazione/aggiornamento

- [ ] Compila senza warning su ES1! M5
- [ ] Le tre display mode cambiano correttamente densità visiva e righe dashboard
- [ ] Oggetti sotto i cap con 20k barre caricate (Standard: attesi ~60-90)
- [ ] I 7 alert compaiono nel menu Create Alert
- [ ] DST check: NY AM KZ parte alle 08:30 ET in inverno e in estate
- [ ] Zone riempite/invalidate spariscono (Standard) o diventano ghost (Analysis)
- [ ] Su simbolo senza volume: nessun errore runtime
- [ ] Su TF H4+: moduli sessione auto-off senza errori
