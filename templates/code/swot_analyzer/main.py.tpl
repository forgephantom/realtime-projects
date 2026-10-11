#!/usr/bin/env python3
"""@@PROJECT_TITLE@@.

@@TOPIC_CONCEPT@@

Demo dataset idea: @@DATA_IDEA@@.
"""

import argparse
import random

SLUG = "swot-analyzer"
PARAMS = @@TOPIC_PARAMS@@


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


def build_factors(seed: int) -> dict:
    """Seeded factor lists per quadrant with weight and impact score."""
    rng = random.Random(seed)
    topic = "@@TOPIC_NAME@@"
    pools = {
        "strengths": [
            "Strong %s engineering culture" % topic,
            "Automated deployment pipeline",
            "Deep observability coverage",
            "Experienced on-call rotation",
            "Reusable platform components",
            "Fast incident response record",
        ],
        "weaknesses": [
            "Manual capacity reviews",
            "Sparse runbook documentation",
            "Single-region deployment",
            "Flaky integration test suite",
            "Tribal knowledge in one team",
            "Stale dependency versions",
        ],
        "opportunities": [
            "Growing demand for %s" % topic,
            "New multi-region customers",
            "Automation tooling maturity",
            "Cloud cost optimization programs",
            "Open-source ecosystem growth",
            "Partnership channel expansion",
        ],
        "threats": [
            "Aggressive competitor pricing",
            "Talent market competition",
            "Regulatory compliance burden",
            "Supply chain cost pressure",
            "Shifting customer priorities",
            "Security incident fallout",
        ],
    }
    count = _param("factors", 4)
    factors = {}
    for quadrant, pool in pools.items():
        chosen = rng.sample(pool, min(count, len(pool)))
        factors[quadrant] = [
            {"factor": name,
             "weight": round(rng.uniform(0.5, 1.0), 2),
             "score": rng.randint(1, 5)}
            for name in chosen
        ]
    return factors


def score_quadrant(factors: list) -> float:
    """Weighted total (sum of weight x score) for one quadrant."""
    return round(sum(f["weight"] * f["score"] for f in factors), 2)


def categorize(factors: dict) -> dict:
    """Score all quadrants and name the dominant one."""
    scores = {q: score_quadrant(fs) for q, fs in factors.items()}
    dominant = max(scores, key=scores.get) if scores else None
    internal = scores.get("strengths", 0) - scores.get("weaknesses", 0)
    external = scores.get("opportunities", 0) - scores.get("threats", 0)
    return {"scores": scores, "dominant": dominant,
            "internal_net": round(internal, 2),
            "external_net": round(external, 2)}


def _top(factors: list) -> str:
    """Highest weight x score factor name, or a fallback note."""
    if not factors:
        return "no factors listed"
    best = max(factors, key=lambda f: f["weight"] * f["score"])
    return best["factor"]


def tows_actions(factors: dict) -> list:
    """Pair top factors into SO/WO/ST/WT action items."""
    s = _top(factors.get("strengths", []))
    w = _top(factors.get("weaknesses", []))
    o = _top(factors.get("opportunities", []))
    t = _top(factors.get("threats", []))
    return [
        ("SO", "Use '%s' to capture '%s'." % (s, o)),
        ("WO", "Fix '%s' to unlock '%s'." % (w, o)),
        ("ST", "Use '%s' to blunt '%s'." % (s, t)),
        ("WT", "Address '%s' to survive '%s'." % (w, t)),
    ]


def render_matrix(factors: dict, scores: dict) -> str:
    """Format quadrants and scores as an ASCII 2x2 matrix."""
    bar = "+" + "-" * 35 + "+" + "-" * 35 + "+"
    lines = [bar]
    pairs = [("strengths", "opportunities"),
             ("weaknesses", "threats")]
    labels = {"strengths": "STRENGTHS", "weaknesses": "WEAKNESSES",
              "opportunities": "OPPORTUNITIES", "threats": "THREATS"}
    for left, right in pairs:
        lines.append("| %-33s | %-33s |"
                     % ("%s (%.1f)" % (labels[left], scores[left]),
                        "%s (%.1f)" % (labels[right], scores[right])))
        lines.append(bar)
        for i in range(max(len(factors[left]), len(factors[right]))):
            l = factors[left][i] if i < len(factors[left]) else None
            r = factors[right][i] if i < len(factors[right]) else None
            lt = ("- %s [w%s s%d]" % (l["factor"][:24], l["weight"],
                                      l["score"])) if l else ""
            rt = ("- %s [w%s s%d]" % (r["factor"][:24], r["weight"],
                                      r["score"])) if r else ""
            lines.append("| %-33s | %-33s |" % (lt, rt))
        lines.append(bar)
    return "\n".join(lines)


def run_demo(seed: int) -> int:
    """Seeded demo: score quadrants, print matrix and TOWS actions."""
    factors = build_factors(seed)
    result = categorize(factors)
    print("@@PROJECT_TITLE@@  (topic: @@TOPIC_NAME@@, seed=%d)\n" % seed)
    print(render_matrix(factors, result["scores"]))
    print("\nDominant quadrant: %s" % result["dominant"].upper())
    print("Internal net (S-W): %+.2f   External net (O-T): %+.2f"
          % (result["internal_net"], result["external_net"]))
    print("\nTOWS action items:")
    for code, action in tows_actions(factors):
        print("  [%s] %s" % (code, action))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="@@PROJECT_TITLE@@: @@TOPIC_CONCEPT@@"
    )
    parser.add_argument("--seed", type=int, default=@@SEED@@,
                        help="Random seed for the demo (default: @@SEED@@).")
    parser.add_argument("--factors", type=int, default=None,
                        help="Seeded factors per quadrant (overrides params).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded SWOT analyzer demo."""
    args = build_parser().parse_args(argv)
    if args.factors is not None and isinstance(PARAMS, dict):
        PARAMS["factors"] = args.factors
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
