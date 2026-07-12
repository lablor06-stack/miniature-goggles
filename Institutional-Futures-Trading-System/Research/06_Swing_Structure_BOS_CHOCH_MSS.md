# 06 — Swing Structure, BOS, CHoCH, MSS

> La struttura è lo **scheletro sintattico** del sistema: tutte le altre componenti (liquidità,
> zone, premium/discount) si definiscono *relativamente* agli swing. Il problema n.1 della
> struttura è la soggettività; la soluzione IFTS è una definizione algoritmica unica, con lag
> dichiarato, identica nei documenti e nel codice.

---

## 1. Teoria

### 1.1 Swing e frattalità

- **Swing high (pivot):** massimo con N barre più basse a sinistra e a destra. Confermato solo
  N barre dopo il massimo (lag intrinseco e ineliminabile: qualunque definizione senza lag
  repainta).
- Il mercato è **frattale**: la stessa grammatica si applica a ogni TF. Il sistema usa due
  granularità per TF: **interna** (N=3, il "respiro") ed **esterna** (N=8, la "falcata") — i
  valori sono i parametri canonici P1/P2.
- **Dealing range:** dall'ultimo swing esterno low all'ultimo swing esterno high rilevanti
  (post-sweep quando esiste). È l'unità di contesto su cui si calcolano premium/discount.

### 1.2 Gli eventi strutturali (definizioni operative IFTS)

| Evento | Definizione | Significato |
|---|---|---|
| **BOS** | *Close* oltre l'ultimo swing confermato **in direzione del trend** | Continuazione; il trend si auto-conferma |
| **CHoCH** | Primo *close* oltre l'ultimo swing **contro trend** | Avviso; da solo NON opera |
| **MSS** | CHoCH con **displacement** (P4: body ≥ 1.5× media body 20) e, in versione A+, preceduto da sweep di un pool | L'unico evento di inversione operativo del sistema |

Precisazioni non negoziabili:

1. **Close, non wick:** un wick oltre lo swing senza close è uno *sweep* (evento di liquidità,
   spesso segnale opposto). Confondere i due è l'errore più costoso dell'intero vocabolario SMC.
2. **Trend = sequenza di swing esterni:** uptrend finché gli swing esterni marcano HH+HL. Gli
   eventi interni (N=3) generano segnali *dentro* il contesto esterno, mai contro.
3. **Displacement:** proxy dell'iniziativa; un CHoCH "lento" (grinding) è statisticamente più
   spesso un allargamento di range che un'inversione → non è MSS.

### 1.3 Cicli struttura ↔ liquidità

Il pattern generativo del sistema (dettagli in `07_Liquidity`):
`sweep di liquidità esterna → MSS → espansione verso liquidità opposta → BOS in serie → nuovo range`.
La struttura da sola (BOS/CHoCH contati meccanicamente su ogni pivot) produce rumore; è la
**sequenza con la liquidità** a selezionare gli eventi informativi.

---

## 2. Vantaggi

- Grammatica **completamente algoritmica** (pivot parametrici + close + displacement):
  riproducibile, backtestabile, identica su chart e in Pine.
- Lag di conferma **esplicito e prezzato**: il sistema sa che ogni pivot è noto N barre dopo e
  costruisce i trigger di conseguenza (il trigger operativo è il *close di rottura*, che non
  repainta mai).
- Doppia granularità interna/esterna: risolve il classico "trend su quale timeframe?" senza
  aprire un secondo chart.

## 3. Svantaggi e limiti

- **Parametro-dipendenza:** N=3/8 sono scelte; con N diversi cambiano gli eventi. Mitigazione:
  sensitivity analysis in `Testing/03` (il sistema deve restare profittevole in un intorno di
  N, o la regola è overfit).
- In **chop** (balance stretto) produce CHoCH/BOS alternati senza informazione → serve il
  filtro di regime (ampiezza range vs ATR) prima di leggere gli eventi.
- Il lag su TF alti è sostanziale (8 barre H4 = giorni): la struttura esterna HTF è un
  *contesto lento* per costruzione — va bene così, ma non va usata come timing.
