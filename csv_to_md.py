#!/usr/bin/env python3
"""Convert a CSV file to a Markdown table. Usage: python3 csv_to_md.py filename.csv  ->  filename.csv.md"""
import csv
import sys

def clean(value):
    # Keep table cells on one line and stop pipes from breaking columns
    return value.replace("\r", " ").replace("\n", " ").replace("|", "\\|")

path = sys.argv[1]
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

lines = ["| " + " | ".join(clean(c) for c in rows[0]) + " |",
         "| " + " | ".join("---" for _ in rows[0]) + " |"]
for row in rows[1:]:
    lines.append("| " + " | ".join(clean(c) for c in row) + " |")

with open(path + ".md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"Wrote {path}.md ({len(rows) - 1} rows)")
