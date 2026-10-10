#!/usr/bin/env python3
"""Build the Product Technical Appendix from the dataset (one entry per product record).

Usage: python3 -I tools/build_appendix.py <repo_root> [--pdf]
Writes <PKG>/02_Appendix/Product_Technical_Appendix.{md,docx}
       (a PDF only with --pdf: no PDF is made from any Word document by default, user decision 10 October 2026;
        --no-pdf is still accepted and does nothing)
Each product carries a "Fit by view" table: its score and indicative fit under the seven views
(05_Data/views.json, built by tools/build_views.py; Parts XIII-XVIII of the master document).
Assessment prose keeps claim tags (converted to footnote-style in Word/PDF, CP5-1); fact tables list
source IDs as plain text (resolve in 06_References/bibliography.xlsx).
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import E, PKG, fill
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tagfmt import load_index, convert_markdown

root = sys.argv[1]; os.chdir(root)
OUT = PKG + "/02_Appendix"; os.makedirs(OUT, exist_ok=True)
prods = json.load(open(PKG + "/05_Data/products.json", encoding="utf-8"))
VJ = json.load(open(PKG + "/05_Data/views.json", encoding="utf-8"))
VIEWS = VJ["views"]; VFIT = {r["id"]: r for r in VJ["products"]}
PARTS = {"FS": "Parts I–XII", "TS": "Part XIII", "SW": "Part XIV", "SU": "Part XV", "AT": "Part XVI", "DV": "Part XVII", "AG": "Part XVIII"}
ORDER = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]  # layer order L1 -> L9 (user decision, 9 Oct 2026)
NAMES = {"L9": "Evaluation and observability", "L8": "Data extraction, ingestion and web", "L7": "Embeddings and reranking",
         "L6": "Retrieval and knowledge stores", "L5": "Memory", "L4": "Tools, protocols and connectivity",
         "L3": "Agent frameworks and orchestration", "L2": "Inference, serving and model access", "L1": "Foundation models",
         "C1": "AI / LLM gateway", "C2": "Guardrails", "C3": "DLP and PII protection", "C4": "Identity and access for agents",
         "C5": "Prompt and configuration management", "C6": "AI FinOps", "C7": "AI security", "C8": "Model risk, governance and auditability"}
CRIT = [("technical", "Technical"), ("enterprise_readiness", "Enterprise readiness"), ("security_compliance", "Security and compliance"),
        ("deployment_flexibility", "Deployment flexibility"), ("ecosystem", "Ecosystem"), ("reliability_maturity", "Reliability and maturity"),
        ("cost_tco", "Cost / TCO"), ("lockin_portability", "Lock-in / portability")]
FIELDS = [("company", "Company"), ("category", "Category"), ("version_or_lineup", "Version / lineup"), ("licence_model", "Licence"),
          ("status_events", "Status events"), ("strategic_direction", "Strategic direction"), ("what_it_does", "What it does"),
          ("stack_position", "Stack position"), ("integration_model", "Integration"), ("dependencies", "Dependencies"),
          ("certifications", "Certifications"), ("gdpr_residency", "GDPR / residency"), ("security_features", "Security features"),
          ("access_controls", "Access controls"), ("enterprise_support", "Enterprise support"), ("pricing", "Pricing"),
          ("infra_cost_note", "Infrastructure cost"), ("ecosystem", "Ecosystem"), ("adoption_signals", "Adoption signals"), ("maturity", "Maturity")]

def cell(c):
    if not isinstance(c, dict) or "v" not in c:
        return ("", "", "")
    v = c["v"]; v = "; ".join(map(str, v)) if isinstance(v, list) else str(v)
    return (v.replace("|", "/").replace("\n", " "), c.get("label", ""), ", ".join(c.get("src") or []))

def name(p):
    c = p.get("current_name"); return c["v"] if isinstance(c, dict) else p["id"]

ncore = {v["id"]: sum(1 for r in VJ["products"] if r["fit"][v["id"]] == "Core candidate") for v in VIEWS}
md = ["---\ntitle: \"Product Technical Appendix\"\nsubtitle: \"The Enterprise GenAI Stack: {VIEW_LABEL_LC}\"\n---\n",
      "This review sets a new baseline for the enterprise GenAI stack, and this appendix holds its product record: %d products across nine stack layers (L1–L9) and eight enterprise controls (C1–C8), as {AS_AT} [AJ]. Each entry gives the current facts with their claim labels and source IDs (resolve in `06_References/bibliography.xlsx`), the assessment, the classification, the scorecard (generic and regulated-FS weights) and the product's fit under each of the seven views. Fact cells marked *Not publicly verified* could not be confirmed from a public source and were never guessed. Disclosure: researched and drafted by an Anthropic model; Anthropic-related items were scored on the same rubric, an independent alternative is named beside each, and tiers set by the reader at checkpoints are noted in the relevant chapter.\n" % len(prods),
      "# The seven views\n",
      "The master document reads the stack through seven views. The regulated-financial-services view is the master (Parts I–XII); six further views follow as Parts XIII–XVIII. Every view uses the same facts and the same eight criterion scores; only the weights change, and each weight profile sums to 100 [AJ]. Each product entry below ends its scorecard with a **Fit by view** table: the product's re-weighted score (1–5) and its indicative fit under each view, computed by `tools/build_views.py` (full table in `05_Data/views.xlsx`) [AJ].\n",
      "| View | Reader | Part | Tech. | Ent. | Sec. | Dep. | Eco. | Mat. | Cost | Lock-in | Core candidates |\n|---|------------|---|" + "--:|" * len(CRIT) + "--:|"]
for v in VIEWS:
    mx = max(v["weights"].values())
    md.append("| %s | %s | %s | %s | %d of %d |" % (v["id"], v["name"], PARTS.get(v["id"], ""),
              " | ".join(("**%d**" if v["weights"][k] == mx else "%d") % v["weights"][k] for k, _ in CRIT), ncore[v["id"]], len(VJ["products"])))
md += ["", "*Weights in per cent; the highest weight in each view is in bold. Columns: technical; enterprise readiness; security and compliance; deployment flexibility; ecosystem; reliability and maturity; cost / TCO; lock-in / portability.*\n",
       "**Who each view is for [AJ].**\n"] + ["- **%s, %s (%s).** %s" % (v["id"], v["name"].replace(" (the master view)", ""), ("master view, " if v["id"] == "FS" else "") + PARTS.get(v["id"], ""), v["profile"]) for v in VIEWS] + ["",
       "**How to read the fit.** %s The tier in each entry remains the master (regulated-FS) tier, with its conditions [AJ].\n" % VJ["fit_rules"]["rule"],
       "**Where to read more.** Part XIII (technology service provider), Part XIV (software product company), Part XV (start-up), Part XVI (start-ups selling AI tools into the enterprise stack), Part XVII (start-ups selling agentic SDLC tools) and Part XVIII (start-ups selling agents to enterprises) of the master document give each view's findings, architecture, reference stack and worked example. A view's weights never change a fact in this appendix [AJ].\n"]
for L in ORDER:
    group = [p for p in prods if p.get("layer") == L]
    if not group: continue
    md.append("# %s: %s\n" % (L, NAMES[L]))
    for p in sorted(group, key=lambda x: -((x.get("scores") or {}).get("fs_total") or 0)):
        cl = p.get("classification") or {}; sc = p.get("scores") or {}; a = p.get("assessment") or {}
        md.append("## %s (`%s`)\n" % (name(p), p["id"]))
        tier = cl.get("tier") or "Not scored"
        flags = ", ".join(cl.get("flags") or []) or "none"
        md.append("**Tier:** %s · **Flags:** %s\n" % (tier, flags))
        if cl.get("rationale"): md.append("*Rationale:* %s\n" % cl["rationale"])
        if sc.get("criteria"):
            md.append("| Criterion | Score | Rationale |\n|--------|--:|------------------------------|")
            for k, lab in CRIT:
                md.append("| %s | %s | %s |" % (lab, sc["criteria"].get(k, ""), (sc.get("rationale") or {}).get(k, "").replace("|", "/").replace("\n", " ")))
            md.append("| **Total (generic / FS)** | **%.2f / %.2f** | |\n" % (sc.get("generic_total") or 0, sc.get("fs_total") or 0))
            caps = sc.get("evidence_caps_applied") or []
            if caps: md.append("*Evidence rules applied:* " + "; ".join(caps) + "\n")
        vf = VFIT.get(p["id"])
        if vf:
            md.append("**Fit by view** (re-weighted score; core candidate or situational; see *The seven views*)\n")
            md.append("| View | " + " | ".join(v["id"] for v in VIEWS) + " |\n|------|" + "--:|" * len(VIEWS))
            md.append("| Score | " + " | ".join("%.2f" % vf["scores"][v["id"]] for v in VIEWS) + " |")
            md.append("| Fit | " + " | ".join("**Core**" if vf["fit"][v["id"]] == "Core candidate" else "Situational" for v in VIEWS) + " |\n")
        elif not sc.get("criteria"):
            md.append("*Fit by view:* not scored, so no view fit.\n")
        if a:
            if a.get("capabilities"): md.append("**Capabilities.** " + a["capabilities"] + "\n")
            for key, lab in [("strengths", "Strengths"), ("limitations_risks", "Limitations and risks"), ("choose_when", "Choose when"), ("avoid_when", "Avoid when")]:
                items = a.get(key) or []
                if items:
                    md.append("**%s**\n\n" % lab + "\n".join("- " + str(i) for i in items) + "\n")
            if a.get("competitors"): md.append("**Nearest competitors:** " + ", ".join(map(str, a["competitors"])) + "\n")
            if a.get("fs_note"): md.append("**Regulated-FS note.** " + a["fs_note"] + "\n")
        md.append("**Facts (as of %s)**\n\n| Field | Value | Label | Sources |\n|---------|--------------------------|--------|-----|" % (p.get("last_verified") or E["month_year"]))
        for k, lab in FIELDS:
            v, l, s = cell(p.get(k))
            if v: md.append("| %s | %s | %s | %s |" % (lab, v[:600], l, s))
        dep = p.get("deployment") or {}
        if isinstance(dep, dict):
            dv = "; ".join("%s: %s" % (k, cell(v)[0]) for k, v in dep.items() if cell(v)[0])
            if dv: md.append("| Deployment | %s | | |" % dv)
        md.append("")
full = fill("\n".join(md))
open(os.path.join(OUT, "Product_Technical_Appendix.md"), "w", encoding="utf-8").write(full)
src, regs, pr = load_index(".")
conv = convert_markdown(full, src, regs, pr)
open("work/stageD/appendix.pandoc.md", "w", encoding="utf-8").write(conv)
r = subprocess.run(["pandoc", "work/stageD/appendix.pandoc.md", "-f", "markdown+pipe_tables+bracketed_spans+footnotes-implicit_figures-tex_math_dollars-raw_tex-tex_math_single_backslash",
                    "-o", os.path.join(OUT, "Product_Technical_Appendix.docx"), "--toc", "--toc-depth=2", "--reference-doc=tools/templates/reference.docx"],
                   capture_output=True, text=True)
print("pandoc", r.returncode, r.stderr[-300:])
if "--pdf" in sys.argv and r.returncode == 0:
    r2 = subprocess.run([sys.executable, "-I", "tools/docx2pdf.py", os.path.join(OUT, "Product_Technical_Appendix.docx"), os.path.join(OUT, "Product_Technical_Appendix.pdf")],
                        capture_output=True, text=True, timeout=3600)
    print("pdf", r2.returncode, (r2.stdout + r2.stderr)[-300:])
print(len(full.split()), "words")
