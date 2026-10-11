#!/usr/bin/env python3
"""Release Notes Writer: Prompt_Playground.

A release-notes writer converts raw commit messages and pull-request titles into grouped, user-facing notes by change type: features, fixes, and breaking changes. Breaking changes are detected from keywords and flagged prominently. The output follows a changelog template with version headers.

Demo dataset idea: Generates seeded commit histories with known breaking changes and checks grouping and flag accuracy..
"""

import argparse
import random
import re
import zlib

SLUG = "prompt-playground"
PARAMS = {'breaking_keywords': 'signals of breaking changes', 'grouping': 'how changes are categorized', 'template': 'output format template'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def _param(key, default):
    """Read a project param defensively; coerce descriptive text to the default's type."""
    v = PARAMS.get(key, default) if isinstance(PARAMS, dict) else default
    if isinstance(default, bool):
        return v if isinstance(v, bool) else default
    if isinstance(default, (int, float)) and not isinstance(v, (int, float)):
        return _num(v, default)
    return v


def render_template(template: str, variables: dict) -> str:
    """Substitute {placeholders} with variables; unknown keys stay literal."""

    def _replace(match):
        key = match.group(1)
        return str(variables.get(key, match.group(0)))

    return re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", _replace, template)


def build_variants() -> dict:
    """The A/B prompt variants sharing the same variable slots."""
    return {
        "concise": ("Answer in one short sentence. "
                    "Topic: {topic}. Question: {question}"),
        "thorough": ("You are a helpful expert on {topic}. Think through "
                     "the key facts, then answer the question completely "
                     "in two to three sentences. Question: {question}"),
    }


def make_inputs(seed: int, n: int = 6) -> list:
    """Seeded test inputs: the topic plus a sampled question each."""
    rng = random.Random(seed)
    topic = "Release Notes Writer"
    questions = [
        "What is the core idea?",
        "How does it scale under load?",
        "What are the main costs involved?",
        "How is it monitored in production?",
        "What can go wrong at scale?",
        "How do teams get started?",
        "What metrics matter most?",
        "How does automation help?",
    ]
    return [{"topic": topic, "question": q}
            for q in rng.sample(questions, min(n, len(questions)))]


def stub_generate(prompt: str, variant: str, topic: str) -> str:
    """Deterministic stand-in model: the prompt hash picks canned content."""
    bank = [
        "The core idea is efficient resource planning at scale.",
        "Capacity planning balances cost against headroom for growth.",
        "Monitoring latency and throughput guides scaling decisions.",
        "Automation reduces manual toil in routine operations.",
    ]
    digest = zlib.crc32(prompt.encode("utf-8"))
    out = "%s overview. %s" % (topic, bank[digest % len(bank)])
    if variant == "thorough":
        out += " " + bank[(digest // len(bank)) % len(bank)]
    return out


def build_rubric() -> dict:
    """Scoring rubric: required words plus word-count bounds."""
    return {"required_words": ["scale", "cost", "latency"],
            "min_words": 5, "max_words": 60}


def score_response(response: str, variables: dict, rubric: dict) -> float:
    """Heuristic 0..1 score: topic term, required words, length bounds."""
    text = response.lower()
    first_word = variables.get("topic", "").lower().split()
    points, total = 0, 0
    total += 1
    if first_word and first_word[0] in text:
        points += 1
    for word in rubric.get("required_words", []):
        total += 1
        if word in text:
            points += 1
    total += 1
    words = len(response.split())
    if rubric.get("min_words", 0) <= words <= rubric.get("max_words", 10**9):
        points += 1
    return round(points / total, 3) if total else 0.0


def run_variant(name: str, template: str, inputs: list, rubric: dict) -> dict:
    """Run one variant over all inputs; returns per-input scores."""
    topic = "Release Notes Writer"
    scores = []
    prompts = []
    for variables in inputs:
        prompt = render_template(template, variables)
        response = stub_generate(prompt, name, topic)
        prompts.append((prompt, response))
        scores.append(score_response(response, variables, rubric))
    return {"scores": scores, "prompts": prompts}


def print_table(results: dict) -> None:
    """Print the variant-by-input score table and the winner."""
    names = list(results.keys())
    n = len(results[names[0]]["scores"])
    header = ("variant".ljust(10)
              + "".join(("in-%d" % i).rjust(8) for i in range(n))
              + "avg".rjust(8))
    print(header)
    print("-" * len(header))
    for name in names:
        scores = results[name]["scores"]
        avg = sum(scores) / len(scores)
        print(name.ljust(10)
              + "".join(("%8.2f" % s) for s in scores)
              + "%8.2f" % avg)
    winner = max(names, key=lambda nm: sum(results[nm]["scores"])
                 / len(results[nm]["scores"]))
    print("Winner: %s" % winner)


def run_demo(seed: int) -> int:
    """Seeded demo: render prompts, score both variants, print the table."""
    n = _param("inputs", 6)
    inputs = make_inputs(seed, n=n)
    variants = build_variants()
    rubric = build_rubric()
    print("Release Notes Writer: Prompt_Playground  (topic: Release Notes Writer, seed=%d)" % seed)
    print("Rubric: required_words=%s, words in [%d, %d]\n"
          % (rubric["required_words"], rubric["min_words"],
             rubric["max_words"]))
    results = {}
    for name, template in variants.items():
        results[name] = run_variant(name, template, inputs, rubric)
        prompt, response = results[name]["prompts"][0]
        print("[%s] prompt: %s" % (name, prompt[:90]))
        print("[%s] response: %s\n" % (name, response[:120]))
    print_table(results)
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Release Notes Writer: Prompt_Playground: A release-notes writer converts raw commit messages and pull-request titles into grouped, user-facing notes by change type: features, fixes, and breaking changes. Breaking changes are detected from keywords and flagged prominently. The output follows a changelog template with version headers."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--inputs", type=int, default=None,
                        help="Number of seeded test inputs (overrides params).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded prompt playground demo."""
    args = build_parser().parse_args(argv)
    if args.inputs is not None and isinstance(PARAMS, dict):
        PARAMS["inputs"] = args.inputs
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
