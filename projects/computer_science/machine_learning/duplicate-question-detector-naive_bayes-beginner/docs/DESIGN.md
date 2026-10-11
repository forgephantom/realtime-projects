# Design (LLD) — Duplicate Question Detector: Naive Bayes Classifier

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| GaussianNB | Naive Bayes classifier with Gaussian feature likelihoods. |

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_dataset | generate_dataset(seed, n) | Generate 2-feature topic vectors with binary labels. |
| split_dataset | split_dataset(X, y, train_frac, seed) | Shuffle and split into (X_train, y_train, X_test, y_test). |
| GaussianNB.fit | GaussianNB.fit(self, X, y) | Estimate per-class priors and per-feature (mean, var). |
| GaussianNB.predict | GaussianNB.predict(self, X) | Return the most likely class for each feature vector. |
| main | main() | Parse args, train, and print accuracy and confusion matrix. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Duplicate Question Detector:

| Parameter | Meaning |
|---|---|
| threshold | similarity cutoff |
| features | similarity feature set |
| blocking | candidate-pair blocking strategy |

## Algorithm & Complexity

The core of this project is Gaussian Naive Bayes with log-space scoring.

- **Time complexity:** O(n*d) to fit n samples with d features; O(c*d) per prediction
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/machine_learning/duplicate-question-detector-naive_bayes-beginner
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
