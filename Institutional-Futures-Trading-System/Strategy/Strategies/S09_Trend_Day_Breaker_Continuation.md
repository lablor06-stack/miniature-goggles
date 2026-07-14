# S09 — Trend Day Continuation (Breaker / IFVG)

**Famiglia:** Continuation in imbalance · **Riferimenti research:** 02§1.2, 08, 09

---

## 1. Concetto e razionale

Il 15-25% delle giornate è trend day: iniziativa other-timeframe che non torna sul valore.
In quei giorni i reversal (S01/S06) sono NT o perdenti; il denaro è nel **ricaricare col
flusso** ai pullback. Le stazioni di ricarico di qualità sono le zone flip del movimento:
**breaker block** e **IFVG** (le zone dove i contro-trend sono intrappolati), più l'OB di
continuazione col suo FVG. Il setup formalizza: riconoscere il trend day presto, poi comprare
ogni pullback qualificato finché il regime dura.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | NQ (trend intraday più estesi), ES |
| **Timeframe** | Regime: M15 + day-type · Esecuzione: M5 |
| **Bias** | Direzione del trend day (definita entro le 10:30) |
| **Contesto** | Trend day: open-drive/gap-and-go, IB extension netta, accettazione fuori dalla VA di ieri, VWAP monotono |
| **Sessione** | Ingressi 10:00–15:00 (il primo pullback utile arriva di rado prima delle 10:00) |

## 3. Filtri (riconoscimento del regime — il cuore del setup)

Trend day "dichiarato" quando **≥ 3 su 4**:
1. Apertura fuori VA di ieri con accettazione (nessun rientro > 15').
2. IB extension entro le 10:30 (rottura dell'IB con displacement).
3. VWAP inclinato costantemente; prezzo sempre dallo stesso lato dalla 09:45.
4. Pullback M5 che non raggiungono mai il 50% del leg precedente (sequenza impulsiva).

Fino a "dichiarazione": nessun trade su questo setup.

## 4. Sequenza di ingresso (long in up-trend day)

1. Trend dichiarato (≥3/4). DOL davanti (estremo settimanale, misura 2×IB…) ≥ 2R.
2. Pullback M5 che consegna su: **breaker** (preferito), **IFVG**, o OB+FVG di continuazione
   — la prima zona qualificata sul percorso, in discount *del leg corrente* (fib del leg,
   non del range del giorno).
3. Trigger: reazione alla zona = mini-sweep di uno swing M1 dentro la zona + close M5 a favore
   (non serve MSS: siamo pro-trend).
4. Ripetibile a ogni nuova zona (max P15: 3 trade/giorno).

## 5. Conferme

- Zona che coincide col primo tocco del VWAP di giornata (+1: il "VWAP first touch" nei trend
  day è la variante più forte) · delta pro-trend sul pullback in contrazione (+½) ·
  correlato in trend concorde (+½ — qui la SMT si usa al contrario: conferma, non divergenza).

## 6. Stop

Sotto la zona (origine) − P16 **oppure** sotto lo swing M5 del pullback, il più stretto dei
due che resti strutturale. I pullback in trend day sono ordinati: stop tipico 0.15–0.25×ADR.

## 7. Target

- TP1: nuovo massimo marginale (liquidità sopra l'ultimo high) — 1/2 + BE.
- Runner: trail sotto gli swing M5 fino a: (a) MSS M15 contrario, (b) 15:50, (c) DOL raggiunto.
- I trend day pagano col runner: chiudere tutto a TP1 rovescia l'expectancy del setup.

## 8. Invalidazione

- Regime: rientro nella VA di ieri / MSS M15 contro trend / pullback > 61.8% del leg →
  trend day finito, setup OFF.
- Post-entry: stop. Un fallimento di zona in trend day è informazione seria (spesso segna
  il massimo di giornata): niente re-entry sulla stessa zona.

## 9. Esempio pratico (NQ, up trend day)

- Open 22600 in gap sopra VAH 22520, mai rientrato ✓. 10:18: IB high 22655 rotto con body
  2.3× ✓. VWAP in salita, prezzo sopra dalla 09:35 ✓ → trend dichiarato (3/4).
- 10:40: pullback lascia IFVG (il bearish FVG 22638–22656 del pullback viene attraversato
  in su con close 10:55) → zona flip 22638–22656.
- 11:10: ritest 22650, mini-sweep swing M1 22646, close M5 22668 ✓ → long 22668,
  stop 22630 (sotto zona) = 38 pt.
- TP1 22712 (sopra high, 1.2R) 1/2+BE · runner trailed per tutta la sessione, MSS M15
  contrario alle 14:55 → out 22890 (+5.8R sul mezzo) ≈ **+3.5R** ponderato.

## 10. Errori frequenti

1. Dichiarare il trend day alle 09:40 (prima dell'evidenza) o negarlo alle 13:00 (contro
   l'evidenza) — il setup vive del riconoscimento onesto del regime.
2. Aspettare pullback "profondi" (al 61.8% del giorno): nei trend day veri non arrivano; le
   zone del leg corrente sono la mappa giusta.
3. Fade "perché è tirato" (il conto delle 2σ nei trend day lo paga chi lo fa).
4. Chiudere il runner al primo tentennamento (l'expectancy del setup È il runner).
5. Continuare a comprare pullback dopo un MSS M15 contrario (il regime è finito).

## 11. Note quantitative attese

- **Frequenza:** 3–6 giorni/mese; 1–3 ingressi per giorno valido.
- **Profilo:** WR 50–60% con distribuzione win asimmetrica (runner) → expectancy +0.5/+1.0R
  nei giorni validi; il rischio è la falsa dichiarazione di regime.
- **Robustezza:** buona: i 4 criteri di regime sono strutturali, non parametrici.
- **Nota per la matrice:** complementare esatto di S01 (copre il regime dove S01 è vietata);
  insieme formano una coppia regime-completa — osservazione centrale per la Fase 3.
