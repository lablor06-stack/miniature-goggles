# 08 — Order Blocks, Breaker Blocks, Mitigation Blocks

> Le "zone" sono i luoghi dove il sistema *entra*. La loro funzione è geometrica prima che
> mistica: offrono un punto di ingresso con stop stretto e invalidazione chiara dentro un
> contesto già selezionato da liquidità+struttura. Senza quel contesto, un OB è solo una
> candela colorata.

---

## 1. Teoria

### 1.1 Order Block (OB)

**Definizione IFTS:** ultima candela (o cluster ≤ 3 candele) di segno opposto immediatamente
precedente un displacement (P4) che produce BOS o MSS.
- Bullish OB = ultima candela ribassista prima dell'impulso rialzista che rompe struttura.
- **Zona:** dal open al low (bullish) / dall'open all'high (bearish) della candela — cioè il
  *body + wick del lato di origine*. Su LTF (M1-M5) è ammesso il raffinamento al solo body.
- **Validità condizionale:** un OB è operabile solo se (a) ha originato displacement con
  rottura, (b) non è ancora stato mitigato, (c) giace nella metà corretta del dealing range
  (discount per i long, premium per gli short), (d) idealmente la sua formazione include lo
  sweep di un pool.

**Razionale meccanico (ipotesi, dichiarata come tale):** l'ultima candela opposta è dove le
esecuzioni passive dell'iniziatore si sono concentrate (compra nel sell-off finale); il ritorno
sulla zona rappresenta (i) ricarico a prezzo medio, (ii) difesa dell'inventory. Il footprint
mostra spesso lì lo shift di iniziativa. Non esiste letteratura accademica sull'OB in quanto
tale: la fiducia deriva dal meccanismo generico "i grandi ordini vengono lavorati e difesi
attorno al loro prezzo medio" (E1, letteratura meta-order) + misurazione in-house (RQ-6).

### 1.2 Breaker Block

**Definizione:** OB **fallito e invertito**. Sequenza completa (bullish breaker):
1. swing low → rally → swing high;
2. sweep del swing low (presa di liquidità sotto);
3. displacement rialzista che rompe lo swing high (MSS);
4. la zona dell'ex candela ribassista/di distribuzione tra i punti 1-2 — attraversata dal
   movimento — diventa **supporto** al retest.

Il breaker è il "lato B" dello sweep-reversal: chi ha venduto la rottura del low è intrappolato;
il retest della zona è dove il loro stop-out (buy) incontra il ricarico degli iniziatori. Per
questo il sistema considera il breaker **la zona di continuation di massima qualità** dopo un
MSS con sweep.

### 1.3 Mitigation Block

Come il breaker ma **senza lo sweep** al punto 2 (il low tiene, higher low). Zona di "pareggio"
degli intrappolati, senza il carburante degli stop presi → qualità inferiore, size ridotta o
solo gestione (non ingresso) nel sistema.

### 1.4 Ciclo di vita di una zona (state machine, identica nel Pine)

`FRESH → TESTED (primo tocco: mitigata, one-shot di default) → o REGENERATED (se il tocco
produce displacement a favore: la zona resta mappata come riferimento) → BROKEN (close oltre il
lato lontano) → eventuale FLIP (OB→Breaker; FVG→IFVG)`.

Regole di igiene: max 3 zone attive per direzione per TF (le più recenti/vicine); zone più
vecchie di 5 giorni (LTF) decadono; una zona dentro un'altra si fonde (si usa il bordo esterno
comune).

---

## 2. Vantaggi

- **Geometria del rischio eccellente:** ingresso al bordo, stop oltre l'origine (+P16 buffer),
  invalidazione binaria → R:R ≥ 2 raggiungibile sistematicamente con target su DOL.
- Il breaker incorpora *nella sua definizione* l'intera sequenza contestuale (sweep+MSS):
  auto-seleziona i contesti giusti.
- Stato binario (fresh/tested/broken) → perfettamente loggabile e backtestabile.

## 3. Svantaggi e limiti

- **Inflazione di zone:** con definizioni lasche ogni chart ne ha decine. Le condizioni di
  validità (§1.1) e il cap di igiene servono a questo.
