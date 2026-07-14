# Manuale IFTS — Vol. 3: Psicologia ed Errori

> Approccio da performance coach: la psicologia del trading non si "risolve" con la forza di
> volontà ma con **ingegneria del contesto** (regole, limiti, rituali) + **allenamento
> deliberato** (review, simulazione) + **igiene di base** (sonno, energia). La motivazione è
> inaffidabile per design; il sistema è costruito per funzionare anche nei giorni in cui il
> trader è mediocre.

---

## 1. Il modello mentale: i due capitali

Si gestiscono **due capitali**: quello monetario (Vol.2) e quello **psicologico** — la
capacità residua di eseguire regole sotto stress. Ogni violazione, ogni tilt, ogni sessione
oltre l'orario consuma capitale psicologico; ogni esecuzione pulita (anche perdente!) lo
ricostituisce. I limiti giornalieri/settimanali proteggono ENTRAMBI i capitali: −2R si
recupera in un giorno buono; il tilt da −6R costa settimane.

## 2. Gli errori catalogati (tassonomia ufficiale del journal, campo `rule_break`)

### Classe E — Errori di esecuzione (violano una regola scritta)

| Codice | Errore | Radice psicologica | Contromisura primaria |
|---|---|---|---|
| E1 | Ingresso anticipato (pre-conferma) | FOMO, bisogno di "prendere il minimo" | La checklist §2.1 compilata PER ISCRITTO |
| E2 | Chasing (ingresso senza pullback) | FOMO post-segnale | Regola: se il CE non è raggiunto, il trade non esiste |
| E3 | Stop allargato | Negazione della perdita | Stop in server + regola R10 (violarla = fine sessione) |
| E4 | Media della perdita | Illusione del controllo | R12; size pre-impostata rende scomodo aggiungere |
| E5 | Size oltre grade | Avidità/rivalsa | Size pre-calcolate in piattaforma per grade |
| E6 | Trade fuori KZ / fuori setup | Noia, bisogno di agire | R2; terminale chiuso fuori finestra |
| E7 | Revenge trade (< 15' da uno stop senza nuovo setup completo) | Rabbia | Timer post-stop 15' lontano dallo schermo |
| E8 | TP rimosso / runner tenuto oltre le regole | Avidità | Ordini TP in server al momento dell'entry |
| E9 | Chiusura anticipata senza regola | Paura di restituire | Vietato P&L in valuta a schermo; solo R |
| E10 | Pre-market saltato | Fretta, overconfidence | R20: senza pre-market scritto la giornata è NT |

### Classe C — Errori cognitivi (bias nella lettura)

| Codice | Bias | Manifestazione tipica | Antidoto |
|---|---|---|---|
| C1 | Confirmation bias | Vedere solo i pool nella direzione "sperata" | Il pre-market OBBLIGA a scrivere entrambi gli scenari |
| C2 | Recency bias | Dopo 2 stop, "il setup non funziona più" | n≥100 prima di giudicare (R19); leggere la propria equity curve Monte Carlo |
| C3 | Outcome bias | Giudicare la decisione dall'esito | Review a doppia colonna: qualità decisione vs esito |
| C4 | Sunk cost | "Ormai sono dentro, aspetto" | Time-stop R13 (meccanico, non negoziabile) |
| C5 | Hindsight | "Lo sapevo" a fine giornata | La narrativa pre-market scritta è la prova di cosa si sapeva DAVVERO |
| C6 | Apofenia | Pattern ovunque (specie a fine giornata) | Lista chiusa dei setup (R5): se non ha nome, non esiste |
| C7 | Gambler's fallacy | "Dopo 3 stop il prossimo vince di sicuro" → size up | Size fissa per grade, sempre |

### Classe S — Errori di stato (il trader non era in condizione)

Stanchezza, alcol/sostanze, conflitto personale acuto, malattia, notte < 6h di sonno,
overtrading da noia dopo giorni NT consecutivi. Contromisura: lo **stato-check pre-market**
(score 1-10 su sonno/stress/tempo disponibile): < 6 → size −1 grade; < 4 → NT d'ufficio.

## 3. I protocolli

### 3.1 Protocollo post-stop (ogni stop, anche "giusto")

1. Stop preso → mani via dal mouse. Timer 15'.
2. Nei 15': riga journal + una domanda: "rifarei lo stesso trade? sì/no perché".
3. Rientro solo con nuovo setup completo (checklist da zero). 2° stop → fine sessione (R9).

### 3.2 Protocollo tilt (attivarlo è un punto di merito, non di vergogna)

Trigger: respiro corto, rabbia, click compulsivi, "devo recuperare". Azione: flat tutto,
piattaforma chiusa, camminata 20', nota nel journal (`tilt=1`), giornata finita. Il tilt
loggato onestamente vale più di un trade vinto: è il dato che salva il mese.

### 3.3 Protocollo winning streak (il rischio mascherato)

Dopo +5R settimanali o 4 vittorie di fila: il pericolo è l'overconfidence (size creep,
filtri "ammorbiditi"). Contromisura: la settimana dopo una settimana > +5R si opera con
gli stessi identici limiti (il sistema non ha "modalità hot hand") e la review settimanale
verifica il grade-assignment trade per trade.

