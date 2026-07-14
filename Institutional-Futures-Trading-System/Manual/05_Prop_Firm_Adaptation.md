# Manuale IFTS — Vol. 5: Adattamento Prop Firm

> Il sistema è nato prop-firm-compatible (intraday, flat 15:50, rischio frazionale), ma le
> prop futures hanno vincoli specifici — soprattutto il **trailing drawdown** — che cambiano
> l'aritmetica del rischio. Questo volume adatta i parametri senza toccare il modello.

---

## 1. I vincoli tipici (verificare SEMPRE il regolamento specifico)

| Vincolo | Forma tipica (evaluation/funded 50k-150k) | Impatto sul sistema |
|---|---|---|
| **Trailing max drawdown** | 2-4.5k dal picco *unrealized* o EOD | Il vero capitale non è il nominale: è il DD residuo |
| Daily loss limit | 1-3k o assente | Spesso più stretto del nostro R14 → domina |
| Consistency rule | max 20-50% del profit da un solo giorno | Limita i giorni runner; gestire i target |
| Position size cap | 5-15 mini | Irrilevante alle nostre size |
| Orari | flat pre-close obbligatorio; news vietate su alcune | R3/R4 già conformi |
| Scaling plan | contratti sbloccati per step di profit | Rende obbligatoria la progressione micro→mini |

## 2. La regola centrale: ridefinire l'equity

**Equity operativa prop = min(daily loss residuo, trailing DD residuo).**
Tutte le percentuali P11 e i limiti R14-R17 si calcolano su QUESTA equity, non sul nominale.

Esempio: conto 100k, trailing DD 3.000$, picco corrente = start → equity operativa 3.000$.
Grade A (0.35%)… su 3.000$ = 10.5$? Non operabile. → In prop si usa la **conversione a R
fissi**: si definisce 1R in dollari come frazione del DD residuo.

### 2.1 Parametri prop ufficiali IFTS

| Parametro | Valore prop | Razionale |
|---|---|---|
| 1R | **DD residuo / 12** (cap: daily limit / 2.5) | Sopravvivere alla peggior serie attesa (8 stop) mantenendo margine |
| Stop giornaliero | −2R (≡ R14) | Coerente; con 1R=DD/12 → −2R ≈ −17% del DD residuo |
| Setup ammessi in evaluation | Solo A e B grade ≥ A | Ridurre varianza dove il tempo è vincolato |
| Consistency guard | Se il giorno supera +N% del target totale: stop alle nuove entry | Calcolato nel pre-market prop |
| Micro-first | Prime 2 settimane (o fino a +6R) solo micro | Calibrazione slippage/esecuzione della piattaforma prop |

### 2.2 Esempio numerico (conto 50k, trailing 2.500$, daily 1.250$)

- 1R = min(2500/12, 1250/2.5) = min(208, 500) = **208$** → su MES con stop 8 pt (40$/contratto):
  5 MES; su ES: 0 → si opera MES finché il DD residuo non cresce.
- Dopo +5R (equity picco +1.040$): DD residuo 2.500$ (trailing al picco) + cushion → 1R
  resta 208$ ma con cuscinetto: upgrade a 1 ES sulle distanze ≤ 4 pt? NO: si ricalcola solo
  a step (+6R) per evitare size creep — tabella di progressione scritta PRIMA di iniziare.

## 3. Evaluation vs funded: due mestieri

### 3.1 Evaluation (obiettivo: passare SENZA imparare vizi)

- Target tipico +6-10% con DD 3-5%: il rapporto è aggressivo per design della prop →
  la tentazione è over-risk. L'antidoto: **il tempo è la risorsa gratis** (molte prop non
  hanno limite di giorni o costano poco al mese): passare in 6-10 settimane a rischio
  normale batte il 50/50 del passare-in-5-giorni.
- Vietato: "one-shot day" (tutto il target in un giorno di leva) — anche dove non violasse
  la consistency, insegna il vizio che ucciderà il funded.
- KPI evaluation: identici (compliance ≥ 95%); la sola differenza è 1R prop (§2.1).

### 3.2 Funded (obiettivo: primo prelievo, poi regime)

- Fase 1 (fino a +12R): costruire cushion sopra il trailing → size invariata, nessun grade A+
  (il DD vicino è ancora "vivo").
- Fase 2 (cushion ≥ 12R o trailing bloccato al breakeven, dove previsto): parametri standard.
- **Prelievi:** appena consentiti e a ogni soglia (il denaro sul conto prop non è tuo finché
  non è prelevato — è la vera funzione obiettivo).
- Più conti (copy non consentito quasi ovunque — verificare): meglio sequenziali che
  paralleli; due conti = due journal = metà attenzione.

## 4. Differenze operative rispetto al conto privato

| Tema | Conto privato | Prop |
|---|---|---|
| Unità di rischio | % equity (P11) | R fisso da DD residuo (§2.1) |
| Runner | Pieno (P17) | Cap ai giorni-monstre se c'è consistency rule |
| Setup C (PM) | Ammesso | Solo in funded fase 2 |
| News | Protocollo Vol.1 §2.4 | Alcune prop le VIETANO: il regolamento vince |
| Micro | Strumento di scaling | Strumento primario fase iniziale |
| Psicologia | DD = proprio denaro | DD = "vite" a tempo: pressione diversa, protocolli identici |

## 5. Selezione della prop (checklist di due-diligence)

- [ ] Trailing DD: intraday o EOD? (EOD è molto più vivibile per il sistema) Si blocca al BE?
- [ ] Daily limit: hard (chiusura forzata) o soft?
- [ ] Consistency rule: formula esatta?
- [ ] News trading: consentito? finestre vietate?
- [ ] Micro disponibili? Commissioni e dati inclusi?
- [ ] Payout: frequenza, minimo, split, storia di pagamenti (community feedback recente)
- [ ] Piattaforme supportate e qualità dati (il sistema richiede candele CME reali)
- [ ] Regole "nascoste": DCA vietato? flat obbligatorio alle news? max trade/day?

**Nota finale:** nessun adattamento prop modifica trigger, filtri o gestione del Core Model.
Cambia SOLO l'aritmetica del rischio. Se una prop impone vincoli che costringono a violare
il modello (es. vietare gli stop larghi strutturali di NQ), si cambia prop o si opera solo
ES/MES — mai piegare il modello al vincolo sbagliato.
