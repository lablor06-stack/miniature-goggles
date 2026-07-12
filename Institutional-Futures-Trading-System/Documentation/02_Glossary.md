# 02 — Glossario Tecnico

> Definizioni **operative** (testabili) dei termini usati nel sistema. Dove la definizione IFTS
> differisce dall'uso comune retail, la differenza è indicata con ⚠. Parametri numerici: vedi
> `00_Conventions_and_Specs.md` §4.

## Struttura di mercato

| Termine | Definizione operativa IFTS |
|---|---|
| **Swing High/Low** | Pivot confermato: massimo/minimo con N barre inferiori/superiori su entrambi i lati (N=3 interno, N=8 esterno). ⚠ Un pivot è *confermato* solo N barre dopo: ogni logica a valle sconta questo lag. |
| **Struttura interna** | Sequenza di swing a pivot corto (P1=3) dentro il leg esterno corrente. |
| **Struttura esterna** | Sequenza di swing a pivot lungo (P2=8) che definisce il dealing range. |
| **BOS (Break of Structure)** | *Close* oltre l'ultimo swing confermato **nella direzione del trend corrente**. Conferma di continuazione. ⚠ Wick oltre il livello senza close = sweep, non BOS. |
| **CHoCH (Change of Character)** | Primo *close* oltre l'ultimo swing **contro il trend corrente**. Primo avviso di possibile inversione; da solo NON è un segnale. |
| **MSS (Market Structure Shift)** | CHoCH qualificato da **displacement** (P4) e preferibilmente preceduto da sweep di liquidità. È il CHoCH "che conta" nel sistema. |
| **Displacement** | Movimento impulsivo: candela (o cluster) con body ≥ 1.5× media dei body a 20 periodi che rompe un livello. Proxy dell'iniziativa istituzionale. |
| **Dealing range** | Range tra l'ultimo swing esterno high e low rilevanti (post-sweep). Base per premium/discount. |

## Liquidità

| Termine | Definizione |
|---|---|
| **Liquidità (pool)** | Cluster di stop/ordini presunti oltre un estremo visibile: old high/low, EQH/EQL, estremi di sessione, PDH/PDL, PWH/PWL. |
| **BSL / SSL** | Buyside liquidity (stop dei corti sopra i massimi) / Sellside liquidity (stop dei lunghi sotto i minimi). |
| **Liquidità esterna** | Pool oltre gli estremi del dealing range (old highs/lows). |
| **Liquidità interna** | Inefficienze dentro il range (FVG, OB non mitigati) che il prezzo tende a rivisitare. Ciclo tipico: esterna → interna → esterna. |
| **EQH / EQL** | Equal highs/lows: due o più estremi entro tolleranza P3 (0.10×ATR14). Liquidità "ingegnerizzata" particolarmente attraente. |
| **Sweep (liquidity raid/purge)** | Violazione di un pool con **wick** e ritorno con close entro 3 barre (P6). Se il prezzo *accetta* oltre (close multipli), non è sweep: è espansione. |
| **Turtle Soup** | Trade che sfrutta un falso breakout di un massimo/minimo di riferimento — nome storico (Connors/Raschke) dello sweep-fade. |
| **Draw on Liquidity (DOL)** | Il pool opposto più probabile come destinazione corrente del prezzo. La "narrativa" del sistema è: da quale pool veniamo, verso quale andiamo. |
| **Inducement (IDM)** | Pool interno creato per indurre ingressi anticipati (tipicamente il primo pullback sotto/ sopra un estremo), che viene spazzato prima del vero movimento. |

## Zone (PD Arrays)

| Termine | Definizione |
|---|---|
| **PD Array** | (Premium/Discount Array) Insieme ordinato delle zone di interesse ICT: OB, FVG, Breaker, Mitigation, wick, old H/L. |
| **Order Block (OB)** | Ultima candela (o cluster) opposta prima di un displacement che rompe struttura. Bullish OB = ultima candela ribassista prima dell'impulso rialzista. Zona = da open a extreme della candela (definizione IFTS: body preferito, wick incluso solo su LTF). |
| **Propulsion/Refined OB** | Raffinamento dell'OB sul TF inferiore (riduce la zona, aumenta R:R, riduce hit-rate). |
| **Breaker Block** | OB **fallito**: prezzo lo attraversa con close e rompe struttura → la zona si inverte di polarità (ex-support diventa resistenza operativa e viceversa). Richiede sweep del lato originario per essere di qualità. |
| **Mitigation Block** | Come il breaker ma senza sweep preventivo dell'estremo: candela opposta che ha originato un movimento poi negato; zona di "pareggio" degli ordini intrappolati. Qualità inferiore al breaker. |
| **FVG (Fair Value Gap)** | Inefficienza a 3 candele: `low[0] > high[2]` (bullish) o `high[0] < low[2]` (bearish) sul candle 1..3. Filtro dimensione P5. Sinonimo AMT: *liquidity void*. |
| **CE (Consequent Encroachment)** | 50% del FVG — livello di reazione atteso più preciso del bordo. |
| **IFVG (Inverse FVG)** | FVG attraversato con close → inverte polarità (da support a resistance e viceversa). Concettualmente il "breaker dei gap". |
| **Mitigazione** | Primo ritorno del prezzo in una zona. La zona si considera *consumata* (one-shot di default nel sistema). |

## Range, Fibonacci, VWAP

