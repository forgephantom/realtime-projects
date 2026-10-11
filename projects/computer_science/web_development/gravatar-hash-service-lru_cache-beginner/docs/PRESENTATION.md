# Presentation Guide — Gravatar Hash Service: Lru Cache

## 60-Second Pitch

I built a Gravatar Hash Service that evicts the least-recently-used entry on overflow and tracks hit rates to show how well it performs. Gravatar maps emails to avatars via MD5: the service normalizes (trim, lowercase), hashes, and builds avatar URLs with size and default-image parameters.

Gravatar Hash Service in two sentences: Gravatar maps emails to avatars via MD5: the service normalizes (trim, lowercase), hashes, and builds avatar URLs with size and default-image parameters. It handles the 404-vs-default fallback choice and caches lookups. The privacy trade-off is that email hashes are enumerable, which is why many sites moved to initials.

## Architecture Talking Points

- Components: `LRUCache` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: LRU eviction via OrderedDict (front = least-recently-used); runs in O(1) get and put (amortized).
- Honest scaling limit: Single-process structure; capacity is bounded by RAM and there is no sharding or cross-process sharing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Implemented a Gravatar Hash Service in Python on an OrderedDict with O(1) get/put and hit/miss/eviction instrumentation.
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
