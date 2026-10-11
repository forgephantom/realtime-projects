#!/usr/bin/env python3
"""Critic Debate Agents: Eval_Harness.

Critic debate pits two agents against each other: one proposes a solution and the other attacks it, with a judge picking the winner after several rounds. Adversarial critique surfaces flaws that a single agent rationalizes away. The simulation scores final answers against a ground-truth rubric.

Demo dataset idea: Generates seeded problems with hidden flaws in naive solutions and measures debate versus solo accuracy..
"""

import argparse
import random
import time
import zlib

SLUG = "eval-harness"
PARAMS = {'debate_rounds': 'attack and defend exchanges', 'judge_criteria': 'how the judge scores', 'roles': 'proposer and critic personas'}


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


def build_cases(seed: int, n: int = 8) -> list:
    """Seeded arithmetic test cases with expected answers."""
    rng = random.Random(seed)
    cases = []
    for i in range(n):
        a = rng.randint(2, 20)
        b = rng.randint(2, 20)
        op = rng.choice(["+", "*"])
        expected = a + b if op == "+" else a * b
        cases.append({"id": "case-%02d" % i,
                      "input": "What is %d %s %d?" % (a, op, b),
                      "expected": str(expected),
                      "kind": "arithmetic"})
    return cases


def stub_model(case: dict, seed: int) -> str:
    """Deterministic stub model: usually right, sometimes off by one."""
    digest = zlib.crc32((case["id"] + str(seed)).encode("utf-8"))
    value = int(case["expected"])
    if digest % 4 == 3:
        value += 1 if digest % 2 else -1
    return "The answer is %d." % value


def run_case(case: dict, model_fn, seed: int) -> dict:
    """Run one case: model output, latency, exact-match correctness."""
    start = time.perf_counter()
    try:
        output = model_fn(case, seed)
        error = ""
    except Exception as exc:  # one bad case never kills the run
        output, error = "", str(exc)
    latency_ms = (time.perf_counter() - start) * 1000.0
    correct = (not error) and output.strip().split()[-1].rstrip(".") \
        == case["expected"].strip()
    return {"id": case["id"], "input": case["input"],
            "expected": case["expected"], "output": output,
            "correct": correct, "latency_ms": latency_ms, "error": error}


def build_rubric() -> dict:
    """Judge rubric: checks that must appear, plus a max word count."""
    return {"max_words": 10}


def judge_score(output: str, rubric: dict) -> float:
    """LLM-as-judge sim: rubric checks over the output text, 0..1."""
    text = output.strip().lower()
    if not text:
        return 0.0
    checks = rubric.get("checks", ["the answer is"])
    hits = sum(1 for check in checks if check.lower() in text)
    score = hits / len(checks) if checks else 1.0
    if len(output.split()) > rubric.get("max_words", 10**9):
        score *= 0.5
    return round(score, 3)


def summarize(results: list, judged: list) -> dict:
    """Aggregate accuracy, avg/p95 latency, and average judge score."""
    n = len(results)
    accuracy = sum(1 for r in results if r["correct"]) / n if n else 0.0
    latencies = sorted(r["latency_ms"] for r in results)
    avg_lat = sum(latencies) / n if n else 0.0
    p95 = latencies[min(n - 1, int(0.95 * n))] if n else 0.0
    avg_judge = sum(judged) / len(judged) if judged else 0.0
    return {"n": n, "accuracy": round(accuracy, 3),
            "avg_latency_ms": round(avg_lat, 3),
            "p95_latency_ms": round(p95, 3),
            "avg_judge": round(avg_judge, 3)}


def run_demo(seed: int) -> int:
    """Seeded demo: run cases, judge them, print the table and summary."""
    n = _param("cases", 8)
    cases = build_cases(seed, n=n)
    rubric = build_rubric()
    print("Critic Debate Agents: Eval_Harness  (topic: Critic Debate Agents, seed=%d)" % seed)
    print("%-9s %-18s %-8s %-16s %-7s %-9s %s"
          % ("id", "input", "expect", "output", "ok", "lat(ms)",
             "judge"))
    print("-" * 78)
    results, judged = [], []
    for case in cases:
        result = run_case(case, stub_model, seed)
        rubric_case = dict(rubric)
        rubric_case["checks"] = ["the answer is", result["expected"]]
        score = judge_score(result["output"], rubric_case)
        results.append(result)
        judged.append(score)
        print("%-9s %-18s %-8s %-16s %-7s %-9.3f %.2f"
              % (result["id"], result["input"][:18], result["expected"],
                 result["output"][:16], "PASS" if result["correct"]
                 else "FAIL", result["latency_ms"], score))
    summary = summarize(results, judged)
    print("-" * 78)
    print("Summary: n=%d accuracy=%.2f avg_latency=%.3fms "
          "p95_latency=%.3fms avg_judge=%.2f"
          % (summary["n"], summary["accuracy"],
             summary["avg_latency_ms"], summary["p95_latency_ms"],
             summary["avg_judge"]))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Critic Debate Agents: Eval_Harness: Critic debate pits two agents against each other: one proposes a solution and the other attacks it, with a judge picking the winner after several rounds. Adversarial critique surfaces flaws that a single agent rationalizes away. The simulation scores final answers against a ground-truth rubric."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--cases", type=int, default=None,
                        help="Number of seeded test cases (overrides params).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded eval harness demo."""
    args = build_parser().parse_args(argv)
    if args.cases is not None and isinstance(PARAMS, dict):
        PARAMS["cases"] = args.cases
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
