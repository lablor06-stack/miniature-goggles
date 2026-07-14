# 07 — Decision Support System (v3.0.0)

> Trasformazione da indicatore object-driven a **sistema di supporto decisionale
> state-driven**. Il grafico non mostra più "che cosa il motore ha trovato": mostra **in che
> punto del ciclo di vita del trade ci troviamo e qual è la prossima azione**. Logic layer
> (condizioni, calcoli, alert, statistiche) invariato al bit rispetto a v2.x — FSM e
> Confidence Engine sono layer di *interpretazione* sopra gli eventi esistenti.

---

## 1. La macchina a stati (uno stato alla volta)

```
0 IDLE                  fuori dalle kill zone
1 WAITING LIQUIDITY     KZ attiva, nessun raid recente          → mostra: pool primari
2 LIQUIDITY TAKEN       sweep P6 su questa barra                → + marker SWEEP
3 WAITING MSS           raid in essere, struttura non confermata
4 STRUCTURE CONFIRMED   MSS nella direzione del raid (≤3 barre)
5 WAITING RETRACEMENT   setup armato, limit al CE in attesa     → + zona d'ingresso, E/S/T, OTE
6 ENTRY READY           prezzo a contatto della zona (≤0.25×ATR)
7 TRADE ACTIVE          fill rilevato (A) o trigger B adottato  → SOLO E/S/T
8 TRADE CLOSED          TARGET HIT / STOPPED / SESSION END (10 barre) → poi chart pulito
```

Risoluzione con priorità (trade > closed > armed > narrativa sweep > KZ > idle):
impossibile avere due stati. La direzione (`fsmDir`) segue: il trade → il setup → il lato
del raid → il bias HTF.

**Trade tracker (nuovo, livello UI):** rileva a posteriori l'esito visivo (stop toccato /
target toccato / fine sessione) per completare il ciclo 7→8→0 e pulire il grafico. Non
scrive nelle statistiche né nei segnali: il journal resta il record di verità.

## 2. Confidence Engine (pesi fissi, somma 100)

| Componente | Peso | Sorgente (già calcolata dal motore) |
|---|---|---|
| HTF bias | 20 | `biasDir` vs direzione ipotesi (neutro = 10) |
| Kill zone | 10 | `kzAny` |
| Liquidity sweep | 15 | memoria sweep nel lato giusto, finestra P6/arm |
| MSS | 20 | stato ≥ 4 |
| SMT | 10 | divergenza recente lato giusto |
| Discount/Premium | 10 | `pdPct` nella metà favorevole (n/d = 5) |
| VWAP | 5 | prezzo dal lato giusto del VWAP |
| FVG quality | 5 | zona armata (composita = pieno, semplice = 3) |
| RR | 5 | ≥ minRr pieno, ≥ 1 parziale |

Mostrato SOLO il totale (es. `LONG 87%`); la scomposizione esiste unicamente in **Debug**.
Non tocca i segnali: è la traduzione numerica della checklist per l'occhio.

## 3. Execution Panel (sostituisce la dashboard)

```
┌──────────────────────────┐
│        LONG   87%        │   ← header merged, campitura direzionale
│ Status   WAITING RETRACE │
│ Next     Limit 6216.50   │
│ Entry    6216.50         │
│ Stop     6209.00         │
│ Target   6248.00         │
└──────────────────────────┘
```

Righe fisse (niente layout dinamico = niente clear/flicker); E/S/T mostrano "—" fuori dagli
stati 5-7. Analysis appende il blocco statistiche RQ; Debug appende stato interno, pesi
confidence, memorie sweep, voti regime, correlazione SMT.

## 4. Audit elemento-per-elemento (giustificazione o rimozione)

| Elemento | Stato v3 | Giustificazione |
|---|---|---|
| Execution panel | ✅ unico elemento informativo primario | È la risposta alla domanda del sistema |
| Pool PDH/PDL/AS.H/AS.L | ✅ stati 0-6 | La liquidità è l'oggetto della fase di attesa; ranghi minori restano logic-only |
| Marker SWEEP | ✅ evento | Transizione di stato 1→2, dev'essere visibile sul prezzo |
| Linea MSS corrente | ✅ solo se avanza la narrativa | Ancora visiva dello stato 4; in Exec cap = 1 |
| Zona d'ingresso (FVG armato) | ✅ solo stati 5-6 | Il "dove" dell'ordine limite |
| E/S/T lines | ✅ stati 5-7 | L'ordine stesso |
| OTE | ✅ solo armato | Contesto del retracement; rimossa al fill |
| VWAP | ✅ sempre | Unico riferimento continuo (bianco) |
| KZ shading | ✅ | Comunica lo stato 0↔1 senza testo |
| EQ line | ❌ in Exec (Analysis sì) | Il P-D è già una riga del panel: disegnarlo è ridondante |
| OB boxes | ❌ in Exec (Analysis sì) | Il panel comunica il B-trigger; la box non aggiunge decisione |
| Key opens / AVWAP / bande σ | ❌ in Exec (Analysis sì) | Contesto analitico, non esecuzione |
| Label di zona/EQ, pannello setup on-chart | ❌ rimossi | Il panel narra; doppia scrittura = rumore |
| BOS/choch storici | ❌ in Exec | Storia, non azione |
| Ghost/fading | ❌ ovunque | Lifecycle completo: creazione→update→scadenza→delete |

