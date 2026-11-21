"""Pick file/directory paths from fullpaths.csv that don't have a note yet.

Usage: python scripts/pick_paths.py [COUNT|all] [--seed N]
Prints one path per line.
"""
import csv
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "kb", "tools", "os", "windows", "dir")


def note_path(p):
    # Drop drive letter, keep the rest as folders, all lowercase (no case duplicates).
    rel = re.sub(r"^[A-Za-z]:\\", "", p).replace("\\", "/").lower()
    return os.path.join(OUT, rel + ".md")


def is_file_or_dir(p):
    # Filesystem paths only: drive-letter paths or %ENVVAR% paths. Excludes registry hives.
    return bool(re.match(r"^([A-Za-z]:\\|%|HK(LM|CU|U|CR|CC)\\)", p, re.I))


def main():
    args = sys.argv[1:]
    count = args[0] if args and not args[0].startswith("--") else "10"
    seed = int(args[args.index("--seed") + 1]) if "--seed" in args else None

    with open(os.path.join(ROOT, "fullpaths.csv"), newline="", encoding="utf-8") as fh:
        paths = [r["fullpath"] for r in csv.DictReader(fh)]

    todo = [p for p in paths if is_file_or_dir(p) and not os.path.exists(note_path(p))]
    if count != "all":
        random.Random(seed).shuffle(todo)
        todo = todo[: int(count)]
    for p in todo:
        print(p)
    print(f"# {len(todo)} selected", file=sys.stderr)


if __name__ == "__main__":
    main()
