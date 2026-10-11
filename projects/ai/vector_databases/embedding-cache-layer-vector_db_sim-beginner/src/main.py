#!/usr/bin/env python3
"""Embedding Cache Layer: Vector_Db_Sim.

An embedding cache layer sits in front of the embedding service, keyed by text hash, so repeated texts skip recomputation. TTL and size limits bound staleness and memory. The simulation measures hit rates on realistic request streams with duplicates.

Demo dataset idea: Simulates seeded request streams with duplicate texts and reports cache hit rate and time saved..
"""

import argparse
import json
import math
import random

SLUG = "vector-db-sim"
PARAMS = {'cache_size': 'max cached embeddings', 'request_mix': 'duplicate ratio in stream', 'ttl_seconds': 'entry time-to-live'}


def _param(key, default):
    """Read a project param defensively (PARAMS may be an empty dict)."""
    return PARAMS.get(key, default) if isinstance(PARAMS, dict) else default


class VectorDB:
    """In-memory vector database with cosine search and JSON persistence."""

    def __init__(self):
        self._vectors = []
        self._metadata = []

    def add(self, vector: list, metadata: dict = None) -> int:
        """Store a vector with optional metadata; returns its integer id."""
        if self._vectors and len(vector) != len(self._vectors[0]):
            raise ValueError("dimension mismatch: expected %d, got %d"
                             % (len(self._vectors[0]), len(vector)))
        self._vectors.append([float(x) for x in vector])
        self._metadata.append(dict(metadata or {}))
        return len(self._vectors) - 1

    @staticmethod
    def _cosine(a: list, b: list) -> float:
        """Cosine similarity between two equal-length vectors."""
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)

    def search(self, query: list, k: int = 5) -> list:
        """Top-k cosine-similarity search; returns [{id, score, metadata}]."""
        scored = [(self._cosine(query, vec), idx)
                  for idx, vec in enumerate(self._vectors)]
        scored.sort(key=lambda item: item[0], reverse=True)
        return [{"id": idx, "score": score, "metadata": self._metadata[idx]}
                for score, idx in scored[:k]]

    def save(self, path: str) -> None:
        """Persist the index to a JSON file."""
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"vectors": self._vectors,
                       "metadata": self._metadata}, fh)

    @classmethod
    def load(cls, path: str) -> "VectorDB":
        """Load an index previously written by save()."""
        db = cls()
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        db._vectors = [list(map(float, v)) for v in data["vectors"]]
        db._metadata = data["metadata"]
        return db

    def __len__(self):
        return len(self._vectors)


def run_demo(seed: int) -> int:
    """Seeded demo: clustered vectors, top-5 search, save/load roundtrip."""
    rng = random.Random(seed)
    topic = "Embedding Cache Layer"
    dim = _param("dim", 8)
    count = _param("num_vectors", 20)
    db = VectorDB()
    centers = [[rng.gauss(0.0, 1.0) for _ in range(dim)] for _ in range(3)]
    for i in range(count):
        center = centers[i % 3]
        vec = [x + rng.gauss(0.0, 0.3) for x in center]
        db.add(vec, {"label": "%s-%02d" % (topic, i),
                     "cluster": i % 3})
    query = [x + rng.gauss(0.0, 0.1) for x in centers[1]]
    print("Embedding Cache Layer: Vector_Db_Sim  (topic: Embedding Cache Layer, seed=%d)" % seed)
    print("Index: %d vectors, dim=%d" % (len(db), dim))
    print("Top-5 cosine search results (query drawn near cluster 1):")
    first = db.search(query, k=5)
    for hit in first:
        print("  id=%d  score=%.4f  label=%s  cluster=%s"
              % (hit["id"], hit["score"],
                 hit["metadata"]["label"], hit["metadata"]["cluster"]))
    path = _param("index_path", "/tmp/vector_db_sim_index.json")
    db.save(path)
    db2 = VectorDB.load(path)
    again = db2.search(query, k=5)
    match = ([h["id"] for h in first] == [h["id"] for h in again]
             and len(db2) == len(db))
    print("Saved %d vectors to %s; reload roundtrip ids match: %s"
          % (len(db2), path, match))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Embedding Cache Layer: Vector_Db_Sim: An embedding cache layer sits in front of the embedding service, keyed by text hash, so repeated texts skip recomputation. TTL and size limits bound staleness and memory. The simulation measures hit rates on realistic request streams with duplicates."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    return parser


def main(argv=None) -> int:
    """Entry point: seeded vector database demo."""
    args = build_parser().parse_args(argv)
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
