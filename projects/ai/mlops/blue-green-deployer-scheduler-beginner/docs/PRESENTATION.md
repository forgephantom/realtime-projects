# Presentation Guide — Blue-Green Deployment Runner: Task Scheduler

## 60-Second Pitch

A Blue-Green Deployment Runner task scheduler in pure Python using a heap of next-run times, demonstrated by running real jobs on short intervals and printing the log. Blue-green deployment runs two full environments and flips a router from blue to green: instant cutover with instant rollback by flipping back.

Blue-Green Deployment Runner in two sentences: Blue-green deployment runs two full environments and flips a router from blue to green: instant cutover with instant rollback by flipping back. The green environment is validated with smoke tests and shadow traffic before the switch. The runner models both environments on seeded traffic with a failure-injection drill.

## Architecture Talking Points

- Components: `Scheduler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Heap-ordered next-run-time scheduling loop; runs in O(log j) per execution for j jobs.
- Honest scaling limit: Single-threaded with O(log j) dispatch; suited to lightweight periodic jobs, not to thousands of concurrent or long-running tasks.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Blue-Green Deployment Runner interval scheduler in Python (stdlib heapq) with drift-free rescheduling; demo registers jobs on sub-second intervals, runs them, and prints a timestamped execution log.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Do jobs keep their cadence if one runs long?

**A:** Yes; jobs reschedule themselves by next_run + interval, so a slow job does not drift its cadence.

**Q:** Is the scheduler multi-threaded?

**A:** No; everything runs on one thread, so jobs must be quick and non-blocking for the demo cadence to hold.

**Q:** How is the demo configured?

**A:** --duration sets the demo length and --jobs sets how many demo jobs register.
