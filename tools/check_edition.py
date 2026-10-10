#!/usr/bin/env python3
"""After a rebuild, list what still names the previous edition (run by tools/rebuild_all.sh at the end).

Usage: python3 -I tools/check_edition.py <repo_root> [--strict]

Reads edition.json. For each deliverable in the current package (Markdown, HTML, JSON and the text inside .docx,
.pptx and .xlsx) and each source the deliverables are built from, it counts:
  - LABEL : the previous edition's label or "as at" phrase, or its package folder name. These should be zero after
            tools/new_edition.py and a rebuild; any left are edition labels written by hand. Fix them in the source.
  - DATED : the previous quarter or month ("Q3 2026", "October 2026"). Many are dated evidence and correct as
            they stand (an acquisition completed in October 2026 stays so); the refresh (R1-R4) decides each one.
It also checks that every deliverable carries the current label. --strict exits 1 when a LABEL count is not zero.
The LinkedIn series and its book keep their own first edition and are reported separately, for information only.
"""
import glob, json, os, re, sys, zipfile

root = sys.argv[1]; os.chdir(root)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import E, PKG, title_case

def text_of(p):
    if p.endswith((".docx", ".pptx", ".xlsx")):
        try:
            z = zipfile.ZipFile(p)
        except zipfile.BadZipFile:
            return ""
        parts = [n for n in z.namelist() if n.endswith(".xml") and re.search(r"(word/(document|footnotes|header\d*|footer\d*)|ppt/(slides|notesSlides)/|xl/sharedStrings)", n)]
        return " ".join(re.sub(r"<[^>]+>", "", z.read(n).decode("utf-8", "ignore")) for n in parts)
    try:
        return open(p, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError):
        return ""

DELIV = [p for p in glob.glob(PKG + "/**/*", recursive=True)
         if p.endswith((".md", ".html", ".json", ".docx", ".pptx", ".xlsx")) and "/06_References/snapshots/" not in p
         and "/06_References/originals/" not in p]
SOURCES = (["work/stageC/synthesis.md", "work/stageD/method.md", "tools/print/master_front.md", "tools/print/book.json"]
           + glob.glob("work/stageB/*/section.md") + glob.glob("work/stageE/views/*/view.md")
           + glob.glob("tools/*.py") + glob.glob("tools/*.js") + glob.glob("tools/deck/*.js"))
LINKEDIN = lambda p: "/07_LinkedIn/" in p or "/08_Graphic/linkedin/" in p

prev = E.get("previous")
strict_fail = 0
print("Edition: %s (%s, package %s)" % (E["view_label"], E["evidence_date"], PKG))
if not prev:
    print("First edition: no previous edition to compare with.")
else:
    lc = lambda s: s[0].lower() + s[1:]
    label_pats = sorted({prev["view_label"], lc(prev["view_label"]), prev["view_label"].upper(), title_case(prev["view_label"]),
                         prev["as_at"], prev["package"]} - {E["view_label"], E["as_at"], PKG}, key=len, reverse=True)
    dated_pats = [x for x in (prev.get("quarter"), prev.get("month_year")) if x and x not in (E["quarter"], E["month_year"])]
    rows = []
    for p in sorted(set(DELIV + SOURCES)):
        if p.endswith(("check_edition.py", "new_edition.py", "edition.py")):
            continue
        t = text_of(p)
        lab = sum(t.count(x) for x in label_pats)
        t2 = t
        for x in label_pats:
            t2 = t2.replace(x, " ")
        dat = sum(t2.count(x) for x in dated_pats)
        if lab or dat:
            rows.append((p, lab, dat))
    main = [r for r in rows if not LINKEDIN(r[0])]
    li = [r for r in rows if LINKEDIN(r[0])]
    print("\nPrevious edition: %s. Files that still name it (LABEL should be 0; DATED is for the refresh to review):" % prev["view_label"])
    print("%-80s %6s %6s" % ("file", "LABEL", "DATED"))
    for p, a, b in main:
        print("%-80s %6d %6d" % (p[:80], a, b))
    strict_fail = sum(a for _, a, _ in main)
    if li:
        print("\nLinkedIn series and book (own first edition, not relabelled): %d files, %d label mentions" % (len(li), sum(a for _, a, _ in li)))
missing = [p for p in DELIV if p.endswith((".docx", ".pptx")) and not LINKEDIN(p)
           and E["view_label"].lower() not in text_of(p).lower() and E["as_at"] not in text_of(p)]
if missing:
    print("\nDeliverables that do not carry the current label (%s): %s" % (E["view_label"], ", ".join(missing)))
print("\nLABEL total: %d" % strict_fail)
if "--strict" in sys.argv and strict_fail:
    sys.exit(1)
