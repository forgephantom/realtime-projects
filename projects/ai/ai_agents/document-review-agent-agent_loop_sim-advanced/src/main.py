#!/usr/bin/env python3
"""Document Review Agent: Agent_Loop_Sim.

A document review agent checks contracts and policies against a checklist of required clauses and risky language. Each finding cites the exact passage and suggests replacement wording. Review coverage reporting shows which checklist items were addressed.

Demo dataset idea: Generates seeded documents with planted missing clauses and risky terms, then measures finding recall..
"""

import argparse
import ast
import random
import re

SLUG = "agent-loop-sim"
PARAMS = {'checklist': 'required clauses and risks', 'risk_keywords': 'terms triggering flags', 'severity_scale': 'finding severity levels'}


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


def make_calculator():
    """Safe arithmetic evaluator built on the ast module."""

    allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv,
               ast.Mod, ast.Pow, ast.UAdd, ast.USub, ast.Load)

    def calculate(expression: str):
        node = ast.parse(expression, mode="eval")
        for sub in ast.walk(node):
            if not isinstance(sub, allowed):
                raise ValueError("unsupported expression: %r" % expression)
            if isinstance(sub, ast.Constant) and not isinstance(
                    sub.value, (int, float)):
                raise ValueError("non-numeric constant in: %r" % expression)
        return eval(compile(node, "<calc>", "eval"), {"__builtins__": {}}, {})

    return calculate


class LookupTable:
    """Seeded key-value table exposed as a lookup tool."""

    def __init__(self, table: dict):
        self.table = table

    def __call__(self, key: str):
        key = key.strip().lower()
        if key in self.table:
            return self.table[key]
        return "unknown key: %s" % key


def make_lookup(seed: int) -> LookupTable:
    """Build the seeded lookup table for the demo."""
    rng = random.Random(seed)
    table = {
        "latency_ms": rng.randint(20, 80),
        "error_budget_pct": round(rng.uniform(0.05, 0.3), 2),
        "oncall_team_size": rng.randint(4, 10),
        "region": rng.choice(["us-central1", "us-east1", "eu-west1"]),
    }
    return LookupTable(table)


class Agent:
    """ReAct agent: think picks a tool, act calls it, observe formats."""

    def __init__(self, tools: dict, max_steps: int = 6):
        self.tools = tools
        self.max_steps = max_steps

    def think(self, question: str, history: list) -> tuple:
        """Decide the next step: (thought, tool_name, arg) or final answer."""
        if history and history[-1]["kind"] == "observation":
            result = history[-1]["text"]
            return ("I have the tool result, so I can give the final "
                    "answer.", "final", result)
        expr_match = re.search(r"[\d][\d\s+\-*/().%()]*", question)
        if expr_match:
            expr = expr_match.group(0).rstrip(" +-*/.%")
            if re.search(r"[+\-*/%]", expr):
                return ("The question contains arithmetic; I will use the "
                        "calculator.", "calculator", expr)
        lowered = question.lower()
        for key in self.tools["lookup"].table:
            if key in lowered:
                return ("The question asks about a stored value; I will "
                        "use the lookup table.", "lookup", key)
        return ("No tool fits this question.", "final",
                "I do not know.")

    def act(self, tool_name: str, arg: str):
        """Call the named tool with the argument; returns the raw result."""
        return self.tools[tool_name](arg)

    def observe(self, result) -> str:
        """Format a tool result as an observation string."""
        return "Observation: %s" % result

    def run(self, question: str) -> str:
        """Thought -> Action -> Observation loop; returns the final answer."""
        history = []
        print("Question: %s" % question)
        for step in range(1, self.max_steps + 1):
            thought, action, arg = self.think(question, history)
            print("Thought %d: %s" % (step, thought))
            if action == "final":
                print("Final answer: %s\n" % arg)
                return str(arg)
            result = self.act(action, arg)
            print("Action %d: %s(%r)" % (step, action, arg))
            print("%s" % self.observe(result))
            history.append({"kind": "observation", "text": str(result)})
        print("Final answer: (step limit reached)\n")
        return ""


def _demo_questions() -> list:
    """Seeded question set: arithmetic, lookup, and an unknown."""
    topic = "Document Review Agent"
    return [
        "What is 12 * (7 + 5)?",
        "What is the latency_ms for %s?" % topic,
        "What is 250 // 7?",
        "Who won the championship in 1998?",
    ]


def run_demo(seed: int) -> int:
    """Seeded demo: run the agent on three questions and print traces."""
    rng = random.Random(seed)
    tools = {"calculator": make_calculator(),
             "lookup": make_lookup(seed)}
    agent = Agent(tools, max_steps=_param("max_steps", 6))
    questions = rng.sample(_demo_questions(), 3)
    print("Document Review Agent: Agent_Loop_Sim  (topic: Document Review Agent, seed=%d)" % seed)
    print("Tools: calculator, lookup(%s)\n"
          % ", ".join(tools["lookup"].table))
    for question in questions:
        agent.run(question)
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Document Review Agent: Agent_Loop_Sim: A document review agent checks contracts and policies against a checklist of required clauses and risky language. Each finding cites the exact passage and suggests replacement wording. Review coverage reporting shows which checklist items were addressed."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--steps", type=int, default=None,
                        help="Max ReAct loop steps (overrides params).")
    parser.add_argument("--question", type=str, default=None,
                        help="Run a single custom question instead of the demo set.")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded agent loop demo."""
    args = build_parser().parse_args(argv)
    max_steps = args.steps if args.steps is not None else _param("max_steps", 6)
    tools = {"calculator": make_calculator(),
             "lookup": make_lookup(args.seed)}
    agent = Agent(tools, max_steps=max_steps)
    if args.question:
        print("Document Review Agent: Agent_Loop_Sim  (topic: Document Review Agent, seed=%d)"
              % args.seed)
        agent.run(args.question)
        return 0
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
