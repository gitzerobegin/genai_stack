#!/usr/bin/env python3
"""Compare tiers and scores between a baseline commit and the current working tree.

Used by the quarterly refresh (REFRESH_QUARTERLY.md, step R5) to produce the
"What changed since the last edition" table.

Usage:
  python3 -I tools/diff_tiers.py <repo_root> [base_ref] [--base-path P] [--path P] [--out FILE]

  base_ref    git commit or tag of the previous edition (default: edition.json "previous.commit",
              written by tools/new_edition.py)
  --base-path products.json path at base_ref
              (default: the previous edition's <package>/05_Data/products.json)
  --path      products.json path now (default: <PKG>/05_Data/products.json for the current edition)
  --out       markdown output (default work/refresh/tier_changes.md)
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import E, PKG

root = sys.argv[1]
os.chdir(root)
PREV = E.get("previous") or {}
base = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else PREV.get("commit")
if not base:
    sys.exit("No previous edition: pass a base_ref, or start the edition with tools/new_edition.py")

def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

base_path = arg("--base-path", (PREV.get("package") or PKG) + "/05_Data/products.json")
cur_path = arg("--path", PKG + "/05_Data/products.json")
out = arg("--out", "work/refresh/tier_changes.md")

old = json.loads(subprocess.run(["git", "show", "%s:%s" % (base, base_path)], capture_output=True, text=True, check=True).stdout)
new = json.load(open(cur_path, encoding="utf-8"))

def view(p):
    c = p.get("current_name")
    sc = p.get("scores") or {}
    return {"name": c["v"] if isinstance(c, dict) else p["id"], "layer": p.get("layer"),
            "tier": (p.get("classification") or {}).get("tier") or "Not scored",
            "fs": sc.get("fs_total"), "gen": sc.get("generic_total")}

o = {p["id"]: view(p) for p in old}
n = {p["id"]: view(p) for p in new}
rows = []
for pid in sorted(set(o) | set(n)):
    a, b = o.get(pid), n.get(pid)
    if a is None:
        rows.append((b["layer"], b["name"], pid, "New record", "", b["tier"], "", b["fs"]))
    elif b is None:
        rows.append((a["layer"], a["name"], pid, "Removed", a["tier"], "", a["fs"], ""))
    elif a["tier"] != b["tier"] or a["fs"] != b["fs"]:
        kind = "Tier change" if a["tier"] != b["tier"] else "Score change"
        rows.append((b["layer"], b["name"], pid, kind, a["tier"], b["tier"], a["fs"], b["fs"]))

order = {"Tier change": 0, "New record": 1, "Removed": 2, "Score change": 3}
rows.sort(key=lambda r: (order[r[3]], r[0] or "", r[1]))
fmt = lambda v: "" if v in (None, "") else ("%.2f" % v if isinstance(v, (int, float)) else str(v))
md = ["# Tier and score changes since %s\n" % base,
      "%d records compared: %d tier changes, %d new, %d removed, %d score-only changes.\n" % (
          len(set(o) | set(n)), sum(r[3] == "Tier change" for r in rows), sum(r[3] == "New record" for r in rows),
          sum(r[3] == "Removed" for r in rows), sum(r[3] == "Score change" for r in rows)),
      "| Layer | Product | ID | Change | Tier before | Tier now | FS before | FS now |",
      "|---|---|---|---|---|---|--:|--:|"]
md += ["| %s | %s | `%s` | %s | %s | %s | %s | %s |" % (r[0], r[1], r[2], r[3], r[4], r[5], fmt(r[6]), fmt(r[7])) for r in rows]
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
open(out, "w", encoding="utf-8").write("\n".join(md) + "\n")
print(md[1].strip(), "->", out)
