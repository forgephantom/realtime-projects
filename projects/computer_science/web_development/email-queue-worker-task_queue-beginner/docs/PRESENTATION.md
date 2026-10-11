# Presentation Guide — Email Queue Worker: Task Queue

## 60-Second Pitch

I built a Email Queue Worker that distributes work across a pool of threads and reports per-job results and timing. Sending email synchronously blocks requests, so a queue worker dequeues jobs, renders templates, and sends with per-domain throttling and bounce handling.

Email Queue Worker in two sentences: Sending email synchronously blocks requests, so a queue worker dequeues jobs, renders templates, and sends with per-domain throttling and bounce handling. Failed sends retry with backoff; hard bounces suppress future sends to protect sender reputation. Dead-letter review catches template bugs before they burn the list.

## Architecture Talking Points

- Components: `Job`, `TaskQueue` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Thread-pool work queue with a shared queue.Queue and sentinel shutdown; runs in O(1) enqueue/dequeue; wall time scales with jobs/workers.
- Honest scaling limit: Single process and GIL-bound; fine for dozens of workers on I/O or hashing-style work, not a substitute for a distributed queue.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Email Queue Worker in Python with worker threads and a shared queue, adding per-job timing and SHA-256 digest verification in the demo run.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How do workers know when to stop?

**A:** After the queue drains, run() pushes one None sentinel per worker; each worker exits when it pulls its sentinel.

**Q:** What happens if one job raises an exception?

**A:** The worker catches it, records an ERROR digest for that job, and keeps processing the rest of the queue.

**Q:** Is the demo deterministic?

**A:** Job payloads are seeded, but per-job elapsed times vary with machine load; the table layout and digests are stable.
