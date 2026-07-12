# 12 — SMT Divergence (Smart Money Technique)

> L'SMT confronta due aste parallele sullo stesso flusso macro (ES vs NQ): quando una fa un
> nuovo estremo e l'altra no, una delle due sta mentendo. Usata al posto giusto — su pivot
> confermati, a livelli rilevanti, in KZ — è la conferma di reversal più economica del toolkit.

---

## 1. Teoria

### 1.1 Definizione operativa

Dati due strumenti correlati A e B (default: ES↔NQ; tie-breaker YM):

- **SMT bearish:** A segna HH (sopra il pivot high precedente) e B **non conferma** (LH),
  con entrambi i pivot confermati (P1) entro una finestra di ±5 barre.
- **SMT bullish:** A segna LL e B non conferma (HL), stesse condizioni.

Lettura: il nuovo estremo non confermato è *sospetto* — l'aggressione ha spinto un solo
strumento oltre il livello (tipicamente per prendere quel pool) mentre il flusso aggregato
non ha seguito. È l'impronta cross-market dello sweep.

### 1.2 Perché ES/NQ (e quando la coppia si rompe)

- Correlazione strutturale altissima (stesso macro-flusso, membri sovrapposti), ma **beta
  settoriale diversa** (NQ tech-heavy): nelle giornate di rotazione settoriale la divergenza
  è *fondamentale*, non tecnica → SMT inaffidabile.
- **Filtro di regime (obbligatorio):** correlazione rolling 20 periodi sul TF di lavoro
  ≥ 0.7. Sotto: modulo in standby (il Pine lo espone in dashboard).
- YM come **tie-breaker**: se ES diverge da NQ, il lato confermato da 2 su 3 vince.

### 1.3 Le tre condizioni di qualità (tutte necessarie)

1. **Livello:** la divergenza avviene su un pool di rank ≥ 4 (`07` §1.1) o su estremo di
   dealing range — non "in mezzo".
2. **Tempo:** dentro una KZ.
3. **Struttura:** segue (o accompagna) un MSS sul proprio strumento — l'SMT *conferma* un
   segnale che esiste già, non lo crea.

### 1.4 Relazione col lead-lag accademico

La letteratura documenta lead-lag tra future e cash e tra strumenti correlati a orizzonti
brevissimi (E1), ma si dissolve in millisecondi/secondi per arbitraggio HFT. L'SMT a scala
di *swing* non è quel fenomeno: è una **divergenza di forza relativa** attorno a un evento di
liquidità. Va quindi difesa non come "NQ anticipa ES" (falso a scala umana) ma come "il
mancato allineamento a un estremo segnala asta non genuina" — formulazione compatibile con la
microstruttura (E3, testabile).

---

## 2. Vantaggi

- **Ortogonale** a tutto il resto del toolkit (usa un'informazione — il correlato — che
  nessun altro modulo vede): la confluenza SMT aggiunge informazione vera, non conteggio
  doppio.
- Gratuita: nessun dato aggiuntivo oltre a un secondo simbolo.
- Definizione algoritmica precisa (pivot P1 + finestra ±5) → backtestabile, zero estetica.
- Eccellente contro i falsi sweep: raid che prende il pool su ES *e* su NQ simultaneamente è
  più probabilmente espansione; raid solo su uno = classico grab.

## 3. Svantaggi e limiti

- **Frequenza bassa** (con le tre condizioni): poche occorrenze/settimana → mai richiesta come
  condizione necessaria, solo upgrade di grade.
- Regime-dipendente (rotazioni settoriali, §1.2): senza il filtro di correlazione produce
  segnali sistematicamente sbagliati proprio nei giorni peggiori.
- Il lag dei pivot (P1=3) si somma su due strumenti: l'SMT confermata arriva tardi rispetto
  al tocco — coerente col ruolo di *conferma*, non di trigger.
- Su TradingView richiede `request.security` (budget limitato, gestito nel Pine con
  `dynamic_requests`).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Lead-lag tra strumenti correlati esiste ma decade in ms-s (arbitraggio) | Letteratura microstruttura/HFT (es. Budish et al. su arbitraggio ES-SPY) | **E1** (e per questo NON è il razionale usato) |
| Divergenze di forza relativa a estremi correlati precedono reversal più del caso | Consenso practitioner (ICT, ma anche classica intermarket analysis di Murphy) | **E3 → RQ-10** |
| SMT senza filtro correlazione degrada nei regimi di rotazione | Conseguenza logica misurabile | **E2 da produrre** (il journal logga `smt` + `corr_regime`) |
| "L'SMT indica sempre il vero direzionale" | Assoluto non falsificabile | **E4** |

## 5. Contesti favorevoli

- Sweep di PDH/PDL o estremo settimanale su un solo strumento in NY AM KZ: lo scenario
  d'oro (tutte e tre le condizioni + pool pesante).
- Doppio test di un livello con seconda gamba solo su uno dei due indici.
- Giorni indice-driven (macro releases): il flusso è comune → correlazione alta → SMT
  affidabile.

## 6. Contesti sfavorevoli

- Earnings mega-cap (NVDA/AAPL/MSFT…): NQ vive di vita propria → SMT spenta.
- Rotazione value/growth conclamata (correlazione rolling < 0.7).
- Orari sottili: pivot su rumore.
- Rollover non sincronizzato dei due contratti.

## 7. Errori comuni

1. SMT "vista" su wick non confermati (pivot ancora aperti) → repaint mentale.
2. Usarla in mezzo al range come segnale autonomo (viola le 3 condizioni).
3. Ignorare il regime settoriale (il più dannoso: proprio nei giorni di rotazione l'SMT
   "appare" ovunque).
4. Confrontare TF diversi tra i due strumenti.
5. Trattare la mancata SMT come segnale contrario ("confermano entrambi ⇒ va giù davvero"):
   l'assenza di divergenza è assenza di informazione, non informazione opposta.

## 8. Miglioramenti proposti (IFTS)

- **Filtro di correlazione rolling integrato** (novità rispetto agli indicatori SMT pubblici,
  che non ce l'hanno): l'SMT si spegne da sola nei regimi sbagliati.
- **Tie-breaker YM opzionale** (2-su-3).
- **Solo pivot confermati + finestra ±5 barre** hardcoded: la versione "che repainta" non
  esiste nel sistema.
- **Campo journal `smt`** (bull/bear/none/na) → RQ-10: uplift di expectancy dei Setup A
  con/senza SMT dopo 100 trade.

## 9. Implicazioni per il sistema

1. SMT = **conferma di grado** (A → A+) per il Setup A; mai condizione necessaria, mai
   trigger autonomo.
2. Nel Pine: modulo dedicato con simbolo correlato configurabile, filtro correlazione,
   etichette solo su eventi qualificati, riga dashboard (stato + correlazione corrente).
3. Il razionale dichiarato in vendita/due-diligence è la versione difendibile (§1.4), non il
   lead-lag ingenuo.