| Termine | Definizione |
|---|---|
| **Premium / Discount** | Metà superiore / inferiore del dealing range. Regola: si compra in discount, si vende in premium — mai il contrario senza downgrade del setup. |
| **Equilibrium (EQ)** | 50% del dealing range. Magnete naturale + spartiacque P/D. |
| **OTE (Optimal Trade Entry)** | Zona di retracement 62–79% del leg di displacement (P7). |
| **VWAP** | Volume-Weighted Average Price di sessione (ancorato a 18:00 ET). Bande a ±1σ/±2σ (dev. standard pesata per volume). Benchmark di esecuzione istituzionale (E1). |
| **AVWAP** | VWAP ancorato a un evento (open settimanale/mensile, swing rilevante, giorno di news). |
| **POC / VAH / VAL** | Point of Control (prezzo col massimo volume) / Value Area High/Low (68% del volume) del profilo di riferimento (giornata precedente o composito). |
| **Naked/Virgin POC** | POC di una sessione passata mai ritestato — magnete statistico. |

## Auction Market Theory / Profile

| Termine | Definizione |
|---|---|
| **Value Area** | Zona di accettazione: ±1σ (≈68%) del volume/TPO attorno al POC. |
| **Balance / Range day** | Mercato in accettazione: rotazioni dentro la value area, profilo a campana. |
| **Imbalance / Trend day** | Mercato in ricerca: range extension, profilo allungato, value che migra. |
| **Open types** | Open-Drive, Open-Test-Drive, Open-Rejection-Reverse, Open-Auction (in ordine decrescente di convinzione direzionale). |
| **IB (Initial Balance)** | Range della prima ora RTH (09:30–10:30). IB stretto → probabile range extension; IB ampio → probabile balance. |
| **80% Rule** | Se il prezzo apre/torna dentro la value area del giorno prima e vi resta accettato (2 mezz'ore TPO), alta probabilità di traversata dell'intera VA. (Livello evidenza E3 — verificare in-house.) |
| **Excess** | Coda di rifiuto (tail) a un estremo del profilo — asta terminata. Assenza di excess = possibile continuazione. |
| **Poor High/Low** | Estremo senza excess (asta incompleta) → probabile revisit. |

## Order Flow

| Termine | Definizione |
|---|---|
| **Delta** | Volume aggressivo in acquisto (market buy) − volume aggressivo in vendita (market sell) per barra. |
| **CVD** | Cumulative Volume Delta: somma progressiva del delta. Utile in divergenza (prezzo HH, CVD LH = assorbimento). |
| **Footprint** | Vista bid×ask per livello di prezzo dentro la barra. |
| **Assorbimento** | Aggressione consistente che NON muove il prezzo (limit order dominanti) — tipico agli estremi/sweep. |
| **Exhaustion** | Aggressione decrescente in prossimità di un livello — fine dell'iniziativa. |
| **DOM** | Depth of Market (book a 10 livelli). Nei futures moderni: pesante spoofing → si usa per contesto, non per segnali. |
| **Stop run** | Movimento innescato dall'esecuzione a mercato degli stop — meccanicamente ciò che il sistema chiama sweep. |

## Tempo

| Termine | Definizione |
|---|---|
| **Kill Zone (KZ)** | Finestre orarie a massima partecipazione istituzionale (vedi Conventions §2). Unico tempo in cui il sistema autorizza ingressi. |
| **Silver Bullet** | Finestre 03–04 / 10–11 / 14–15 ET: setup FVG-centrico verso liquidità opposta con narrativa già chiara. |
| **Judas Swing** | Falso movimento di inizio sessione contro la direzione reale della giornata (manipolazione), tipicamente completato in London o primo NY. |
| **PO3 / AMD** | Power of Three: Accumulation (range) → Manipulation (Judas/sweep) → Distribution (movimento reale). Frattale su ogni orizzonte. |
| **PDH/PDL, PWH/PWL** | Previous Day/Week High/Low — pool esterni di riferimento. |
| **Midnight Open** | 00:00 ET — riferimento per il "premio" giornaliero (sopra = premium intraday per short, sotto = discount per long, nel modello ICT). |

## Correlazioni

| Termine | Definizione |
|---|---|
| **SMT Divergence** | Smart Money Technique: divergenza tra strumenti correlati sugli swing (ES nuovo low, NQ no) → il mancato conferma segnala assorbimento sul più forte. Si valuta SOLO a pivot confermati su livelli rilevanti. |
| **Crack di correlazione** | Rottura temporanea della correlazione ES/NQ — contesto favorevole a reversal, sfavorevole a continuation "in simpatia". |

## Rischio e misura

| Termine | Definizione |
|---|---|
| **R** | Unità di rischio: perdita a stop pieno. Trade da +2.4R = profitto pari a 2.4 volte il rischio iniziale. |
| **Expectancy** | E = (WR × avgWin_R) − ((1−WR) × avgLoss_R), in R per trade. |
| **Profit Factor** | Σ profitti / |Σ perdite|. |
| **MAE / MFE** | Maximum Adverse/Favorable Excursion: massima escursione contro/pro durante il trade. |
| **Drawdown (DD)** | Distanza % dal picco di equity. MaxDD = il peggiore della serie. |
| **Sharpe / Sortino** | Rendimento in eccesso / deviazione standard (Sortino: solo downside). Definizioni e periodicità in `Testing/01`. |
| **Walk-forward (WFA)** | Ottimizzazione su finestra IS + verifica su finestra OOS successiva, iterata nel tempo. |
| **Monte Carlo** | Ricampionamento (bootstrap) della sequenza di trade per stimare distribuzioni di DD/CAGR e probabilità di rovina. |
