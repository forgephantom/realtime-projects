# Presentation Guide — FASTQ Quality Trimmer: File Organizer

## 60-Second Pitch

I built a FASTQ Quality Trimmer that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. Sequencing reads carry per-base Phred quality scores, and quality typically decays toward read ends.

FASTQ Quality Trimmer in two sentences: Sequencing reads carry per-base Phred quality scores, and quality typically decays toward read ends. Sliding-window trimming cuts low-quality tails, while adapter clipping removes leftover sequencing adapters. Synthetic reads with known quality decay let developers verify that trimming keeps the good bases and drops the bad.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a FASTQ Quality Trimmer in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'read_count': 'number of synthetic reads', 'read_length': 'length of each read', 'error_profile': 'quality decay profile', 'seed': 'random seed for read generation'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
