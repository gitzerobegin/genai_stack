#!/usr/bin/env python3
"""Check claim tags in Stage B sections: every [VF: ...]/[R: ...] source id must exist in the bibliography sources;
report tag counts, untagged-paragraph ratio, and style-guide banned words / American spellings.
Usage: python3 -I tools/check_tags.py <repo_root> work/stageB/L9/section.md [...]
"""
import csv, glob, json, os, re, sys
root = sys.argv[1]; os.chdir(root)
ids = set()
for p in glob.glob("work/stageA/*/sources.csv") + glob.glob("work/stageA_verify/*/sources.csv") + glob.glob("work/stageB/*/sources_added*.csv"):
    for r in csv.DictReader(open(p, encoding="utf-8")):
        if r.get("id"): ids.add(r["id"].strip())
regs = {r["id"] for r in json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json"))}
prods = {r["id"] for r in json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/products.json"))}
BANNED = ["revolutionary", "game-changing", "game changing", "cutting-edge", "seamless", "leverage ", "leverages", "it's important to note"]
US = [r"\boptimiz", r"\borganiz", r"\banalyz", r"\bbehavior", r"\bcenter\b", r"\bmodeling\b", r"\bcatalog\b", r"\bdefense\b", r"\blicense\b(?! (key|file))", r"\butiliz", r"\bprioritiz", r"\bstandardiz"]
for f in sys.argv[2:]:
    t = open(f, encoding="utf-8").read()
    tags = re.findall(r"\[(VF|R)\s*:\s*([^\]]+)\]", t)
    bad = []
    for kind, body in tags:
        for tok in re.split(r"[,;]\s*", body):
            tok = tok.strip()
            if not tok: continue
            if tok in ids or tok in regs or tok in prods: continue
            bad.append(tok)
    counts = {k: len(re.findall(r"\[%s[\]:]" % k, t)) for k in ["VF", "R", "AJ", "Rec", "NPV"]}
    paras = [p for p in re.split(r"\n\s*\n", t) if p.strip() and not p.strip().startswith(("#", "|", "```", ">")) and len(p.split()) > 25]
    untagged = [p for p in paras if not re.search(r"\[(VF|R|AJ|Rec|NPV)", p)]
    ban = [w for w in BANNED if w in t.lower()]
    us = sorted({m.group(0) for pat in US for m in re.finditer(pat, t, re.I)})
    print(json.dumps({"file": f, "words": len(t.split()), "tags": counts, "unknown_source_ids": sorted(set(bad))[:40],
                      "long_untagged_paragraphs": len(untagged), "banned_words": ban, "american_spellings": us}))
