# S01 — NY AM Sweep Reversal ("Judas Reversal")

**Famiglia:** Reversal da liquidità esterna · **Riferimenti research:** 01§1.3, 06, 07, 09, 11
**Ruolo atteso:** candidata primaria — è la monetizzazione diretta del modello unificato.

---

## 1. Concetto e razionale

Nella prima parte della sessione NY (08:30–11:00) il mercato completa con alta frequenza il
raid di un pool overnight/di ieri (Judas swing). Se il raid avviene **senza sponsor
informativo** e viene assorbito (sweep P6), l'iniziativa che ne segue (MSS con displacement)
tende a espandere verso la liquidità opposta. Si entra sul ritracciamento nella zona lasciata
dal displacement.

## 2. Specifiche

| Campo | Valore |
|---|---|
| **Mercati** | ES, NQ (uno alla volta; l'altro serve per SMT) |
| **Timeframe** | Bias: H4/H1 · Setup: M15 · Esecuzione: M1–M5 |
| **Bias** | Direzione della struttura esterna HTF; il trade è pro-bias (contro il Judas) |
| **Contesto richiesto** | Overnight dentro/vicino al range di ieri; pool rank ≥ 4 intatto su entrambi i lati; DOL identificabile entro 1.5×ADR |
| **Sessione** | Solo NY AM KZ 08:30–11:00 ET |

## 3. Filtri (tutti obbligatori)

1. **V1/V2:** dentro KZ; nessuna release tier-1 entro ±15' (se release 08:30 → si opera solo dal 08:45).
2. **V3:** giornata non classificata trend-day contro la direzione del trade (open-drive
   contro = NT per questo setup).
3. **V6:** l'ingresso deve trovarsi nella metà favorevole del dealing range M15.
4. Range Asia+London non già oltre 80% dell'ADR (benzina residua).

## 4. Sequenza di ingresso (long; short speculare)

1. **Mappa:** pool sotto (es. PDL + London low ravvicinati) e DOL sopra (es. PDH/nPOC).
2. **Raid:** il prezzo viola il pool inferiore con wick e **chiude di ritorno entro 3 barre M5** (sweep P6).
3. **Shift:** MSS su M1–M5 — close sopra l'ultimo swing interno con displacement P4
   (body ≥ 1.5× media body-20). Il movimento lascia un FVG e/o rompe formando un breaker.
4. **Ingresso:** limit al **CE del FVG di displacement** (o bordo del breaker se presente);
   in OTE del leg. Niente chasing: se il ritracciamento non arriva, il trade non esiste.
5. Ordine valido fino a 11:00 o fino a invalidazione (vedi §8).

## 5. Conferme (upgrade di grade, non necessarie)

- **SMT** bullish col correlato al momento dello sweep (+1 grade).
- **Assorbimento order-flow** al pool, se piattaforma disponibile (+1).
- Sweep multi-pool (PDL+session low in un colpo) (+1).
- VWAP: reclaim della session VWAP durante l'MSS (+½).

Grade A+ = size 0.50% · A = 0.35% · B (minimo ammesso: sequenza pulita senza conferme) = 0.25%.

## 6. Stop

Sotto il minimo dello sweep − buffer P16 (2 tick ES / 4 tick NQ). MAI dentro il FVG.
Se la distanza supera 1.2×ATR(M5)×3 → il trade è "troppo largo": si passa a MES/MNQ o si salta.

## 7. Target

- **TP1 = EQ del dealing range** o primo pool interno (chiusura 1/3, stop a BE+1 tick).
- **TP2 = DOL** (il pool opposto della narrativa) (chiusura 1/3).
- **Runner 1/3** con trailing sotto gli swing M5 confermati, flat obbligatorio 15:50.
- R:R minimo a TP2 ≥ 2.0 verificato prima dell'ingresso, altrimenti NT (V7).

## 8. Invalidazione

- **Pre-entry:** close M5 sotto il low dello sweep (il raid era espansione) → cancellare ordini.
- **Pre-entry:** il prezzo raggiunge il DOL senza ritracciare → trade mancato, non si insegue.
- **Post-entry:** stop = invalidazione; nessun "ridare respiro".
- **Narrativa:** nuova release/news improvvisa → flat discrezionale ammesso (unica eccezione).

## 9. Esempio pratico (numerico, ES)

- Ieri: PDL 6212.00, PDH 6248.50. Asia range 6220–6234; London low 6216.75.
- 09:38 ET: spike a 6209.50 (viola PDL di 2.5 punti = 0.3×ATR14 ✓), close M5 6215.25 (sopra
  PDL in 2 barre ✓). NQ non fa il nuovo low (SMT ✓).
- 09:44: displacement M5 (body 9.25 pt vs media 4.1 ✓) chiude sopra swing interno 6221.50 =
  MSS ✓, lascia FVG 6214.50–6218.25 (3.75 pt ≥ 0.25×ATR ✓).
- Ingresso limit 6216.50 (CE), stop 6209.00 (sotto sweep 6209.50 − 2 tick) = 7.5 pt.
- TP1 EQ 6230.50 (+14 pt ≈ 1.9R, 1/3 + BE), TP2 6248.00 sotto PDH (+31.5 pt = 4.2R).
- Esito esempio: TP1 10:12, TP2 10:56 → trade da ~+2.4R medio ponderato.

## 10. Errori frequenti

1. Entrare al tocco del PDL *prima* dello sweep confermato (anticipare il meccanismo).
2. Contare come sweep una violazione con accettazione (2+ close sotto) e comprare in faccia
   a un breakdown.
3. Chasing del displacement senza aspettare il CE (R:R distrutto in partenza).
4. Ignorare il vincolo P/D: comprare uno sweep che avviene in pieno premium del range M15.
5. Terzo tentativo sullo stesso pool dopo 2 stop (il pool è "bruciato": max 2 tentativi/lato/giorno).

## 11. Note quantitative attese

- **Frequenza:** 2–4 occasioni/settimana per strumento (con tutti i filtri).
- **Profilo:** WR atteso 40–55% con avg win ~2.2R, avg loss ~1R → expectancy attesa
  +0.4/+0.7R (da validare, RQ-1/2).
- **Robustezza:** alta ai parametri (P4/P5/P6 ampi), sensibile alla disciplina oraria.
- **Rischi di modello:** trend day contro (mitigato dal filtro V3), news improvvise.
