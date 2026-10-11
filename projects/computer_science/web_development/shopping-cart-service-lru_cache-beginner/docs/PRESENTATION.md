# Presentation Guide — Shopping Cart Service: Lru Cache

## 60-Second Pitch

I built a Shopping Cart Service that evicts the least-recently-used entry on overflow and tracks hit rates to show how well it performs. Carts bridge browsing and checkout: the service holds items with quantities, validates price and availability at each mutation, merges anonymous and logged-in carts on sign-in, and expires abandoned carts.

Shopping Cart Service in two sentences: Carts bridge browsing and checkout: the service holds items with quantities, validates price and availability at each mutation, merges anonymous and logged-in carts on sign-in, and expires abandoned carts. Price snapshots at add-time versus live pricing is a real business decision. Inventory holds start at checkout, not before.

## Architecture Talking Points

- Components: `LRUCache` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: LRU eviction via OrderedDict (front = least-recently-used); runs in O(1) get and put (amortized).
- Honest scaling limit: Single-process structure; capacity is bounded by RAM and there is no sharding or cross-process sharing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Implemented a Shopping Cart Service in Python on an OrderedDict with O(1) get/put and hit/miss/eviction instrumentation.
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
