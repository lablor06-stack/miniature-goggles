# 06 — UI Design System (v2.1.0)

> Il sistema visivo dell'indicatore, documentato come design system: token, gerarchia,
> lifecycle di visibilità e razionali. Vincolo fondante del redesign: **la logica non è
> stata toccata** — Logic Layer (engine, array, segnali, alert, statistiche) identico a
> v2.0.0; è cambiato solo ciò che viene *disegnato*, *quando* e *come*.

---

## 1. Principio

> *Il grafico deve rispondere in un colpo d'occhio a sei domande: bias? liquidità? setup
> attivo? entry? stop? target. Tutto ciò che non contribuisce a una di queste sei risposte
> non merita pixel.*

Riferimenti estetici: LuxAlgo (gerarchia cromatica), Bookmap (informazione = luminosità),
Sierra/TradingLite (sobrietà istituzionale), built-in premium TradingView (tipografia).

## 2. Palette (5 colori semantici — token)

| Token | Hex | Semantica | Uso esclusivo |
|---|---|---|---|
| `COL_BULL` | `#4c9a70` | Rialzista | zone di supporto, MSS ▲, entry long, target |
| `COL_BEAR` | `#c65b5b` | Ribassista | zone di resistenza, MSS ▼, entry short, stop |
| `COL_NEUT` | `#787b86` | Contesto | struttura secondaria, opens, AVWAP, EQ, OTE, MIT |
| `COL_VWAP` | `#e0e3eb` | Riferimento primario | SOLO il VWAP (unico oggetto "bianco") |
| `COL_LIQ` | `#d4b96a` | Liquidità | SOLO pool e marker SWEEP |

Regole: nessun colore saturo; la gerarchia si costruisce con la **trasparenza** (fresco
60-88, contesto 45-65, sfondo 90-97), non con nuovi colori. Le zone flip (Breaker/IFVG) si
distinguono con il **bordo tratteggiato**, non con un sesto colore.

## 3. Modalità di display

| | EXECUTION (default) | STANDARD | ANALYSIS |
|---|---|---|---|
| Missione | decidere ADESSO | operatività con contesto | studio/review |
| Liquidità | solo PDH · PDL · AS.H · AS.L | tutti i pool | tutti i pool |
| Zone | **1 FVG + 1 OB per lato** (champion) | tutte le attive | tutte le attive |
| Struttura | SOLO l'evento corrente (1) | MSS + BOS (storia cap) | + choch, ext completa |
| VWAP | linea sola | linea sola | + bande ±1σ/±2σ |
| Key opens / AVWAP | nascosti | visibili | visibili |
| Etichette zone/EQ | nessuna | sì | sì |
| Dashboard | 9 righe | 9 righe | + blocco statistiche |

**Champion rendering:** gli array restano pieni (il Signal Engine sceglie tra TUTTE le zone,
identico a prima); in Execution viene *disegnata* solo la migliore per slot — FVG: la più
recente attiva per lato; OB: la più vicina al prezzo per lato. Quando ne nasce una migliore,
la precedente sparisce dal grafico (resta nell'engine).

## 4. Lifecycle di visibilità adattiva (req. "adaptive visibility")

```
IDLE          → liquidità (4 pool) + VWAP + EQ                    (~10 oggetti)
SWEEP         → + marker SWEEP giallo sul raid                    (evento, non stato)
MSS           → + evento strutturale corrente + champion zones
SETUP ARMED   → pannello LONG/SHORT·grade·RR·E/S/T + 3 linee + OTE;
                le zone champion SI RITIRANO (il grafico è il trade)
FILLED        → pannello marcato FILLED; OTE rimossa
STOP/TARGET/EXPIRY → tutto rimosso → ritorno a IDLE pulito
```

La quantità di informazione **decresce** man mano che la decisione converge: quando sei nel
trade, il grafico mostra il trade.

## 5. Oggetti: budget e ciclo di vita

| Oggetto | Nasce | Muore (ELIMINATO, mai sbiadito) |
|---|---|---|
| Pool ray + label | creazione pool (se whitelisted in Exec) | sweep (istantaneo) · accettazione (istantaneo) · sostituzione |
| Zona (box + CE) | champion pass (Exec) / creazione (Std+) | fill · invalidazione · seconda rottura post-flip · età |
| Evento struttura | evento confermato | superamento cap (Exec: 1) |
| Pannello setup + linee E/S/T + OTE | arm | invalidazione · scadenza · (OTE anche al fill) |
| SMT | divergenza qualificata | cap FIFO |

Budget tipico on-chart in Execution: **~15-25 oggetti totali** (v1: ~200; v2.0 Standard:
~60-90) → riduzione del rumore ≫ 60% richiesto.

## 6. Tipografia e dashboard

- Un solo pannello, **senza bordi** (`border_width=0, frame_width=0`), fondo `#0b0e13` @24.
- 9 righe fisse: `IFTS/mode · Bias · Regime · P-D · VWAP σ · SMT · Setup · Grade · RR`.
- Chiavi in grigio neutro a sinistra, valori semantici a destra; refresh a chiusura barra.
- Pannello setup: label unica multiriga `LONG A+ / RR 2.8 / E / S / T`, testo bianco su
  campitura direzionale @12 — l'unico elemento "forte" del grafico, per design.

## 7. Etichette (−80%)

Ammesse SOLO: `SWEEP` (marker evento), `MSS` (evento corrente), pannello SETUP, sorgenti dei
4 pool di Execution (PDH/PDL/AS.H/AS.L), `SMT`. Tutto il resto è visual-only. In Standard+
tornano le etichette di zona e EQ (contesto).

## 8. Nota di conformità logica (per la due-diligence)

Invariati al bit: condizioni di segnale, detection FVG/OB/sweep, SMT, VWAP, grading,
statistiche RQ, tutte le 7 alertcondition e i payload dinamici. Unica correzione collaterale
(documentata nel CHANGELOG): la memoria interna dei pool swept ora ha lo stesso orizzonte
TTL in ogni modalità — in v2.0 la modalità Analysis, conservando i ghost, allungava di
fatto la memoria del filtro SMT "near pool": la logica non deve dipendere dalla modalità di
visualizzazione.
