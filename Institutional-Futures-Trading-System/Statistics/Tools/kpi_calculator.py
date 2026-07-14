#!/usr/bin/env python3
"""
IFTS — KPI Calculator
Computes every metric defined in Testing/01_Metrics_Definitions.md from a journal CSV
(schema: Journal/journal_schema.csv). Stdlib only, deterministic.

Usage:
  python3 kpi_calculator.py journal.csv
  python3 kpi_calculator.py journal.csv --by killzone
  python3 kpi_calculator.py journal.csv --by grade --min-n 10
  python3 kpi_calculator.py --size-table 100000
"""
import argparse
import csv
import math
import random
import statistics as st
import sys

BE_EPS = 0.05          # |R| <= eps → breakeven (excluded from WR)
MIN_SAMPLE = 10        # below this: refuse result metrics
BOOT_N = 2000          # bootstrap resamples for expectancy CI
REQUIRED_COLS = {"date", "symbol", "setup", "killzone", "result_r", "rule_break", "missed", "tilt"}

EXECUTED_SETUPS = {"A", "B", "C"}


def parse_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("ERROR: empty file")
    missing = REQUIRED_COLS - set(rows[0].keys())
    if missing:
        sys.exit(f"ERROR: journal schema mismatch, missing columns: {sorted(missing)}")
    return rows


def executed(rows):
    out = []
    for r in rows:
        if r.get("setup", "").strip() in EXECUTED_SETUPS and r.get("missed", "0").strip() != "1":
            x = parse_float(r.get("result_r"))
            if x is not None:
                r = dict(r)
                r["_r"] = x
                out.append(r)
    return out


def max_drawdown(series):
    peak = 0.0
    eq = 0.0
    dd = 0.0
    dds = []
    peak_i = 0
    longest = 0
    for i, x in enumerate(series):
        eq += x
        if eq > peak:
            peak = eq
            peak_i = i
        cur = peak - eq
        dds.append(cur)
        dd = max(dd, cur)
        longest = max(longest, i - peak_i)
    ulcer = math.sqrt(sum(d * d for d in dds) / len(dds)) if dds else 0.0
    return dd, longest, ulcer


def streaks(series):
    worst = best = cw = cl = 0
    for x in series:
        if x > BE_EPS:
            cw += 1
            cl = 0
        elif x < -BE_EPS:
            cl += 1
            cw = 0
        else:
            cw = cl = 0
        worst = max(worst, cl)
        best = max(best, cw)
    return best, worst


def boot_ci(series, n=BOOT_N, seed=42):
    rng = random.Random(seed)
    k = len(series)
    means = sorted(sum(rng.choice(series) for _ in range(k)) / k for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n)]


def fmt(x, nd=2):
    return "—" if x is None else f"{x:+.{nd}f}" if isinstance(x, float) else str(x)


def result_metrics(trades, label="ALL"):
    rs = [t["_r"] for t in trades]
    n = len(rs)
    print(f"\n── Result metrics [{label}]  (n={n})")
    if n < MIN_SAMPLE:
        print(f"  insufficient sample (n<{MIN_SAMPLE}) · sum R = {sum(rs):+.2f}")
        return
    wins = [x for x in rs if x > BE_EPS]
    losses = [x for x in rs if x < -BE_EPS]
    bes = n - len(wins) - len(losses)
    wr = len(wins) / (len(wins) + len(losses)) if wins or losses else 0.0
    aw = st.mean(wins) if wins else None
    al = abs(st.mean(losses)) if losses else None
    exp = st.mean(rs)
    lo, hi = boot_ci(rs)
    pf = (sum(wins) / abs(sum(losses))) if losses else float("inf")
    sd = st.stdev(rs) if n > 1 else 0.0
    sqn = math.sqrt(n) * exp / sd if sd > 0 else None
    dd, dd_len, ulcer = max_drawdown(rs)
    bstk, wstk = streaks(rs)
    print(f"  Win rate          : {wr*100:5.1f}%   (BE excluded: {bes})")
    print(f"  Avg win / loss    : {fmt(aw)} / {fmt(-al if al is not None else None)}   payoff {aw/al:.2f}" if aw and al else f"  Avg win / loss    : {fmt(aw)} / {fmt(-al if al is not None else None)}")
    print(f"  Median win / loss : {fmt(st.median(wins) if wins else None)} / {fmt(st.median(losses) if losses else None)}")
    print(f"  Expectancy        : {exp:+.3f} R   (boot 95% CI {lo:+.2f} … {hi:+.2f})")
    print(f"  Profit factor     : {'inf' if pf == float('inf') else f'{pf:.2f}'}")
    print(f"  Std dev / SQN     : {sd:.2f} / {fmt(sqn)}")
    print(f"  Total R           : {sum(rs):+.2f}")
    print(f"  Max DD (R) / len  : {dd:.2f} / {dd_len} trades   ulcer {ulcer:.2f}   recovery {sum(rs)/dd if dd>0 else float('inf'):.2f}")
    print(f"  Streak best/worst : {bstk} / {wstk}")
    maes = [(t["_r"], parse_float(t.get("mae_r"))) for t in trades]
    maes = [(r, m) for r, m in maes if m is not None]
    if maes:
        w_ok = [1 for r, m in maes if r > BE_EPS and m < 0.5]
        w_all = [1 for r, m in maes if r > BE_EPS]
        if w_all:
            print(f"  MAE efficiency    : {100*len(w_ok)/len(w_all):.0f}% of winners with MAE < 0.5R (n={len(w_all)})")
    mfes = [(t["_r"], parse_float(t.get("mfe_r"))) for t in trades]
    mfes = [(r, m) for r, m in mfes if m is not None and m > 0 and r > BE_EPS]
    if mfes:
        capt = st.median([min(r / m, 1.0) for r, m in mfes])
        print(f"  MFE capture (med) : {capt*100:.0f}% of available MFE on winners (n={len(mfes)})")


