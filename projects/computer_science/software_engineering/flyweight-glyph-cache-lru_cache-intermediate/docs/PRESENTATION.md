# Presentation Guide — Flyweight (Glyph Cache): Lru Cache

## 60-Second Pitch

I built a Flyweight (Glyph Cache) that evicts the least-recently-used entry on overflow and tracks hit rates to show how well it performs. Flyweight shares intrinsic state across many objects: a text renderer caches one glyph per character instead of per occurrence, with extrinsic state (position, style) passed in.

Flyweight (Glyph Cache) in two sentences: Flyweight shares intrinsic state across many objects: a text renderer caches one glyph per character instead of per occurrence, with extrinsic state (position, style) passed in. Memory drops from O(chars) to O(alphabet). The demo measures the savings.

## Architecture Talking Points

- Components: `LRUCache` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: LRU eviction via OrderedDict (front = least-recently-used); runs in O(1) get and put (amortized).
- Honest scaling limit: Single-process structure; capacity is bounded by RAM and there is no sharding or cross-process sharing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Implemented a Flyweight (Glyph Cache) in Python on an OrderedDict with O(1) get/put and hit/miss/eviction instrumentation.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is recency tracked?

**A:** An OrderedDict keeps keys in access order; get() and put() call move_to_end() so the front is always the least-recently-used key.

**Q:** What happens on a put when the cache is full?

**A:** The new entry is added, then popitem(last=False) removes the front (LRU) entry and the eviction counter increments.

**Q:** Is it thread-safe?

**A:** No locking is included; it is designed for single-threaded use or external synchronization.
