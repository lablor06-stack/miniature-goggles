# S07 — Value Area Rotation ("80% Rule")

**Famiglia:** Value rotation (profile-driven) · **Riferimenti research:** 02§4, 03

---

## 1. Concetto e razionale

Se il prezzo apre (o torna) fuori dalla value area di ieri e poi vi **rientra con accettazione**
(due periodi da 30' consecutivi dentro), la probabilità practitioner-quoted è che attraversi
l'intera VA fino al lato opposto (la "80% rule" — E3/E4, il numero è folklore ma il meccanismo
è solido AMT: rientro in valore = il breakout è fallito, l'asta torna a ruotare nel consenso).
Trade: ingresso al rientro accettato, target il lato opposto della VA.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES (VA più pulita), NQ secondaria |
| **Timeframe** | Riferimenti: VA daily RTH di ieri · Trigger: M30/M15 · Esecuzione: M5 |
| **Bias** | Verso l'interno della VA (direzione = attraversamento) |
| **Contesto** | Apertura/escursione fuori VA fallita; giornata non trend contro il rientro |
| **Sessione** | RTH; ingresso tipico 10:00–13:30; flat 15:50 |

## 3. Filtri

1. VA di ieri **ben formata** (giornata normale, non trend-day sottile né half-day).
2. Apertura fuori VA di ≤ 1×ADR (aperture lontanissime = altro regime, i riferimenti sono morti).
3. **Accettazione:** 2 chiusure M30 consecutive dentro la VA (la definizione classica; proxy
   anticipata ammessa: 4 close M15).
4. Nessun MSS M15 contrario tra rientro e ingresso.

## 4. Sequenza di ingresso (long da sotto)

1. Open sotto VAL; tentativo ribassista che fallisce (idealmente con sweep di un pool ON).
2. Rientro sopra VAL; accettazione (filtro 3).
3. Ingresso: limit sul retest di VAL da sopra (VAL = supporto ora) o market alla seconda
   close M30 se il retest non arriva entro 30'.
4. Un tentativo per giorno.

## 5. Conferme

- Il fallimento sotto VAL è uno sweep P6 di ON-low/PDL (+1: diventa quasi-S01 con vestito
  profile) · VWAP reclaim (+½) · POC di ieri sopra il prezzo ma sotto VAH (percorso "pulito") (+½).

## 6. Stop

Sotto il minimo dell'escursione fuori-VA + P16; cap 0.4×ADR.

## 7. Target

- TP1: POC di ieri — 1/2 + BE.
- TP2: VAH (lato opposto: il compimento della rule).
- Nessun runner oltre VAH di default (la tesi finisce alla traversata; estensioni = altri setup).

## 8. Invalidazione

- Pre-entry: rigetto del rientro (close M30 di nuovo fuori) = NT.
- Post-entry: close M15 sotto il low dell'escursione = stop concettuale.
- Time-stop: la traversata media richiede ore, ma un prezzo fermo su VAL per > 90' senza
  progresso → ridurre 1/2.

## 9. Esempio pratico (ES)

- Ieri: VAL 6228.50, POC 6241.00, VAH 6252.25 (VA regolare ✓).
- Oggi open 6219 (sotto VAL di 9.5 pt ✓); 09:50 low 6214.25 che spazza ON-low 6215.50 (+1 ✓).
- 10:30 e 11:00: due close M30 dentro VA (6231.75, 6234.50) = accettazione ✓.
- Long 6229.25 sul retest VAL 11:20, stop 6212.25 (low − buffer) = 17 pt... > cap 0.4×ADR
  (16.8) → size ridotta al minimo (0.25%) e ok marginale.
- TP1 6241 (POC, 0.7R) — troppo vicino per la regola R:R? No: TP finale è VAH 6252.25 (1.35R)…
  **R:R < 2 → per le regole IFTS questo esempio è NT.** (Esempio lasciato di proposito:
  mostra il conflitto tipico del setup con V7 — vedi §11.)

## 10. Errori frequenti

1. Contare il "rientro" su un wick M5 (serve accettazione, è la parola chiave della rule).
2. Usare VA miste RTH+ETH (03§7.1).
3. Pretendere la traversata nei giorni di apertura lontana (> 1×ADR).
4. Ignorare che spesso il R:R risultante è < 2 con stop strutturale (V7 boccia molti trade
   del setup — vedi esempio).
5. Restare nel trade contro un MSS M15 contrario "perché la rule dice 80%".

## 11. Note quantitative attese

- **Frequenza:** 1–2/settimana.
- **Profilo:** WR quotato alto (folklore 70-80%, realisticamente 55–65%) ma avg win ~1.2R
  e frequente conflitto con V7 (stop strutturale largo vs target a bordo VA).
- **Robustezza:** meccanismo AMT solido; numero "80%" non affidabile.
- **Nota per la matrice:** expectancy/qualità geometrica mediocre sotto i vincoli IFTS
  (V7 in primis) → probabile *retrocessione a contesto* (il concetto di accettazione in VA
  resta preziosissimo come filtro di regime per S06 e come conferma di narrativa).
