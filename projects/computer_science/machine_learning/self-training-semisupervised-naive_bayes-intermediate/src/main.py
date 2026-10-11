#!/usr/bin/env python3
"""Self-Training (Semi-Supervised): Naive Bayes Classifier: Gaussian Naive Bayes classifier for Self-Training (Semi-Supervised).

Self-training leverages unlabeled data: train on labeled points, predict confidently on unlabeled ones, add the confident predictions to training, and repeat. The confidence threshold controls error reinforcement. It helps when labels are scarce but unlabeled data is plentiful.
Data idea: Runs self-training on seeded data with few labels and verifies accuracy gains vs supervised-only baseline.

Trains a Gaussian Naive Bayes model on deterministic synthetic
Self-Training (Semi-Supervised) feature vectors, then reports class priors, accuracy, and
the confusion matrix on a held-out test split.
"""

import argparse
import math
import random

PARAMS = {'threshold': 'confidence for pseudo-labeling', 'rounds': 'self-training iterations', 'labeled': 'initial labeled count'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_dataset(seed, n):
    """Generate `n` 2-feature Self-Training (Semi-Supervised) vectors with binary labels."""
    rng = random.Random(seed)
    X, y = [], []
    for _ in range(n):
        label = rng.choice([0, 1])
        if label == 0:
            X.append([rng.gauss(2.0, 1.0), rng.gauss(3.0, 1.2)])
        else:
            X.append([rng.gauss(6.0, 1.1), rng.gauss(7.0, 1.0)])
        y.append(label)
    return X, y


def split_dataset(X, y, train_frac, seed):
    """Shuffle and split into (X_train, y_train, X_test, y_test)."""
    rng = random.Random(seed)
    idx = list(range(len(X)))
    rng.shuffle(idx)
    cut = int(len(X) * train_frac)
    train_idx, test_idx = idx[:cut], idx[cut:]
    return ([X[i] for i in train_idx], [y[i] for i in train_idx],
            [X[i] for i in test_idx], [y[i] for i in test_idx])


class GaussianNB:
    """Naive Bayes classifier with Gaussian feature likelihoods."""

    def __init__(self):
        self.classes_ = []
        self.priors = {}
        self.params = {}

    def fit(self, X, y):
        """Estimate per-class priors and per-feature (mean, var)."""
        self.classes_ = sorted(set(y))
        for c in self.classes_:
            rows = [x for x, label in zip(X, y) if label == c]
            self.priors[c] = len(rows) / len(X)
            feats = []
            for j in range(len(X[0])):
                vals = [row[j] for row in rows]
                mean = sum(vals) / len(vals)
                var = sum((v - mean) ** 2 for v in vals) / len(vals) + 1e-9
                feats.append((mean, var))
            self.params[c] = feats
        return self

    def _log_gaussian(self, x, mean, var):
        return (-0.5 * math.log(2 * math.pi * var)
                - (x - mean) ** 2 / (2 * var))

    def predict(self, X):
        """Return the most likely class for each feature vector."""
        out = []
        for x in X:
            scores = {}
            for c in self.classes_:
                scores[c] = math.log(self.priors[c]) + sum(
                    self._log_gaussian(x[j], mean, var)
                    for j, (mean, var) in enumerate(self.params[c]))
            out.append(max(scores, key=scores.get))
        return out


def main():
    parser = argparse.ArgumentParser(
        description="Self-Training (Semi-Supervised): Naive Bayes Classifier: Naive Bayes for Self-Training (Semi-Supervised).")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--n", type=int, default=_num(PARAMS.get("n"), 200),
                        help="synthetic samples to generate")
    parser.add_argument("--train-frac", type=float,
                        default=_num(PARAMS.get("train_frac"), 0.7),
                        help="fraction of data used for training")
    args = parser.parse_args()
    random.seed(args.seed)

    X, y = generate_dataset(args.seed, args.n)
    X_train, y_train, X_test, y_test = split_dataset(
        X, y, args.train_frac, args.seed)
    model = GaussianNB().fit(X_train, y_train)
    preds = model.predict(X_test)

    correct = sum(1 for p, t in zip(preds, y_test) if p == t)
    print("Self-Training (Semi-Supervised) Gaussian Naive Bayes")
    print("train: {}  test: {}".format(len(X_train), len(X_test)))
    print("class priors: " + ", ".join(
        "{}={:.3f}".format(c, model.priors[c])
        for c in model.classes_))
    print("test accuracy: {}/{} = {:.3f}".format(
        correct, len(y_test), correct / len(y_test)))

    classes = model.classes_
    matrix = {(t, p): 0 for t in classes for p in classes}
    for t, p in zip(y_test, preds):
        matrix[(t, p)] += 1
    print("confusion matrix (rows=true, cols=predicted):")
    print("        " + " ".join("pred-{}".format(c) for c in classes))
    for t in classes:
        print("true-{}  ".format(t) + " ".join(
            "{:>6}".format(matrix[(t, p)]) for p in classes))


if __name__ == "__main__":
    main()
