# S03 — Power of Three Intraday (AMD sull'open)

**Famiglia:** Reversal da manipolazione d'apertura · **Riferimenti research:** 02§1.3, 10§1.4, 11§1.3

---

## 1. Concetto e razionale

La giornata (ancorata al true day open 00:00 ET, con replica sul RTH open 09:30) si sviluppa
spesso come Accumulation → Manipulation → Distribution. Il setup: identificare l'accumulazione
(range post-open), attendere la manipolazione (spinta contro la direzione del bias HTF che
prende un pool), entrare al **ritorno attraverso il prezzo di open** in direzione del bias.
L'open cross è la firma del PO3: chi ha comprato/venduto la manipolazione è ora underwater
rispetto all'open.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ |
| **Timeframe** | Bias: Daily/H4 · Riferimenti: 00:00 e 09:30 open · Esecuzione: M5 |
| **Bias** | Obbligatoriamente HTF (daily): il PO3 si opera SOLO pro-bias |
| **Contesto** | Bias HTF chiaro (struttura esterna daily non in transizione); manipolazione = raid di un pool rank ≥ 4 |
| **Sessione** | Trigger valido solo in London KZ o NY AM KZ |

## 3. Filtri

1. Bias daily definito (no giorni post-MSS daily appena avvenuto = struttura in transizione).
2. La "manipolazione" deve aver preso un pool reale (non un semplice drift contro bias).
3. Open cross con displacement (P4) — il rientro lento non qualifica.
4. Niente release tier-1 tra il raid e l'ingresso.

## 4. Sequenza di ingresso (bias long)

1. Prezzo sotto il daily open (00:00) nelle prime ore = "sconto" giornaliero in costruzione.
2. Raid di un pool sell-side (Asia low / PDL) con sweep P6 in London o NY AM.
3. Rientro sopra il **daily open** con candela di displacement M5 = trigger.
4. Ingresso: metà su market al close del trigger, metà limit sul retest dell'open (o del FVG
   del rientro). Stop comune sotto il low del raid − P16.

## 5. Conferme

- SMT sul raid (+1) · London che ha già "provato" lo stesso lato senza successo (+½) ·
  raid che coincide con discount del range settimanale (+½).

## 6. Stop

Sotto/sopra l'estremo della manipolazione − P16. È lo stop *narrativo*: se la manipolazione
viene ri-violata, il giorno non è un PO3 pro-bias.

## 7. Target

- TP1: liquidità interna (ultimo swing M15 sopra l'open) — 1/3 + BE.
- TP2: estremo previsto della distribution = PDH o high settimanale (pro-bias) — 1/3.
- Runner verso il DOL daily con trail su swing M15 (questo setup ha i target più ambiziosi:
  la distribution di un PO3 pro-bias può durare tutta la sessione). Flat 15:50.

## 8. Invalidazione

- Pre-entry: close M15 sotto il low del raid = il "raid" era espansione → NT (o valutare
  bias review).
- Post-entry: ri-perdita dell'open con displacement contrario = uscita anche prima dello stop.
- Doppia manipolazione (raid di ENTRAMBI i lati dell'accumulazione): struttura non-PO3 →
  flat e NT per la giornata su questo setup.

## 9. Esempio pratico (ES, bias daily long)

- Daily open (00:00) 6230.00. Notte: drift sotto, Asia low 6221.
- 03:20 London: sweep 6217.25 (sotto Asia low + PDL 6218.50 in un colpo ✓), close M5 di
  ritorno 6222.75.
- 04:05: displacement M5 chiude 6233.50 sopra il daily open ✓ (body 2.1× media ✓).
- Ingresso: 1/2 market 6233.50, 1/2 limit 6229.75 (retest open, filled 04:40).
  Stop 6216.75 (sweep low − 2 tick). Rischio medio ~14.9 pt.
- TP1 6244 (swing M15) 1/3+BE · TP2 6259.50 (PDH) · runner chiuso 6262 in NY AM.
  Risultato ~+2.1R ponderato.

## 10. Errori frequenti

1. Decidere "oggi è PO3" al mattino e forzare la lettura (il PO3 si *riconosce* dal raid
   compiuto, non si prevede).
2. Operarlo contro bias HTF ("reversal day"): statisticamente è la variante peggiore — vietata.
3. Trigger sull'open cross senza displacement (rientri lenti = range).
4. Stop sotto l'open invece che sotto il raid (invalidazione sbagliata: l'open verrà ritestato
   spesso).
5. Chiudere tutto a +1R su un setup che per costruzione mira all'espansione giornaliera.

## 11. Note quantitative attese

- **Frequenza:** 1–3/settimana (richiede bias daily chiaro + notte "in sconto").
- **Profilo:** WR 40–50%, avg win 2.5R+ (i runner pagano il setup) → expectancy +0.4/+0.8R.
- **Robustezza:** media — dipende dalla qualità del bias daily (input umano).
- **Correlazione:** con S01 alta (il raid è lo stesso evento visto da ancore diverse).
