# S02 — Silver Bullet FVG (finestre 10-11 / 14-15 / 03-04)

**Famiglia:** Continuation/expansion a finestra fissa · **Riferimenti research:** 09, 11
**Ruolo atteso:** complementare a S01 — cattura l'espansione quando il reversal è già avvenuto.

---

## 1. Concetto e razionale

Nelle finestre "macro" (10:00–11:00 la primaria; 14:00–15:00 e 03:00–04:00 le secondarie) il
mercato, avendo già stabilito la direzione della sessione (post-raid), tende a produrre
un'espansione ordinata verso il DOL residuo. Il setup compra/vende **il primo FVG formato
dentro la finestra** in direzione della narrativa già confermata. È un'operazione di
*continuazione*: la decisione direzionale è stata presa prima (da un S01 compiuto, anche se
non tradato).

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ |
| **Timeframe** | Bias: H1+M15 (narrativa di sessione) · Esecuzione: M1–M5 |
| **Bias** | Direzione dell'ultimo MSS di sessione (la direzione post-manipolazione) |
| **Contesto richiesto** | Raid di sessione già avvenuto E risolto (sweep→MSS visibili); DOL residuo ≥ 1R×2 di distanza |
| **Sessione** | Solo dentro la finestra oraria; ordini scaduti a fine finestra |

## 3. Filtri

1. La finestra 10–11 richiede: nessuna release alle 10:00 in agenda (o attendere +10').
2. **DOL residuo:** il target della narrativa NON deve essere già stato raggiunto (se il DOL
   è preso prima delle 10:00, la finestra è NT — la benzina è finita).
3. **V6:** l'FVG d'ingresso deve giacere nella metà favorevole del range di sessione.
4. Distanza percorsa dalla sessione < 100% ADR (no ingresso su giornata già "spesa").

## 4. Sequenza di ingresso (long)

1. Narrativa: sweep del lato sell-side + MSS rialzista già in essere prima delle 10:00.
2. Dentro 10:00–11:00 si forma un bullish FVG M1–M5 (≥ P5) nel senso della narrativa.
3. Limit al CE del FVG; stop sotto l'origine del gap (swing che lo ha generato) − P16.
4. Se il primo FVG fallisce (close sotto), ammesso UN secondo tentativo sul FVG successivo
   se la struttura M5 non ha invertito.

## 5. Conferme

- FVG che si sovrappone a OB/breaker della narrativa (+1).
- Reclaim/hold del VWAP di sessione (+½).
- IB extension in corso nella direzione (contesto profile) (+½).

## 6. Stop

Oltre l'origine del leg che genera il FVG − P16. Tipico: 4–8 pt ES / 15–35 pt NQ su M5.

## 7. Target

- TP1: liquidità interna successiva (swing high M15 precedente) — 1/3 + BE.
- TP2: DOL residuo di sessione — 1/3.
- Runner: trail M5, flat a fine finestra +30' se il momentum muore (time-stop specifico del
  setup), comunque flat 15:50.

## 8. Invalidazione

- Pre-entry: MSS contrario su M5 prima del fill → cancella.
- Post-entry: close M5 oltre l'origine del FVG = stop concettuale anche se lo stop fisico
  (a −P16) non è stato ancora toccato → uscita manuale ammessa.
- Fine finestra senza fill → ordine cancellato, nessun inseguimento.

## 9. Esempio pratico (NQ)

- 09:47: sweep di ON-low 22412 → MSS rialzista M5, prezzo 22480 alle 10:00. DOL: PDH 22610.
- 10:08: pullback impulsivo lascia bullish FVG M5 22468–22492 (24 pt ≥ P5 ✓), dentro discount
  del range di sessione ✓.
- Limit 22480 (CE), fill 10:14. Stop 22436 (origine 22440 − 4 tick) = 44 pt.
- TP1 22540 (swing M15, ~1.4R) 1/3+BE · TP2 22600 (sotto PDH, 2.7R) 1/3 · runner trailed,
  chiuso 22585 alle 11:20 (momentum in calo post-finestra).

## 10. Errori frequenti

1. Usare la finestra come licenza di trade *senza narrativa pregressa* (il Silver Bullet non
   crea la direzione: la esegue).
2. Comprare l'FVG contro l'MSS di sessione "perché siamo nella finestra".
3. Ignorare il DOL residuo: entrare quando il target è a 1R di distanza.
4. Moltiplicare i tentativi (max 2 per finestra).
5. Aspettarsi il setup ogni giorno: 2-3 volte/settimana è la base rate realistica.

## 11. Note quantitative attese

- **Frequenza:** 2–3/settimana (finestra AM), +1–2 (PM) per strumento.
- **Profilo:** WR atteso 45–55%, avg win ~1.8R → expectancy +0.3/+0.5R.
- **Robustezza:** alta (la finestra è fissa, il trigger è oggettivo); rischio principale:
  applicazione senza narrativa (errore umano, non di modello).
- **Correlazione con S01:** alta per costruzione (stessa narrativa, timing diverso) — punto
  chiave per la Fase 3.
