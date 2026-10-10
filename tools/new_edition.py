#!/usr/bin/env python3
"""Start a new edition (any month): move the package folder, update edition.json, relabel the sources.

Usage:
  python3 -I tools/new_edition.py <repo_root> --month YYYY-MM [--evidence-date "8 January 2027"]
                                  [--label "The view at end of Q4 2026"] [--as-at "at the end of Q4 2026"] [--dry-run]

What it does (mechanics only; the research and writing are REFRESH_QUARTERLY.md R0-R5):
  1. Records the current edition as "previous" in edition.json (its package, label and the HEAD commit), so
     tools/diff_tiers.py and tools/check_edition.py compare against it without arguments.
  2. git mv <old package> <new package> (Enterprise_GenAI_Stack_<Mon><YYYY>), and renames the stack graphic files
     named after the package (08_Graphic/<package>.md/.html/.png/.pdf).
  3. Writes the new edition.json: package, month, quarter, view label, "as at" phrase, evidence date, edition number.
     Label rule unless --label is given: a run in the first month of a quarter (Jan, Apr, Jul, Oct) is
     "The view at end of Q<n> <year>" for the quarter just ended; any other month is "The view in <Month> <year>".
  4. Replaces the old edition's label phrases with the new ones in the master's sources (synthesis, the 17
     chapters, the six view Parts, method, the stack graphic and one-page sources, the package README, the
     master's publishing kit).
  5. Replaces the old package folder name (a path) in every tracked text file, so figure links and data paths
     resolve after the move; history (MEMORY.md, checkpoints/, inputs/, archived web content) is left as written. Dated facts ("as of 8 October 2026") are NOT changed:
     they are evidence, re-verified by the refresh; tools/check_edition.py lists what still names the old edition.
  The LinkedIn series and its book keep their own (first) edition and are not relabelled.
Then: bash tools/rebuild_all.sh, python3 -I tools/check_edition.py ., and the refresh steps in REFRESH_QUARTERLY.md.
"""
import calendar, datetime, glob, json, os, re, subprocess, sys

root = sys.argv[1]; os.chdir(root)
def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
DRY = "--dry-run" in sys.argv
month = arg("--month")
if not month or not re.fullmatch(r"\d{4}-\d{2}", month):
    sys.exit("--month YYYY-MM is required, e.g. --month 2026-12")
y, m = int(month[:4]), int(month[5:])
OLD = json.load(open("edition.json", encoding="utf-8"))
mon_name = calendar.month_name[m]
new_pkg = "Enterprise_GenAI_Stack_%s%d" % (calendar.month_abbr[m], y)
if new_pkg == OLD["package"]:
    sys.exit("The current edition is already %s; nothing to do (for a desktop re-run of the same edition, just run rebuild_all.sh)" % new_pkg)

