#!/usr/bin/env python3
"""Collect the per-stream "What changed since the original diagram" tables (notes.md section (a))
into one table: work/cp1/what_changed_raw.md and .json (layer order 9 -> 1, then controls, then regulation).

Usage: python3 -I tools/build_what_changed.py <repo_root>
"""
import json, os, re, sys

root = sys.argv[1]
os.chdir(root)
STREAMS = ["A1_L9_L8", "A2_L7_L6", "A3_L5_L4", "A4_L3_L2", "A5_L1", "A6_C1_C4", "A7_C5_C8", "A8_Regulation"]
rows = []
for s in STREAMS:
    p = "work/stageA/%s/notes.md" % s
    if not os.path.exists(p):
        continue
    text = open(p, encoding="utf-8").read()
    m = re.search(r"^## \(a\)[^\n]*\n(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        continue
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|\s*-", line) or "Original label" in line or "Plan assumption" in line[:40]:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        rows.append({"stream": s.split("_")[0], "original": cells[0], "current": " | ".join(cells[1:-2]) if len(cells) > 4 else cells[1],
                     "flag": cells[-2], "sources": cells[-1]})
os.makedirs("work/cp1", exist_ok=True)
json.dump(rows, open("work/cp1/what_changed_raw.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
with open("work/cp1/what_changed_raw.md", "w", encoding="utf-8") as f:
    f.write("| # | Stream | Original label | Current reality | Flag | Sources |\n|---:|---|---|---|---|---|\n")
    for i, r in enumerate(rows, 1):
        f.write("| %d | %s | %s | %s | %s | %s |\n" % (i, r["stream"], r["original"], r["current"], r["flag"], r["sources"]))
print(len(rows))
