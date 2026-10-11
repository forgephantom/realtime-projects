#!/usr/bin/env python3
"""In-App Inbox Service: Lru Cache.

An in-app inbox gives users a durable message list: the service stores notifications per user, tracks read/unread, supports archiving and categories, and syncs read state across devices. Pagination and unread badges complete it. Unlike email, delivery is guaranteed once the app is opened.

Demo dataset idea: Drives seeded notification lifecycles across devices, verifying read-state sync, retention expiry, and badge counts..
"""

import argparse
import random
from collections import OrderedDict

SLUG = "in-app-inbox-service-lru_cache-beginner"
PARAMS = {'retention_days': 'message lifetime', 'categories': 'inbox categories (orders, alerts, promos)', 'badge_rule': 'what counts toward the unread badge'}


class LRUCache:
    """A fixed-capacity cache with least-recently-used eviction.

    Backed by an OrderedDict: the front holds the least-recently-used key and
    the back holds the most-recently-used key. Both get() and put() refresh a
    key's recency. Hit, miss, and eviction counters are kept for the demo.
    """

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self.capacity = capacity
        self._store = OrderedDict()
        self.hits = 0
        self.misses = 0
        self.evictions = 0

    def get(self, key: str):
        """Return the value for key, or None on a miss; a hit refreshes recency."""
        if key not in self._store:
            self.misses += 1
            return None
        self.hits += 1
        self._store.move_to_end(key)
        return self._store[key]

    def put(self, key: str, value: str) -> None:
        """Insert or update key; evict the least-recently-used entry if full."""
        if key in self._store:
            self._store.move_to_end(key)
        self._store[key] = value
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)
            self.evictions += 1

    def keys_mru_first(self) -> list:
        """Keys ordered most-recently-used first."""
        return list(reversed(self._store.keys()))

    def stats(self) -> dict:
        """Hit/miss/eviction counters, current size, and the hit rate."""
        total = self.hits + self.misses
        return {
            "hits": self.hits,
            "misses": self.misses,
            "evictions": self.evictions,
            "size": len(self._store),
            "hit_rate": self.hits / total if total else 0.0,
        }


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="In-App Inbox Service: Lru Cache: An in-app inbox gives users a durable message list: the service stores notifications per user, tracks read/unread, supports archiving and categories, and syncs read state across devices. Pagination and unread badges complete it. Unlike email, delivery is guaranteed once the app is opened."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--capacity", type=int, default=None,
                        help="Cache capacity (see the topic params).")
    parser.add_argument("--lookups", type=int, default=None,
                        help="Number of demo operations (see the topic params).")
    parser.add_argument("--key-space", type=int, default=None,
                        help="Distinct keys the demo draws from (see the topic params).")
    return parser


def run_demo(seed: int, capacity: int, lookups: int, key_space: int) -> int:
    """Run a seeded mix of puts and gets against the cache and print a trace."""
    rng = random.Random(seed)
    cache = LRUCache(capacity)
    # Pre-fill part of the cache so early lookups can actually hit.
    for i in range(max(1, capacity // 2)):
        cache.put("%s-key-%d" % (SLUG, i), "value-%d" % i)

    print("In-App Inbox Service: Lru Cache  (topic: In-App Inbox Service, seed=%d)" % seed)
    print("capacity=%d, %d operations over %d keys" % (capacity, lookups, key_space))
    print("%4s %-4s %-22s %-6s %s" % ("step", "op", "key", "result", "evictions"))
    for step in range(1, lookups + 1):
        key = "%s-key-%d" % (SLUG, rng.randint(0, key_space - 1))
        if rng.random() < 0.25:
            before = cache.evictions
            cache.put(key, "value-%d" % step)
            result = "stored (evicted)" if cache.evictions > before else "stored"
            op = "put"
        else:
            found = cache.get(key)
            result = "hit" if found is not None else "miss"
            op = "get"
        print("%4d %-4s %-22s %-6s %d" % (step, op, key, result, cache.evictions))

    summary = cache.stats()
    print("\nFinal cache, most-recently-used first:")
    for key in cache.keys_mru_first():
        print("  %s -> %s" % (key, cache._store[key]))
    print("\nHits: %d, misses: %d, evictions: %d, hit rate: %.1f%%" % (
        summary["hits"], summary["misses"], summary["evictions"],
        100.0 * summary["hit_rate"]))
    return 0


def main(argv=None) -> int:
    """Entry point: parse flags and run the cache demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    capacity = args.capacity or int(PARAMS.get("capacity", 4))
    lookups = args.lookups or int(PARAMS.get("lookups", 16))
    key_space = args.key_space or int(PARAMS.get("key_space", 6))
    return run_demo(args.seed, capacity, lookups, key_space)


if __name__ == "__main__":
    raise SystemExit(main())
