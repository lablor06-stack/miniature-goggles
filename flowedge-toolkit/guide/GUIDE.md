# FlowEdge ICT Toolkit — User Guide

Thank you for getting **FlowEdge**. This toolkit gives you a clean, automated
read of Smart Money price action plus a journal to track your edge.

It contains:
1. **FlowEdge ICT Indicator** (Pine Script for TradingView)
2. **FlowEdge Trading Journal** (Excel / Google Sheets)
3. This guide

---

## 1. Installing the indicator

1. Open [TradingView](https://www.tradingview.com) and load any chart.
2. Bottom panel → **Pine Editor**.
3. Delete the default code, then paste the contents of `FlowEdge_ICT.pine`.
4. Click **Save** (name it "FlowEdge"), then **Add to chart**.
5. To pin it permanently: click the indicator name → **Add to favorites**.

## 2. What it draws

| Feature | What you see | What it means |
|---|---|---|
| **Fair Value Gaps** | Shaded teal/red boxes | Imbalances price often returns to. Teal = bullish, red = bearish. Boxes auto-delete when filled. |
| **Market Structure** | Dashed lines + BOS / CHoCH labels | **BOS** = trend continuation. **CHoCH** = potential reversal (first break against trend). |
| **Liquidity Sweeps** | ✖ markers above/below candles | Price grabbed liquidity beyond a swing then rejected — common reversal trigger. |
| **Kill Zones** | Shaded background | High-probability session windows (London / New York open). |

## 3. Settings worth tuning

- **Swing strength (pivots):** higher = fewer, stronger structure points. Start at 5; use 3 on lower timeframes.
- **Extend FVG (bars):** how far gap boxes project to the right.
- **Remove FVG when filled:** keep ON for a clean chart.
- **Kill Zones:** times are in the **exchange timezone** — adjust the session strings to your market.

## 4. A simple framework to trade it

> This is an example workflow, not financial advice.

1. Wait for price to enter a **Kill Zone**.
2. Look for a **liquidity sweep** (✖) of a recent high/low.
3. Confirm with a **CHoCH** in your direction.
4. Enter on a return to the nearest **FVG**; stop beyond the swept level.
5. Log the trade in the journal.

## 5. Using the journal

1. Open `FlowEdge_Trading_Journal.xlsx` (Excel) — or upload to **Google Sheets**
   (File → Import → keep formulas).
2. Fill one row per trade in the **Trades** tab (dropdowns help you stay consistent).
3. The **Dashboard** tab updates automatically: win rate, total R, expectancy,
   and performance by setup — so you learn *which* FlowEdge signals make you money.

## 6. Alerts

In TradingView, click the **⏰ Alert** button → Condition: *FlowEdge* →
choose "Any alert() function call". You'll get pings for new FVGs, BOS/CHoCH,
and liquidity sweeps.

---

*Risk disclaimer: FlowEdge is an analysis tool, not financial advice. Trading
involves risk of loss. Always use proper risk management.*
