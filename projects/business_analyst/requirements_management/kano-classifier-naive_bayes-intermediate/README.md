# Kano Feature Classifier: Naive Bayes Classifier

**Domain:** business_analyst | **Subdomain:** requirements_management | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Kano Feature Classifier built as a Naive Bayes classifier. The Kano model classifies features as basic expectations, performance satisfiers, or delighters that surprise. Basics cause anger when missing but no joy when present; delighters do the opposite. Classifying the backlog this way guides where to invest for differentiation versus table stakes. Trains a Gaussian Naive Bayes classifier on seeded synthetic features and reports priors, accuracy, and the confusion matrix.

**Core concept — Kano Feature Classifier:** The Kano model classifies features as basic expectations, performance satisfiers, or delighters that surprise. Basics cause anger when missing but no joy when present; delighters do the opposite. Classifying the backlog this way guides where to invest for differentiation versus table stakes.

**Why this matters in the real world:** Product teams use Kano results to balance must-have quality against differentiating features.

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
cd projects/business_analyst/requirements_management/kano-classifier-naive_bayes-intermediate
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
