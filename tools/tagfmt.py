#!/usr/bin/env python3
"""Shared helpers: load the source/record index and convert claim tags for Word/PDF export.

Inline tags in the Markdown drafts:
  [VF: A1-S023, A1-S024]  verified fact      [R: A2-S010]  reported
  [AJ] architectural judgement   [Rec] recommendation   [NPV] not publicly verified
For the Word/PDF edition (CP5-1 decision) these become:
  - VF/R  -> a small grey label + a pandoc footnote listing each source (title, publisher, URL, access date)
  - AJ/Rec/NPV -> a small grey label only (custom-style "Claim Label")
Fenced code blocks (diagrams) are left untouched.
"""
import csv, glob, json, os, re

def load_index(root):
    src = {}
    pats = ["work/stageA/*/sources.csv", "work/stageA_verify/*/sources.csv", "work/stageB/*/sources_added*.csv",
            "work/stageC*/sources_added*.csv", "work/gapfill/*/sources*.csv"]
    for pat in pats:
        for p in glob.glob(os.path.join(root, pat)):
            with open(p, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    r = {k.strip(): (v or "").strip() for k, v in r.items() if k}
                    if r.get("id"):
                        src[r["id"]] = r
    regs, prods = {}, {}
    rp = os.path.join(root, "Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json")
    if os.path.exists(rp):
        for r in json.load(open(rp, encoding="utf-8")):
            v = r.get("instrument", {})
            regs[r["id"]] = v.get("v") if isinstance(v, dict) else str(v)
    pp = os.path.join(root, "Enterprise_GenAI_Stack_Oct2026/05_Data/products.json")
    if os.path.exists(pp):
        for p in json.load(open(pp, encoding="utf-8")):
            v = p.get("current_name", {})
            prods[p["id"]] = v.get("v") if isinstance(v, dict) else str(v)
    return src, regs, prods

def _esc(s):
    return s.replace("[", "(").replace("]", ")").replace("^", "").replace("\n", " ")

def describe(tok, src, regs, prods):
    tok = tok.strip()
    if tok in src:
        r = src[tok]
        title = r.get("title") or r.get("publisher") or ""
        bits = [tok + ":", _esc(title)[:160]]
        if r.get("publisher") and r.get("publisher") not in title:
            bits.append("(" + _esc(r["publisher"])[:60] + ")")
        if r.get("url"):
            bits.append("<" + r["url"] + ">")
        if r.get("accessed"):
            bits.append("accessed " + r["accessed"])
        if (r.get("access_status") or "").startswith("extract"):
            bits.append("[search-tool extract]")
        return " ".join(b for b in bits if b)
    if tok in regs:
        return "%s: %s (see regulatory_facts.json)" % (tok, _esc(regs[tok] or ""))
    if tok in prods:
        return "%s: product record %s (see products.json)" % (tok, _esc(prods[tok] or ""))
    return tok

TAG = re.compile(r"\[(VF|R)\s*:\s*([^\]\[]+)\]")
SIMPLE = re.compile(r"\[(AJ|Rec|NPV)\]")
LABEL = {"VF": "VF", "R": "R", "AJ": "AJ", "Rec": "Rec", "NPV": "NPV"}

def convert_line(line, src, regs, prods):
    def tag(m):
        kind, body = m.group(1), m.group(2)
        toks = [t for t in re.split(r"[,;]\s*", body) if t.strip()]
        note = "; ".join(describe(t, src, regs, prods) for t in toks)
        return '[%s]{custom-style="Claim Label"}^[%s — %s]' % (LABEL[kind], "Verified fact" if kind == "VF" else "Reported", note)
    parts = re.split(r"(`[^`]*`)", line)  # never convert tags quoted inside inline code
    for i in range(0, len(parts), 2):
        parts[i] = TAG.sub(tag, parts[i])
        parts[i] = SIMPLE.sub(lambda m: '[%s]{custom-style="Claim Label"}' % m.group(1), parts[i])
    return "".join(parts)

def convert_markdown(text, src, regs, prods):
    out, in_code = [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line); continue
        out.append(line if in_code else convert_line(line, src, regs, prods))
    return "\n".join(out)
