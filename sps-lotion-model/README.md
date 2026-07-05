# SPS Lotion Model+ (Pine Script v6)

Toolkit di esecuzione in stile ICT per TradingView, costruito attorno a un'idea centrale:
individuare il **Draw on Liquidity** più rilevante in entrambe le direzioni e collegargli un
**Fair Value Gap** del timeframe corrente. Un solo overlay al posto di 5-6 script separati.

## Installazione

1. Apri TradingView → **Pine Editor**
2. Incolla il contenuto di `SPS_Lotion_Model_Plus.pine`
3. **Salva** → **Aggiungi al grafico**

Pensato per mercati intraday liquidi (ES, NQ, YM e micro, forex majors, crypto majors)
su timeframe di esecuzione da 1 a 15 minuti.

## Moduli

| Modulo | Cosa fa |
|---|---|
| **Session Liquidity** | H/L di NY AM, NY PM, Asia e London disegnati a chiusura sessione, rimossi allo sweep |
| **Previous Day (PDH/PDL)** | High/Low del giorno precedente (confine giornata NY), rimossi allo sweep |
| **Data High/Low** | Rilevatore datawick a 1 minuto sulla finestra NY 8:30 (sequenza 8:29→8:30→8:31, wick ≥ 6 punti) |
| **Midnight Open** | True Day Open (NY 00:00) con "Days Kept" configurabile (0–30 giorni) |
| **SMT Divergence** | Confronto con asset correlato (Automatico: NQ↔ES, MNQ↔MES, YM→ES, MYM→MES, GC↔SI, MGC↔SIL — o Manuale), 3 preset di sensibilità, SMT real-time e Gap SMT |
| **EQH / EQL** | Equal highs/lows sul timeframe grafico con tolleranza di prezzo e gate sul timeframe minimo |
| **HTF FVG** | FVG non riempiti su timeframe superiore (default 5m), linee sul bordo prossimale con etichetta M5/H1, filtro weekend e min gap size |
| **DOL** | Motore centrale: seleziona ogni barra un BSL sopra e un SSL sotto il prezzo da 5 sorgenti attivabili (HTF Swings, Data H/L, HTF FVG Edges, PDH/PDL, Session H/L) |
| **Linked FVG** | Collega un FVG bullish al DOL.L e uno bearish al DOL.H; l'inversione in chiusura genera il bias direzionale (LONG/SHORT) con alert |
| **Overlap merging** | Lo stesso prezzo non viene mai disegnato due volte: i livelli nominati (PD > Sessioni > Data) mantengono la loro etichetta e il DOL si attenua quando coincide |
| **Watermark** | Nome indicatore + timeframe, ticker e data in basso al centro |

## Consigli rapidi

- Parti con **DOL + Session Liquidity** attivi e solo **HTF Swings** come sorgente DOL
- Aggiungi **Data H/L** nei giorni di news, **HTF FVG Edges** nei range HTF ben definiti
- Il setup da manuale: tap del DOL + divergenza SMT sullo stesso pivot + Linked FVG appena invertito nella direzione corrispondente
- SMT **Sensitive** su 1–3m, **Strict** su 5–15m
- **Days Kept** del Midnight Open a 5–7 per mantenere il contesto senza affollare il grafico

## Alert disponibili

- **Linked FVG LONG bias** — FVG bearish collegato invertito al rialzo con DOL.H attivo
- **Linked FVG SHORT bias** — FVG bullish collegato invertito al ribasso con DOL.L attivo
