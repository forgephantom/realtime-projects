# Presentation Guide — Privacy Data Export Tool: Backup Tool

## 60-Second Pitch

I built a Privacy Data Export Tool that copies your files and proves the copy is exact by verifying SHA-256 checksums. Data-portability law lets users download their data: the export tool collects a user's records across services, packages them in machine-readable formats, and delivers a secure expiring download.

Privacy Data Export Tool in two sentences: Data-portability law lets users download their data: the export tool collects a user's records across services, packages them in machine-readable formats, and delivers a secure expiring download. It must include everything, exclude others' data, and complete within legal deadlines. Completeness is the compliance risk.

## Architecture Talking Points

- Components: `BackupJob` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Full copy with SHA-256 manifest, then re-hash verification; runs in O(bytes) to copy and hash every file.
- Honest scaling limit: Single-machine full copies; large trees would want incremental backups and parallel hashing.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Privacy Data Export Tool in Python that copies a folder tree and verifies integrity with SHA-256 checksums stored in a JSON manifest.
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
