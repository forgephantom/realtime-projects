#!/usr/bin/env python3
"""Plan-and-Execute Agent: Task Queue.

Plan-and-execute agents first write an explicit step-by-step plan, then work through it, revising the plan when steps fail or reveal new information. Separating planning from execution makes the strategy inspectable and lets a human approve the plan up front. Replanning triggers on failed steps or surprising observations.

Demo dataset idea: Generates seeded tasks with hidden obstacles and measures plan success and replanning frequency..
"""

import argparse
import hashlib
import queue
import random
import threading
import time

SLUG = "plan-execute-agent-task_queue-beginner"
PARAMS = {'max_replans': 'allowed replanning attempts', 'plan_steps': 'initial plan length', 'require_approval': 'human approval before execution'}


class Job:
    """A unit of work: a numeric id, a kind label, and a payload string."""

    def __init__(self, job_id: int, kind: str, payload: str):
        self.job_id = job_id
        self.kind = kind
        self.payload = payload


class TaskQueue:
    """A small thread-pool task queue.

    Workers pull Job objects off an internal queue, run them, and record
    (job_id, kind, worker name, elapsed ms, result digest) tuples.
    A None sentinel cleanly shuts each worker down.
    """

    def __init__(self, num_workers: int):
        self.num_workers = num_workers
        self._jobs = queue.Queue()
        self._results = []
        self._lock = threading.Lock()
        self._threads = []

    def submit(self, job: Job) -> None:
        """Enqueue a Job for the worker threads."""
        self._jobs.put(job)

    def _run_job(self, job: Job) -> str:
        # Real CPU work: repeatedly hash the payload; rounds depend on kind.
        rounds = {"compress": 400, "hash": 900, "resize": 250}.get(job.kind, 300)
        data = job.payload.encode()
        for _ in range(rounds):
            data = hashlib.sha256(data).digest()
        return hashlib.sha256(data).hexdigest()[:16]

    def _worker(self, name: str) -> None:
        while True:
            job = self._jobs.get()
            if job is None:  # shutdown sentinel
                self._jobs.task_done()
                return
            started = time.perf_counter()
            try:
                digest = self._run_job(job)
            except Exception as exc:  # never let one bad job kill a worker
                digest = "ERROR: " + str(exc)
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            with self._lock:
                self._results.append((job.job_id, job.kind, name, elapsed_ms, digest))
            self._jobs.task_done()

    def run(self) -> None:
        """Start the workers, wait until the queue drains, then stop them."""
        for i in range(self.num_workers):
            thread = threading.Thread(
                target=self._worker, args=("worker-%d" % (i + 1),), daemon=True
            )
            thread.start()
            self._threads.append(thread)
        self._jobs.join()
        for _ in self._threads:
            self._jobs.put(None)
        for thread in self._threads:
            thread.join()

    def results(self) -> list:
        """Completed results as (job_id, kind, worker, elapsed_ms, digest), by job id."""
        return sorted(self._results, key=lambda row: row[0])

    def stats(self) -> dict:
        """Aggregate stats: job count plus total and mean elapsed milliseconds."""
        rows = self._results
        total = sum(row[3] for row in rows)
        return {
            "jobs": len(rows),
            "total_ms": total,
            "mean_ms": total / len(rows) if rows else 0.0,
        }


def make_jobs(n: int, kinds: list, rng: random.Random) -> list:
    """Build n demo Job objects with seeded random payloads."""
    jobs = []
    for i in range(n):
        kind = kinds[i % len(kinds)]
        payload = SLUG + "-payload-%d-" % (i + 1)
        payload += "".join(rng.choice("abcdef0123456789") for _ in range(16))
        jobs.append(Job(i + 1, kind, payload))
    return jobs


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Plan-and-Execute Agent: Task Queue: Plan-and-execute agents first write an explicit step-by-step plan, then work through it, revising the plan when steps fail or reveal new information. Separating planning from execution makes the strategy inspectable and lets a human approve the plan up front. Replanning triggers on failed steps or surprising observations."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--workers", type=int, default=None,
                        help="Worker threads (see the topic params).")
    parser.add_argument("--jobs", type=int, default=None,
                        help="Number of jobs to submit (see the topic params).")
    parser.add_argument("--kinds", type=str, default=None,
                        help="Comma-separated job kinds (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: submit demo jobs, run the queue, print the results."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    rng = random.Random(args.seed)

    workers = args.workers or int(PARAMS.get("workers", 3))
    n_jobs = args.jobs or int(PARAMS.get("jobs", 8))
    kinds = args.kinds.split(",") if args.kinds else PARAMS.get(
        "job_kinds", ["compress", "hash", "resize"])

    task_queue = TaskQueue(workers)
    for job in make_jobs(n_jobs, kinds, rng):
        task_queue.submit(job)

    wall_start = time.perf_counter()
    task_queue.run()
    wall_ms = (time.perf_counter() - wall_start) * 1000.0

    print("Plan-and-Execute Agent: Task Queue  (topic: Plan-and-Execute Agent, seed=%d)" % args.seed)
    print("%4s %-9s %-9s %10s %s" % ("job", "kind", "worker", "elapsed_ms", "digest"))
    for job_id, kind, worker, elapsed_ms, digest in task_queue.results():
        print("%4d %-9s %-9s %10.1f %s" % (job_id, kind, worker, elapsed_ms, digest))
    summary = task_queue.stats()
    print("\nCompleted %d jobs on %d workers in %.1f ms wall time "
          "(mean job time %.1f ms)." % (
              summary["jobs"], workers, wall_ms, summary["mean_ms"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
