# FlowEdge ICT Toolkit 🎯

A small, original digital product you can sell to cover your TradingView /
indicator subscription. Everything here is built from scratch using **public**
Smart Money / ICT concepts — it's yours to publish and sell.

## What's inside

```
flowedge-toolkit/
├── indicators/
│   └── FlowEdge_ICT.pine          # TradingView indicator (Pine Script v6)
├── journal/
│   ├── build_journal.py           # script that builds the journal
│   └── FlowEdge_Trading_Journal.xlsx
├── guide/
│   └── GUIDE.md                   # buyer-facing setup guide
├── marketing/
│   └── launch.md                  # Gumroad copy + launch posts
└── README.md                      # this file
```

## How to launch it (your part — ~30 min, no coding)

1. **Create a free [Gumroad](https://gumroad.com) account.**
2. **New product** → "Digital product". Title & description: copy from
   `marketing/launch.md`. Suggested price: €9–12.
3. **Bundle the files** to sell: zip together
   - `indicators/FlowEdge_ICT.pine`
   - `journal/FlowEdge_Trading_Journal.xlsx`
   - `guide/GUIDE.md` (or its PDF)
   Upload the zip to the Gumroad product.
4. **Add 2–3 images:** screenshot the indicator on a chart + the journal
   Dashboard tab. (These sell the product — don't skip them.)
5. **Publish**, copy the product link.
6. **Post** the launch messages from `marketing/launch.md` (X, Reddit, ICT
   Discords). Reply to every comment — that's where sales come from.

### Math
At €12, **~5 sales = €50/month covered.** First sale is the hard one; after
reviews + screenshots it compounds.

## Regenerating the journal
```bash
cd journal
pip install openpyxl
python3 build_journal.py
```

## Important
- This is **original work** — not a copy of any paid/closed-source indicator.
- It is **not financial advice**; include the disclaimer when you sell it.
- Customise freely: rename it, recolor, add features. It's yours.
