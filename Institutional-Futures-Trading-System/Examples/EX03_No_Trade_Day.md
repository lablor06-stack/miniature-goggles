# EX03 — Giornata No-Trade: il trade più difficile del sistema

> Il 20-40% delle giornate finisce NT. Questo esempio mostra una giornata in cui *tutto
> sembra quasi-tradabile* e il sistema dice no — con il conto economico del perché.

## 1. Pre-market (07:55)

- **Calendario:** FOMC 14:00 ⚠⚠ → per regola (Manual/01 §2.4): AM operativa solo con
  setup A+ conclamato, PM solo post-14:30 Setup C ridotto.
- **HTF:** daily dentro un range di 5 giorni; H4 alterna MSS in entrambe le direzioni ogni
  2 giorni. **Bias: NEUTRO** (→ size −1 grade su tutto, R: Manual/01 §1.2).
- **Mappa:** ON range di 9 pt (21% ADR) incollato all'EQ del range multi-day. Pool sopra
  (ONH 6234, PDH 6237.75 vicinissimi) e sotto (ONL 6225, PDL 6222.50): **tutto a meno di
  0.4×ADR** → nessun DOL a ≥ 2R di distanza da nessun punto ragionevole d'ingresso.
- **Narrativa scritta:** *"Pre-FOMC classico: compressione attorno all'EQ. Nessuno scenario
  primario onesto. NT salvo raid AM di PDH/PDL con sequenza A+ completa E R:R ≥ 2 reale.
  PM: eventuale C post-14:30."*

## 2. Le tentazioni della mattinata (e i motivi del no)

| Ora | Cosa appare | Perché NON è un trade |
|---|---|---|
| 09:41 | Wick sotto ONL 6225, ritorno in barra | Pool rank 3 preso, MA: MSS successivo senza displacement (body 0.9× media — P4 ✗) e DOL sopra a 12 pt con stop a 7 → R:R 1.7 < 2 (A6 ✗) |
| 10:20 | "FVG bullish pulito" M5 | Fuori sequenza: nessuno sweep alle spalle (A3 ✗) — un FVG in mezzo al range è liquidità interna, non un ingresso |
| 11:12 | EQH sopra 6234/6234.25 spazzati, close di ritorno | Sequenza A short parte... MA sono le 11:12: KZ AM chiusa (A1 ✗). Il journal registra `missed=0` — non è un setup mancato, è un setup *inesistente* per definizione |
| 12:30 | Drift sotto VWAP "che sembra un breakdown" | Lunch (R2) + pre-FOMC: il grind-through senza displacement è il caso 3 della tassonomia sweep (Research/07 §1.2) = zero informazione |

Alle 10:30 il classificatore segna **CHOP** (range < 0.5×ADR, alternanza interna) —
conferma quantitativa di ciò che la mappa diceva alle 07:55.

## 3. FOMC e chiusura

- 14:00: statement → spike 22 pt up, reversal completo in 11 minuti (classico whipsaw).
  Chi "aveva ragione" sulla direzione è stato stoppato lo stesso: senza struttura post-
  annuncio non c'è geometria, solo moneta lanciata con leva.
- 14:30-15:00: nessuna sequenza C qualificata (il primo raid post-FOMC accetta invece di
  rigettare → esito 2, espansione... che muore subito: doppia manipolazione = struttura
  non-PO3, Setup C ✗).
- 15:00: giornata chiusa NT. Journal: riga `NT` con motivo, review 5'.

## 4. Il conto economico del no

- Costo della giornata NT: 0R (+ un po' di pazienza).
- Costo atteso delle 4 tentazioni (stime conservative dai profili dei rispettivi errori):
  −0.4R (R:R insufficiente pagato a WR pieno), −0.5R (FVG fuori sequenza ≈ coin flip con
  costi), −0.3R (fuori KZ), −0.8R (whipsaw FOMC) ≈ **−2R evitati** = uno stop giornaliero
  intero.
- Su 250 giornate/anno, ~60-80 NT: la differenza tra un sistema in verde e lo stesso
  sistema in rosso sta in gran parte QUI, non nei trade presi.

## 5. Note didattiche

1. Il NT non è assenza di lavoro: pre-market, monitoraggio leggero, journal — il *filtro*
   è il prodotto del lavoro.
2. Ogni tentazione respinta cita una regola specifica (A1/A3/A4/A6, R2): "non mi piaceva"
   non è mai la motivazione — le regole decidono, l'umore no.
3. La riga NT nel journal è ciò che rende misurabile la selettività (KPI "NT discipline",
   Manual/04 §2.1): un sistema che non logga i no non può dimostrare di saper dire no.
