#!/usr/bin/env python3
"""Re-fetch sources that the cloud research environment could not fetch directly.

Run this on a machine with open internet access (e.g. your desktop). For every logged source whose
access_status is `extract` or `link-only`, it tries a direct fetch with tools/snapshot.py:
  - PDF  -> saved as an original under Enterprise_GenAI_Stack_Oct2026/06_References/originals/
  - HTML -> saved as a text snapshot next to the existing extract (the extract is kept)
and rewrites the source row (access_status, archive_path) in the CSV it came from.
Blocked/paywalled responses (401/402/403/429/451) are recorded and NOT worked around.

Usage:
  python3 -I tools/refetch_sources.py <repo_root> [--dry-run] [--limit N] [--stream A5] [--types primary-trust-centre,regulatory]
Writes work/gapfill/refetch_report.md.  Then run tools/build_dataset.py to rebuild bibliography.xlsx.
"""
import argparse, csv, glob, json, os, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("root"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--stream", default=""); ap.add_argument("--types", default="")
a = ap.parse_args()
os.chdir(a.root)
types = set(t for t in a.types.split(",") if t)
csvs = sorted(glob.glob("work/stageA/*/sources.csv") + glob.glob("work/stageA_verify/*/sources.csv") + glob.glob("work/stageB/*/sources_added*.csv") + glob.glob("work/gapfill/*/sources*.csv"))
done, tried, report = 0, 0, []
for path in csvs:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f)); fields = list(rows[0].keys()) if rows else []
    changed = False
    for r in rows:
        sid, url, st = r.get("id", ""), r.get("url", ""), (r.get("access_status") or "")
        if not sid or not url.startswith("http") or not (st.startswith("extract") or st.startswith("link-only")):
            continue
        if a.stream and not sid.startswith(a.stream + "-"):
            continue
        if types and r.get("source_type", "") not in types:
            continue
        if a.limit and tried >= a.limit:
            break
        tried += 1
        if a.dry_run:
            report.append("| %s | %s | (dry run) |" % (sid, url)); continue
        out_dir = "Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/" + sid.split("-")[0]
        p = subprocess.run([sys.executable, "-I", "tools/snapshot.py", sid, url, out_dir], capture_output=True, text=True)
        try:
            res = json.loads(p.stdout.strip().splitlines()[-1])
        except Exception:
            res = {"access_status": "link-only (snapshot error)"}
        new = res.get("access_status", "")
        if new in ("snapshot", "original"):
            r["access_status"] = new + " (refetched; earlier extract kept)"
            r["archive_path"] = res.get("path", r.get("archive_path", "")) + (" ; " + r["archive_path"] if r.get("archive_path") else "")
            changed = True; done += 1
        report.append("| %s | %s | %s |" % (sid, url, new + (" — " + res.get("note", "") if res.get("note") else "")))
    if changed:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
os.makedirs("work/gapfill", exist_ok=True)
with open("work/gapfill/refetch_report.md", "w", encoding="utf-8") as f:
    f.write("# Re-fetch report\n\nTried %d sources; %d now have a direct snapshot or original.\n\n| Source | URL | Result |\n|---|---|---|\n" % (tried, done))
    f.write("\n".join(report) + "\n")
print(json.dumps({"tried": tried, "refetched": done}))
