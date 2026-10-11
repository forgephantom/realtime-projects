# Presentation Guide — Checkpoint and Recovery (ARIES-lite): Backup Tool

## 60-Second Pitch

I built a Checkpoint and Recovery (ARIES-lite) that copies your files and proves the copy is exact by verifying SHA-256 checksums. ARIES recovery replays the WAL in three passes: analysis finds dirty pages and active transactions, redo repeats history, undo rolls back losers.

Checkpoint and Recovery (ARIES-lite) in two sentences: ARIES recovery replays the WAL in three passes: analysis finds dirty pages and active transactions, redo repeats history, undo rolls back losers. Checkpoints bound the replay work. The lite version implements the three passes on a page model. It is the algorithm that made crash recovery boring (in a good way).

## Architecture Talking Points

- Components: `BackupJob` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Full copy with SHA-256 manifest, then re-hash verification; runs in O(bytes) to copy and hash every file.
- Honest scaling limit: Single-machine full copies; large trees would want incremental backups and parallel hashing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Checkpoint and Recovery (ARIES-lite) in Python that copies a folder tree and verifies integrity with SHA-256 checksums stored in a JSON manifest.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How are checksums recorded?

**A:** After copying, run() hashes each destination file and writes path, size, and SHA-256 into backup/manifest.json.

**Q:** How does verification work?

**A:** verify() re-hashes every file in the backup and compares against the manifest, reporting ok and failed lists.

**Q:** Does it preserve file metadata?

**A:** shutil.copy2 preserves file metadata like modification times along with the content.
