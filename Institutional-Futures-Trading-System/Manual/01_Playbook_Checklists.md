# Manuale IFTS — Vol. 1: Checklist Operative

> Le checklist sono **strumenti di esecuzione sotto stress**, non burocrazia: la loro
> funzione è rendere la qualità della decisione indipendente dallo stato emotivo. Si usano
> COMPILANDOLE (per iscritto o a voce alta), non "sapendole". Modello: aviazione — la
> checklist letta batte la memoria dell'esperto, ogni volta.

---

## 1. CHECKLIST PRE-MARKET (obbligatoria, 30' prima della prima KZ — R20)

### 1.1 Calendario e perimetro (2')

- [ ] Release economiche di oggi con orari ET (CPI/NFP/PIL/FOMC/aste rilevanti)?
- [ ] Giorno speciale? (half-day, rollover week, festivo ponte, OPEX) → se sì: NT o perimetro ridotto scritto
- [ ] Earnings mega-cap stasera/domani (per NQ)? → nota per SMT e size
- [ ] Finestre operative di OGGI dichiarate: `______` (default: NY AM; London se sveglio; PM sì/no)

### 1.2 Struttura HTF e bias (5')

- [ ] Daily: ultima sequenza swing esterni (HH/HL o LH/LL)? MSS recente?
- [ ] H4: struttura concorde o in transizione?
- [ ] Dealing range HTF: estremi `____ / ____` → EQ `____` → prezzo ora in **P / D / EQ**
- [ ] **Bias dichiarato: LONG / SHORT / NEUTRO** (se neutro: solo setup A entrambi i lati, size −1 grade)
- [ ] Il bias di ieri era `____` → cambiato? perché? (una riga)

### 1.3 Mappa della liquidità (5')

- [ ] PWH/PWL: `____ / ____` (presi? intatti?)
- [ ] PDH/PDL: `____ / ____` · ONH/ONL: `____ / ____` · Asia H/L: `____ / ____` · London H/L: `____ / ____`
- [ ] EQH/EQL visibili (M15+): `________`
- [ ] VA ieri: VAH `____` POC `____` VAL `____` · nPOC aperti rilevanti: `________`
- [ ] Key opens: Midnight `____` · Weekly `____` · Daily 18:00 `____`
- [ ] **Pool più probabile lato buy:** `____` (rank __) · **lato sell:** `____` (rank __)

### 1.4 Narrativa del giorno (3') — il cuore del pre-market

Scrivere 2-3 righe nel formato:
> "Il prezzo viene da `[contesto HTF]`. Sopra ha `[pool]`, sotto ha `[pool]`. Lo scenario
> primario è: raid di `[pool X]` in `[finestra]` → reversal verso `[DOL]` (Setup A). Lo
> scenario alternativo è: accettazione oltre `[livello]` → continuation (Setup B). Sono NT se
> `[condizione]`."

- [ ] Narrativa scritta ✍
- [ ] Open vs VA ieri: dentro (prior Rotation) / fuori (prior Trend)?
- [ ] ADR: `____` · già speso in notte: `__%` → benzina residua OK?

### 1.5 Pronti al combattimento (2')

- [ ] Chart setup: M15 (setup) + M1-M5 (esecuzione) + HTF di riferimento; IFTS Master attivo,
      moduli KZ/Liquidity/Structure/Zones ON
- [ ] Size calcolate per grade sul capitale corrente: B=`__` micro/mini · A=`__` · A+=`__`
- [ ] Stato personale (Vol.3 §4): sonno/stress/tempo → **score ≥ 6/10?** Sotto: size −1 grade o NT
- [ ] Stop giornaliero residuo: `____R` · settimanale: `____R`

---

## 2. CHECKLIST DI INGRESSO (da compilare PRIMA dell'ordine — R6)

### 2.1 Setup A (Sweep Reversal)

