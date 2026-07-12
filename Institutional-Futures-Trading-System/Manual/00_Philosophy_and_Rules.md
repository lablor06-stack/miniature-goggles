# Manuale IFTS — Vol. 0: Filosofia e Regole Fondamentali

> Il manuale traduce il Core Model in **procedura**. Questo volume stabilisce il contratto
> che il trader firma con sé stesso: la filosofia (perché le regole meritano obbedienza) e
> le regole non negoziabili. I volumi 1-5 dettagliano checklist, rischio, psicologia,
> misurazione e adattamento prop firm.

---

## 1. Filosofia operativa

### 1.1 I sette principi

1. **Il mercato non si prevede; si riconosce.** Il lavoro non è indovinare la direzione, è
   riconoscere — in una lista finita di configurazioni studiate — quale si sta presentando,
   e agire di conseguenza. Se nessuna si presenta, il lavoro di oggi era riconoscerlo.

2. **L'edge è la somma di tre selettività:** *quando* (KZ), *dove* (liquidità+zone),
   *quanto* (rischio per grade). Nessuna delle tre è negoziabile perché l'edge misurabile
   esiste solo alla loro intersezione — un trade "quasi da manuale" non è nel campione
   statistico del sistema: è un altro mestiere, non incluso.

3. **Prima la sopravvivenza, poi l'expectancy, poi la crescita.** Ordine lessicografico:
   nessun miglioramento di rendimento giustifica un peggioramento della probabilità di
   rovina. Da qui: size fissa per grade, stop giornaliero/settimanale, niente martingale.

4. **Il processo è l'unica cosa sotto controllo.** Esito e qualità della decisione sono
   indipendenti sul singolo trade (varianza); convergono solo sul campione. Perciò: si
   valuta la settimana sul rispetto delle checklist, il trimestre sui numeri.

5. **Ogni regola è un'ipotesi con un numero addosso.** Le regole non sono dogmi: sono
   ipotesi formalizzate (RQ) in attesa di conferma/smentita dal journal. Ma finché il
   campione non parla (n≥100), si eseguono COME dogmi — cambiare regole a metà campione
   distrugge sia l'edge sia la misura.

6. **La noia è un costo del mestiere, non un segnale.** Il sistema produce 3-6 trade a
   settimana. Le ore senza trade non sono tempo perso: sono il filtro che lavora.

7. **Onestà radicale col journal.** Il journal registra ciò che è successo, incluso ciò che
   imbarazza (regole violate, exit emotive). Un journal edulcorato rende falsi tutti i KPI
   a valle — è l'unico peccato capitale del sistema.

### 1.2 Che cosa si sta davvero facendo (il modello di business)

Vendiamo al mercato un servizio: **assorbire rischio nei momenti di dislocazione** (dopo i
raid, sui pullback di iniziativa) in cambio di un premio (l'expectancy). Come ogni
assicuratore: (a) selezioniamo i rischi (filtri), (b) prezziamo per grade (size),
(c) teniamo riserve (stop giornaliero/settimanale), (d) misuriamo la sinistralità (journal).
Un assicuratore che "sente" che oggi va bene e raddoppia le polizze è fallito in partenza —
questa immagine risolve il 90% dei dilemmi psicologici del Volume 3.

## 2. Le Regole Fondamentali (R1–R20)

### Perimetro

- **R1.** Si opera solo ES/NQ (+ micro per scalare); un solo strumento a mercato per volta.
- **R2.** Si opera solo nelle finestre autorizzate (Conventions §2). Fuori finestra il
  terminale d'esecuzione è chiuso.
- **R3.** Flat entro le 15:50 ET. Nessuna posizione overnight (v1).
- **R4.** Nei giorni tier-1 (CPI, NFP, FOMC…): protocollo news (Vol.1 §2.4). Half-day,
  rollover, festivi ponte: NT.

### Ingresso

- **R5.** Solo Setup A, B o C come da Core Model. Se non sai nominare il setup, non esiste.
- **R6.** Tutte le condizioni necessarie (A1-A7 / B1-B6) verificate PRIMA dell'ordine —
  checklist a voce alta o per iscritto.
- **R7.** R:R ≥ 2.0 ex-ante col target alla parte conservativa del DOL. Sotto: NT.
- **R8.** Size dal grade (0.25/0.35/0.50%), calcolata sul rischio a stop pieno, arrotondata
  PER DIFETTO al contratto. Se 1 micro eccede il rischio: NT.
- **R9.** Max 3 trade/giorno; max 2 tentativi per lato/pool; stop dopo 2 perdite consecutive
  di sessione.

### Gestione

- **R10.** Lo stop iniziale non si allarga MAI. Si stringe solo per regola (BE dopo TP1,
  trailing P17).
- **R11.** TP1/TP2/runner come da Core Model §6. Nessuna chiusura anticipata "a sensazione"
  salvo `exit_news` (loggata).
- **R12.** Niente media del prezzo, niente hedging interno, niente flip istantaneo
  (stop→reverse richiede un nuovo setup completo).
- **R13.** Time-stop: A 90' senza TP1 → −1/2; B: MSS M15 contrario → flat.

### Protezione del capitale

- **R14.** Stop giornaliero: −2R o −1.0% (il primo). Raggiunto → piattaforma chiusa, giornata
  finita, journal compilato.
- **R15.** Stop settimanale: −4R → settimana finita, review straordinaria (Vol.4).
- **R16.** Dopo un giorno −2R: il giorno successivo size massima 0.25% a prescindere dal grade.
- **R17.** Drawdown > 8R dal picco: dimezzare tutte le size fino a nuovo massimo di equity.

### Integrità del sistema

- **R18.** Ogni trade loggato entro fine giornata (schema `Journal/journal_schema.csv`),
  incluse violazioni (`rule_break` ≠ vuoto).
- **R19.** Nessuna modifica a regole/parametri se non in sede di review mensile, con la
  procedura del CHANGELOG (motivo scritto → test → bump di versione).
- **R20.** 30 minuti prima della prima KZ: pre-market completo (Vol.1 §1). Senza pre-market
  scritto la giornata è NT d'ufficio.

## 3. Gerarchia in caso di conflitto tra regole

`Protezione del capitale (R14-R17) > Perimetro (R1-R4) > Integrità (R18-R20) >
Ingresso (R5-R9) > Gestione (R10-R13)`

Esempio: un Setup A+ perfetto alle 10:58 con stop giornaliero a −1.8R → si può prendere solo
con rischio ≤ 0.2R → sotto il minimo operativo → NT (la protezione vince sull'opportunità).

## 4. Deroghe

Non esistono deroghe intraday. Il modulo "proposta di deroga" è la review mensile (R19).
Qualunque idea brillante venuta alle 10:23 va scritta nel journal campo `notes` e valutata
a mercati chiusi. Questa regola non ha eccezioni perché è la regola che protegge tutte le
altre.