- Hit-rate del *tocco* non garantito: il prezzo può ripartire senza retest (costo: trade
  mancati — accettato, il sistema non insegue).
- Il raffinamento (body-only, LTF) aumenta R:R ma riduce hit-rate: trade-off da misurare
  (RQ-6b), non da decidere per estetica.
- Nessuna evidenza accademica diretta; è la parte del sistema più dipendente dalla validazione
  interna → per questo le zone non sono mai trigger da sole ma solo *luoghi* dove il trigger
  (reazione al tocco in contesto) può avvenire.

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| I grandi ordini vengono frazionati e lavorati attorno a prezzi di riferimento; il loro impatto persiste | Letteratura meta-order/impact (Almgren, Bouchaud) | **E1** (meccanismo generico) |
| Il retest di breakout level tiene più spesso del caso (throwback/pullback studies) | Letteratura tecnica classica su pullback dopo breakout (risultati misti ma il fenomeno del retest è documentato) | **E2/E3** |
| OB "da manuale" (con displacement e sweep) ha hit-rate di reazione superiore a OB generico | Ipotesi qualificante IFTS | **E3 → RQ-6** (Statistics module conta reazioni ≥ 1R dal tocco) |
| Breaker > Mitigation in qualità | Coerente col meccanismo (stop-fuel); da quantificare | **E3 → RQ-6c** |
| "Le banche mettono gli ordini negli order block" (letterale) | Non verificabile/naive | **E4** — il sistema usa la versione debole (zona di concentrazione di esecuzioni) |

## 5. Contesti favorevoli

- Post-MSS in kill zone, prima zona di ingresso sul percorso del displacement (il "first
  presented PD array" nel lessico ICT).
- Trend day ordinato: breaker/OB in direzione = stazioni di ricarico ripetute (Setup B).
- Confluenza zona + livello indipendente (VWAP, VAL/VAH, OTE): confluenze *ortogonali* (fonti
  diverse) valgono più di confluenze omogenee.

## 6. Contesti sfavorevoli

- Zona contro la metà sbagliata del range (OB bullish in pieno premium): geometria contraddetta
  dal contesto → vietata (condizione (c)).
- Chop: displacement rari → OB "tecnici" deboli, tutti mitigati in ore.
- Post-news: le zone pre-news hanno perso il loro sponsor informativo.
- Zone HTF appena sotto/sopra zone LTF opposte: conflitto → NT o attesa risoluzione.

## 7. Errori comuni

1. Chiamare OB ogni candela opposta (senza displacement/rottura) — l'errore definitorio base.
2. Entrare al tocco **senza reazione** su zone LTF sottili con mercato in accettazione contro.
3. Ricomprare la stessa zona dopo il primo stop-out ("deve tenere!") — one-shot di default.
4. Ignorare il flip: un OB rotto è un breaker *per l'altra direzione*, non un OB "ancora valido".
5. Accatastare 8 zone sovrapposte e chiamarla confluenza (sono la stessa informazione contata
   8 volte).

## 8. Miglioramenti proposti (IFTS)

- **Condizioni di validità (a)-(d)** formalizzate → il Pine disegna *solo* zone conformi
  (riduzione drastica del rumore rispetto agli indicatori OB pubblici).
- **State machine esplicita** con stati loggabili → statistiche per stato (fresh vs
  regenerated).
- **Fusione zone sovrapposte** e cap per direzione → chart leggibile, oggetti sotto controllo.
- **Metrica di reazione standard** (MFE ≥ 1R entro 10 barre dal tocco) per confrontare
  OB/Breaker/Mitigation/FVG sullo stesso metro (RQ-6).

## 9. Implicazioni per il sistema

1. Le zone sono il **dove** dell'ingresso; mai il perché. Ordine gerarchico immutabile:
   tempo (KZ) → liquidità (sweep) → struttura (MSS/BOS) → zona (dove) → conferma (trigger).
2. Priorità di zona post-MSS: **Breaker/IFVG > OB con sweep > FVG semplice > Mitigation**
   (dal più al meno "carburato") — codificata nel Signal Engine.
3. Stop sempre oltre l'**origine** della zona + P16; mai dentro la zona.
