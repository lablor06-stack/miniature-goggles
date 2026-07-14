#!/usr/bin/env python3
"""
IFTS — Monte Carlo simulator (bootstrap of trade R series)
Implements Testing/02_Monte_Carlo_Protocol.md. Stdlib only, reproducible via --seed.

Usage:
  python3 monte_carlo.py journal.csv
  python3 monte_carlo.py journal.csv --horizon 100 --sims 10000 --block 5
  python3 monte_carlo.py journal.csv --ruin-r 10        # P(equity touches -10R)
  python3 monte_carlo.py --r-list " -1,2.4,-1,0.5,3.1"  # ad-hoc series
"""
import argparse
import csv
import random
import statistics as st
import sys

TAIL_EVENT_R = -3.0     # synthetic catastrophic loss (gap through stop)
TAIL_EVENT_P = 0.01     # probability per trade when --inject-tail (default on)


def load_rs(path):
    rs = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("setup", "").strip() in ("A", "B", "C") and row.get("missed", "0").strip() != "1":
                try:
                    rs.append(float(row["result_r"]))
                except (KeyError, ValueError, TypeError):
                    pass
    return rs


def path_stats(seq):
    eq = peak = dd = 0.0
    cl = worst = 0
    for x in seq:
        eq += x
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
        if x < -0.05:
            cl += 1
            worst = max(worst, cl)
        else:
            cl = 0
    return eq, dd, worst


def touches_ruin(seq, level):
    eq = 0.0
    for x in seq:
        eq += x
        if eq <= -abs(level):
            return True
    return False


def sample_path(rng, pool, horizon, block):
    if block <= 1:
        return [rng.choice(pool) for _ in range(horizon)]
    out = []
    n = len(pool)
    while len(out) < horizon:
        start = rng.randrange(n)
        out.extend(pool[start:start + block])
        if len(pool[start:start + block]) < block:  # wrap for short tail blocks
            out.extend(pool[0:block - (n - start)])
    return out[:horizon]


def pctile(sorted_vals, p):
    i = min(len(sorted_vals) - 1, max(0, int(p / 100 * len(sorted_vals))))
    return sorted_vals[i]


def run(pool, sims, horizon, block, seed, inject_tail, ruin_r, label):
    rng = random.Random(seed)
    work = list(pool)
    tot, dds, stks = [], [], []
    neg = 0
    ruin = 0
    for _ in range(sims):
        seq = sample_path(rng, work, horizon, block)
        if inject_tail:
            seq = [TAIL_EVENT_R if rng.random() < TAIL_EVENT_P else x for x in seq]
        e, d, w = path_stats(seq)
        tot.append(e)
        dds.append(d)
        stks.append(w)
        if e < 0:
            neg += 1
        if ruin_r and touches_ruin(seq, ruin_r):
            ruin += 1
    tot.sort()
    dds.sort()
    stks.sort()
    print(f"\n── Monte Carlo [{label}] · sims={sims} · horizon={horizon} trades · block={block} · tail-inject={'on' if inject_tail else 'off'}")
    print(f"  {'':<14}{'P5':>8}{'P25':>8}{'P50':>8}{'P75':>8}{'P95':>8}")
    print(f"  {'Total R':<14}" + "".join(f"{pctile(tot, p):>8.1f}" for p in (5, 25, 50, 75, 95)))
    print(f"  {'Max DD (R)':<14}" + "".join(f"{pctile(dds, p):>8.1f}" for p in (5, 25, 50, 75, 95)))
    print(f"  {'Worst streak':<14}" + "".join(f"{pctile(stks, p):>8.0f}" for p in (5, 25, 50, 75, 95)))
    print(f"  P(total R < 0)      : {100*neg/sims:.1f}%")
    for x in (6, 8, 10, 15):
        p = sum(1 for d in dds if d > x) / sims
        print(f"  P(MaxDD > {x:>2}R)     : {100*p:.1f}%")
    if ruin_r:
        print(f"  P(touch −{abs(ruin_r):.0f}R)      : {100*ruin/sims:.1f}%   ← ruin barrier")


def main():
    ap = argparse.ArgumentParser(description="IFTS Monte Carlo (bootstrap)")
    ap.add_argument("journal", nargs="?", help="journal CSV path")
    ap.add_argument("--r-list", help="comma-separated R values instead of a CSV")
    ap.add_argument("--sims", type=int, default=10000)
    ap.add_argument("--horizon", type=int, default=100)
    ap.add_argument("--block", type=int, default=5, help="block size for block-bootstrap (1 = iid)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--ruin-r", type=float, help="ruin barrier in R (e.g. 10 → -10R)")
    ap.add_argument("--no-tail", action="store_true", help="disable synthetic -3R tail injection")
    args = ap.parse_args()

    if args.r_list:
        pool = [float(x) for x in args.r_list.replace(" ", "").split(",") if x]
    elif args.journal:
        pool = load_rs(args.journal)
    else:
        ap.error("provide a journal CSV or --r-list")

    if len(pool) < 10:
        sys.exit(f"ERROR: need ≥ 10 trades, got {len(pool)}")
    if len(pool) < 30:
        print(f"WARNING: n={len(pool)} < 30 — intervals will be wide and tails underestimated")

    print(f"IFTS Monte Carlo — input n={len(pool)} · empirical mean {st.mean(pool):+.3f}R · sd {st.stdev(pool):.2f}")
    run(pool, args.sims, args.horizon, 1, args.seed, not args.no_tail, args.ruin_r, "iid bootstrap")
    if args.block > 1:
        run(pool, args.sims, args.horizon, args.block, args.seed, not args.no_tail, args.ruin_r, f"block bootstrap (b={args.block})")
    print("\nNote: percentiles are conditional on the observed regime (Testing/02 §4). Compare runs over time; a deteriorating distribution IS the early edge-decay signal.")


if __name__ == "__main__":
    main()
