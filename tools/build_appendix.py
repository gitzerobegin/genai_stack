#!/usr/bin/env python3
"""Build the Product Technical Appendix from the dataset (one entry per product record).

Usage: python3 -I tools/build_appendix.py <repo_root> [--no-pdf]
Writes Enterprise_GenAI_Stack_Oct2026/02_Appendix/Product_Technical_Appendix.{md,docx,pdf}
Assessment prose keeps claim tags (converted to footnote-style in Word/PDF, CP5-1); fact tables list
source IDs as plain text (resolve in 06_References/bibliography.xlsx).
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tagfmt import load_index, convert_markdown

root = sys.argv[1]; os.chdir(root)
OUT = "Enterprise_GenAI_Stack_Oct2026/02_Appendix"; os.makedirs(OUT, exist_ok=True)
prods = json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/products.json", encoding="utf-8"))
ORDER = ["L9", "L8", "L7", "L6", "L5", "L4", "L3", "L2", "L1", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
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

md = ["---\ntitle: \"Product Technical Appendix\"\nsubtitle: \"Enterprise GenAI Full-Stack Architecture, October 2026\"\n---\n",
      "This appendix holds the full record for every product assessed: current facts with their claim labels and source IDs (resolve in `06_References/bibliography.xlsx`), the assessment, the classification and the scorecard (generic and regulated-FS weights). Fact cells marked *Not publicly verified* could not be confirmed from a public source and were never guessed. Disclosure: researched and drafted by an Anthropic model; Anthropic-related items were scored on the same rubric, and tiers set by the reader at checkpoints are noted in the relevant chapter.\n"]
for L in ORDER:
    group = [p for p in prods if p.get("layer") == L]
    if not group: continue
    md.append("# %s: %s\n" % (L, NAMES[L]))
    for p in sorted(group, key=lambda x: -((x.get("scores") or {}).get("fs_total") or 0)):
        cl = p.get("classification") or {}; sc = p.get("scores") or {}; a = p.get("assessment") or {}
        md.append("## %s (`%s`)\n" % (name(p), p["id"]))
        tier = cl.get("tier") or "Not scored"
        flags = ", ".join(cl.get("flags") or []) or "none"
        md.append("**Tier:** %s · **Flags:** %s · **Original graphic label:** %s\n" % (tier, flags, p.get("original_label") or "not in graphic"))
        if cl.get("rationale"): md.append("*Rationale:* %s\n" % cl["rationale"])
        if sc.get("criteria"):
            md.append("| Criterion | Score | Rationale |\n|--------|--:|------------------------------|")
            for k, lab in CRIT:
                md.append("| %s | %s | %s |" % (lab, sc["criteria"].get(k, ""), (sc.get("rationale") or {}).get(k, "").replace("|", "/").replace("\n", " ")))
            md.append("| **Total (generic / FS)** | **%.2f / %.2f** | |\n" % (sc.get("generic_total") or 0, sc.get("fs_total") or 0))
            caps = sc.get("evidence_caps_applied") or []
            if caps: md.append("*Evidence rules applied:* " + "; ".join(caps) + "\n")
        if a:
            if a.get("capabilities"): md.append("**Capabilities.** " + a["capabilities"] + "\n")
            for key, lab in [("strengths", "Strengths"), ("limitations_risks", "Limitations and risks"), ("choose_when", "Choose when"), ("avoid_when", "Avoid when")]:
                items = a.get(key) or []
                if items:
                    md.append("**%s**\n\n" % lab + "\n".join("- " + str(i) for i in items) + "\n")
            if a.get("competitors"): md.append("**Nearest competitors:** " + ", ".join(map(str, a["competitors"])) + "\n")
            if a.get("fs_note"): md.append("**Regulated-FS note.** " + a["fs_note"] + "\n")
        md.append("**Facts (as of %s)**\n\n| Field | Value | Label | Sources |\n|-------|------------------------------|----|-----|" % (p.get("last_verified") or "October 2026"))
        for k, lab in FIELDS:
            v, l, s = cell(p.get(k))
            if v: md.append("| %s | %s | %s | %s |" % (lab, v[:600], l, s))
        dep = p.get("deployment") or {}
        if isinstance(dep, dict):
            dv = "; ".join("%s: %s" % (k, cell(v)[0]) for k, v in dep.items() if cell(v)[0])
            if dv: md.append("| Deployment | %s | | |" % dv)
        md.append("")
full = "\n".join(md)
open(os.path.join(OUT, "Product_Technical_Appendix.md"), "w", encoding="utf-8").write(full)
src, regs, pr = load_index(".")
conv = convert_markdown(full, src, regs, pr)
open("work/stageD/appendix.pandoc.md", "w", encoding="utf-8").write(conv)
r = subprocess.run(["pandoc", "work/stageD/appendix.pandoc.md", "-f", "markdown+pipe_tables+bracketed_spans+footnotes-implicit_figures-tex_math_dollars-raw_tex-tex_math_single_backslash",
                    "-o", os.path.join(OUT, "Product_Technical_Appendix.docx"), "--toc", "--toc-depth=2", "--reference-doc=tools/templates/reference.docx"],
                   capture_output=True, text=True)
print("pandoc", r.returncode, r.stderr[-300:])
if "--no-pdf" not in sys.argv and r.returncode == 0:
    r2 = subprocess.run([sys.executable, "-I", "tools/docx2pdf.py", os.path.join(OUT, "Product_Technical_Appendix.docx"), os.path.join(OUT, "Product_Technical_Appendix.pdf")],
                        capture_output=True, text=True, timeout=3600)
    print("pdf", r2.returncode, (r2.stdout + r2.stderr)[-300:])
print(len(full.split()), "words")
