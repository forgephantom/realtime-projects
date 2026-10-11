# Gaussian Naive Bayes Classifier Toy: Naive Bayes Classifier

**Domain:** mathematics | **Subdomain:** mathematics | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Gaussian Naive Bayes Classifier Toy built as a Naive Bayes classifier. Naive Bayes classifies by multiplying per-feature likelihoods under the independence assumption, working surprisingly well on text and tabular data. Gaussian naive Bayes fits a normal distribution per feature per class. The toy trains on synthetic labeled points and reports accuracy and confusion counts. Trains a Gaussian Naive Bayes classifier on seeded synthetic features and reports priors, accuracy, and the confusion matrix.

**Core concept — Gaussian Naive Bayes Classifier Toy:** Naive Bayes classifies by multiplying per-feature likelihoods under the independence assumption, working surprisingly well on text and tabular data. Gaussian naive Bayes fits a normal distribution per feature per class. The toy trains on synthetic labeled points and reports accuracy and confusion counts.

**Why this matters in the real world:** Naive Bayes filters spam, classifies documents, and triages support tickets.

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
cd projects/mathematics/mathematics/naive-bayes-classifier-toy-naive_bayes-beginner
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
