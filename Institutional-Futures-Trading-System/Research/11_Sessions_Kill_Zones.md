# 11 — Sessioni, Kill Zones, Power of Three, Judas Swing

> Il tempo è il filtro con il **miglior rapporto evidenza/costo dell'intero sistema**: la
> concentrazione intraday di volume e volatilità è un fatto E1 replicabile in un pomeriggio,
> e il filtro orario costa zero in complessità. Se si potesse tenere una sola regola di tutto
> il progetto, sarebbe: *opera solo nelle finestre giuste*.

---

## 1. Teoria

### 1.1 La giornata ES/NQ (orari canonici in `00_Conventions` §2)

| Fase (ET) | Carattere tipico | Funzione nel sistema |
|---|---|---|
| 18:00–20:00 | Riposizionamento post-settlement, sottile | Nessuna |
| **Asia 20:00–00:00** | Range building, ~20-30% dell'ADR | Costruisce i primi pool (Asia H/L) |
| 00:00–02:00 | Transizione, minimo di attività | Midnight open si fissa |
| **London 02:00–05:00** | Prima espansione vera; spesso *un* lato di Asia viene preso | Judas #1; costruisce London H/L |
| 05:00–08:00 | Pausa/pre-NY, news EU digerite | Mappa pre-market |
| 08:30 | **News window USA** (CPI/NFP/PIL…) | Regole news (no-trade ±) |
| **NY AM 08:30–11:00** | Il blocco di volume dominante; 09:30 open cash, 10:00 dati | **Finestra primaria**: sweep decisivo + movimento del giorno |
| 11:00–12:00 | Decadimento | Gestione, non ingressi |
| **Lunch 12:00–13:00** | Rotazioni sottili, mean-reversion casuale | NO-TRADE |
| **NY PM 13:30–15:00** | Ripresa; 14:00 FOMC nei giorni Fed | Setup C (playbook ridotto) |
| 15:00–16:00 | MOC flows, squaring | Flat entro 15:50 |

### 1.2 Kill Zones: cosa sono davvero

Finestre in cui la **partecipazione istituzionale è massima** → i meccanismi su cui il sistema
scommette (cascate assorbite, displacement sponsorizzato) hanno la controparte necessaria.
Fuori KZ lo stesso pattern grafico è *sintassi senza semantica* (vedi `06` §6). La versione
"gli algoritmi delle banche si attivano alle 08:30" è narrativa E4; la versione "volume,
volatilità e ampiezza delle rotazioni si concentrano lì" è E1 — e per operare basta la seconda.

### 1.3 Power of Three (PO3 / AMD) e Judas Swing

- **PO3:** la sessione/giornata come `Accumulation (range) → Manipulation (falsa rottura
  contro la direzione vera) → Distribution (l'espansione reale)`. In AMT: balance → falso
  breakout → range extension. Frattale: vale per la giornata, la settimana, la singola KZ.
- **Judas Swing:** la manipolazione d'apertura — il primo movimento post-open (00:00 o 09:30)
  che prende liquidità dal lato *sbagliato* e inverte. Statisticamente: "il high/low del giorno
  si forma spesso nella prima parte della sessione" — verificabile (RQ-9: % di giorni in cui
  l'estremo giornaliero si forma entro le 10:30 / entro London).
- **Implicazione operativa:** il sistema NON si fida della prima direzione del giorno; aspetta
  che un pool rilevante venga preso e *rigettato* (il Judas è il Setup A visto dal lato tempo).

### 1.4 Profilo settimanale (uso leggero, E3)

Tendenze practitioner: lunedì range/estremo settimanale provvisorio; martedì-mercoledì
espansione (spesso low/high of the week); giovedì continuazione/reversal; venerdì squaring.
Uso IFTS: **solo come prior debole** nel pre-market (mai come filtro bloccante) + misurazione
nel journal (`day_of_week` è un campo obbligatorio).

---

## 2. Vantaggi

- **Evidenza E1, costo zero, anti-overfitting** (nessun parametro continuo: o sei nella
  finestra o no).
- Taglia automaticamente le due fasce a peggior expectancy del retail (lunch, notte) e
  concentra il campione statistico in condizioni omogenee → tutte le altre statistiche del
  sistema diventano più pulite.
- Riduce il tempo-schermo a 2-4 ore/giorno → sostenibilità psicologica (Manual/03).

