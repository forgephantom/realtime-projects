# Presentation Guide — Snapshot Diff Engine: File Organizer

## 60-Second Pitch

I built a Snapshot Diff Engine that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Snapshot diffs compare full table snapshots to produce change sets (inserts, updates, deletes) without CDC: the engine hashes rows, joins on keys, and emits typed changes.

Snapshot Diff Engine in two sentences: Snapshot diffs compare full table snapshots to produce change sets (inserts, updates, deletes) without CDC: the engine hashes rows, joins on keys, and emits typed changes. It handles late-arriving snapshots and schema drift. It is the batch world's change capture.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Snapshot Diff Engine in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'keys': 'primary key for matching', 'hash': 'row hash for change detection', 'tolerance': 'float comparison tolerance'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