### 3.4 Protocollo rientro da drawdown

A −8R (R17): size dimezzate + SOLO Setup A/B grade ≥ A (si taglia il grade B: meno trade,
più qualità) finché non si torna al picco. Se il DD raggiunge −10R mensile: stop, audit,
2 settimane in SIM con le stesse checklist (l'audit distingue: esecuzione? varianza? regime?).

## 4. Igiene della performance (il 50% silenzioso)

- **Sonno:** 7-8h; la KZ di NY per un europeo è pomeriggio — proteggere il post-pranzo.
  Chi opera London dall'Europa: NO sveglie alle 3 per "vedere il mercato" se poi opera NY.
- **Energia:** niente pasti pesanti prima della sessione; caffeina solo pre-market, non
  intra-sessione (amplifica il tilt); acqua sulla scrivania.
- **Ambiente:** postazione dedicata, telefono in un'altra stanza durante le KZ, social e
  chat di trading CHIUSE durante l'operatività (il "sentiment" altrui è rumore che
  sovrascrive la propria narrativa).
- **Corpo:** 30' di movimento al giorno; lo stress del trading è fisiologico (cortisolo),
  si smaltisce col corpo, non col pensiero.

## 5. Routine psicologiche (integrate con Vol.4)

- **Pre-sessione (5'):** rilettura narrativa; 10 respiri lenti; frase d'intento: "oggi
  eseguo il processo; l'esito è del campione".
- **Post-sessione (5'):** chiusura rituale a orario fisso; score emotivo 1-10 nel journal;
  UNA cosa fatta bene oggi (anche in giornata negativa — ricostituisce capitale psicologico).
- **Settimanale:** replay dei trade con la domanda C3 (decisione vs esito); conteggio
  `rule_break` per classe: è IL KPI psicologico (Vol.4 §2).
- **Mensile:** sessione "pre-mortem": *"se il prossimo mese finisse a −10R, cosa sarà
  successo?"* — scrive i rischi mentre la mente è lucida.

## 6. Il contratto psicologico (da firmare, letteralmente)

> Io, ________, accetto che: (1) le perdite entro le regole sono un costo del mestiere e non
> un mio fallimento; (2) i profitti fuori dalle regole sono un danno al sistema e non un mio
> merito; (3) il mio lavoro è eseguire e misurare, non avere ragione; (4) quando i limiti
> scattano, ho già finito di lavorare per oggi/questa settimana; (5) rileggerò questo
> contratto a ogni review mensile.
> Firma: ________ Data: ________