## 3. Svantaggi e limiti

- Trade eccellenti fuori finestra vengono persi (accettato: il sistema compra varianza bassa
  con selettività).
- Le finestre sono legate al ciclo news/cash USA: nei giorni senza dati la 08:30-09:30 è più
  debole; nei giorni FOMC il pomeriggio domina → il calendario resta un input quotidiano.
- DST: due volte l'anno UK/USA disallineano di una settimana → SOLO orari ET con timezone
  esplicita (P nel codice: `America/New_York` ovunque — errore classico dei toolkit retail
  eliminato by-design).

## 4. Prove statistiche

| Claim | Evidenza | Livello |
|---|---|---|
| Volume/volatilità intraday a U con picchi a open/close cash | Wood-McInish-Ord (1985), Admati-Pfleiderer (1988); replicabile su ES in un'ora di lavoro | **E1** |
| Le mosse più ampie si concentrano attorno a release macro programmate (08:30/10:00/14:00) | Letteratura event-study macro-announcements (es. Andersen-Bollerslev-Diebold-Vega 2003) | **E1** |
| L'estremo del giorno si forma sproporzionatamente spesso nelle prime ore | Misurabile direttamente (RQ-9); consenso practitioner ampio | **E3 → E2 facile** |
| Lunch = expectancy peggiore per strategie direzionali | Consenso + coerenza con la U del volume | **E3 → E2 facile** |
| Profilo settimanale (Tue/Wed extreme of week, ecc.) | Solo folklore strutturato | **E3 debole** — prior, mai regola |
| "Le KZ funzionano perché gli algo bancari partono a orari fissi" | Narrativa non necessaria e non provata | **E4** — il sistema usa la spiegazione E1 |

## 5. Contesti favorevoli

- Giorni con calendario "pulito" (nessuna release entro la KZ): la meccanica sweep/reversal
  domina — Setup A al meglio.
- Giorni con overnight compresso e pool simmetrici: la KZ NY AM ha massima probabilità di
  produrre il raid decisivo.
- FOMC days per il Setup C PM (post-14:30, dopo la prima onda): regole dedicate nel playbook.

## 6. Contesti sfavorevoli

- Half-days, vigilie, settimana di Natale/Ferragosto: KZ formalmente attive ma vuote.
- Rollover (volume splittato).
- Release tier-1 DENTRO la finestra: la KZ si opera solo dal +15' post-release (regola R-news
  nel Manual).

## 7. Errori comuni

1. Operare il pattern giusto all'ora sbagliata (il n.1 in assoluto tra chi impara SMC).
2. Orari hardcoded nel fuso del broker/della piattaforma → tutto slitta col DST.
3. Forzare il Setup C con le regole del mattino (il PM ha meno benzina: target più corti,
   size minore — playbook dedicato).
4. Ignorare il calendario economico ("tanto guardo il grafico") — il grafico non mostra la
   release di tra 3 minuti.
5. Restare a schermo 8 ore "per non perdere nulla": il decadimento decisionale post-2h è il
   vero costo (Manual/03).

## 8. Miglioramenti proposti (IFTS)

- **Time-filter come modulo master nel Pine:** ogni segnale di ogni modulo porta il flag
  `inKZ`; gli alert operativi sono emessi SOLO in finestra (configurabile).
- **RQ-9 automatizzata:** la dashboard traccia dove si è formato l'estremo di giornata rispetto
  alle finestre — accumula la statistica per il proprio strumento.
- **News-guard manuale ma proceduralizzato:** checklist pre-market obbligatoria con orari
  release; il Pine mostra un campo "News OK?" in dashboard che il trader setta da input
  (onestà: Pine non ha accesso al calendario in modo affidabile → non si finge).
- **Session map SVG** (`Images/`) come riferimento visivo unico.

## 9. Implicazioni per il sistema

1. Le KZ sono una **condizione necessaria** di ogni setup (nessuna eccezione discrezionale:
   un'eccezione qui invalida tutte le statistiche a valle).
2. Il PO3 fornisce la *narrativa di default* della giornata: il pre-market formula l'ipotesi
   (quale lato verrà manipolato?), la KZ la verifica o la falsifica.
3. Flat entro 15:50 ET sempre (MOC): niente overnight nel sistema v1.