Budget oggetti in Execution: **~12-20** (4 pool+label, 1 MSS, 1 zona+CE, 3 linee, OTE,
VWAP, shading, panel).

## 5. Architettura del file

```
SIGNAL ENGINE (§6-13, invariato) → STATE MACHINE (tracker + fsm) → CONFIDENCE ENGINE
→ OBJECT MANAGER / RENDERING (visibilità per stato, ensure/undraw simmetrici)
→ EXECUTION / ANALYSIS / DEBUG UI (panel a righe fisse, refresh a chiusura barra)
```

Regole rispettate: nessun rendering nel codice dei segnali; nessun calcolo nelle funzioni di
disegno (leggono stato e disegnano); ogni oggetto ha creazione/aggiornamento/scadenza/
cancellazione; le funzioni non assegnano globali.

## 6. Conformità e compatibilità

- **Invariati:** condizioni A/B, detection FVG/OB/sweep/SMT, calcoli VWAP/regime/grading,
  le 7 `alertcondition` e i payload `alert()` (chi ha alert configurati non deve toccarli),
  statistiche RQ, zero repaint (tutto su barre confermate).
- **Nuovo stato UI dichiarato:** trade tracker (esito visivo), `aState` azzerato al
  trasferimento di proprietà al tracker (bookkeeping visivo, non condizione di segnale).
- **Due secondi:** direzione+confidenza nel header colorato, stato e next-step nelle prime
  due righe — l'obiettivo di leggibilità è strutturale, non tipografico.

## 7. Addendum v3.1 — Quality Engine, MTF, checklist, auto-journal

- **Quality Engine (sostituisce il Confidence Engine v3.0):** 13 componenti pesati
  (somma 100, pesi in testa al file) → classi A+ ≥95 · A ≥90 · B ≥80 · IGNORE <80. Le
  classi pilotano SOLO l'enfasi: spessore/dimming della entry line, badge nel panel,
  testo degli alert dinamici. Nessun gate sui segnali (le 7 alertcondition e le condizioni
  di arm sono identiche).
- **MTF context:** mini-bias pivot-hysteresis su H1/M15/M5 (stessa struttura dell'H4),
  attivo solo per TF ≥ chart TF; riga `MTF H4·H1·15·5` con ✓ quando tutto è allineato
  alla direzione d'ipotesi; componente di score (allineamento proporzionale).
- **Smart zone selection:** ranking qualità FVG (size/ATR 30 · unmitigated 25 · freshness
  20 · confluenza OB 15 · prossimità 10) e OB (kind 30 · unmitigated 25 · freshness 20 ·
  prossimità 15 · size 10). Analysis mostra solo il campione per lato; Execution mostra il
  best-FVG del lato-narrativa allo stato 4 e la zona armata agli stati 5-6; Debug tutto.
- **Checklist automatica:** Explain mode (toggle — Pine non ha eventi hover) appende 9
  requisiti ✓/✗ (soglia: ≥75% del peso) + riepilogo `x/9 · WAIT/READY`; Debug aggiunge la
  scomposizione numerica completa dei 13 pesi.
- **Trade lifecycle:** stage per MFE in R (≥1 BE, ≥1.5 PARTIAL, ≥2.5 RUNNER) nella riga
  Status durante il trade.
- **Auto-journal (campione chart, cap 50):** R realizzato, confidenza, esito per ogni
  trade chiuso dal tracker; aggregati in Analysis (n · WR · avg R · conf media win/loss).
  Complementare — non sostitutivo — del journal scritto.
- **Target engine:** invariato per mandato (la selezione del target è dentro l'RR gate dei
  segnali); estensioni a tier documentate come roadmap.

## 8. Verifica finale eseguita

Zero funzioni annidate; dichiarazioni sempre prima dell'uso (tracker vars spostate prima
dei gate degli arm); 7 alertcondition; ~17 plot/shape; f_panelFill ritorna il conteggio
righe; nessun identificatore delle versioni precedenti residuo; arm durante trade attivo
non clobbera le linee del tracker (gate `tState == 0`); ri-materializzazione delle linee
armate alla chiusura del trade se un arm è ancora valido.
