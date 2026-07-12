# 09 — Fair Value Gap (FVG) & Inverse FVG (IFVG)

> Il FVG è l'inefficienza più oggettiva del vocabolario SMC: tre candele, una disuguaglianza,
> zero interpretazione. Questo lo rende il candidato ideale per la statistica in-house — ed è
> esattamente ciò che fa il modulo Statistics del Pine.

---

## 1. Teoria

### 1.1 Definizione (a 3 candele, indici 1-2-3 dal più vecchio)

- **Bullish FVG:** `low(3) > high(1)` → gap = [high(1), low(3)].
- **Bearish FVG:** `high(3) < low(1)` → gap = [high(3), low(1)].
- **CE (Consequent Encroachment):** il 50% del gap — il livello di reazione di riferimento.
- **Filtro dimensione (P5):** gap < 0.25×ATR14 ignorati (rumore di quotazione).
- Equivalente AMT: **liquidity void / single prints** — il prezzo ha attraversato senza asta
  bilaterale; equivalente profile: LVN di nuova formazione.

### 1.2 Perché il prezzo "torna" sui gap (i due meccanismi, onestamente)

1. **Two-sided auction:** il mercato massimizza gli scambi; una zona attraversata senza scambi
   è business non fatto → quando l'iniziativa si esaurisce, la rotazione naturale la ricopre.
2. **Inventory rebalancing:** il market making che ha accompagnato l'impulso è sbilanciato;
   il ritracciamento parziale (spesso fino al CE) è il riequilibrio.

**MA:** un FVG dentro un'espansione *sponsorizzata* (news, trend day) può non essere ricoperto
per giorni — il "torna sempre" è E4. La domanda operativa non è *se* torna, ma **cosa fa quando
ci torna**: rimbalza (gap che "lavora", continuation) o lo attraversa (fallimento → IFVG).

### 1.3 IFVG (Inverse FVG)

FVG attraversato da **close** oltre il lato lontano → inverte polarità: bullish FVG violato
diventa resistenza (bearish IFVG). Meccanica gemella del breaker (chi ha comprato "lo sconto"
del gap è intrappolato). Qualificatori: displacement nella violazione; primo retest entro
~20 barre; contesto MSS concordante.

### 1.4 Classificazione operativa IFTS

| Tipo | Contesto di formazione | Uso |
|---|---|---|
| **FVG di displacement** (post sweep+MSS) | Il gap del movimento-segnale | Zona d'ingresso primaria Setup A |
| **FVG di continuazione** (in trend, dentro KZ) | Impulsi successivi | Ingresso Setup B (con BOS interno) |
| **FVG di esaurimento** (dopo run esteso, controtendenza al bias) | Ultimo spasmo | NON si compra; candidato IFVG |
| **FVG fuori KZ / lunch** | Bassa partecipazione | Ignorato dalle statistiche operative |

---

## 2. Vantaggi

- **Oggettività totale** (disuguaglianza su OHLC): zero ambiguità, backtest banale, nessun
  parametro estetico. Il concetto SMC più adatto a fare da "unità statistica".
- Fornisce ingressi *dentro* il displacement con stop definito (oltre l'origine del gap /
  oltre lo sweep) → traduce l'impulso in geometria operabile.
- Il CE dà un livello di precisione intra-zona non arbitrario.
- L'IFVG dà un secondo uso (fallimento → segnale opposto): l'informazione non muore mai, cambia
  segno — proprietà rara e preziosa.

## 3. Svantaggi e limiti

- **Frequenza altissima:** su M1 gli FVG sono ovunque; senza filtri (P5 + KZ + contesto) il
  concetto è inservibile. Il valore è tutto nella selezione.
- Comportamento **regime-dipendente:** fill-rate e reazione cambiano tra balance e trend day →
  le statistiche vanno stratificate (il modulo Statistics separa per KZ).
- Il retest può fermarsi al bordo, al CE, o all'origine: la scelta del limit d'ingresso è un
  trade-off preciso/hit-rate (default IFTS: limit al CE, stop oltre origine+P16).
