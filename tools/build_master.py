#!/usr/bin/env python3
"""Assemble the master architecture document and export Word + PDF.

Usage: python3 -I tools/build_master.py <repo_root> [--no-pdf]

Order (plan §16): title & disclosure · Executive summary (synthesis Part I) · Method & quality rules ·
Nine layers 9→1 · Controls C1–C8 · remaining synthesis Parts (hypotheses … final stack) ·
LinkedIn series · Annex: What changed since the original diagram.
Writes:
  Enterprise_GenAI_Stack_Oct2026/01_Report/Master_Architecture.md   (full inline tags)
  Enterprise_GenAI_Stack_Oct2026/01_Report/Master_Architecture.docx (footnote-style tags, CP5-1)
  Enterprise_GenAI_Stack_Oct2026/01_Report/Master_Architecture.pdf  (via LibreOffice)
"""
import collections, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tagfmt import load_index, convert_markdown

root = sys.argv[1]; os.chdir(root)
OUT = "Enterprise_GenAI_Stack_Oct2026/01_Report"
os.makedirs(OUT, exist_ok=True)
LAYERS = ["L9", "L8", "L7", "L6", "L5", "L4", "L3", "L2", "L1"]
CTRLS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]

def read(p):
    return open(p, encoding="utf-8").read().strip() + "\n" if os.path.exists(p) else ""

def demote(md, levels=1):
    out, in_code = [], False
    for line in md.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^#{1,5} ", line):
            line = "#" * levels + line
        out.append(line)
    return "\n".join(out)

# --- stats for the method chapter
prods = json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/products.json", encoding="utf-8"))
regs = json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json", encoding="utf-8"))
src, regidx, prodidx = load_index(".")
def cells(o):
    if isinstance(o, dict) and "v" in o and "label" in o: yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ("assessment", "classification", "scores"): yield from cells(v)
allcells = [c for p in prods for c in cells(p)]
tiers = collections.Counter((p.get("classification") or {}).get("tier") for p in prods if p.get("scores"))
acc = collections.Counter((s.get("access_status") or "").split(" ")[0] for s in src.values())
stats = dict(N_PRODUCTS=len(prods), N_SCORED=sum(1 for p in prods if p.get("scores")), N_STRATEGIC=tiers.get("Strategic", 0),
             N_TACTICAL=tiers.get("Tactical", 0), N_EXPERIMENTAL=tiers.get("Experimental", 0), N_REG=len(regs),
             N_SOURCES=f"{len(src):,}", N_SNAPSHOT=f"{acc.get('snapshot', 0):,}", N_EXTRACT=f"{acc.get('extract', 0):,}",
             N_LINK=acc.get("link-only", 0), N_NPV=f"{sum(1 for c in allcells if c.get('label') == 'Not publicly verified'):,}",
             N_CELLS=f"{len(allcells):,}")
method = read("work/stageD/method.md")
for k, v in stats.items():
    method = method.replace("{%s}" % k, str(v))

# --- synthesis parts
syn = read("work/stageC/synthesis.md")
parts = re.split(r"(?m)^(?=# )", syn) if syn else []
parts = [p for p in parts if p.strip().startswith("# ")]
exec_part = next((p for p in parts if re.match(r"# .*(Executive summary)", p, re.I)), "")
rest = [p for p in parts if p is not exec_part]

doc = []
doc.append("---\ntitle: \"Enterprise GenAI Full-Stack Architecture\"\nsubtitle: \"Reference architecture, product assessment and regulated-FS view, October 2026\"\ndate: \"%s\"\n---\n" % "October 2026")
doc.append("> **Status:** final package (CP5). Personal research; not a description of any firm's actual platform or vendor choices. Disclosure: researched and drafted by an Anthropic model; see Method.\n")
if exec_part:
    doc.append(exec_part)
doc.append(method)
doc.append("# The nine layers (analysed 9 → 1)\n")
for L in LAYERS:
    doc.append(read("work/stageB/%s/section.md" % L))
doc.append("# Cross-cutting enterprise controls (C1–C8)\n")
for C in CTRLS:
    doc.append(read("work/stageB/%s/section.md" % C))
doc.extend(rest)
li = read("work/stageC2/linkedin_series.md")
if li:
    doc.append(demote(re.sub(r"(?m)^# .*\n", "", li, count=1), 0) if li.startswith("# ") else li)
    if not li.lstrip().startswith("# "):
        doc.insert(len(doc) - 1, "# LinkedIn thought-leadership series\n")
wc = read("checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md")
if wc:
    doc.append("# Annex A: What changed since the original diagram\n" + demote(re.sub(r"(?m)^# .*\n", "", wc, count=1), 1))
doc.append("# Annex B: Sources and data\n\nAll sources: `06_References/bibliography.xlsx` (sources and claim map). Product dataset: `05_Data/products.xlsx` / `products.json`. Product deep dives for every record: `02_Appendix/Product_Technical_Appendix`. Scores: `05_Data/products.xlsx` (sheet *products*).\n")
full = "\n\n".join(d for d in doc if d)
open(os.path.join(OUT, "Master_Architecture.md"), "w", encoding="utf-8").write(full)

# --- Word edition with footnote-style tags
conv = convert_markdown(full, src, regidx, prodidx)
open("work/stageD/Master_Architecture.pandoc.md", "w", encoding="utf-8").write(conv)
cmd = ["pandoc", "work/stageD/Master_Architecture.pandoc.md", "-f", "markdown+pipe_tables+bracketed_spans+footnotes-implicit_figures",
       "-o", os.path.join(OUT, "Master_Architecture.docx"), "--toc", "--toc-depth=2",
       "--reference-doc=tools/templates/reference.docx"]
r = subprocess.run(cmd, capture_output=True, text=True)
print("pandoc:", r.returncode, r.stderr[-500:])
if "--no-pdf" not in sys.argv and r.returncode == 0:
    r2 = subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", OUT, os.path.join(OUT, "Master_Architecture.docx")],
                        capture_output=True, text=True, timeout=3000)
    print("soffice:", r2.returncode, (r2.stdout + r2.stderr)[-300:])
print(json.dumps({"words": len(full.split()), **{k: str(v) for k, v in stats.items()}}))
