# S05 — Opening Range Break & Retest (ORB con contesto Profile)

**Famiglia:** Breakout/continuation d'apertura · **Riferimenti research:** 02§1.2 (IB), 03, 11

---

## 1. Concetto e razionale

Il range dei primi 15' RTH (09:30–09:45) definisce l'asta iniziale. La rottura con conferma
(retest tenuto) in direzione del gap/bias, nei giorni in cui l'apertura è *fuori* dal valore
di ieri, sfrutta la convinzione dell'open (Open-Drive/Open-Test-Drive) — la variante con
maggior supporto pubblico recente (studio ORB di Zarattini-Aziz 2023 su QQQ, E2 replicabile).
È la strategia "anti-S01": monetizza i giorni in cui NON c'è reversal ma iniziativa
d'apertura.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ (lo studio pubblico è su QQQ ≈ NQ) |
| **Timeframe** | OR: 09:30–09:45 (M15) · Esecuzione: M5 |
| **Bias** | Direzione del gap d'apertura vs value di ieri (open fuori VA = convinzione) |
| **Contesto** | Open-Drive o Open-Test-Drive; gap ≥ 0.3×ADR dal close di ieri |
| **Sessione** | Ingresso tra 09:45 e 11:00; flat 15:50 |

## 3. Filtri

1. **Apertura fuori dalla VA di ieri** (sopra VAH per long): senza questo, l'ORB degrada
   verso il coin-flip (i giorni in-value sono rotazionali).
2. Prima candela M5 direzionale (close nel terzo estremo del range — proxy Open-Drive).
3. Nessuna release alle 10:00 tra breakout e retest (o gestirla flat).
4. ADR residuo ≥ 2× rischio previsto.

## 4. Sequenza di ingresso (long)

1. OR definito 09:45 (ORH/ORL su M15).
2. Breakout: close M5 sopra ORH con displacement (P4) — non un wick.
3. **Retest:** limit sul lato superiore dell'OR (ORH diventa supporto) o sul FVG del breakout;
   fill entro 45' dal break, altrimenti ordine cancellato.
4. Un secondo ingresso è ammesso su BOS interno successivo se il primo non ha fillato.

## 5. Conferme

- VWAP sotto il prezzo e inclinato a favore (+½) · IB extension già in corso (+½) ·
  volume del breakout > 1.5× media 20 barre M5 (+½) · nPOC/target LVN davanti (+½).

## 6. Stop

Sotto il midpoint dell'OR (per OR normali ≤ 0.5×ADR) oppure sotto ORL − P16 per OR stretti.
Regola pratica: lo stop non supera 0.35×ADR, altrimenti NT.

## 7. Target

- TP1: 1× ampiezza OR proiettata (measured move) — 1/2 + BE.
- TP2: DOL daily (PDH esterno / nPOC) o 2× OR.
- Runner facoltativo SOLO se la giornata è classificata trend-day alle 10:30 (IB extension
  netta): trail su swing M15. Altrimenti tutto chiuso a TP2.

## 8. Invalidazione

- Pre-entry: rientro con close M5 *dentro* l'OR dopo il breakout = falso break → NT lato long
  (e attenzione: è carburante per S01 short).
- Post-entry: close M5 sotto ORL = uscita immediata anche se lo stop formale non è toccato.
- 11:00 senza TP1 → ridurre 1/2 e time-stop 12:00.

## 9. Esempio pratico (NQ)

- Ieri VAH 22480. Oggi open 09:30 a 22540 (gap sopra VA ✓ = 0.45×ADR ✓).
- OR 09:30–09:45: 22505–22562. 09:55: close M5 22578 con body 2× media ✓ (breakout).
- Limit 22564 sul retest ORH, fill 10:04. Stop 22533 (mid OR) = 31 pt.
- TP1 22619 (+1 OR, 1.8R) 1/2+BE · TP2 22665 (PDH) raggiunto 11:40 (+3.3R sul secondo mezzo).
- Nota: alle 10:30 IB extension confermata → runner autorizzato ma non usato nell'esempio.

## 10. Errori frequenti

1. ORB su apertura *dentro* la value di ieri (il filtro n.1 è il 70% dell'edge).
2. Comprare il breakout a mercato sull'high del movimento (si entra SOLO al retest: metà
   della qualità del setup è nel prezzo d'ingresso).
3. OR troppo stretto preso alla lettera (sotto 0.15×ADR il rumore domina: allargare al range
   09:30–10:00 o saltare).
4. Ignorare il MOC/PM: l'ORB è un setup AM; la sua estensione pomeridiana va gestita col
   playbook PM, non tenuta "a fede".
5. Confondere falso breakout (rientro nell'OR) con retest (tocco del bordo): il primo nega,
   il secondo conferma.

## 11. Note quantitative attese

- **Frequenza:** 1–3/settimana (i gap fuori-value non sono quotidiani).
- **Profilo:** WR 40–50%, avg win ~2R; expectancy attesa +0.3/+0.6R (lo studio pubblico
  suggerisce edge concentrato nei giorni gap — coerente col filtro).
- **Robustezza:** buona; parametri quasi tutti strutturali (OR, VA) e non ottimizzabili.
- **Nota per la matrice:** unica candidata *breakout-side* con supporto E2 pubblico recente;
  copre il regime (trend-from-open) in cui S01/S03 sono NT → ottima complementarità.
