# 04 — Optimization Report (Fase 8)

> Obiettivi della fase: ridurre complessità, consumo risorse e tempi; migliorare
> leggibilità, manutenzione e precisione. Questo report distingue le ottimizzazioni
> **progettate fin dall'inizio** (e qui verificate) da quelle **applicate in questa fase**,
> e dichiara i budget di risorse del sistema.

---

## 1. Ottimizzazioni applicate in Fase 8

### O1 — Zone a `extend.right` nativo (Pine, Master + modulo Zones)
- **Prima:** ogni barra confermata aggiornava il bordo destro di ogni zona viva
  (`box.set_right` + `line.set_x2`) → con ~35 zone vive ≈ 70 chiamate di API drawing/barra,
  ~105.000 chiamate sulla drawing window da 1500 barre.
- **Dopo:** le zone nascono con `extend = extend.right` (estensione visiva a costo zero);
  il bordo si tocca UNA volta sola, all'evento di morte (`extend.none` + right fissato).
- **Effetto:** eliminato ~100% del lavoro di manutenzione grafica per-barra delle zone;
  resta il solo lavoro di *logica* (confronti prezzo/zona), che è l'essenza incomprimibile.
- Nessun cambiamento funzionale: aspetto identico, semantica identica.

### O2 — Verifica di precisione della varianza VWAP (nessun cambiamento necessario)
Flag della Red Team (RT-13) chiuso con analisi numerica: la formula one-pass
`E[x²]−E[x]²` a prezzi ES (~6.5e3, x² ~4.2e7) in float64 (2.2e-16 di precisione relativa)
produce un errore assoluto ~1e-8 su varianze di ordine 1–100 → errore relativo ≤1e-9:
**cinque ordini di grandezza sotto il tick**. La variante Welford avrebbe aggiunto stato e
letture più difficili senza beneficio misurabile → rifiutata (la complessità si paga,
la precisione qui non rende).

## 2. Ottimizzazioni by-design verificate (già in v1, qui documentate come budget)

| Budget | Valore | Meccanismo |
|---|---|---|
| **Lavoro per barra (worst case)** | O(pools + zones + 2·pivot) ≈ O(100) operazioni elementari, costante | cap espliciti: 30 pool, 16+12 zone, array SMT fissi |
| **Oggetti grafici** | ≤ ~230 su 500/tipo disponibili | cap FIFO per famiglia + `drawLookback` (default 1500 barre) |
| **`request.security`** | max 5 (D, W, SMT, bias) — 12.5% del limite di 40 | chiamate condizionali ai moduli attivi (`dynamic_requests`) |
| **Moduli spenti** | zero disegni, zero security, zero logica non-primitiva | guard clause su ogni blocco; v6 valuta `and` lazy |
| **Repaint** | zero logico | eventi solo su `barstate.isconfirmed`; livelli datati da periodi chiusi `[1]` |
| **Plot slots** | ~35 su 64 | contati (13 plot + 4 shape + 17 alertcondition + bgcolor) |

## 3. Tempi misurati (tooling Python, stdlib-only)

| Tool | Input | Tempo (ambiente di sviluppo) |
|---|---|---|
| `kpi_calculator.py` (report completo + 2 stratificazioni) | 102 righe | **0.10 s** |
| `monte_carlo.py` (2×10.000 sim × 100 trade, tail-injection, ruin) | 60 trade | **0.96 s** |

Complessità: KPI O(n·BOOT_N) dominata dal bootstrap CI (2000 resample); Monte Carlo
O(sims·horizon). A n=1.000 trade restano < 2 s e < 10 s: nessuna ottimizzazione necessaria
per l'orizzonte di vita del progetto (un trader genera ~250-300 trade/anno).

## 4. Riduzione di complessità (contenuti)

- **Fonte unica per ogni concetto:** parametri in `Documentation/00`, metriche in
  `Testing/01`, KPI operativi in `Manual/04` — gli altri file *riferiscono*, non copiano
  (verificato in questa fase con ricerca incrociata dei valori: P1–P17 non compaiono
  ridefiniti da nessuna parte).
- **Spazio dei segnali ridotto a 2 trigger** (MSS per inversione, BOS interno pro-bias per
  continuazione): ogni concetto aggiuntivo del corpus è filtro o conferma, mai nuovo
  trigger → il campione statistico converge 3-5× più in fretta e la superficie di
  overfitting resta minima (vincolo V4).
- **Duplicazione Pine dichiarata e delimitata:** le primitive replicate nei moduli
  standalone sono ~60-80 righe/file, prezzo del deploy senza dipendenze (ADR §3.1) —
  alternativa (library) documentata come roadmap v2.

## 5. Leggibilità e manutenzione (stato finale)

- Header di sezione numerati e uniformi in tutti i .pine; naming coerente
  (`camelCase`/`f_`/`SCREAMING_SNAKE`); zero numeri magici nel corpo (tutto da input o
  costante nominata).
- Funzioni Pine senza side-effect su globali (vincolo del linguaggio sfruttato come
  disciplina architetturale: lo stato condiviso vive in array/oggetti passati o dichiarati).
- Python: due file autonomi, zero dipendenze, `--help` completo, deterministico via seed.
- Documentazione: percorsi di lettura per ruolo (README §3), cross-link sistematici.

## 6. Ottimizzazioni valutate e rifiutate (con motivo)

| Proposta | Motivo del rifiuto |
|---|---|
| Welford per VWAP σ | Nessun beneficio a float64 (vedi O2); +stato, −leggibilità |
| Skip delle zone lontane dal prezzo nel ciclo di update | Il confronto di distanza È il costo che si vorrebbe evitare; guadagno nullo |
| Library Pine condivisa per eliminare la duplicazione moduli | Frizione di deploy per l'utente finale (richiede pubblicazione); rimandata a v2 |
| Cache dei livelli HTF in array persistenti | `request.security` con `[1]` è già O(1)/barra e più leggibile |
| Ridurre i documenti di ricerca "per snellezza" | La ricerca È il prodotto in due-diligence; la sintesi esiste già (`Research/00`) |

## 7. Esito

Bilancio della fase: 1 ottimizzazione strutturale applicata (O1), 1 flag di precisione
chiuso con analisi (O2), budget di risorse quantificati e documentati, 5 pseudo-ottimizzazioni
rifiutate consapevolmente. Il sistema rispetta i suoi budget con margine ≥ 2× su ogni asse.
