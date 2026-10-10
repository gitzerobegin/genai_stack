#!/usr/bin/env python3
"""List every fact cell that is still "Not publicly verified" (or low confidence), by product and field.
Drives a targeted gap-filling research pass on a machine with open internet access.

Usage: python3 -I tools/npv_report.py <repo_root> [--include-low]
Writes work/gapfill/npv_by_product.md and work/gapfill/npv_cells.csv
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import E, PKG
from collections import defaultdict

root = sys.argv[1]; inc_low = "--include-low" in sys.argv
os.chdir(root)
d = json.load(open(PKG + "/05_Data/products.json", encoding="utf-8"))
SKIP = {"assessment", "classification", "scores"}

def walk(o, path=""):
    if isinstance(o, dict) and "v" in o and "label" in o:
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in SKIP:
                yield from walk(v, (path + "." if path else "") + k)

rows, by = [], defaultdict(list)
for p in d:
    for path, c in walk(p):
        if c.get("label") == "Not publicly verified" or (inc_low and c.get("conf") == "low"):
            rows.append([p["id"], p["layer"], path, c.get("label"), c.get("conf", ""), str(c.get("v"))[:200]])
            by[p["id"]].append(path)
os.makedirs("work/gapfill", exist_ok=True)
with open("work/gapfill/npv_cells.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["product_id", "layer", "field", "label", "conf", "current_value"]); w.writerows(rows)
with open("work/gapfill/npv_by_product.md", "w", encoding="utf-8") as f:
    f.write("# Gap list: unverified fact cells by product\n\n%d cells across %d products.\n\n| Product | # | Fields |\n|---|---:|---|\n" % (len(rows), len(by)))
    for pid in sorted(by, key=lambda k: -len(by[k])):
        f.write("| %s | %d | %s |\n" % (pid, len(by[pid]), ", ".join(by[pid])))
print(json.dumps({"cells": len(rows), "products": len(by)}))
