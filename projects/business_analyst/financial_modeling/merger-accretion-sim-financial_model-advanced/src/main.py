#!/usr/bin/env python3
"""Merger Accretion Dilution Simulator: Financial_Model.

A merger is accretive when the combined earnings per share rise after the deal and dilutive when they fall. The model combines the two income statements, adds synergies, subtracts financing costs and new shares, and compares pro-forma EPS to standalone EPS. Accretion math decides whether a deal creates or destroys shareholder value on paper.

Demo dataset idea: Builds seeded acquirer and target financials, applies purchase price, financing mix, and synergy assumptions, then computes accretion or dilution with sensitivity to the price paid..
"""

import argparse
import random

SLUG = "financial-model"
PARAMS = {'financing_mix': 'cash, debt, and stock split', 'purchase_price': 'total consideration paid', 'synergies': 'annual cost and revenue synergies'}


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


def npv(rate: float, cashflows: list) -> float:
    """Net present value of cashflows at the discount rate."""
    return sum(cf / ((1.0 + rate) ** t) for t, cf in enumerate(cashflows))


def irr(cashflows: list, lo: float = -0.9999, hi: float = 10.0, tol: float = 1e-6) -> float:
    """Internal rate of return via bisection on NPV(r) = 0."""
    f_lo = npv(lo, cashflows)
    f_hi = npv(hi, cashflows)
    if f_lo * f_hi > 0:
        raise ValueError("no sign change in [%.4f, %.4f]; IRR undefined"
                         % (lo, hi))
    for _ in range(200):
        mid = (lo + hi) / 2.0
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid <= 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2.0


def dcf_value(free_cash_flows: list, discount_rate: float, terminal_growth: float) -> float:
    """DCF enterprise value with Gordon-growth terminal value."""
    if discount_rate <= terminal_growth:
        raise ValueError("discount rate must exceed terminal growth")
    pv = sum(fcf / ((1.0 + discount_rate) ** (t + 1))
             for t, fcf in enumerate(free_cash_flows))
    terminal = (free_cash_flows[-1] * (1.0 + terminal_growth)
                / (discount_rate - terminal_growth))
    pv_terminal = terminal / ((1.0 + discount_rate) ** len(free_cash_flows))
    return pv + pv_terminal


def breakeven(fixed_costs: float, price: float, variable_cost: float) -> float:
    """Units needed for contribution margin to cover fixed costs."""
    margin = price - variable_cost
    if margin <= 0:
        raise ValueError("price must exceed variable cost")
    return fixed_costs / margin


def amortization_schedule(principal: float, annual_rate: float, years: int) -> list:
    """Monthly payment split into interest, principal, and balance."""
    months = years * 12
    r = annual_rate / 12.0
    if r == 0:
        payment = principal / months
    else:
        payment = principal * r / (1.0 - (1.0 + r) ** (-months))
    rows, balance = [], principal
    for m in range(1, months + 1):
        interest = balance * r
        princ = payment - interest
        balance = max(0.0, balance - princ)
        rows.append({"month": m, "payment": payment, "interest": interest,
                     "principal": princ, "balance": balance})
    return rows


def build_inputs(seed: int) -> dict:
    """Seeded synthetic inputs: project cashflows, loan, unit economics."""
    rng = random.Random(seed)
    horizon = _param("horizon_years", 5)
    investment = _param("investment", 250000.0)
    cashflows = [-investment] + [round(rng.uniform(40000.0, 95000.0), 2)
                                 for _ in range(horizon)]
    return {"cashflows": cashflows,
            "discount_rate": _param("discount_rate", 0.10),
            "terminal_growth": _param("terminal_growth", 0.02),
            "fixed_costs": 120000.0,
            "price": round(rng.uniform(90.0, 140.0), 2),
            "variable_cost": round(rng.uniform(30.0, 60.0), 2),
            "loan_principal": 200000.0,
            "loan_rate": 0.065,
            "loan_years": 5}


def _money(value: float) -> str:
    return "$%s" % format(int(round(value)), ",")


def run_demo(seed: int) -> int:
    """Seeded demo: print NPV/IRR/DCF/break-even/amortization tables."""
    data = build_inputs(seed)
    cfs = data["cashflows"]
    rate = data["discount_rate"]
    print("Merger Accretion Dilution Simulator: Financial_Model  (topic: Merger Accretion Dilution Simulator, seed=%d)" % seed)
    print("\nProject cashflows (discount rate %.1f%%):" % (rate * 100))
    print("%-6s %12s %10s %14s" % ("year", "cashflow", "df", "pv"))
    for t, cf in enumerate(cfs):
        df = 1.0 / ((1.0 + rate) ** t)
        print("%-6d %12s %10.4f %14s"
              % (t, _money(cf), df, _money(cf * df)))
    print("NPV: %s" % _money(npv(rate, cfs)))
    print("IRR: %.2f%%" % (irr(cfs) * 100.0))
    print("DCF value (g=%.1f%%): %s"
          % (data["terminal_growth"] * 100.0,
             _money(dcf_value(cfs[1:], rate, data["terminal_growth"]))))
    be = breakeven(data["fixed_costs"], data["price"],
                   data["variable_cost"])
    print("\nBreak-even: %s units (fixed %s, price %s, var cost %s)"
          % (format(int(round(be)), ","), _money(data["fixed_costs"]),
             _money(data["price"]), _money(data["variable_cost"])))
    sched = amortization_schedule(data["loan_principal"], data["loan_rate"],
                                  data["loan_years"])
    print("\nAmortization: %s at %.2f%% for %d years, payment %s/mo"
          % (_money(data["loan_principal"]), data["loan_rate"] * 100.0,
             data["loan_years"], _money(sched[0]["payment"])))
    print("%-6s %10s %10s %10s %12s"
          % ("month", "payment", "interest", "principal", "balance"))
    for row in sched[:6] + sched[-1:]:
        print("%-6d %10s %10s %10s %12s"
              % (row["month"], _money(row["payment"]),
                 _money(row["interest"]), _money(row["principal"]),
                 _money(row["balance"])))
    print("  ... (%d months total)" % len(sched))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Merger Accretion Dilution Simulator: Financial_Model: A merger is accretive when the combined earnings per share rise after the deal and dilutive when they fall. The model combines the two income statements, adds synergies, subtracts financing costs and new shares, and compares pro-forma EPS to standalone EPS. Accretion math decides whether a deal creates or destroys shareholder value on paper."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded financial model demo."""
    args = build_parser().parse_args(argv)
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
