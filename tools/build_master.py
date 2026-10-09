#!/usr/bin/env python3
"""Assemble the master architecture document and export Word + PDF.

Usage: python3 -I tools/build_master.py <repo_root> [--no-pdf]

Order (plan §16): title & disclosure · Executive summary (synthesis Part I) · Method & quality rules ·
Nine layers L1→L9 · Controls C1–C8 · remaining synthesis Parts (hypotheses … what changed since the popular stack diagram) ·
Annex: sources, data and companion documents. The LinkedIn series and the tile-by-tile what-changed table each have
one home elsewhere (07_LinkedIn, 05_Data/what_changed.xlsx) and are not repeated here. Each LinkedIn post visual
(08_Graphic/linkedin/P<NN>.png) is placed in the chapter or Part it illustrates (VISUALS below).
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
LAYERS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9"]  # L1 -> L9 (user decision, 9 Oct 2026)
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

# --- LinkedIn post visuals, placed where they illustrate the text (P00, the series map, stays in the LinkedIn document)
VDIR = "Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin"
CHAPTER_VIS = {"L1": "P01", "C6": "P02", "L2": "P03", "C1": "P04", "L3": "P05", "C2": "P06", "L4": "P07", "C4": "P08", "L5": "P09",
               "L6": "P11", "C7": "P12", "L7": "P13", "C5": "P14", "L8": "P15", "C3": "P16", "C8": "P18"}
# synthesis: (visual, heading the figure goes immediately before)
SYN_VIS = [("P10", "## V.1 "), ("P19", "## VI.3 "), ("P20", "# Part VIII"), ("P21", "# Part IX"), ("P22", "## IX.4 "),
           ("P23", "# Part X:"), ("P24", "# Part XII")]

def visual(pid, width="4.8in"):
    src = os.path.join(VDIR, pid + ".md")
    if not os.path.exists(src) or not os.path.exists(os.path.join(VDIR, pid + ".png")):
        return ""
    s = open(src, encoding="utf-8").read()
    title = re.search(r"(?m)^#\s+(.+)$", s).group(1).strip()
    cap = (re.search(r"(?m)^Caption:\s*(.+)$", s) or [None, ""])[1].strip()
    return ("![%s](%s/%s.png){width=%s}\n\n*Figure: %s. %s Editable source: `08_Graphic/linkedin/%s.md`.* [AJ]\n\n"
            % (title, VDIR, pid, width, title.rstrip("."), cap, pid))

def place_chapter_visual(code, md):
    pid = CHAPTER_VIS.get(code)
    fig = visual(pid) if pid else ""
    if code == "L9":  # the L9 card contrasts with the popular stack diagram, so it lives under 9.13 (house convention)
        fig = visual("P17")
        return re.sub(r"(?m)^(### 9\.13 [^\n]*\n)", lambda m: m.group(1) + "\n" + fig, md, count=1) if fig else md
    if not fig:
        return md
    return re.sub(r"(?m)^(?=### %s\.1 )" % re.escape(code[1:] if code.startswith("L") else code), fig, md, count=1)

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
# synthesis preamble (disclosure + CP4 tier-change table) goes up front, before the executive summary
pre_part = next((p for p in parts if not re.match(r"# Part ", p)), "")
pre_orig = pre_part
if pre_part:
    pre_part = re.sub(r"^# .*\n", "# About this document: disclosure and final tiers\n", pre_part, count=1)
    pre_part = re.sub(r"\n---\s*$", "\n", pre_part)
    pre_part = re.sub(r"(?ms)^\| \| \|\n.*?\n\n", "", pre_part, count=1)  # drop the internal metadata table (work/ paths)
rest = [p for p in parts if p is not exec_part and p is not pre_orig]

doc = []
doc.append("---\ntitle: \"The Enterprise GenAI Stack\"\nsubtitle: \"The view at end of Q3 2026: reference architecture and product assessment for regulated financial services, technology service providers, software companies and start-ups\"\ndate: \"%s\"\n---\n" % "Veyan · evidence as of 9 October 2026")
doc.append("![Veyan](brand/veyan_lockup.png){width=2.6in}\n")
doc.append("> **The view at end of Q3 2026.** The popular stack diagram was the inspiration and baseline; this document presents the stack as it stands at the end of Q3 2026, and Part XII sets out what changed since the diagram. Not a description of any firm's actual platform or vendor choices. Disclosure: researched and drafted by an Anthropic model; see Part II.\n")
if pre_part:
    doc.append(pre_part)
if exec_part:
    doc.append(exec_part)
doc.append(re.sub(r"^# Method", "# Part II: Method", method, count=1))
doc.append("# The nine layers (L1 → L9)\n")
for L in LAYERS:
    doc.append(place_chapter_visual(L, read("work/stageB/%s/section.md" % L)))
doc.append("# Cross-cutting enterprise controls (C1–C8)\n")
for C in CTRLS:
    doc.append(place_chapter_visual(C, read("work/stageB/%s/section.md" % C)))
rest_md = "\n\n".join(rest)
for pid, head in SYN_VIS:
    fig = visual(pid)
    if fig and head in rest_md:
        rest_md = rest_md.replace("\n" + head, "\n" + fig + head, 1)
doc.append(rest_md)
# Stage E further views (Parts XIII-XV): technology service provider, software product company, start-up
for vid in ("TS", "SW", "SU"):
    doc.append(read("work/stageE/views/%s/view.md" % vid))
doc.append("# Annex: Sources, data and companion documents\n\nEach item below has one home; this document does not repeat it [AJ].\n\n"
           "| Item | Where it lives |\n|---|---|\n"
           "| All sources, with access dates and the claim map | `06_References/bibliography.xlsx` |\n"
           "| Product dataset (140 records, fact cells and scores) | `05_Data/products.xlsx` and `products.json` |\n"
           "| Product fact sheets for every record | `02_Appendix/Product_Technical_Appendix` |\n"
           "| Tile-by-tile table: what changed since the popular stack diagram | `05_Data/what_changed.xlsx` (summary in Part XII) |\n"
           "| Regulatory and standards records | `05_Data/regulatory_facts.json` |\n"
           "| LinkedIn series (introduction and 24 posts, with visuals) | `07_LinkedIn/LinkedIn_Series.docx` and `Content_Calendar.xlsx` |\n"
           "| Editable sources of every figure | `08_Graphic/` (stack graphic, one-page architecture, `diagrams/`, `linkedin/`) |\n"
           "| Executive deck | `03_Slides/Executive_Deck.pptx` |\n")
full = "\n\n".join(d for d in doc if d)
open(os.path.join(OUT, "Master_Architecture.md"), "w", encoding="utf-8").write(full)

# --- Word edition with footnote-style tags
conv = convert_markdown(full, src, regidx, prodidx)
open("work/stageD/Master_Architecture.pandoc.md", "w", encoding="utf-8").write(conv)
cmd = ["pandoc", "work/stageD/Master_Architecture.pandoc.md", "-f", "markdown+pipe_tables+bracketed_spans+footnotes-implicit_figures-tex_math_dollars-raw_tex-tex_math_single_backslash",
       "-o", os.path.join(OUT, "Master_Architecture.docx"), "--toc", "--toc-depth=2",
       "--reference-doc=tools/templates/reference.docx"]
r = subprocess.run(cmd, capture_output=True, text=True)
print("pandoc:", r.returncode, r.stderr[-500:])
if "--no-pdf" not in sys.argv and r.returncode == 0:
    r2 = subprocess.run([sys.executable, "-I", "tools/docx2pdf.py", os.path.join(OUT, "Master_Architecture.docx"), os.path.join(OUT, "Master_Architecture.pdf")],
                        capture_output=True, text=True, timeout=3600)
    print("pdf:", r2.returncode, (r2.stdout + r2.stderr)[-300:])
print(json.dumps({"words": len(full.split()), **{k: str(v) for k, v in stats.items()}}))
