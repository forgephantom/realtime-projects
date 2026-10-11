# Design (LLD) — ABG Interpreter (Educational): Decision Tree Classifier

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| DecisionTree | Binary decision tree grown with greedy Gini-impurity splits. |

## Functions

| Function | Signature | Description |
|---|---|---|
| gini | gini(labels) | Gini impurity of a label list. |
| majority | majority(labels) | Most common label. |
| accuracy | accuracy(y_true, y_pred) | Fraction of correct predictions. |
| generate_dataset | generate_dataset(seed, n) | Generate 2-feature topic rows with binary labels. |
| DecisionTree.fit | DecisionTree.fit(self, X, y) | Grow the tree from training features X and labels y. |
| DecisionTree.predict | DecisionTree.predict(self, X) | Predict labels for feature vectors X. |
| print_tree | print_tree(node, depth=0) | Print the tree structure as indented text. |
| main | main() | Parse args, train, print the tree, and report accuracy. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for ABG Interpreter (Educational):

| Parameter | Meaning |
|---|---|
| cases | synthetic case count |
| patterns | disorder patterns |
| steps | interpretation steps |

## Algorithm & Complexity

The core of this project is Greedy binary splits maximizing Gini impurity gain.

- **Time complexity:** O(d * n^2) worst case to find splits for d features, n rows
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/healthcare/clinical_tools/abg-interpreter-edu-decision_tree-intermediate
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
