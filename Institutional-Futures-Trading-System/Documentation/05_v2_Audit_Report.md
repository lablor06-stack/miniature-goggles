# 05 — Audit v2.0.0: da indicatore completo a strumento quotidiano

> Audit integrale del Master v1 condotto dal punto di vista di: Senior Pine Engineer, UX
> designer finanziario, quant istituzionale, performance engineer, software architect.
> Obiettivo dichiarato: **nessuna feature nuova** — pulizia, velocità, usabilità quotidiana.
> Esito: riscrittura completa → `IFTS_Master.pine` **v2.0.0** (breaking changes su input e
> alert, migrazione in `Pine/README.md`).

---

## 1. CODE REVIEW — problemi trovati e corretti

### Bug funzionali (sfuggiti anche alla Red Team di Fase 7)

| ID | Problema | Impatto | Fix v2 |
|---|---|---|---|
| **B1** | `vwapSideCnt / rthBarCnt` tra due `int`: a seconda della semantica di `/` su interi il voto VWAP del classificatore può risultare sempre 0 → regime TREND dichiarato quasi mai dai soli altri voti | Classificatore degradato | Cast esplicito `1.0 *` → divisione float garantita |
| **B2** | Flip-flop infinito delle zone: un IFVG rotto ri-flippava in IFVG (e ri-contava le statistiche fill a ogni giro) | Statistiche RQ-7 gonfiate; zone "zombie" | Campo `flipped`: **un solo flip per vita della zona**; la seconda rottura ritira la zona; i contatori fill scattano solo su kind FVG originario |
| **B3** | Codice morto: `prevOwnPh/prevOwnPhBi` (SMT) dichiarati e mai usati; `lastMssUpBi/lastMssDnBi` scritti e mai letti; tuple di ritorno con `dummyFlip1/2` | Rumore, manutenzione | Rimossi; API di ritorno ridisegnata |
| **B4** | Doppio sistema di alert sovrapposto (17 `alertcondition` + 5 `alert()`) per gli stessi eventi | Spam, confusione, slot plot sprecati | Sistema unico ridisegnato (vedi §7) |

### Performance

| ID | Problema | Costo | Fix v2 |
|---|---|---|---|
| **P1** | Dashboard: `table.clear` + ~20 righe × 2 celle ricostruite **a ogni tick realtime** (string concat + 40 chiamate API/tick) | Il singolo costo runtime maggiore | Layout fisso senza clear; update **solo a chiusura barra** + primo render al load (`var dashDrawn`); righe ridotte per modalità |
| **P2** | Zone morte mai rimosse dagli array: restavano iterate ogni barra fino all'eviction FIFO | O(dead+alive) per barra | Ritiro immediato: drawing cancellati e **rimozione dall'array** alla morte (tranne modalità Analysis: ghost dimmerati) |
| **P3** | Pool "accepted" tenuti in array e iterati | idem | Rimozione immediata (un livello accettato non è più liquidità) |
| **P4** | Pool "swept" tenuti per sempre (dim) | Oggetti inutili dopo la finestra decisionale | TTL 20 barre (input Performance) poi rimozione |
| **P5** | 12 blocchi quasi identici per il disegno struttura; 4 loop fotocopiati nel Setup B; 2 blocchi speculari ~40 righe nel Setup A | Superficie di bug, leggibilità | Fattorizzati: `f_setupA(dir)` unico parametrizzato, `f_bScan(arr, dir)` unico, draw a one-liner |
| **P6** | Colori zona ricalcolati a ogni evento con funzione a due ternarie | micro | Palette risolta a costanti al top |

### Repaint / lag — verificati, nessun nuovo intervento
Eventi solo su `barstate.isconfirmed`; livelli datati da periodi chiusi `[1]`; `lookahead_off`
ovunque; lag dei pivot dichiarato. Il throttle della dashboard (P1) rende anche i valori
mostrati coerenti con la barra chiusa (prima erano intrabar: un lettore poteva vedere una
σ-position che poi "spariva" — micro-repaint cosmetico ora eliminato).

## 2-3. UX REVIEW + PRIORITÀ VISIVA — il cambiamento principale

**Diagnosi:** v1 mostrava tutto sempre: choch minori, BOS interni ed esterni, etichette su
ogni pool, testo su ogni box, 13 plot, marker sweep ovunque. Su M1-M5 in NY AM il chart
diventava un poster. Il costo non è estetico: è **tempo-decisione** e falsi inviti.

