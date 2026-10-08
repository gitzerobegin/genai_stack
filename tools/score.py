#!/usr/bin/env python3
"""Compute weighted scorecard totals for a Stage B assessments file and print a markdown table.

Usage: python3 -I tools/score.py work/stageB/<LAYER>/assessments.json [--write]
Scores are integers 1-5 per criterion. Totals are weighted averages on the same 1-5 scale (2 dp).
With --write, the totals are written back into the file (scores.generic_total / scores.fs_total).
"""
import json, sys

CRIT = ["technical", "enterprise_readiness", "security_compliance", "deployment_flexibility",
        "ecosystem", "reliability_maturity", "cost_tco", "lockin_portability"]
GEN = dict(zip(CRIT, [20, 15, 15, 15, 10, 10, 10, 5]))
FS = dict(zip(CRIT, [15, 15, 20, 15, 5, 10, 5, 15]))
HEAD = ["Tech", "Ent", "Sec", "Deploy", "Eco", "Mature", "Cost", "Lock-in"]

path = sys.argv[1]
data = json.load(open(path, encoding="utf-8"))
errors = []
print("| Product | " + " | ".join(HEAD) + " | Generic | FS | Tier |")
print("|---|" + "---:|" * (len(HEAD) + 2) + "---|")
for a in data:
    s = (a.get("scores") or {}).get("criteria")
    if not s:
        print("| %s | %s | n/a | n/a | %s |" % (a["id"], " | ".join(["–"] * len(HEAD)), (a.get("classification") or {}).get("tier") or "not scored"))
        continue
    for c in CRIT:
        if c not in s or not isinstance(s[c], int) or not 1 <= s[c] <= 5:
            errors.append("%s: bad or missing score for %s" % (a["id"], c))
    if any(e.startswith(a["id"] + ":") for e in errors):
        continue
    g = round(sum(s[c] * GEN[c] for c in CRIT) / 100, 2)
    f = round(sum(s[c] * FS[c] for c in CRIT) / 100, 2)
    a["scores"]["generic_total"], a["scores"]["fs_total"] = g, f
    print("| %s | %s | %.2f | %.2f | %s |" % (a["id"], " | ".join(str(s[c]) for c in CRIT), g, f, a["classification"]["tier"]))
if errors:
    print("\nERRORS:\n" + "\n".join(errors)); sys.exit(1)
if "--write" in sys.argv:
    json.dump(data, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
