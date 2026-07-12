# Manuale IFTS — Vol. 4: KPI, Diario e Routine di Review

> Ciò che non si misura non si migliora; ciò che si misura male peggiora. Questo volume
> definisce COSA misurare (KPI), DOVE (journal) e QUANDO (routine G/S/M). Le definizioni
> formali delle metriche sono in `Testing/01`; i tool di calcolo in `Statistics/Tools/`.

---

## 1. Il diario (journal): lo strumento centrale

- **Formato dati:** una riga per trade (e per giornata NT) secondo `Journal/journal_schema.csv`
  — lo schema è un contratto: i tool Python lo validano.
- **Formato narrativo:** template in `Journal/Journal_Template.md` (screenshot marcato +
  4 righe: contesto, trigger, gestione, lezione).
- **Quando:** riga dati entro fine giornata (R18); parte narrativa entro la review settimanale.
- **Regola d'oro:** il journal registra anche i quasi-trade (setup validi non eseguiti —
  campo `missed=1`): dopo 3 mesi, la differenza tra expectancy dei presi vs dei mancati
  misura la qualità del "giudizio residuo" (se i mancati rendono di più: il filtro
  discrezionale sta togliendo valore).

## 2. I KPI ufficiali

### 2.1 KPI di processo (si guardano OGNI settimana — sono sotto controllo diretto)

| KPI | Formula | Banda obiettivo | Allarme |
|---|---|---|---|
| **Compliance rate** | trade senza `rule_break` / totali | ≥ 95% | < 90% → Vol.3, review straordinaria |
| Pre-market rate | giorni con pre-market scritto / giorni operativi | 100% | < 100% |
| Grade accuracy | trade il cui grade regge alla review / totali | ≥ 90% | < 80% → ricalibrare §grading |
| Time-in-rules | uscite da regola (TP/SL/time/15:50) / totali | ≥ 95% | — |
| NT discipline | giorni NT dichiarati e rispettati | 100% | — |
| Tilt count | protocolli tilt attivati | ≤ 1/mese | ≥ 2 |

### 2.2 KPI di risultato (si giudicano SOLO su n ≥ 30, meglio trimestre)

| KPI | Definizione breve | Ipotesi di lavoro |
|---|---|---|
| Expectancy | media R per trade | +0.35/+0.6R |
| Win rate | % trade > 0 | 42-55% |
| Payoff | avg win / avg loss | ≥ 2.0 |
| Profit Factor | Σwin/|Σloss| | ≥ 1.6 |
| Max DD (R) | dal picco equity in R | entro P95 Monte Carlo |
| R settimanale medio | ΣR/settimane | +1/+3R |
| MAE efficiency | % winner con MAE < 0.5R | ≥ 60% (misura la qualità degli ingressi) |
| MFE capture | R realizzato / MFE mediana | ≥ 55% (misura la qualità delle uscite) |

### 2.3 KPI di ricerca (alimentano le RQ — si guardano al mese/trimestre)

Expectancy per: setup (A/B/C) · grade (B/A/A+) · killzone · day-type · sweep_grade ·
pd_position (quintili) · smt (sì/no) · vwap_sigma (fasce) · day_of_week.
→ Output automatico di `kpi_calculator.py --by <campo>`.

## 3. Routine giornaliera (totale ~45' oltre le KZ)

| Quando | Cosa | Durata |
|---|---|---|
| Pre-market (T−30') | Checklist Vol.1 §1 completa, narrativa scritta | 20' |
| Sessione | Esecuzione con checklist §2-3; NIENTE ricerca/social | KZ |
| Post-trade | Checklist §4 per ogni trade | 5'/trade |
| Fine giornata (post 16:00) | Checklist §5: journal completo, replay 60'', note per domani | 10' |
| Chiusura | Rituale di stacco a orario fisso (Vol.3 §5) | 2' |

## 4. Routine settimanale (venerdì post-close o sabato, 45-60')

1. **Numeri:** `kpi_calculator.py` sulla settimana → R totale, compliance, KPI di processo.
2. **Replay:** ogni trade della settimana su chart (2' l'uno): decisione vs esito
   (doppia colonna C3); tag degli errori per classe.
3. **Narrative review:** le 5 narrative pre-market vs realtà → calibrazione (quante volte lo
   scenario primario si è realizzato? Non per punirsi: per tarare i prior).
4. **Livelli:** aggiornare mappa settimanale (PWH/PWL nuovi, nPOC aperti, dealing range HTF).
5. **Stato limiti:** DD corrente, distanza da R15/R17, size della prossima settimana.
6. **Una frase:** "la lezione della settimana è ______" → in cima al journal della prossima.

## 5. Routine mensile (primo weekend del mese, 2-3h)

1. **KPI completi** su mese e rolling 3 mesi (`kpi_calculator.py --period month`).
2. **Monte Carlo refresh** (`monte_carlo.py` sul campione cumulato): il DD reale è dentro
   le bande? La size è ancora giustificata (Vol.2 §2.3)?
3. **Research review:** stato delle RQ (i contatori del Pine + i tagli §2.3): qualche
   ipotesi ha raggiunto n sufficiente per una decisione?
4. **Proposte di modifica** (R19): SOLO ora si valutano; se approvate → CHANGELOG, versione,
   eventuale re-test.
5. **Equity administration:** ricalcolo equity di riferimento, eventuale prelievo (Vol.2 §5).
6. **Pre-mortem** (Vol.3 §5) + rilettura del contratto psicologico.
7. **Manutenzione:** roll calendar del trimestre, backup journal, versione indicatore.

## 6. Routine trimestrale (mezza giornata)

- Walk-forward check: le metriche OOS del trimestre vs le attese del Core Model §10.
- Kill-switch review (Core Model §10): expectancy < +0.1R su 100+ trade? → procedura audit.
- Revisione della matrice comparativa: c'è evidenza per ri-ammettere una famiglia esclusa
  (es. mean-reversion) o per declassare un setup?
- Formazione: un tema di studio per il trimestre successivo (es. order flow Vol.ricerca 05).

## 7. Il ciclo di miglioramento (come il sistema evolve senza rompersi)

```
Journal (dati) → KPI mensili → anomalia? → Research Question → 
test su dati storici/forward SIM → review mensile → modifica versionata (R19) → 
30 trade di verifica → adozione o rollback
```

Una modifica per volta, mai due parametri insieme, mai a metà mese, mai in drawdown emotivo.
Il sistema cresce alla velocità del campione, non alla velocità delle idee.
