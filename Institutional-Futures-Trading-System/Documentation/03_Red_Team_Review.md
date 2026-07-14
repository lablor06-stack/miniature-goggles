# 03 — Red Team Review (Fase 7)

> Revisione avversariale dell'intero progetto: bias, overfitting, errori logici,
> inefficienze, parti inutili, codice migliorabile. Ogni finding ha severità, decisione e
> stato. Le correzioni marcate ✅ sono applicate nel repository in questa stessa versione.

**Metodo:** (a) ri-derivazione indipendente di ogni formula e numero; (b) lettura del codice
con il modello "cosa direbbe il compilatore/il runtime"; (c) caccia esplicita ai punti in cui
il progetto potrebbe mentire a sé stesso (proxy silenziosi, definizioni circolari, gradi di
libertà nascosti).

---

## 1. Findings di CODICE

### C1 — 🔴 CRITICO · Filtro correlazione SMT calcolato sui LIVELLI di prezzo
- **Dove:** `IFTS_Master.pine` §10, `IFTS_SMT.pine`.
- **Problema:** `ta.correlation(close, corrCl, 20)` correla i *livelli*: due serie di prezzo
  qualunque in trend hanno correlazione ≈ ±1 quasi sempre (correlazione spuria da radice
  unitaria). Il filtro `corrMin = 0.7` non si sarebbe quasi mai disattivato → l'SMT avrebbe
  operato anche nei regimi di rotazione settoriale che il filtro doveva escludere
  (Research/12 §1.2). Il componente più promosso del modulo era, di fatto, decorativo.
- **Fix:** correlazione sui **rendimenti**: `ta.correlation(ta.change(close),
  ta.change(corrCl), corrLen)`. Soglia default ricalibrata a 0.55 (le correlazioni di
  rendimento sono strutturalmente più basse dei livelli; ES/NQ intraday tipicamente
  0.7-0.9, rotazioni < 0.5). — ✅ applicato a entrambi i file + Research/12 aggiornato.

### C2 — 🟠 ALTO · Setup A non applicava il vincolo Premium/Discount (V6)
- **Dove:** `IFTS_Master.pine` Signal Engine.
- **Problema:** il Core Model (A5) richiede l'ingresso nella metà favorevole del dealing
  range; il codice armava il setup ovunque → incoerenza modello↔codice (viola il contratto
  di `Documentation/01` §2).
- **Fix:** gate aggiunto: long solo se `entry ≤ rngEq`, short solo se `entry ≥ rngEq`
  (quando il modulo P/D è attivo). Deviazione dichiarata: il range è quello del TF del
  chart, non M15 fisso — documentato nel tooltip e in Pine/README §5. — ✅ applicato.

### C3 — 🟡 MEDIO · Finestre in barre cambiano significato con il TF
- **Dove:** `armWindow`, `armExpiry`, cooldown Setup B.
- **Problema:** 12 barre = 12' su M1 ma 3h su M15: il default era tarato implicitamente su
  M5 senza dirlo (grado di libertà nascosto = terreno da overfitting).
- **Fix:** tooltip con equivalenze e raccomandazioni per TF (M1: 25 · M5: 12 · M15: 6);
  default invariato (M5 è il TF di esecuzione canonico). — ✅ applicato.

### C4 — 🟡 MEDIO · Marker swing con offset hardcoded
- **Dove:** `IFTS_Structure.pine` plotshape `offset = -3` con pivot length configurabile.
- **Fix:** `offset = -msIntLen`. — ✅ applicato.

### C5 — 🟡 MEDIO · Aritmetica dei parziali imprecisa nel Manuale
- **Dove:** `Manual/02` §4.
- **Problema:** l'expectancy dei quattro scenari (30/20/30/20%) è **+0.73R**, non "≈ +0.9R"
  come scritto; la deduzione verso +0.35/0.5R netto non era esplicitata.
- **Fix:** tabella ricalcolata esattamente (−0.30 +0.10 +0.40 +0.53 = +0.73R lordo) +
  derivazione esplicita del netto (degrado stimato per time-stop/slippage/errore umano).
  — ✅ applicato.

### C6 — 🟢 BASSO · Descrizione fuorviante nel journal schema
- `risk_r` descritto come "% equity" ma chiamato `_r` → rinominata la descrizione in
  "Rischio pianificato in % equity (0.25/0.35/0.50) — N.B. non è in R". — ✅ applicato.

### C7 — 🟢 BASSO · MFE capture degenerava a 0 con WR < 50%
- Individuato al collaudo del tool (mediana su tutti i trade: i perdenti hanno capture 0);
  ridefinita sui soli winner in `Testing/01` + `kpi_calculator.py`. — ✅ già applicato in
  Fase 6 (documentato qui per completezza).

### C8 — 🟢 BASSO · Lag noti e dichiarati (non fixati, by design)
- Pool PDH/PDL creati alla chiusura della prima barra della nuova sessione (1 barra di lag).
- IDM-wait (Core Model 3.3) non implementato nel Signal Engine: resta procedura umana.
- Setup B parte dalle 10:30 (fine IB) anziché 10:00 (B6): scelta più conservativa del
  modello, allineata alla dichiarazione del regime.
