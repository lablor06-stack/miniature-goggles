# 03 — Volume Profile & Market Profile

> Il profilo è la **rappresentazione empirica del valore**: dove il mercato ha accettato prezzo
> con volume/tempo. Nel sistema serve a tre cose: (a) classificare la giornata, (b) qualificare
> i livelli (HVN/LVN), (c) scegliere target realistici.

---

## 1. Teoria

### 1.1 Costruzione

- **Market Profile (TPO):** ogni mezz'ora è una lettera; il profilo conta *tempo* per livello.
- **Volume Profile:** conta *contratti scambiati* per livello. Più diretto per i futures; è lo
  standard IFTS. TPO resta utile per la struttura (excess, single prints).
- **POC:** livello a volume massimo. **VA (68-70%):** espansione dal POC fino a contenere ~70%
  del volume. **VAH/VAL:** i bordi.
- **Profili di riferimento:** giornaliero RTH (default IFTS), composito multi-day (per swing),
  per-sessione (Asia/London) usato solo per gli estremi.

**Scelta motivata — RTH vs ETH:** il profilo di *valore* si costruisce sulla sessione RTH
(09:30–16:00 ET), dove passa la maggioranza del volume ES/NQ e dove operano i flussi che
definiscono il valore (cash, opzioni, MOC). La sessione Globex serve per gli **estremi di
liquidità** (Asia/London H/L), non per il valore. Mescolare le due cose produce POC diluiti e
VA non confrontabili tra giornate.

### 1.2 Nodi e comportamento del prezzo

- **HVN (High Volume Node):** accettazione passata → attrito: il prezzo vi rallenta, rotea.
- **LVN (Low Volume Node):** rifiuto passato → il prezzo li attraversa in fretta o li rifiuta
  subito. Gli LVN coincidono spesso con FVG lasciati da displacement.
- **Naked/Virgin POC (nPOC):** POC di giornate passate mai ritestato → riferimento magnetico
  di medio periodo (lista tenuta aggiornata nel pre-market).

### 1.3 Forme di profilo e diagnosi

| Forma | Lettura | Aspettativa condizionale |
|---|---|---|
| Campana simmetrica (D) | Balance | Fade degli estremi VA, target POC |
| "b" (volume in basso) | Liquidazione lunghi poi accettazione | Base potenziale; sopra VAL → rotazione |
| "P" (volume in alto) | Short covering poi accettazione | Tetto potenziale; sotto VAH → rotazione |
| Doppia distribuzione | Migrazione del valore intraday | Trade nella direzione della seconda distribuzione; il collo (LVN) è il riferimento |
| Sottile e allungato | Trend day | NON fare mean reversion; pullback = Setup B |

### 1.4 Riferimenti derivati usati dal sistema

PDH/PDL, VAH/VAL/POC di ieri, nPOC aperti, IBH/IBL, mid del range overnight (ONH/ONL). La
gerarchia completa dei livelli e la loro precedenza è definita nella checklist pre-market
(`Manual/01`).

---

## 2. Vantaggi

- **Oggettività:** il profilo si calcola, non si interpreta; due analisti ottengono lo stesso POC.
- Distingue livelli "spessi" (HVN, dove servono conferme) da "sottili" (LVN, dove il prezzo
  scivola) → migliora la scelta di stop (oltre HVN) e target (prima di HVN, attraverso LVN).
- Il day-type framework dà al sistema il **filtro anti-playbook-unico**.

## 3. Svantaggi e limiti

- **Dipendenza dal periodo scelto:** RTH vs ETH, giornaliero vs composito cambiano i livelli;
  serve una convenzione fissa (fatta: RTH per valore, ETH per estremi).
- Il profilo è **descrittivo, non predittivo**: dice dove il valore È stato. L'uso predittivo
  (magnete nPOC, 80% rule) è probabilistico e da validare.
- Su TradingView i profili disponibili hanno granularità limitata rispetto a piattaforme
  dedicate (Sierra/NinjaTrader); per l'uso IFTS (contesto, non trigger) è sufficiente.
- Nei giorni a bassissimo volume (festivi) il profilo è rumore.

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Il volume per livello è unimodale nei giorni balance; multimodale nei giorni di migrazione | Replicabile su qualunque dataset | **E2** |
| Ritorno al POC del giorno precedente entro N giorni ("POC magnet") | Test practitioner ricorrenti, risultati sensibili alla definizione | **E3** |
| nPOC rivisitati con alta frequenza entro settimane | Folklore quantificabile | **E3** → pipeline |
| 80% rule | Vedi `02_AMT` §4 | **E3/E4** |
| LVN attraversati più velocemente degli HVN (velocity per punto) | Misurabile direttamente | **E2** (da produrre in-house) |
| Value migration come indicatore di trend multi-day | Dalton framework | **E3** |

**Nota di metodo:** il profilo produce molti claim *misurabili ma non ancora misurati* nel
retail. La pipeline `Testing/` §Research-Questions li elenca come studi interni prioritari
perché i dati necessari (volume per livello) sono disponibili.

## 5. Contesti favorevoli

- Giornate post-balance con riferimenti freschi e vicini (VA di ieri sovrapposta all'overnight).
- Trade **verso** LVN/nPOC con VA come sfondo (target ad alta probabilità di essere raggiunti
  velocemente).
- Conferma degli sweep: raid del PDL che coincide con VAL/LVN → confluenza di qualità.

## 6. Contesti sfavorevoli

- Gap ampio oltre l'intera VA precedente: i riferimenti di ieri perdono rilevanza (→ si passa
  ai riferimenti settimanali/compositi).
- News tier-1: il valore si riprezzerà; i profili pre-news sono storia.
- Rollover e half-day: profili non confrontabili.

## 7. Errori comuni

1. Mescolare RTH/ETH senza criterio (il più diffuso in assoluto nel retail).
2. Usare il POC *in formazione* come livello statico (il developing POC migra: riferimento
   dinamico, non linea da fade).
3. Fade meccanico di VAH/VAL in un trend day (il profilo stesso — sottile e allungato — dice
   di non farlo).
4. Considerare il profilo un sistema: è **contesto**; nel sistema IFTS non genera mai trigger.
5. Ignorare che il primo test di un nPOC lontano spesso arriva dopo *giorni*: non è un target
   intraday di default.

## 8. Miglioramenti proposti (IFTS)

- Convenzione fissa RTH/ETH (fatta, §1.1) — elimina la principale fonte di incoerenza.
- **Gerarchia dei livelli con precedenza esplicita** (pre-market checklist): quando due
  riferimenti distano < 0.25×ATR si trattano come *zona unica* (evita il falso senso di
  precisione).
- Lista nPOC mantenuta come dato del journal → misura in-house del "magnete" (research question
  RQ-3 in `Testing/00`).
- Uso degli LVN per la **qualificazione dei target**: target che deve attraversare un HVN spesso
  → ridimensionato o scartato (regola nel Core Model).

## 9. Implicazioni per il sistema

1. Il profilo entra in 3 punti precisi: pre-market (livelli+day-type prior), qualificazione
   target (LVN/HVN), post-trade review (il movimento ha rispettato la mappa?).
2. Nessun trigger dal profilo: mantiene il sistema semplice e il campione statistico
   concentrato sui trigger di struttura/liquidità.
3. VAH/VAL/POC e IB sono nel modulo Sessions/Levels del Pine (righe della dashboard), non
   disegnati come profilo completo (limiti piattaforma + non necessari al processo).
