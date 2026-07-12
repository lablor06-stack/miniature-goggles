# 02 — Auction Market Theory (AMT)

> AMT (Steidlmayer, CBOT anni '80; Dalton, *Mind over Markets*) è la cornice concettuale più
> solida disponibile per il price action: descrive il mercato come **asta bidirezionale continua**
> il cui scopo è facilitare gli scambi. Nel sistema IFTS, AMT è la "fisica" e i concetti
> ICT/SMC sono un "linguaggio operativo" che vi si mappa sopra.

---

## 1. Teoria

### 1.1 I principi

1. **Scopo del mercato = facilitare il trade.** Il prezzo si muove per *cercare* il livello dove
   avvengono più scambi (valore), non per "avere ragione".
2. **Prezzo ≠ valore.** Il prezzo è pubblicità istantanea; il **valore** è dove il volume si
   accumula nel tempo (value area). Il prezzo esplora, il valore ratifica.
3. **Accettazione vs rifiuto.** Se il prezzo passa tempo e volume a un livello → accettazione
   (il valore migra). Se viene respinto rapidamente (wick, excess) → rifiuto.
4. **Balance ↔ Imbalance.** Il mercato alterna fasi di equilibrio (rotazioni dentro un range,
   profilo a campana) e squilibrio (trend, range extension, profilo allungato). Il passaggio
   dall'uno all'altro è il momento informativo chiave.
5. **Timeframe dei partecipanti.** Il day-timeframe (locals, intraday) fornisce rotazione; gli
   "other timeframe" (istituzionali multi-day) causano le estensioni. Le impronte dei secondi
   (iniziativa, range extension, volume alle code) sono ciò che vale la pena seguire.

### 1.2 Vocabolario operativo

- **Value Area (VA):** fascia che contiene ~68-70% del volume/TPO del periodo → VAH/VAL/POC.
- **Excess (coda):** rifiuto rapido a un estremo — l'asta in quella direzione è *finita*.
- **Poor/unfinished high-low:** estremo senza coda — asta incompleta, probabile revisit.
- **Open types** (in ordine di convinzione): Open-Drive (parte e non torna: iniziativa forte),
  Open-Test-Drive (testa un riferimento, poi drive), Open-Rejection-Reverse, Open-Auction
  (rotazione senza convinzione).
- **Initial Balance (IB):** range 09:30–10:30. IB stretto → alta probabilità di range extension;
  IB molto ampio → giornata probabilmente già "spesa".
- **Day types:** Trend day, Double-distribution trend day, Normal day, Normal-variation,
  Neutral day, Neutral-extreme. Utilità: aspettative *condizionali* (cosa è probabile dopo
  l'una o l'altra apertura), non previsioni.

### 1.3 La mappatura AMT ↔ ICT (chiave di volta del progetto)

| AMT | ICT/SMC | Nota |
|---|---|---|
| Balance / bracket | Accumulation (PO3), consolidation | Stessa cosa: costruzione di inventory a valore |
| Falso breakout del bracket | Manipulation / Judas / sweep | La rottura che fallisce = liquidity raid sul lato sbagliato |
| Range extension / imbalance | Displacement / expansion | Iniziativa other-timeframe |
| Ritorno al valore dopo estensione fallita | Reversal verso EQ / DOL opposto | Mean reversion al POC/VA |
| Poor high/low | Old high/low come DOL | Aste incomplete = pool da rivisitare |
| Excess (coda) | Sweep con rejection | Identico fenomeno, lessico diverso |
| LVN (low volume node) | FVG | Il prezzo attraversa in fretta = inefficienza |
| HVN | OB/zona di mitigation "spessa" | Dove l'inventory è stata scambiata |

Questa tabella non è cosmetica: significa che **le regole ICT ereditano il razionale AMT** e che
i due vocabolari possono validarsi a vicenda (es. uno sweep di qualità dovrebbe lasciare excess
nel profilo).

---

## 2. Vantaggi

- Fornisce il **perché** dietro ogni pattern: senza AMT, ICT è una collezione di sigle; con AMT
  ogni sigla è un caso particolare di accettazione/rifiuto del valore.
- **Aspettative condizionali sul tipo di giornata** → il sistema sa quando NON applicare il
  modello reversal (trend day) e quando non applicare il continuation (balance day). È il
  principale antidoto all'errore "un solo playbook per tutte le giornate".
- Concetti direttamente misurabili (VA, IB, excess) → backtestabili.

## 3. Svantaggi e limiti

- Diagnosi spesso **retrospettiva**: il day type si conosce con certezza a fine giornata. Serve
  una versione *anticipata* (open type + prime rotazioni + gap) accettando errori.
- La VA al 70% è una **convenzione**, non una legge; i valori funzionano perché tutti li
  guardano (focal point), il che li rende anche affollati.
- Richiede dati di volume decenti; su TradingView il volume future è del solo exchange (ok per
  CME index futures, che sono il mercato guida).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Il volume intraday si distribuisce ~log-normale attorno a un modo (POC); la campana è la norma nei giorni senza news | Distribuzioni empiriche note; replicabile su qualunque dataset ES | **E2** (facilmente) |
| IB stretto → maggiore probabilità di range extension | Dalton (practitioner); test pubblici parziali | **E3** (da validare in-house) |
| 80% rule (rientro e accettazione in VA → traversata completa) | Dalton/CQG folklore con test retail misti | **E3/E4** — nel sistema è *contesto*, non trigger |
| Poor high/low vengono rivisitati più spesso di estremi con excess | Plausibile, misurabile | **E3** → in pipeline `Testing/` |
| Trend day ~15-20% delle giornate, balance ~60%+ | Stime practitioner ricorrenti su ES | **E3** — il day-type classifier del sistema lo misurerà |
| L'apertura fuori VA precedente cambia la distribuzione dei ritorni della giornata | Studi su "open outside value" (practitioner + alcuni paper su opening gap) | **E3** |

## 5. Contesti favorevoli

- ES/NQ in regime "normale" (VIX 12–25): l'alternanza balance/imbalance è pulita.
- Giornate con riferimenti chiari (VA di ieri ben formata, overnight contenuto).
- Uso della VA come **filtro direzionale**: target dentro area di scarso volume → il prezzo la
  attraversa in fretta (LVN) → trade più efficienti.

## 6. Contesti sfavorevoli

- **Double-distribution days e news days:** il valore "salta" — le VA del mattino diventano
  irrilevanti nel pomeriggio.
- Regimi a volatilità compressa estrema: micro-rotazioni, VA strettissime, segnali di
  accettazione/rifiuto indistinguibili dal rumore.
- Serie di giorni festivi/estivi: campioni di volume non rappresentativi.

## 7. Errori comuni

1. Trattare il day type come previsione invece che come **aspettativa da aggiornare** ora per ora.
2. Fare mean-reversion al POC durante un trend day conclamato (combattere l'iniziativa).
3. Costruire la VA mescolando Globex e RTH senza criterio (il sistema usa RTH per il profilo di
   riferimento e Globex per gli estremi di liquidità — motivato in `03_Volume_Profile`).
4. Usare l'80% rule come trigger secco senza la condizione di *accettazione* (tempo dentro VA).
5. Ridisegnare la VA "a occhio" per confermare il proprio bias.

## 8. Miglioramenti proposti (IFTS)

- **Day-type classifier anticipato** (implementato come euristica nella dashboard Pine): gap vs
  VA precedente + open type + ampiezza IB relativa (IB/ATR) → etichetta provvisoria
  (trend/balance/neutral) con aggiornamento alle 10:30.
- **Excess check sugli sweep:** uno sweep di Setup A è "di qualità" se lascia coda visibile
  anche sul profilo (conferma AMT del raid).
- **LVN come acceleratori di target:** i target del sistema preferiscono attraversare LVN
  (velocità) e fermarsi prima di HVN (attrito).

## 9. Implicazioni per il sistema

1. Il **filtro di regime giornaliero** (balance vs imbalance) decide quale setup è autorizzato:
   Setup A nei giorni bilanciati/aperture in range; Setup B nei giorni di iniziativa.
2. La narrativa "da pool a pool" (DOL) è la lettura ICT della **ricerca di valore** AMT: i target
   del sistema sono sempre o liquidità esterna o riferimenti di valore (POC/EQ).
3. L'IB e l'open type entrano nella checklist pre-market e delle 10:30 (Manual/01).
