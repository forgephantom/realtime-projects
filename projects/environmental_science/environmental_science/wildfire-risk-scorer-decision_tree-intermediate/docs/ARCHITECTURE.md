# Architecture (HLD) — Wildfire Risk Scorer: Decision Tree Classifier

## Problem & Users

Wildfire Risk Scorer built as a Decision tree classifier. Wildfire risk blends fuel dryness, wind, ignition history, and terrain into a score that prioritizes prevention work. The scorer rates landscape cells so crews thin fuels and stage equipment where risk runs highest. Grows a Gini-based decision tree on seeded synthetic features, prints the tree as text, and reports test accuracy.

The intended user is a student or engineer working in environmental_science (environmental_science) who needs a working, runnable reference for Wildfire Risk Scorer — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| DecisionTree | main | Binary decision tree grown with greedy Gini-impurity splits. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_dataset -> 70/30 split
train -> DecisionTree.fit (recursive Gini splits)
test -> DecisionTree.predict -> accuracy
print_tree renders the learned tree as text
```

## Storage

In-memory only: the dataset and the learned tree exist for the run and are not persisted.

## Scaling & Limits

Exhaustive split search is O(n^2)-ish per level, so the demo stays at a few hundred rows; larger data needs histogram or approximate splits.

## Trade-offs

Exhaustive Gini splits are exact and easy to follow but slow on larger data compared to approximate split finders.

## Failure Handling

Pure nodes, max depth, and unsplittable data all terminate as leaf nodes with the majority class, so training always finishes.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
