# Statistics/ — Guida Operativa alla Misurazione

> Le **definizioni formali** delle metriche sono in `Testing/01_Metrics_Definitions.md`
> (fonte unica); le **bande obiettivo** in `Manual/04` §2. Questo file è la guida d'uso
> pratica dei tool.

## 1. I tool

| Tool | Funzione | Input |
|---|---|---|
| `Tools/kpi_calculator.py` | Tutti i KPI (risultato, percorso, processo, settimanali) + stratificazioni | journal CSV (schema `Journal/journal_schema.csv`) |
| `Tools/monte_carlo.py` | Distribuzioni bootstrap (iid + block) di Total R, MaxDD, streak; probabilità di rovina | journal CSV o lista R |
| `Tools/sample_trades.csv` | Dataset sintetico di esempio (102 righe: 60 trade + NT + missed) per provare i tool | — |

## 2. Comandi tipici

```bash
# report completo
python3 Tools/kpi_calculator.py mio_journal.csv

# tagli di ricerca (RQ-2, RQ-8, RQ-10…)
python3 Tools/kpi_calculator.py mio_journal.csv --by killzone --by grade --by sweep_grade --by smt

# tabella contratti per il proprio capitale (Manual/02)
python3 Tools/kpi_calculator.py --size-table 50000

# distribuzioni e rischio di rovina (review mensile, Manual/04 §5)
python3 Tools/monte_carlo.py mio_journal.csv --ruin-r 10
python3 Tools/monte_carlo.py mio_journal.csv --horizon 60 --block 5 --seed 42
```

Requisiti: Python 3.8+ · nessuna dipendenza esterna · output deterministico a parità di
`--seed`.

## 3. Cadenza (rimando a Manual/04)

- **Settimanale:** `kpi_calculator.py` sul file corrente → KPI di processo (compliance!).
- **Mensile:** report completo + `monte_carlo.py`; salvare l'output datato in
  `Statistics/runs/AAAA-MM.txt` (cartella da creare al primo uso reale).
- **Trimestrale:** confronto delle distribuzioni Monte Carlo nel tempo (il deterioramento
  della distribuzione anticipa il P&L nel segnalare edge decay).

## 4. Lettura corretta (tre regole)

1. **n prima di tutto:** nessuna cella con n < 15 va interpretata (il tool le nasconde
   nelle stratificazioni; non aggirarlo abbassando `--min-n` per "vedere qualcosa").
2. **CI accanto alla media:** un'expectancy +0.4R con CI [−0.1, +0.9] non è ancora un
   edge dimostrato — è un edge *plausibile* in accumulo di campione.
3. **Il MaxDD reale si confronta col Monte Carlo, non con la memoria:** dentro P75 =
   normale amministrazione; oltre P95 = allarme di modello (Core Model §10 kill-switch).
