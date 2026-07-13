# Manuale IFTS — Vol. 2: Risk & Money Management

> Il risk management non è un capitolo del sistema: È il sistema. L'edge (expectancy
> positiva) è l'ipotesi; il rischio è l'unica certezza gestibile. Questo volume rende ogni
> decisione di size e di perdita **aritmetica, mai emotiva**.

---

## 1. L'unità di misura: R

- **1R = perdita monetaria a stop pieno** del singolo trade = size × distanza stop × valore punto.
- Tutto si esprime in R: risultati, limiti, drawdown, obiettivi. Il P&L in valuta è vietato
  a schermo durante l'operatività (R: è l'unità della *decisione*; la valuta è l'unità
  dell'*emozione*).

## 2. Sizing per grade (P11)

### 2.1 La formula

```
Rischio_$ = Equity × grade%        (B: 0.25% · A: 0.35% · A+: 0.50%)
Contratti = floor( Rischio_$ / (distanza_stop_punti × valore_punto) )
```

Arrotondamento SEMPRE per difetto (R8). Se il risultato è 0 anche in micro → NT.

### 2.2 Tabelle rapide (esempi)

**Conto 100.000 $, grade A (350 $ di rischio):**

| Stop | ES ($50/pt) | MES ($5/pt) | NQ ($20/pt) | MNQ ($2/pt) |
|---|---|---|---|---|
| 6 pt | 1 ES | 11 MES | 2 NQ | 29 MNQ |
| 10 pt | 0 ES → 7 MES | 7 MES | 1 NQ | 17 MNQ |
| 16 pt | 0 ES → 4 MES | 4 MES | 1 NQ | 10 MNQ |
| 30 pt | — | 2 MES | 0 NQ → 5 MNQ | 5 MNQ |

**Conto 25.000 $ (tipico prop), grade B (62.5 $):**

| Stop | MES | MNQ |
|---|---|---|
| 6 pt | 2 | 5 |
| 10 pt | 1 | 3 |
| 16 pt | 0 → NT su MES | 1 |

*(La tabella si rigenera con `Statistics/Tools/kpi_calculator.py --size-table equity`.)*

### 2.3 Perché 0.25–0.50% (motivazione quantitativa)

Con WR 45% e payoff 2:1, la probabilità di una serie di 8 perdite consecutive su 100 trade è
materiale (≈25%; vedi Monte Carlo). A 0.5% fisso, 8 stop = −4% → recuperabile; a 2% = −16% →
compromette il capitale psicologico e (in prop) viola i limiti. Il rischio per trade è
dimensionato **sulla peggior serie attesa, non sul singolo trade** — output della simulazione
in `Testing/02`.

## 3. Limiti di perdita (la piramide di protezione)

| Livello | Limite | Azione al raggiungimento |
|---|---|---|
| Trade | 1R (stop pieno) | Fine del trade; max 2 consecutivi → fine sessione |
| Giorno | **−2R o −1.0%** (R14) | Piattaforma chiusa; journal; domani size 0.25% (R16) |
| Settimana | **−4R** (R15) | Settimana chiusa; review straordinaria |
| Drawdown | **−8R dal picco** (R17) | Size dimezzate fino a nuovo massimo equity |
| Mese | −10R | Stop totale; audit completo (esecuzione→dati→modello); ripartenza in SIM |

Razionale della progressione: ogni livello scatta *prima* che il danno comprometta il
livello superiore (2R×5gg > 4R settimanali: impossibile bruciare il mese in una settimana
rispettando i limiti).

## 4. Gestione della posizione (aritmetica dei parziali)

Modello A (1/3+1/3+1/3) con TP1 ≈ 1.5R, TP2 ≈ 2.5R, runner variabile — aritmetica esatta:

| Scenario | Calcolo | Esito | Peso ipotizzato | Contributo |
|---|---|---|---|---|
| Stop pieno | −1R | −1.00R | 30% | −0.300R |
| TP1 poi BE | ⅓×1.5 | +0.50R | 20% | +0.100R |
| TP1+TP2 poi BE runner | ⅓×1.5 + ⅓×2.5 | +1.33R | 30% | +0.400R |
| Full target (runner ~4R) | ⅓×1.5 + ⅓×2.5 + ⅓×4 | +2.67R | 20% | +0.533R |
| **Expectancy lorda** | | | 100% | **+0.73R** |

Dal lordo teorico al netto atteso (+0.35/+0.5R, Core Model §10): si sottraggono i degradi
misurabili — time-stop che converte parte degli scenari in ±0.3-0.5R misti, slippage
(~0.03-0.06R/trade a 1-2 tick), errori di esecuzione residui (5% × costo medio). Il cuscino
tra +0.73R teorico e +0.15R di soglia minima di accettazione (Testing/00 §5) è il margine di
sicurezza del sistema.
**Nota:** il time-stop (R13) sposta parte degli "stop pieno" verso perdite parziali (~−0.5R):
a parità di tutto migliora l'expectancy più di qualunque rifinitura dell'ingresso — è la
regola più sottovalutata del sistema.

## 5. Money management del conto

- **Equity di riferimento:** ricalcolata il 1° del mese (non trade-per-trade: evita
  l'accelerazione pro-ciclica della size).
- **Prelievi:** a fine trimestre, 25-50% dell'utile netto se > +15R (paga il trader, consolida
  la disciplina).
- **Compounding:** la size cresce solo col ricalcolo mensile; dopo mesi < 0 la size resta
  invariata (asimmetria prudenziale).
- **Capitale a rischio totale:** margine overnight non applicabile (v1 flat 15:50); margine
  intraday impegnato mai > 30% dell'equity (stress-buffer per slippage/errori tecnici).

## 6. Rischi non di mercato (spesso ignorati, sempre fatali)

| Rischio | Presidio |
|---|---|
| **Tecnologico** (piattaforma/linea giù con posizione aperta) | Stop SEMPRE in server (mai mentale); numero del desk broker su post-it; hotspot di riserva; procedura scritta di flat telefonico |
| **Esecuzione** (fat finger) | Size pre-impostate per grade; conferma ordini ON; mai operare da mobile se non per chiudere |
| **Slippage** (news, sottile) | Vietato l'ordine market nelle release (protocollo news); buffer P16 già nel design |
| **Dati** (feed sbagliato, serie non aggiornata) | Check pre-market: ultimo prezzo vs fonte secondaria; roll calendar |
| **Comportamentale** (revenge, tilt) | I limiti di §3 sono *hard*; Vol.3 |

## 7. Prontuario decisionale rapido

- Stop mancato per gap/slippage oltre 1.5R → flat immediato a mercato, loggare `slippage`,
  fine sessione.
- Ordine parziale eseguito (fill 2 di 5) → gestire i 2 come da piano, non completare.
- Dubbio sulla riga della checklist → la risposta è NT (il dubbio È l'informazione).
- Connessione persa in posizione → protocollo flat telefonico; non "sperare".
- Trade aperto per errore → chiusura immediata a mercato qualunque sia il P&L (non
  "vediamo come va": un trade non pianificato non ha piano di gestione).
