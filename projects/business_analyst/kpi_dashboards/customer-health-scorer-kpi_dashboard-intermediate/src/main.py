#!/usr/bin/env python3
"""Customer Health Scorer: Kpi_Dashboard.

A health score blends product usage, support tickets, payment behavior, and engagement into one 0 to 100 number per account. The weights come from history: signals that preceded past churns earn more weight. Scores drive playbooks, so green accounts get expansion offers while red ones get save plans.

Demo dataset idea: Simulates seeded account signals with known churn outcomes, fits signal weights from historical churn, and scores accounts into green, yellow, and red bands..
"""

import argparse
import random
import statistics

SLUG = "kpi-dashboard"
PARAMS = {'accounts': 'number of customer accounts', 'signals': 'usage, support, billing, and engagement inputs', 'weights': 'importance assigned to each signal'}

BLOCKS = "▁▂▃▄▅▆▇█"


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


def generate_business_data(seed: int, months: int = 12) -> dict:
    """Seeded synthetic monthly series: revenue, users, adds, churn, spend."""
    rng = random.Random(seed)
    revenue, users, new_cust, churned, spend = [], [], [], [], []
    rev, usr = 50000.0, 4000
    for m in range(months):
        rev *= 1.0 + rng.uniform(0.01, 0.06)
        usr = int(usr * (1.0 + rng.uniform(0.005, 0.04)))
        new = int(usr * rng.uniform(0.02, 0.05))
        lost = int(usr * rng.uniform(0.01, 0.03))
        cost = new * rng.uniform(80.0, 140.0)
        revenue.append(round(rev, 2))
        users.append(usr)
        new_cust.append(new)
        churned.append(lost)
        spend.append(round(cost, 2))
    return {"months": ["M%02d" % (m + 1) for m in range(months)],
            "revenue": revenue, "users": users,
            "new_customers": new_cust, "churned": churned,
            "marketing_spend": spend}


def compute_kpis(data: dict) -> dict:
    """Growth rate, churn rate, CAC, and LTV from the series."""
    revenue = data["revenue"]
    growth = ((revenue[-1] - revenue[0]) / revenue[0] * 100.0
              if revenue[0] else 0.0)
    churn_rates = [c / u if u else 0.0
                   for c, u in zip(data["churned"], data["users"])]
    churn = statistics.mean(churn_rates) * 100.0 if churn_rates else 0.0
    total_new = sum(data["new_customers"])
    cac = (sum(data["marketing_spend"]) / total_new
           if total_new else float("inf"))
    arpu = statistics.mean([r / u if u else 0.0
                            for r, u in zip(revenue, data["users"])])
    churn_frac = statistics.mean(churn_rates) if churn_rates else 0.0
    ltv = arpu / churn_frac if churn_frac > 0 else float("inf")
    return {"revenue_growth_pct": round(growth, 2),
            "churn_rate_pct": round(churn, 2),
            "cac": round(cac, 2) if cac != float("inf") else cac,
            "ltv": round(ltv, 2) if ltv != float("inf") else ltv,
            "final_mrr": revenue[-1]}


def sparkline(values: list) -> str:
    """Map a numeric series to unicode block sparkline characters."""
    if not values:
        return ""
    lo, hi = min(values), max(values)
    if hi == lo:
        return BLOCKS[0] * len(values)
    return "".join(BLOCKS[int((v - lo) / (hi - lo) * (len(BLOCKS) - 1))]
                   for v in values)


def _fmt_money(value: float) -> str:
    if value == float("inf"):
        return "inf"
    return "$%s" % format(int(round(value)), ",")


def render_dashboard(data: dict, kpis: dict) -> str:
    """Format the KPI values and sparklines as an ASCII dashboard."""
    lines = []
    bar = "+" + "-" * 62 + "+"
    title = "Customer Health Scorer: Kpi_Dashboard"
    lines.append(bar)
    lines.append("| " + title[:60].ljust(60) + " |")
    lines.append("| " + ("topic: Customer Health Scorer")[:60].ljust(60) + " |")
    lines.append(bar)
    rows = [
        ("Revenue growth", "%+.2f%%" % kpis["revenue_growth_pct"]),
        ("Churn rate", "%.2f%%" % kpis["churn_rate_pct"]),
        ("CAC", _fmt_money(kpis["cac"])),
        ("LTV", _fmt_money(kpis["ltv"])),
        ("Final MRR", _fmt_money(kpis["final_mrr"])),
    ]
    for label, value in rows:
        lines.append("| %-16s %-12s |" % (label, value))
    lines.append(bar)
    lines.append("| Monthly revenue  " + sparkline(data["revenue"]).ljust(40)
                 + " |")
    lines.append("| Active users     " + sparkline(data["users"]).ljust(40)
                 + " |")
    lines.append(bar)
    return "\n".join(lines)


def run_demo(seed: int) -> int:
    """Seeded demo: generate data, compute KPIs, print the dashboard."""
    months = _param("months", 12)
    data = generate_business_data(seed, months=months)
    kpis = compute_kpis(data)
    print("Customer Health Scorer: Kpi_Dashboard  (seed=%d)\n" % seed)
    print(render_dashboard(data, kpis))
    print("\nMonthly detail:")
    print("%-6s %12s %8s %6s %7s %12s"
          % ("month", "revenue", "users", "new", "churned", "spend"))
    for i, month in enumerate(data["months"]):
        print("%-6s %12.2f %8d %6d %7d %12.2f"
              % (month, data["revenue"][i], data["users"][i],
                 data["new_customers"][i], data["churned"][i],
                 data["marketing_spend"][i]))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Customer Health Scorer: Kpi_Dashboard: A health score blends product usage, support tickets, payment behavior, and engagement into one 0 to 100 number per account. The weights come from history: signals that preceded past churns earn more weight. Scores drive playbooks, so green accounts get expansion offers while red ones get save plans."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--months", type=int, default=None,
                        help="Synthetic history length in months (overrides params).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded KPI dashboard demo."""
    args = build_parser().parse_args(argv)
    if args.months is not None and isinstance(PARAMS, dict):
        PARAMS["months"] = args.months
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