→ Elencati in Pine/README §5 (limiti dichiarati). — ✅ documentati.

## 2. Findings di METODO (bias & overfitting audit)

### M1 — 🟠 Il rischio di overfitting si concentra nei PESI del grading
I punteggi (+1 SMT, +1 multi-pool, +0.5 VWAP…) sono convenzioni ragionate, non stime. Un
attaccante direbbe: "state facendo asset pricing con pesi inventati".
**Mitigazione (attiva):** i pesi determinano SOLO la size (0.25→0.50%), mai la validità del
trade; il journal registra ogni componente separatamente (RQ-2/5/10) → dopo n≥100 i pesi si
ristimano dai dati con procedura R19. Dichiarato in Core Model §3.2 nota. — ✅ nota aggiunta.

### M2 — 🟠 Le frequenze/WR attesi delle strategie (Fase 2) sono stime a priori
Usate nella matrice (C2/C3). Se fossero sistematicamente ottimiste, la selezione resterebbe
valida? Sì nelle *relazioni* (la matrice confronta le strategie con lo stesso metro; l'ordine
è robusto a un bias comune), no nei *livelli* (le soglie di accettazione del Testing sono la
rete di sicurezza sui livelli assoluti). — ✅ nota in `Strategy/20` §2.

### M3 — 🟡 Sopravvivenza del bias di conferma nel replay manuale
S2 prevede blind-date e no-rewind, ma il replayer conosce comunque "l'epoca" (es. 2024 =
bull). Mitigazione aggiuntiva: quota di giornate campionate da un assistente/script che non
rivela la data finché possibile + successo misurato ANCHE sui NT (checklist rispettata).
— ✅ aggiunto a Testing/00 §6.

### M4 — 🟢 Doppio conteggio delle confluenze omogenee
Rischio che "FVG dentro OB dentro OTE" venga contato come 3 conferme quando è 1 informazione.
Il design già lo previene in parte (composite zone = +0.5 una volta); esplicitato il principio
di ortogonalità in Core Model §3.2. — ✅ nota aggiunta.

### M5 — 🟢 Il classificatore di regime Pine usa proxy del range (non VA vera)
Dichiarato in Pine/README §5. Coerente con ADR-5 (assistenza, non verità). — già a posto.

## 3. Findings di CONTENUTO (parti deboli o inutili)

| # | Finding | Decisione |
|---|---|---|
| D1 | `Strategy/S07` (80% rule): il documento stesso dimostra il conflitto con V7 — tenerla nel lotto è teatro? | **Tenuta**: la matrice DEVE contenere candidate bocciate per dimostrare il processo di selezione (un lotto di sole promosse è survivorship). Chiarito in `20` §5 |
| D2 | Doppioni concettuali S01/S03/S04/S08 nel lotto | Deliberati (famiglie), già assorbiti in Fase 3 ✓ |
| D3 | Le citazioni accademiche sono verificate? | Sì, riverificate una a una in questa review: Osler 2003/2005 (FRBNY), Hasbrouck 2003 (JF), Admati-Pfleiderer 1988 (RFS), Wood-McInish-Ord 1985 (JF), Berkowitz-Logue-Noser 1988 (JF), Madhavan 2002, Cont-Kukanov-Stoikov 2014, ABDV 2003 (AER), MOP 2012 (JFE), Budish-Cramton-Shim 2015 (QJE), Connors-Raschke 1995, Zarattini-Aziz 2023 (SSRN, dichiarato non peer-reviewed). Nessun numero inventato citato come loro |
| D4 | Il Manuale promette "estremamente dettagliato": mancano i casi limite di esecuzione? | Aggiunto §7 "Prontuario decisionale rapido" a Manual/02 (già presente) ✓ + Examples/ in Fase 9 |
| D5 | Nessun disclaimer sul fatto che il Signal Engine Pine NON è il sistema completo | Aggiunto avviso esplicito in Pine/README §5 e nel label del setup — ✅ |

## 4. Che cosa resta strutturalmente fragile (rischi residui accettati)

1. **L'edge è da dimostrare (E2 da produrre).** Mitigazioni: pipeline S1-S4, soglie
   pre-registrate, kill-switch. Questo progetto vende un *processo misurabile*, non un
   win-rate — chiunque affermi il contrario nel materiale di vendita viola il progetto.
2. **Dipendenza dall'operatore umano** (livelli 0-4 dello stack): mitigata da checklist e
   KPI di processo, non eliminabile in v1 (ADR-1).
3. **Decadimento dell'edge** se i pattern di liquidità si spostano: sorvegliato dal
   confronto Monte Carlo nel tempo (Statistics/00 §3) — non prevenibile.
4. **Rischio piattaforma Pine:** i limiti oggetti/performance su chart molto lunghi;
   mitigato da caps e drawing window, non testato oltre 20k barre.

## 5. Esito della review

- Findings critici/alti: **2 (C1, C2)** — entrambi corretti.
- Findings medi: 3 — corretti.
- Findings bassi/documentali: 7 — corretti o dichiarati.
- La Fase 8 (ottimizzazione) parte da questa base con il debito tecnico azzerato.
