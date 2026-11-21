---
description: Run learn-path-note on file, directory and registry paths from fullpaths.csv (default 10 random) and push notes to kb/tools/os/windows/dir
argument-hint: "[count|all] [--seed N]"
---

Generate Microsoft Learn notes for paths in `fullpaths.csv`.

## 1. Pick paths

Run:

```
python scripts/pick_paths.py $ARGUMENTS
```

- No arguments = 10 random paths. `all` = every remaining path. `--seed N` makes the random pick repeatable.
- File, directory and registry key paths are picked (drive-letter, `%VAR%` and HKLM/HKCU/HKU/HKCR/HKCC paths).
- Paths that already have a note in `kb/tools/os/windows/dir/` are skipped, so re-running continues where it left off.

If nothing is printed, report that everything is done and stop.

## 2. Make the notes

For each printed path, one at a time, follow `.claude/skills/learn-path-note/SKILL.md` exactly (Microsoft Learn tools only, template, save path under `kb/tools/os/windows/dir/`).

- If Microsoft Learn has nothing for a path, still write the note with `_Not documented on Microsoft Learn_` sections.
- If a path fails (tool error), note it and move on; don't stop the batch.

## 3. Commit and push

After every 10 notes (and at the end), from the repo root:

```
git pull --rebase origin main
git add kb/tools/os/windows/dir
git commit -m "Add Microsoft Learn notes (<n> paths)"
git push origin main
```

## 4. Report

Finish with a short table: path | note file | Learn pages used (count) | status (ok / not documented / failed).