- La versione "da manuale ICT" della struttura (con swing scelti a occhio) NON è questa: chi
  arriva da quel mondo deve accettare che alcuni swing "che si vedono" per il sistema non
  esistono (non hanno N barre di conferma). È il prezzo della riproducibilità.

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Esistenza di autocorrelazione/momentum a breve nei futures su indici (i break tendono a proseguire più del caso in regimi di imbalance) | Letteratura su momentum intraday e time-series momentum (Moskowitz, Ooi & Pedersen 2012 a orizzonti lunghi; Heston-Korajczyk-Sadka per pattern intraday) | **E1** (fenomeno generale) |
| I breakout di range falliscono in maggioranza nei regimi balance | Coerente con la letteratura mean-reversion; quantificabile | **E2** (da produrre) |
| "BOS ⇒ continuazione" come regola incondizionata | Falso senza regime filter; è esattamente ciò che l'alternanza balance/imbalance nega | **E4** come assoluto |
| MSS (CHoCH+displacement+sweep) ha follow-through maggiore del CHoCH semplice | Ipotesi centrale del sistema, plausibile (aggancia l'evento all'iniziativa) | **E3 → RQ-1**, misurata dal modulo Statistics del Pine |

## 5. Contesti favorevoli

- Uscita da balance conclamato con sweep: gli eventi MSS sono rari e informativi.
- Kill zone: l'MSS dentro KZ ha alle spalle partecipazione reale (volume conferma).
- HTF trend + LTF pullback: i BOS interni in direzione HTF sono i più affidabili del sistema.

## 6. Contesti sfavorevoli

- Lunch/notte: pivot su volumi sottili → struttura "sintatticamente valida ma semanticamente
  vuota" — il time filter la esclude.
- Chop stretto (range < 1.5×ATR15m): eventi alternati senza edge → regime filter.
- Post-news immediato: displacement ovunque, struttura riscritta più volte in minuti.

## 7. Errori comuni

1. Wick contato come break (vedi §1.2 — errore n.1).
2. Contare i CHoCH interni come inversioni del contesto esterno (inversione di gerarchia).
3. Ridisegnare gli swing a posteriori per giustificare il trade (impossibile con la definizione
   algoritmica — il Pine è anche uno strumento di onestà).
4. Operare il primo CHoCH dopo un trend esteso senza sweep né displacement (di solito è solo
   la prima presa di profitto).
5. Cambiare N finché la struttura "conferma" l'opinione (parameter shopping) — vietato da P1/P2.

## 8. Miglioramenti proposti (IFTS)

- **Displacement qualificato dal contesto**, non solo dalla singola candela: accettato anche un
  cluster di 2-3 candele con body cumulato ≥ 2× media e close oltre il livello (cattura gli
  impulsi "a scala" tipici di NQ — implementato nel Pine come opzione `msClusterDisp`).
- **Stato strutturale sintetico in dashboard:** `EXT: Bull (HH 5843.25 / HL 5811.50) · INT: Bear`
  — elimina l'ambiguità di lettura al volo.
- **Contatore di regime:** n. di eventi interni alternati nelle ultime 20 barre; sopra soglia →
  etichetta CHOP e sospensione segnali (anti-rumore).
- Ogni evento loggato con snapshot dei suoi qualificatori (sweep sì/no, displacement ratio,
  KZ) → il journal può rispondere a "quanto vale un MSS pulito vs sporco?" (RQ-1).

## 9. Implicazioni per il sistema

1. L'MSS è **l'unico trigger di inversione**; il BOS interno in direzione HTF è **l'unico
   trigger di continuazione**. Tutto il resto è contesto — questa riduzione drastica dello
   spazio dei segnali è una scelta anti-overfitting deliberata.
2. La struttura esterna HTF definisce il bias con isteresi (cambia solo su MSS esterno) →
   il bias non "sfarfalla".
3. Nel Pine: Swing Engine e Structure Engine sono il cuore; ogni altro modulo legge i loro
   array (architettura in `Documentation/01`).
