# SLA Breach Predictor: Decision Tree Classifier

**Domain:** business_analyst | **Subdomain:** process_modeling | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

SLA Breach Predictor built as a Decision tree classifier. An SLA breach predictor watches live case age, queue depth, and step dwell times to forecast which cases will miss their deadlines. Early warnings let teams expedite or reassign before the breach. The model learns breach signatures from historical case data. Grows a Gini-based decision tree on seeded synthetic features, prints the tree as text, and reports test accuracy.

**Core concept — SLA Breach Predictor:** An SLA breach predictor watches live case age, queue depth, and step dwell times to forecast which cases will miss their deadlines. Early warnings let teams expedite or reassign before the breach. The model learns breach signatures from historical case data.

**Why this matters in the real world:** Operations centers predict SLA breaches to intervene while recovery is still possible.

---

## Features

- **DecisionTree**: Binary decision tree grown with greedy Gini-impurity splits.
- `gini` (`gini(labels)`): Gini impurity of a label list.
- `majority` (`majority(labels)`): Most common label.
- `accuracy` (`accuracy(y_true, y_pred)`): Fraction of correct predictions.
- `generate_dataset` (`generate_dataset(seed, n)`): Generate 2-feature topic rows with binary labels.
- `DecisionTree.fit` (`DecisionTree.fit(self, X, y)`): Grow the tree from training features X and labels y.
- `DecisionTree.predict` (`DecisionTree.predict(self, X)`): Predict labels for feature vectors X.
- `print_tree` (`print_tree(node, depth=0)`): Print the tree structure as indented text.
- `main` (`main()`): Parse args, train, print the tree, and report accuracy.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Greedy binary splits maximizing Gini impurity gain. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(d * n^2) worst case to find splits for d features, n rows. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/process_modeling/sla-breach-predictor-decision_tree-advanced
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

An indented text rendering of the learned tree followed by the test accuracy line.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