```
[ ] A1 KZ attiva ORA (no ultimi 10' della finestra)
[ ] A2 Nessuna release ±15'
[ ] A3 SWEEP: quale pool? ______ rank ≥ 4? wick oltre + close ritorno ≤ 3 barre M5?
[ ] A4 MSS: close oltre swing ______ con displacement (body ≥ 1.5×)? FVG lasciato? ______
[ ] A5 ZONA: tipo ______ · CE/bordo ______ · metà favorevole del range M15? · OTE?
[ ] A6 DOL: ______ · stop strutturale: ______ · R:R = ____ (≥ 2?)
[ ] A7 Regime: trend contrario dichiarato? (se sì → STOP, niente trade)
GRADE: SMT? __ multi-pool? __ OF? __ weekly? __ VWAP? __ composita? __ → TOT ____ → size ____%
ORDINE: limit ______ · stop ______ · TP1 ______ · TP2 ______ · contratti ____
```

### 2.2 Setup B (Continuation)

```
[ ] B1 Regime trend dichiarato (≥3 voti) O innesco ORB fuori-value O AVWAP-London tenuta
[ ] B2 Bias H4 concorde
[ ] B3 Zona flip: BRK / IFVG / OB+FVG · discount del leg corrente?
[ ] B4 Trigger: mini-sweep M1 + close M5 a favore avvenuto?
[ ] B5 DOL residuo ______ ≥ 2R?
[ ] B6 Orario 10:00-15:00, non lunch-entry
GRADE: VWAP first-touch? __ correlato? __ composita? __ delta? __ → TOT ____ → size ____%
ORDINE: entry ______ · stop ______ · TP1 ______ · runner plan ______
```

### 2.3 Regola dei 10 secondi

Compilata la checklist, PRIMA di trasmettere: respiro, e la domanda:
**"Se questo trade perde, il replay mostrerà un errore o un costo statistico?"**
Se la risposta è "un errore" → non trasmettere.

### 2.4 Protocollo news (giorni tier-1)

1. Nessun ordine pendente attraverso la release (cancellare tutto a T−15').
2. Posizione aperta a T−15': ridurre a 1/3 con stop a BE, o flat se in perdita.
3. Post-release: primo trade non prima di T+15', SOLO se il quadro A1-A7/B1-B6 è ricostruito.
4. FOMC: NT fino a 14:30; poi Setup C con size 0.25%.

---

## 3. CHECKLIST DI GESTIONE (durante il trade)

- [ ] Ordini TP/SL in piattaforma (mai "mentali")
- [ ] TP1 raggiunto → chiusura parziale eseguita? stop a BE+1?
- [ ] Trailing: aggiorno SOLO su swing M5 confermato (non su ogni candela)
- [ ] Time-stop A: 90' senza TP1 → −1/2 · Time-stop B: MSS M15 contro → flat
- [ ] MI È VIETATO: guardare il P&L in valuta (solo R), aggiungere size, allargare stop,
      "gestire a occhio" sul M1 un trade nato su M5
- [ ] Se sto per violare una regola: scrivere nel journal PRIMA di farlo (il 95% delle volte
      basta a non farlo)

## 4. CHECKLIST DI USCITA E POST-TRADE (5' dopo il flat)

- [ ] Uscita per: TP finale / stop / time-stop / trailing / 15:50 / news → coerente con le regole?
- [ ] Journal: riga completa (tutti i campi schema, incluso MAE/MFE, grade, screenshot chart)
- [ ] Replay 60'': la sequenza trigger→entry→gestione rispecchia la checklist? `rule_break`?
- [ ] Stato emotivo post (1-10) e una riga di nota se ≤ 5
- [ ] Stop giornaliero aggiornato: residuo ____R → posso ancora operare? (R14)

## 5. CHECKLIST DI FINE GIORNATA (10', dopo le 16:00)

- [ ] Tutte le righe journal complete (anche i NT-day: riga `no_trade` con motivo)
- [ ] Narrativa pre-market vs realtà: lo scenario primario/alternativo si è realizzato?
      (una riga — allena la calibrazione, non l'autoflagellazione)
- [ ] Screenshot della giornata archiviato (M5 con marcature)
- [ ] Domani: prime note (news, livelli che restano, nPOC nuovi)
- [ ] Chiusura rituale: piattaforma spenta a orario fisso (Vol.3 §5)