**Soluzione: 3 modalità di display** (input General → `Display mode`), implementate come
matrice di visibilità risolta una volta per run:

| Elemento | FOCUS (esecuzione) | STANDARD (default) | ANALYSIS (studio) |
|---|---|---|---|
| Setup A armato (entry/stop/target/OTE) | ✅ | ✅ | ✅ |
| Trigger Setup B (marker) | ✅ | ✅ | ✅ |
| MSS interni | ✅ | ✅ | ✅ |
| BOS interni | ✗ | ✅ | ✅ |
| choch non qualificati | ✗ | ✗ | ✅ |
| Struttura esterna | solo MSS·ext | solo MSS·ext | tutta |
| Pool attivi | linee; label solo rank ≤ 2 | linee + label | tutto |
| Pool swept | rimossi dopo TTL | rimossi dopo TTL | ghost dim |
| Zone morte (FVG riempiti, OB/BRK invalidati) | **rimosse** | **rimosse** | ghost dim |
| Testo dentro le zone | ✗ | ✅ | ✅ |
| Marker sweep | solo in KZ | tutti | tutti |
| Key opens (midnight/RTH/weekly) | ✗ | ✅ | ✅ |
| Bande VWAP ±σ | ✗ (solo linea VWAP) | ✅ | ✅ |
| SMT (rare, alto valore) | ✅ | ✅ | ✅ |
| Dashboard | 7 righe essenziali | 11 righe | 16 (con blocco stats RQ) |
| KZ shading | ✅ (più tenue di v1) | ✅ | ✅ |

Principio applicato: **massima priorità = ciò che è tradabile ora; media = contesto che
modifica una decisione; bassa = tutto il resto, visibile solo a richiesta (Analysis).**

## 4. MODULARITÀ

- Ogni engine: sola responsabilità, scrive solo nel proprio stato, comunica per valori di
  ritorno (vincolo Pine "le funzioni non assegnano globali" usato come disciplina).
- Lifecycle delle zone separato dalle statistiche (prima intrecciati in una funzione da 90
  righe): `f_zoneLifecycle` + contatori isolati in `stArr`.
- Dipendenze fra moduli **dichiarate nei tooltip** (es. "Setup A richiede l'engine FVG"):
  spegnere un modulo degrada il Signal Engine in modo definito, senza errori.

## 5. PERFORMANCE — budget v2 (vs v1)

| Voce | v1 | v2 |
|---|---|---|
| Aggiornamenti dashboard | ~40 API + N stringhe **per tick** | 0 per tick; 1 batch per chiusura barra |
| Zone iterate/barra | vive + morte (fino ai cap) | solo vive (~8-15) |
| Pool iterati/barra | fino a 30 (incl. consumati) | solo attivi + swept in TTL (~8-12) |
| Oggetti grafici simultanei tipici | ~180-230 | **~60-90** (Standard), ~40 (Focus) |
| `request.security` | 5 max | 5 max (invariato, già minimo) |
| alertcondition (slot plot) | 17 | **7** |
| Righe codice Master | 1.396 | ~1.150 con più funzionalità di controllo |

## 6. SMART VISUALIZATION

Auto-hide implementato come *lifecycle*, non come filtro cosmetico: FVG riempito → ritirato;
OB/Breaker invalidato → ritirato; pool accettato → ritirato subito; pool swept → ritirato a
TTL; il flip (FVG→IFVG, OB→BRK) è vita nuova, non morte → resta. In Analysis tutto ciò che
muore resta come ghost dimmerato per lo studio a posteriori.

## 7. ALERT SYSTEM — ridisegno completo

**Prima:** 17 alertcondition granulari (ogni FVG, ogni BOS, ogni touch…) = inutilizzabili in
pratica (o spam, o 17 alert da configurare). **Ora: 7, tutti azionabili:**