def process_metrics(rows, trades):
    print("\n── Process metrics")
    if trades:
        ok = sum(1 for t in trades if t.get("rule_break", "none").strip() in ("", "none"))
        print(f"  Compliance rate   : {100*ok/len(trades):.1f}%  ({ok}/{len(trades)})")
    days = {r["date"] for r in rows if r.get("date")}
    tilt_days = {r["date"] for r in rows if r.get("tilt", "0").strip() == "1"}
    nt_days = {r["date"] for r in rows if r.get("setup", "").strip() == "NT"}
    print(f"  Operative days    : {len(days)}   NT days: {len(nt_days)}   tilt days: {len(tilt_days)}")
    missed = [parse_float(r.get("result_r")) for r in rows if r.get("missed", "0").strip() == "1"]
    missed = [x for x in missed if x is not None]
    if missed and trades:
        gap = st.mean(missed) - st.mean([t["_r"] for t in trades])
        print(f"  Missed-trade gap  : {gap:+.2f} R  (missed n={len(missed)}; positive ⇒ human filter subtracts value)")


def by_field(trades, field, min_n):
    groups = {}
    for t in trades:
        groups.setdefault(t.get(field, "?").strip() or "?", []).append(t["_r"])
    print(f"\n── Stratification by `{field}`  (groups under n={min_n} hidden)")
    print(f"  {'value':<12}{'n':>5}{'WR%':>7}{'exp R':>8}{'sum R':>8}{'maxDD':>7}")
    for k in sorted(groups):
        rs = groups[k]
        if len(rs) < min_n:
            continue
        wins = [x for x in rs if x > BE_EPS]
        losses = [x for x in rs if x < -BE_EPS]
        wr = 100 * len(wins) / (len(wins) + len(losses)) if wins or losses else 0
        dd, _, _ = max_drawdown(rs)
        print(f"  {k:<12}{len(rs):>5}{wr:>7.1f}{st.mean(rs):>8.2f}{sum(rs):>8.2f}{dd:>7.2f}")


def weekly(trades):
    weeks = {}
    for t in trades:
        d = t.get("date", "")
        if len(d) >= 10:
            try:
                import datetime as dt
                iso = dt.date.fromisoformat(d).isocalendar()
                weeks.setdefault(f"{iso[0]}-W{iso[1]:02d}", []).append(t["_r"])
            except ValueError:
                pass
    if len(weeks) < 2:
        return
    wr = [sum(v) for v in weeks.values()]
    print(f"\n── Weekly aggregation  (n={len(wr)} weeks)")
    print(f"  Mean weekly R     : {st.mean(wr):+.2f}   median {st.median(wr):+.2f}   worst {min(wr):+.2f}   best {max(wr):+.2f}")
    neg = sum(1 for x in wr if x < 0)
    print(f"  Negative weeks    : {neg}/{len(wr)} ({100*neg/len(wr):.0f}%)")
    if len(wr) >= 26:
        m, s = st.mean(wr), st.stdev(wr)
        if s > 0:
            downside = [x for x in wr if x < 0]
            ds = math.sqrt(sum(x * x for x in downside) / len(wr)) if downside else 0.0
            print(f"  Sharpe (ann.)     : {m/s*math.sqrt(52):.2f}   Sortino (ann.): {m/ds*math.sqrt(52):.2f}" if ds > 0 else f"  Sharpe (ann.)     : {m/s*math.sqrt(52):.2f}")
    else:
        print("  Sharpe/Sortino    : low_n (< 26 weeks) — not reported")


def size_table(equity):
    print(f"\n── Position size table (equity ${equity:,.0f}) — Manual/02 §2")
    specs = {"ES": 50.0, "MES": 5.0, "NQ": 20.0, "MNQ": 2.0}
    grades = {"B": 0.0025, "A": 0.0035, "A+": 0.005}
    stops = [4, 6, 8, 10, 14, 20, 30, 40]
    for g, pct in grades.items():
        risk = equity * pct
        print(f"  grade {g:<3} risk ${risk:,.0f}")
        hdr = "    stop(pt)" + "".join(f"{s:>7}" for s in stops)
        print(hdr)
        for sym, pv in specs.items():
            row = f"    {sym:<8}" + "".join(f"{int(risk // (s * pv)):>7}" for s in stops)
            print(row)


def main():
    ap = argparse.ArgumentParser(description="IFTS KPI calculator")
    ap.add_argument("journal", nargs="?", help="journal CSV path")
    ap.add_argument("--by", action="append", default=[], help="stratify by column (repeatable)")
    ap.add_argument("--min-n", type=int, default=15, help="min group size for stratifications")
    ap.add_argument("--size-table", type=float, metavar="EQUITY", help="print contract size table and exit")
    args = ap.parse_args()

    if args.size_table:
        size_table(args.size_table)
        return
    if not args.journal:
        ap.error("journal CSV required (or use --size-table)")

    rows = load(args.journal)
    trades = executed(rows)
    print(f"IFTS KPI report — {args.journal}")
    print(f"rows: {len(rows)} · executed trades: {len(trades)}")
    result_metrics(trades)
    for s in ("A", "B", "C"):
        sub = [t for t in trades if t["setup"].strip() == s]
        if sub:
            result_metrics(sub, label=f"Setup {s}")
    process_metrics(rows, trades)
    weekly(trades)
    for f in args.by:
        by_field(trades, f, args.min_n)


if __name__ == "__main__":
    main()