if m in (1, 4, 7, 10):  # first month of a quarter: the view at the end of the quarter just closed
    q, qy = ((m - 1) // 3) or 4, y if m != 1 else y - 1
    quarter = "Q%d %d" % (q, qy)
    label, as_at = "The view at end of %s" % quarter, "at the end of %s" % quarter
else:
    q = (m - 1) // 3 + 1
    quarter = "Q%d %d" % (q, y)
    label, as_at = "The view in %s %d" % (mon_name, y), "in %s %d" % (mon_name, y)
label = arg("--label", label); as_at = arg("--as-at", as_at)
if arg("--evidence-date"):
    ev = arg("--evidence-date"); ev_iso = datetime.datetime.strptime(ev, "%d %B %Y").date().isoformat()
else:
    d = datetime.date.today()
    if (d.year, d.month) != (y, m):
        d = datetime.date(y, m, 1)
    ev, ev_iso = "%d %s %d" % (d.day, calendar.month_name[d.month], d.year), d.isoformat()
num = int(OLD.get("edition_number", 1)) + 1
ORD = {2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Tenth"}
head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
NEW = dict(OLD)
NEW.update({"package": new_pkg, "month_year": "%s %d" % (mon_name, y), "quarter": quarter, "view_label": label,
            "as_at": as_at, "evidence_date": ev, "evidence_iso": ev_iso, "edition_number": num,
            "edition": "%s edition, %s %d" % (ORD.get(num, "Edition %d:" % num), mon_name, y), "roadmap_start": "%s %d" % (mon_name, y),
            "previous": {"package": OLD["package"], "commit": head, "view_label": OLD["view_label"],
                         "as_at": OLD["as_at"], "quarter": OLD["quarter"], "month_year": OLD["month_year"],
                         "evidence_date": OLD["evidence_date"]}})
print(json.dumps({k: NEW[k] for k in ("package", "view_label", "as_at", "quarter", "evidence_date", "edition")}, indent=1))

def lc(s): return s[0].lower() + s[1:]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import title_case
PAIRS = [(OLD["view_label"], label), (lc(OLD["view_label"]), lc(label)), (OLD["view_label"].upper(), label.upper()),
         (title_case(OLD["view_label"]), title_case(label)), (OLD["as_at"], as_at)]
PAIRS = [(a, b) for a, b in PAIRS if a != b]

def rewrite(paths, pairs, quiet=False):
    n = 0
    for p in paths:
        if not os.path.isfile(p):
            continue
        s = open(p, encoding="utf-8").read(); t = s
        for a, b in pairs:
            t = t.replace(a, b)
        if t != s:
            n += 1
            if not quiet:
                print("  relabel", p)
            if not DRY:
                open(p, "w", encoding="utf-8").write(t)
    return n

def run(*cmd):
    print("  $", " ".join(cmd))
    if not DRY:
        subprocess.run(cmd, check=True)

# 2. folder move and stack-graphic rename
run("git", "mv", OLD["package"], new_pkg)
G = os.path.join(new_pkg if not DRY else OLD["package"], "08_Graphic")
for ext in ("md", "html", "png", "pdf"):
    src = os.path.join(G, OLD["package"] + "." + ext)
    if os.path.exists(src):
        run("git", "mv", src, os.path.join(G, new_pkg + "." + ext))
# 3. edition.json
if not DRY:
    json.dump(NEW, open("edition.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False); open("edition.json", "a").write("\n")
# 4. relabel the master's sources and the package README
P = new_pkg if not DRY else OLD["package"]
content = (["work/stageC/synthesis.md", "work/stageD/method.md", os.path.join(P, "00_README.md"),
            os.path.join(P, "08_Graphic", (new_pkg if not DRY else OLD["package"]) + ".md"),
            os.path.join(P, "08_Graphic", "Architecture_One_Page.html"), os.path.join(P, "01_Report/Print/Publishing_Kit.md")]
           + sorted(glob.glob("work/stageB/*/section.md")) + sorted(glob.glob("work/stageE/views/*/view.md")))
print("Relabelled %d source files" % rewrite(content, PAIRS))
# 5. the old package name (a folder path: figure links, data paths, commands) in every tracked text file, so figures
#    and data still resolve after the move. History is left as written: MEMORY.md, checkpoints/, inputs/, archived web
#    content (06_References/snapshots, originals) and REFRESH_QUARTERLY.md, which describes the move itself.
SKIP = ("MEMORY.md", "REFRESH_QUARTERLY.md", "checkpoints/", "inputs/", "/06_References/snapshots/", "/06_References/originals/",
        "tools/new_edition.py", "tools/check_edition.py", "edition.json")
TEXT = (".md", ".py", ".js", ".json", ".html", ".csv", ".txt", ".sh", ".yaml", ".yml", ".css")
files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split("\n")
files = [f for f in files if f.endswith(TEXT) and not any(s in "/" + f if s.startswith("/") else f.startswith(s) or f == s for s in SKIP)
         and "node_modules/" not in f]
if DRY:
    print("Would update the package name in tracked text files that contain it")
else:
    print("Updated the package name in %d files" % rewrite(files, [(OLD["package"], new_pkg)], quiet=True))
print("\nNext: bash tools/rebuild_all.sh ; python3 -I tools/check_edition.py . ; then REFRESH_QUARTERLY.md R0-R5."
      "\nCompare with the previous edition: python3 -I tools/diff_tiers.py .   (base %s)" % head)