- Su TF alti i gap sono rari e larghi: zona troppo ampia per lo stop LTF → si scala d'ingresso
  sul FVG LTF *dentro* il FVG HTF.

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Esistenza di intraday reversal parziale dopo impulsi (retracement medi misurabili) | Letteratura mean-reversion intraday su index futures | **E1** (fenomeno) |
| Fill-rate dei FVG (qualunque %) su ES/NQ per TF/KZ | Nessuna fonte pubblica affidabile; **misurabile in-house con precisione totale** | **E2 da produrre** — RQ-7, già implementata nel Pine (contatori fill/CE-touch per FVG qualificati) |
| Il CE reagisce più del bordo | Ipotesi ICT precisa e testabile | **E3 → RQ-7b** |
| FVG con displacement+sweep reagisce meglio del FVG generico | Ipotesi qualificante (parallela a RQ-6) | **E3 → RQ-7c** |
| "Il FVG viene sempre riempito" | Non falsificabile senza orizzonte; falso su orizzonti operativi | **E4** |

**Nota di design:** è deliberato che le tre research question più importanti del sistema
(RQ-6 zone, RQ-7 FVG, RQ-2 sweep) siano *contatori automatici* nel codice: l'utente accumula
evidenza E2 personalizzata sul proprio strumento/TF semplicemente tenendo il chart aperto.

## 5. Contesti favorevoli

- FVG di displacement post-sweep in KZ (definizione stessa del Setup A): il gap è l'impronta
  dell'iniziativa che vogliamo seguire.
- Serie di FVG nella stessa direzione in trend day = conferma di sponsorship (e stazioni B).
- FVG che coincide con OB/breaker (zona composita: si usa il bordo comune, un solo rischio).

## 6. Contesti sfavorevoli

- Lunch e after-hours: fill casuali, reazioni nulle.
- Post-news immediato: gap giganti con semantica diversa (repricing).
- Contro-bias HTF in premium/discount sbagliato: il gap "bello" nella metà sbagliata è
  un'esca (è il FVG di esaurimento, §1.4).

## 7. Errori comuni

1. Comprare *ogni* bullish FVG (senza KZ/contesto/dimensione): il modo più veloce di morire
   di mille tagli.
2. Stop dentro il gap (al CE "per stare stretti"): lo stop vive **oltre l'origine**, il CE è
   l'ingresso, non l'invalidazione.
3. Ignorare il fallimento: gap attraversato = informazione opposta (IFVG), non "quasi tenuto".
4. Misurare il gap su chart con dati back-adjusted vecchi o su TF con candele heikin/renko
   (il FVG è definito su OHLC reali).
5. Trattare il fill del gap come target del trade (il fill è *l'ingresso di qualcun altro*;
   i target del sistema sono i pool/DOL).

## 8. Miglioramenti proposti (IFTS)

- **Filtro P5 (0.25×ATR)** + filtro KZ *alla formazione* → il chart mostra solo gap che
  appartengono alla popolazione statistica di interesse.
- **Stati espliciti** (fresh / CE-touched / filled / inverted) con contatori per stato → RQ-7.
- **Zona composita** quando FVG⊂OB (bordo comune, dedup del rischio).
- **Auto-declassamento**: FVG contro bias in zona sbagliata etichettato "trap-candidate"
  in dashboard (formazione dell'occhio + onestà del sistema).

## 9. Implicazioni per il sistema

1. Il FVG di displacement è la **zona d'ingresso di default del Setup A** (limit al CE);
   il breaker/IFVG è la zona di default del Setup B.
2. Il fallimento della zona d'ingresso (close oltre origine) È l'invalidazione del trade —
   niente "seconda possibilità" sullo stesso evento.
3. Nel Pine il modulo FVG è anche il **laboratorio statistico** del sistema (RQ-7): la scelta
   di quale concetto strumentare per primo è caduta sul più oggettivo.
