# 00 — Piano di Backtesting e Validazione

> Il Core Model è discrezionale-sistematizzato: la validazione richiede un protocollo ibrido
> (replay manuale a regole strette + forward SIM + statistica automatizzata), non un semplice
> `strategy()` su TradingView — le ragioni sono in ADR-1. Questo documento è il protocollo
> completo; le metriche formali sono in `01_Metrics_Definitions.md`.

---

## 1. Perché NON un backtest automatico ingenuo (e cosa si fa invece)

**Problemi noti dei backtest Pine su setup intraday LTF:** fill simulati ottimistici su wick,
assenza di slippage/coda, livelli 0-4 dello stack (bias, narrativa) non codificabili senza
introdurre proxy arbitrari che il trader reale non usa, overfitting su un decennio di M1.

**Protocollo IFTS a 4 stadi:**

| Stadio | Cosa | Strumento | Output |
|---|---|---|---|
| S1 — Event study | Statistica degli *eventi* (sweep, MSS, FVG) senza gestione | Pine Statistics module + export | Base rates per RQ-1/2/7/9 |
| S2 — Replay manuale strutturato | 60+ giornate campionate, esecuzione con checklist reali su bar replay | TradingView Bar Replay + journal | Distribuzione R per setup/grade |
| S3 — Forward SIM | 6-8 settimane in demo/micro, regole integrali | Broker SIM + journal | Verifica S2 in condizioni reali |
| S4 — Live incrementale | Micro → mini secondo progressione | Reale | KPI di regime |

## 2. Dati

- **Fonte:** dati CME reali (TradingView per S1-S2; feed broker per S3-S4).
- **Serie:** contratto continuo back-adjusted per S1; contratto front per S2+ (con roll
  calendar annotato).
- **Periodi S2 (campionamento stratificato, NON consecutivo):** 20 giornate 2024, 20 del 2025,
  20 del 2026 YTD, stratificate per regime (rotation/trend/chop ≈ 50/30/20) e con quota
  obbligatoria di giornate news. Il campionamento casuale stratificato previene il cherry
  picking dei "bei periodi".
- **Esclusioni dichiarate:** half-days, settimana di Natale, roll days → il sistema non vi
  opera (R4), quindi non vi si testa.

## 3. Separazione In-Sample / Out-of-Sample

- **IS:** 2024 + 2025 H1 (definizione parametri… che sono GIÀ fissati dalle convenzioni P1-P17:
  l'IS serve a verificare, non a ottimizzare).
- **OOS:** 2025 H2 + 2026 YTD, toccato UNA volta a parametri congelati.
- **Regola d'oro:** qualunque modifica ai parametri dopo aver visto l'OOS invalida l'OOS →
  serve nuovo OOS (tempo reale = S3). Registro delle "OOS touches" nel CHANGELOG.

## 4. Walk-Forward (per la componente automatizzabile S1)

- Finestre: IS 12 mesi → OOS 3 mesi, rolling con step 3 mesi (≈ 8 finestre su 3 anni).
- Su ogni finestra: le base-rate degli eventi (es. sweep→MSS follow-through) si ricalcolano
  IS e si confrontano OOS. **WFE (walk-forward efficiency) = metrica OOS / metrica IS**;
  soglia di accettazione: WFE ≥ 0.6 mediana sulle finestre.
- Scopo: verificare che le regolarità NON siano artefatti di un singolo regime (2024 ≠ 2026).

## 5. Criteri di accettazione del modello (pre-registrati, da NON modificare a posteriori)

| Metrica (su S2+S3 cumulati, n ≥ 100) | Soglia minima | Target |
|---|---|---|
| Expectancy | ≥ +0.15R | +0.35/+0.6R |
| Profit Factor | ≥ 1.3 | ≥ 1.6 |
| Win rate | ≥ 35% | 42-55% |
| Max DD | ≤ P95 Monte Carlo | ≤ P75 |
| Compliance rate (S3) | ≥ 90% | ≥ 95% |
| WFE eventi (S1) | ≥ 0.6 | ≥ 0.75 |
| Trade/settimana | ≥ 2 | 3-6 |

Fallimento di una soglia → il modello NON va live; si apre l'audit (esecuzione? definizioni?
regime?) secondo Manual/04 §7.

## 6. Protocollo anti-bias del replay manuale (S2)

1. **Blind date:** le giornate campionate si aprono senza guardare prima il daily (lo
   assistant/replay parte dal pre-market).
2. **Checklist scritte in tempo reale** (le stesse del Manuale) — non si annota a posteriori.
3. **No rewind:** decisione presa = loggata; il tasto indietro invalida la giornata.
4. **Doppio conteggio dei mancati:** i setup validi non visti si contano alla review della
   giornata (campo `missed`) — misurano il gap tra modello e operatore.
5. **Slippage sintetico:** +1 tick di penalità su ogni fill market, +2 sui stop (ES; doppio
   NQ) — parametri conservativi documentati.
6. Journal identico al live (stesso schema CSV): S2, S3, S4 producono dataset omogenei e
   cumulabili.
7. **Mascheramento dell'epoca (Red Team M3):** dove possibile le giornate vengono servite
   senza data visibile (script/assistente che rinomina i file); inoltre il successo del
   replay si misura ANCHE sui no-trade (checklist rispettata nei giorni NT), non solo sui
   trade — un replayer che "sa" che il 2024 è bull non può comunque battere il protocollo
   inventando ingressi fuori regola.

## 7. Research Questions → studi

| RQ | Studio | Stadio | Priorità |
|---|---|---|---|
| RQ-1 MSS qualificato vs CHoCH | base rate follow-through | S1 | ALTA |
| RQ-2 sweep grade → esito | event study per grade | S1+S2 | ALTA |
| RQ-7 FVG fill/CE/react per KZ | contatori Pine → export | S1 | ALTA |
| RQ-9 finestre degli estremi di giornata | contatori Pine | S1 | MEDIA |
| RQ-3 nPOC magnet | studio dedicato con profilo | post-v1 | BASSA |
| RQ-4/5/8/10 (σ, OF, P/D, SMT) | tagli del journal | S2-S4 | continua |

## 8. Igiene statistica

- Nessuna conclusione con n < 30; decisioni di modello con n ≥ 100.
- Intervalli di confidenza sempre accanto alle medie (il tool li calcola: bootstrap 95%).
- Correzione per molteplicità quando si tagliano i dati in k sottogruppi (Bonferroni
  informale: soglia di sorpresa ∝ 1/k — non "scoprire" che il martedì piove).
- Le distribuzioni in R sono asimmetriche → mediane e percentili accanto alle medie.
- Ogni numero pubblicato nel progetto porta: n, periodo, stadio (S1-S4).
