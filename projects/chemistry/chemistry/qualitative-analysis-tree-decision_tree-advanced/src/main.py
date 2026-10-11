#!/usr/bin/env python3
"""Qualitative Analysis Tree: Decision Tree Classifier: a Gini-based decision tree for Qualitative Analysis Tree.

Classic qualitative analysis separates cations into groups by selective precipitation: chlorides first, then sulfides in acid, then sulfides in base. A decision tree walks through the separation scheme from observed precipitates to ion identity.
Data idea: A seeded RNG simulates separation schemes for random ion mixtures, recording observations and the true ions present.

Trains a small binary decision tree (greedy Gini-impurity splits) on
deterministic synthetic Qualitative Analysis Tree features, prints the tree as text,
and reports test accuracy.
"""

import argparse
import random

PARAMS = {'observed_precipitates': 'list of precipitation observations', 'group_reagents': 'reagents used per group', 'training_cases': 'labeled analysis runs'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def gini(labels):
    """Gini impurity of a label list."""
    n = len(labels)
    if n == 0:
        return 0.0
    return 1.0 - sum((labels.count(c) / n) ** 2 for c in set(labels))


def majority(labels):
    """Most common label."""
    return max(set(labels), key=labels.count)


def accuracy(y_true, y_pred):
    """Fraction of correct predictions."""
    return sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)


def generate_dataset(seed, n):
    """Generate `n` 2-feature Qualitative Analysis Tree rows with binary labels."""
    rng = random.Random(seed)
    X, y = [], []
    for _ in range(n):
        x0 = rng.uniform(0.0, 10.0)
        x1 = rng.uniform(0.0, 10.0)
        noisy = x0 + x1 + rng.gauss(0.0, 1.5)
        X.append([x0, x1])
        y.append(1 if noisy > 10.0 else 0)
    return X, y


class DecisionTree:
    """Binary decision tree grown with greedy Gini-impurity splits."""

    def __init__(self, max_depth=4):
        self.max_depth = max_depth
        self.root = None

    def fit(self, X, y):
        """Grow the tree from training features X and labels y."""
        self.root = self._grow(list(zip(X, y)), 0)
        return self

    def _best_split(self, rows):
        parent = gini([label for _, label in rows])
        n = len(rows)
        best = None
        for j in range(len(rows[0][0])):
            for threshold in sorted({x[j] for x, _ in rows}):
                left = [r for r in rows if r[0][j] <= threshold]
                right = [r for r in rows if r[0][j] > threshold]
                if not left or not right:
                    continue
                gain = (parent
                        - (len(left) / n) * gini([l for _, l in left])
                        - (len(right) / n) * gini([l for _, l in right]))
                if best is None or gain > best[0]:
                    best = (gain, j, threshold, left, right)
        return best[1:] if best else None

    def _grow(self, rows, depth):
        labels = [label for _, label in rows]
        if depth >= self.max_depth or len(set(labels)) == 1 or len(rows) < 2:
            return {"leaf": True, "class": majority(labels), "n": len(rows)}
        split = self._best_split(rows)
        if split is None:
            return {"leaf": True, "class": majority(labels), "n": len(rows)}
        j, threshold, left, right = split
        return {"leaf": False, "feature": j, "threshold": threshold,
                "left": self._grow(left, depth + 1),
                "right": self._grow(right, depth + 1)}

    def predict(self, X):
        """Predict labels for feature vectors X."""
        out = []
        for x in X:
            node = self.root
            while not node["leaf"]:
                node = (node["left"] if x[node["feature"]] <= node["threshold"]
                        else node["right"])
            out.append(node["class"])
        return out


def print_tree(node, depth=0):
    """Print the tree structure as indented text."""
    pad = "  " * depth
    if node["leaf"]:
        print("{}leaf: class={} (n={})".format(pad, node["class"], node["n"]))
    else:
        print("{}x[{}] <= {:.3f}".format(pad, node["feature"],
                                         node["threshold"]))
        print_tree(node["left"], depth + 1)
        print_tree(node["right"], depth + 1)


def main():
    parser = argparse.ArgumentParser(
        description="Qualitative Analysis Tree: Decision Tree Classifier: decision tree for Qualitative Analysis Tree.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--n", type=int, default=_num(PARAMS.get("n"), 200),
                        help="synthetic samples to generate")
    parser.add_argument("--max-depth", type=int,
                        default=_num(PARAMS.get("max_depth"), 4),
                        help="maximum tree depth")
    args = parser.parse_args()
    random.seed(args.seed)

    X, y = generate_dataset(args.seed, args.n)
    cut = int(len(X) * 0.7)
    tree = DecisionTree(max_depth=args.max_depth).fit(X[:cut], y[:cut])
    preds = tree.predict(X[cut:])
    print("Qualitative Analysis Tree decision tree (max_depth={})".format(
        args.max_depth))
    print_tree(tree.root)
    print("test accuracy: {}/{} = {:.3f}".format(
        sum(1 for t, p in zip(y[cut:], preds) if t == p),
        len(preds), accuracy(y[cut:], preds)))


if __name__ == "__main__":
    main()
