# Presentation Guide — Satellite Ground Track Plotter: Task Scheduler

## 60-Second Pitch

A Satellite Ground Track Plotter task scheduler in pure Python using a heap of next-run times, demonstrated by running real jobs on short intervals and printing the log. A satellite's ground track is the path its orbit traces over the rotating Earth, shifting westward each revolution.

Satellite Ground Track Plotter in two sentences: A satellite's ground track is the path its orbit traces over the rotating Earth, shifting westward each revolution. Given orbital elements, the plotter predicts passes over ground stations and their timing.

## Architecture Talking Points

- Components: `Scheduler` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Heap-ordered next-run-time scheduling loop; runs in O(log j) per execution for j jobs.
- Honest scaling limit: Single-threaded with O(log j) dispatch; suited to lightweight periodic jobs, not to thousands of concurrent or long-running tasks.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Satellite Ground Track Plotter interval scheduler in Python (stdlib heapq) with drift-free rescheduling; demo registers jobs on sub-second intervals, runs them, and prints a timestamped execution log.
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
