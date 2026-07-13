# Journal — Template Trade (parte narrativa)

> La **riga dati** va nel CSV (schema: `journal_schema.csv`) entro fine giornata (R18).
> Questa scheda narrativa si compila per ogni trade (5') e si completa entro la review
> settimanale. Un trade = una scheda. Screenshot obbligatorio.

---

## Trade #____ · ______ (data) · ES/NQ · Setup A/B/C · Grade ___

### 1. Contesto (compilato PRIMA dell'ingresso — copia dal pre-market)

- Bias HTF: `long / short / neutro` — perché (1 riga): ______
- Narrativa del giorno (dal pre-market, invariata?): ______
- Regime alle 10:30: `rotation / trend / chop` — coerente con il trade? ______
- Pool preso: ______ (rank __) · DOL target: ______

### 2. Trigger ed esecuzione

- Sequenza: sweep ______ → MSS ______ → zona ______ (tipo, prezzi)
- Checklist §2 compilata per iscritto? `sì/no` · Conferme (grade): ______
- Entry ______ · Stop ______ (struttura: ______) · TP1 ______ · TP2/DOL ______ · R:R ex-ante ______

### 3. Gestione (cosa è successo davvero)

- MAE ____R · MFE ____R · Durata ____min
- TP1 eseguito a regola? BE? Trailing su swing M5? Time-stop?
- Deviazioni dalle regole (`rule_break`): ______ — perché è successo: ______

### 4. Esito e lezione

- Risultato: ____R · Uscita per: `TP / stop / time / trail / 15:50 / news`
- **Qualità della decisione (indipendente dall'esito): 1-5** — motivazione: ______
- Rifarei lo stesso trade con le stesse informazioni? `sì/no` — se no, quale filtro
  l'avrebbe escluso? ______
- Una riga per il me-futuro: ______

### 5. Screenshot

`[incolla chart M5 con: pool, sweep, MSS, zona, entry/stop/target marcati]`

---

### Esempio compilato (sintetico)

**Trade #041 · 2026-06-17 · ES · Setup A · Grade A**
1. Bias HTF long (daily HH/HL, H4 concorde). Narrativa: notte in sconto sotto midnight open,
   PDL 6212 + London low 6216.75 sotto, DOL = PDH 6248.50. Regime 10:30: rotation ✓.
2. 09:38 sweep 6209.50 (PDL, rank 2, ritorno in 2 barre M5), SMT vs NQ ✓, MSS 09:44 con
   FVG M5 6214.50–6218.25. Checklist scritta ✓. Entry limit 6216.50 (CE), stop 6209.00,
   TP1 6230.50 (EQ), TP2 6248.00. R:R 4.2 ✓.
3. Fill 09:51. MAE 0.31R. TP1 10:12 (⅓ + BE). TP2 10:56 (⅓). Runner out 6244.75 su trail
   M5 11:22. MFE 4.6R. Nessuna deviazione.
4. +2.41R medio ponderato. Decisione 5/5 (sequenza da manuale). Rifarei: sì.
   Lezione: la pazienza sul CE ha pagato — il primo tocco del bordo FVG non ha filled.
