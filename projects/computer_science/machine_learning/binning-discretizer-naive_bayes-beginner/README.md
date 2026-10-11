# Binning Discretizer: Naive Bayes Classifier

**Domain:** computer_science | **Subdomain:** machine_learning | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Binning Discretizer built as a Naive Bayes classifier. Discretization turns continuous features into bins: equal-width is simple, equal-frequency balances counts, and supervised binning (decision-tree splits) maximizes target separation. Binned features feed linear models nonlinear structure and naive Bayes clean categories. Trains a Gaussian Naive Bayes classifier on seeded synthetic features and reports priors, accuracy, and the confusion matrix.

**Core concept — Binning Discretizer:** Discretization turns continuous features into bins: equal-width is simple, equal-frequency balances counts, and supervised binning (decision-tree splits) maximizes target separation. Binned features feed linear models nonlinear structure and naive Bayes clean categories.

**Why this matters in the real world:** Credit scoring (WOE binning) and naive Bayes pipelines discretize continuous features.

---

## Features

- **GaussianNB**: Naive Bayes classifier with Gaussian feature likelihoods.
- `generate_dataset` (`generate_dataset(seed, n)`): Generate 2-feature topic vectors with binary labels.
- `split_dataset` (`split_dataset(X, y, train_frac, seed)`): Shuffle and split into (X_train, y_train, X_test, y_test).
- `GaussianNB.fit` (`GaussianNB.fit(self, X, y)`): Estimate per-class priors and per-feature (mean, var).
- `GaussianNB.predict` (`GaussianNB.predict(self, X)`): Return the most likely class for each feature vector.
- `main` (`main()`): Parse args, train, and print accuracy and confusion matrix.

---

## Tech Stack

Python 3.8+, stdlib: argparse, math, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Gaussian Naive Bayes with log-space scoring. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n*d) to fit n samples with d features; O(c*d) per prediction. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/machine_learning/binning-discretizer-naive_bayes-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Train/test sizes, class priors, test accuracy, and a confusion matrix (rows=true, cols=predicted).

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