| Alert | Combina | Uso reale |
|---|---|---|
| `Setup A LONG/SHORT armed` (2) | KZ + sweep qualificato + MSS + zona + P/D + R:R | L'alert "vieni a eseguire" |
| `Setup B LONG/SHORT trigger` (2) | regime + bias + zona flip + trigger + DOL | idem, continuation |
| `Qualified sweep in KZ` (1) | sweep P6 + rank ≤ soglia + dentro KZ + cooldown | Il pre-avviso "vieni a guardare" (2-5' prima dell'eventuale MSS) |
| `Kill Zone opened` (1) | London/NY AM start | Sveglia di sessione |
| `Any setup (A or B)` (1) | unione dei 4 | Per chi vuole UN solo alert sul telefono |
| + `alert()` dinamico | payload completo (prezzi entry/stop/target, grade, RR) | Notifiche ricche webhook/mobile |

Rimossi come alert autonomi (restano come *informazione* on-chart/dashboard/grading): FVG
nuovi, BOS, choch, zone touch, flip, SMT isolata, cross VWAP.

## 8. SETTINGS — 12 gruppi nell'ordine richiesto

`General · Market Structure · Liquidity · Order Blocks · FVG · Sessions · VWAP · SMT ·
Dashboard · Alerts · Performance · Advanced` — ogni input con tooltip esplicativo e default
= parametri canonici P1-P17. I knob quantitativi (displacement, tolleranze, finestre barre,
buffer) stanno in **Advanced**: l'utente medio non deve mai aprirli; i cap oggetti e TTL in
**Performance**.

## 9. PROFESSIONAL POLISH

Header標準izzato con version block e contratto di design; banner di sezione uniformi;
naming `f_`/`camelCase`/`SCREAMING_SNAKE` coerente al 100%; nessun numero magico nel corpo;
commenti solo dove spiegano un vincolo non ovvio; palette unica a costanti; tooltip in
inglese tecnico uniforme (il prodotto è vendibile internazionalmente); rimossi tono
colloquiale e ridondanze dai README.

## 10. SELF-CRITIQUE (seconda passata — "cosa cambierebbe un top Pine dev?")

### 10.1 Migliorie pianificate durante la riscrittura (applicate)
1. `f_bScan` unificato per direzione (comparatori derivati dal segno) — zero duplicazione
   residua nel Setup B.
2. Cooldown alert sweep (5 barre) contro i doppi alert su cluster di pool ravvicinati.
3. Dashboard: chiavi statiche scritte UNA volta all'init; solo la colonna valori si
   aggiorna, e solo a chiusura barra (`f_dashFill(keysPass)` a doppio passaggio).
4. `f_lastFvgSince`: scan dall'elemento più recente con early-exit.
5. Sotto `minRr` il setup **non si arma affatto** (v1 lo armava con flag "RR<min ✗" —
   un segnale auto-dichiarato invalido è rumore per definizione; coerenza R7/V7).
6. OTE box legata correttamente all'input `advOteOn`.
7. Rimosso `statsOn` ridondante (le statistiche SONO la modalità Analysis).

### 10.2 Difetti trovati nella verifica finale del codice v2 (corretti prima del rilascio)
8. **Funzione annidata** `f_c` dentro `f_dashFill`: Pine non supporta funzioni nidificate —
   errore di compilazione certo. Estratta come `f_dashCell` globale a responsabilità unica.
9. **Doppio `array.remove` potenziale in `f_zoneRetire`:** nel percorso di eliminazione lo
   stato non veniva marcato `2`; il ramo di age-expiry nella stessa iterazione poteva
   ritirare due volte lo stesso indice, rimuovendo la zona sbagliata (corruzione silenziosa
   dell'array). Fix: `state := 2` in ENTRAMBI i percorsi + guardie sugli stadi successivi.
10. **Input `alKz` non collegato:** dichiarato ma senza effetto (le `alertcondition` non
    sono gate-abili da input). Ora gate-a il payload dinamico `alert()` di apertura KZ.
11. Verifica meccanica anti-regressione: grep dell'intero file per i 30+ identificatori
    v1 rinominati → zero residui; zero funzioni annidate; 7 alertcondition; ~17 plot.

*(La lezione di processo: anche una riscrittura "attenta" produce difetti da compilatore e
da runtime — la seconda passata non è un rituale, è dove si guadagna il diritto di chiamare
il codice professionale.)*

**Non cambiato consapevolmente:** il lag di conferma dei pivot (è il prezzo della
riproducibilità — un "top dev" che lo eliminasse introdurrebbe repaint); il numero di
`request.security` (già minimo); l'assenza di delta/CVD finto (integrità del dato).
