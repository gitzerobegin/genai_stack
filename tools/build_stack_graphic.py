#!/usr/bin/env python3
"""Build the enterprise GenAI stack graphic from its editable Markdown source.

Source:  Enterprise_GenAI_Stack_Oct2026/08_Graphic/Enterprise_GenAI_Stack_Oct2026.md   (edit this)
Output:  the .html next to it (also hand-editable), then render PNG and PDF with
         NODE_PATH=$(npm root -g) node tools/render_graphic.js <html> <out_basename>

Usage:   python3 -I tools/build_stack_graphic.py <repo_root> [--sync] [--md PATH]
  --sync  first update every Tier in the Markdown from 05_Data/products.json, and append any scored product that
          is missing to its layer table (label taken from the dataset, note left blank). Rows whose ID is not in
          the dataset are reported. Then build the HTML as usual.

Markdown format (see the file itself):
  # Title
  - key: value              header settings (subtitle, stats, legend-*); {N} {S} {T} {E} are counted from the tables
  ## <Plane name>           - style: control | eval | plane     - subtitle: ...
  ### <CODE> · <Name>       - duty: ...   - design: ...   then a table | ID | Product | Note | Cloud | Tier |
  ## Footer: <Box title>    free text and bullets; **bold** allowed
  ## Source                 one line under the graphic
"""
import html, json, os, re, sys

root = sys.argv[1]; os.chdir(root)
PKG = "Enterprise_GenAI_Stack_Oct2026"
MD = sys.argv[sys.argv.index("--md") + 1] if "--md" in sys.argv else os.path.join(PKG, "08_Graphic", PKG + ".md")
OUT = os.path.splitext(MD)[0] + ".html"
TIERS = {"Strategic": "s", "Tactical": "t", "Experimental": "e", "Pattern": "p"}

def row_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def sync(path):
    prods = {p["id"]: p for p in json.load(open(PKG + "/05_Data/products.json", encoding="utf-8"))}
    lines = open(path, encoding="utf-8").read().split("\n")
    seen, changed, unknown, layer_end, cur = set(), 0, [], {}, None
    for i, ln in enumerate(lines):
        m = re.match(r"^###\s+([A-Z]\d)\b", ln)
        if m: cur = m.group(1)
        if ln.startswith("|") and not ln.startswith("| ID") and not ln.startswith("|---"):
            c = row_cells(ln)
            if len(c) < 5: continue
            layer_end[cur] = i
            pid = c[0]
            if pid == "-": continue
            p = prods.get(pid)
            if p is None: unknown.append(pid); continue
            seen.add(pid)
            t = (p.get("classification") or {}).get("tier") if p.get("scores") else "Not scored"
            if c[4] != t:
                c[4] = t; lines[i] = "| " + " | ".join(c) + " |"; changed += 1
    added = []
    for pid, p in sorted(prods.items(), key=lambda kv: kv[0], reverse=True):
        if pid in seen or not p.get("scores"): continue
        L = p.get("layer")
        if L not in layer_end:
            print("no table for layer", L, "- add a '### %s · ...' section for" % L, pid); continue
        nm = p.get("current_name"); nm = nm["v"] if isinstance(nm, dict) else pid
        nm = re.split(r"\s*[(;:,]\s*|\s+-\s+", str(nm))[0][:40]
        t = (p.get("classification") or {}).get("tier")
        lines.insert(layer_end[L] + 1, "| %s | %s |  |  | %s |" % (pid, nm, t))
        for k in layer_end:
            if layer_end[k] > layer_end[L]: layer_end[k] += 1
        layer_end[L] += 1; added.append(pid)
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("sync: %d tiers updated, %d products added %s, unknown IDs %s" % (changed, len(added), added, unknown))

def inline(t):
    t = html.escape(t)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)

def parse(path):
    doc = {"title": "", "meta": {}, "sections": []}
    sec = sub = None
    for raw in open(path, encoding="utf-8").read().split("\n"):
        ln = raw.rstrip()
        if ln.startswith("<!--") or not ln.strip():
            if ln.strip() and sec is not None and sec.get("kind") == "box": pass
            continue
        if ln.startswith("# "): doc["title"] = ln[2:].strip(); continue
        if ln.startswith("## "):
            name = ln[3:].strip()
            if name.startswith("Footer:"): sec = {"kind": "box", "title": name[7:].strip(), "body": []}
            elif name == "Source": sec = {"kind": "source", "body": []}
            else: sec = {"kind": "plane", "title": name, "meta": {}, "subs": []}
            doc["sections"].append(sec); sub = None; continue
        if ln.startswith("### "):
            m = re.match(r"^###\s+(\S+)\s*[·\-:]\s*(.+)$", ln)
            sub = {"code": m.group(1), "name": m.group(2).strip(), "meta": {}, "rows": []} if m else {"code": "", "name": ln[4:], "meta": {}, "rows": []}
            sec["subs"].append(sub); continue
        if sec is None:
            m = re.match(r"^-\s+([\w-]+):\s*(.*)$", ln)
            if m: doc["meta"][m.group(1)] = m.group(2)
            continue
        if sec["kind"] in ("box", "source"): sec["body"].append(ln); continue
        m = re.match(r"^-\s+([\w-]+):\s*(.*)$", ln)
        if m and (sub is None or not sub["rows"]):
            (sub["meta"] if sub else sec["meta"])[m.group(1)] = m.group(2); continue
        if ln.startswith("|") and sub is not None:
            c = row_cells(ln)
            if c[0] == "ID" or all(x and set(x) <= set("-: ") for x in c): continue  # header / separator row
            c += [""] * (5 - len(c)); sub["rows"].append(dict(id=c[0], label=c[1], note=c[2], cloud=c[3], tier=c[4]))
    return doc

def tile(r):
    cls = TIERS.get(r["tier"], "x")
    tags = ""
    if r["tier"] == "Pattern": tags = '<span class="tag pat">PATTERN · NOT SCORED</span>'
    if r["cloud"]: tags += '<span class="tag cloud">%s</span>' % html.escape(r["cloud"])
    return ('<div class="tile %s" title="%s"><div class="tags">%s</div><div class="nm">%s</div><div class="nt">%s</div></div>'
            % (cls, html.escape(r["id"]), tags, inline(r["label"]), inline(r["note"])))

def build(doc):
    rows = [r for s in doc["sections"] if s["kind"] == "plane" for sub in s["subs"] for r in sub["rows"]]
    cnt = {k: sum(1 for r in rows if r["tier"] == k) for k in ("Strategic", "Tactical", "Experimental")}
    fill = {"{N}": str(sum(cnt.values())), "{S}": str(cnt["Strategic"]), "{T}": str(cnt["Tactical"]), "{E}": str(cnt["Experimental"])}
    def f(t):
        for k, v in fill.items(): t = t.replace(k, v)
        return t
    M = doc["meta"]
    stats = "".join('<span class="stat">%s</span>' % inline(f(x.strip())) for x in M.get("stats", "").split(";") if x.strip())
    legend = ('<span><span class="sw s"></span>%s</span><span><span class="sw t"></span>%s</span><span><span class="sw e"></span>%s</span>'
              '<span><span class="tag cloud">AWS</span> %s</span>') % tuple(inline(M.get(k, "")) for k in
              ("legend-strategic", "legend-tactical", "legend-experimental", "legend-cloud"))
    body, foot, source = [], [], ""
    for s in doc["sections"]:
        if s["kind"] == "plane":
            style = s["meta"].get("style", "plane"); st = inline(s["meta"].get("subtitle", ""))
            if style == "control":
                cards = "".join('<div class="card"><div class="ch"><span class="code">%s</span> %s<span class="cs">%s</span></div><div class="grid g3">%s</div></div>'
                                % (html.escape(u["code"]), inline(u["name"]), inline(u["meta"].get("duty", "")), "".join(tile(r) for r in u["rows"])) for u in s["subs"])
                body.append('<div class="sec ctrl"><div class="sh"><span class="t1">%s</span><span class="t2">%s</span></div><div class="cards">%s</div></div>' % (inline(s["title"]), st, cards))
            else:
                lrows = "".join('<div class="row"><div class="lab"><div class="code">%s</div><div class="ln">%s</div><div class="duty">%s</div><div class="fix">%s</div></div><div class="grid">%s</div></div>'
                                % (html.escape(u["code"]), inline(u["name"]), inline(u["meta"].get("duty", "")), inline(u["meta"].get("design", "")), "".join(tile(r) for r in u["rows"])) for u in s["subs"])
                if style == "eval":
                    body.append('<div class="sec eval"><div class="sh"><span class="t1">%s</span><span class="t2">%s</span></div>%s</div>' % (inline(s["title"]), st, lrows))
                else:
                    body.append('<div class="plane"><div class="ph">%s</div>%s</div>' % (inline(s["title"]), lrows))
        elif s["kind"] == "box":
            paras, items = [], []
            for ln in s["body"]:
                (items if ln.startswith("- ") else paras).append(inline(ln[2:] if ln.startswith("- ") else ln))
            foot.append('<div class="box"><h3>%s</h3>%s%s</div>' % (inline(s["title"]), "".join('<p style="margin:0 0 8px">%s</p>' % p for p in paras),
                        "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items) if items else ""))
        elif s["kind"] == "source":
            source = " ".join(inline(x) for x in s["body"])
    title = inline(doc["title"])
    return ('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>%s</title>\n<!-- Generated from %s by tools/build_stack_graphic.py. '
            'You can edit this file directly, but the Markdown is the source: re-running the builder overwrites it. -->\n<style>%s</style></head>'
            '<body><div class="wrap">\n<h1>%s</h1>\n<div class="sub">%s</div>\n<div class="stats">%s</div>\n<div class="legend">%s</div>\n%s\n'
            '<div class="foot">%s</div>\n<div class="small">%s</div>\n</div></body></html>\n'
            % (title, os.path.basename(MD), CSS, title, inline(M.get("subtitle", "")), stats, legend, "\n".join(body), "".join(foot), source)), cnt

CSS = """
:root{--navy:#1B2A41;--teal:#0E7C7B;--teal2:#E6F3F2;--amber:#C9822B;--ink:#1F2933;--mute:#5B6B7A;--line:#D5DEE6;--bg:#F6F8FA}
*{box-sizing:border-box}body{margin:0;background:#fff;font-family:Inter,Arial,sans-serif;color:var(--ink);width:1600px}
.wrap{padding:36px 40px 28px}
h1{font-size:46px;letter-spacing:-.5px;margin:0;color:var(--navy);font-weight:800}
.sub{font-size:19px;color:var(--mute);margin-top:6px}
.stats{display:flex;gap:10px;margin:16px 0 12px;flex-wrap:wrap}
.stat{background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:15px}
.stat b{color:var(--navy)}
.legend{display:flex;gap:18px;align-items:center;font-size:14px;color:var(--mute);margin-bottom:18px;flex-wrap:wrap}
.sw{display:inline-block;width:26px;height:16px;border-radius:4px;vertical-align:-3px;margin-right:6px}
.sw.s{background:var(--teal)}.sw.t{background:#fff;border:2px solid var(--teal)}.sw.e{background:#fff;border:2px dashed var(--amber)}.sw.x{background:#EEF1F4;border:1px solid #C3CCD5}
.sec{border-radius:16px;padding:16px 18px 18px;margin-bottom:16px}
.ctrl{background:#EEF2F7;border:2px solid var(--navy)}
.sh{display:flex;align-items:baseline;gap:12px;margin-bottom:12px}
.sh .t1{font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:.5px}
.sh .t2{font-size:15px;color:var(--mute)}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px 12px}
.ch{font-weight:700;font-size:16px;color:var(--navy);margin-bottom:8px}
.ch .code{display:inline-block;background:var(--navy);color:#fff;border-radius:6px;padding:1px 7px;font-size:13px;margin-right:4px}
.cs{font-weight:400;color:var(--mute);font-size:13px;margin-left:8px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-content:start}
.grid.g3{grid-template-columns:repeat(3,1fr)}
.tile{border-radius:9px;padding:7px 9px 8px;min-height:62px;position:relative}
.tile .nm{font-weight:700;font-size:15px;line-height:1.15}
.tile .nt{font-size:12px;line-height:1.25;margin-top:2px}
.tile.s{background:var(--teal);color:#fff}.tile.s .nt{color:#DDF1EF}
.tile.t{background:#fff;border:2px solid var(--teal);color:var(--ink)}.tile.t .nt{color:var(--mute)}
.tile.e{background:#FFFBF4;border:2px dashed var(--amber);color:var(--ink)}.tile.e .nt{color:#8A5A1E}
.tile.x{background:#EEF1F4;border:1px solid #C3CCD5;color:#7D8B98}.tile.x .nm{text-decoration:line-through}
.tile.p{background:#fff;border:2px dotted #8795A3;color:var(--ink)}.tile.p .nt{color:var(--mute)}
.tags{display:flex;gap:4px;flex-wrap:wrap;min-height:0}
.tag{font-size:9.5px;font-weight:700;letter-spacing:.4px;border-radius:4px;padding:1px 5px;margin-bottom:3px}
.tile.s .tag{background:rgba(255,255,255,.18);color:#fff}
.tag.new{background:#E3ECF8;color:#1E4E8C}.tag.acq{background:#FBEBDD;color:#9A4E12}.tag.ren{background:#ECE6F6;color:#5B3E8E}
.tag.cloud{background:#E7F0EC;color:#245C46}.tag.pat{background:#EEF1F4;color:#4C5B69}
.tile.s .tag.cloud,.tile.s .tag.new,.tile.s .tag.acq,.tile.s .tag.ren{background:rgba(255,255,255,.2);color:#fff}
.eval{background:#F3F0FA;border:2px solid #5B4B9A}
.eval .sh .t1{color:#3F3378}
.plane{background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:12px 16px 6px;margin-bottom:14px}
.ph{font-size:20px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:.5px;margin:2px 0 10px}
.row{display:grid;grid-template-columns:300px 1fr;gap:14px;padding:10px 0;border-top:1px solid var(--line)}
.ph + .row{border-top:0}
.lab .code{display:inline-block;background:var(--navy);color:#fff;font-weight:800;border-radius:6px;padding:2px 8px;font-size:14px}
.lab .ln{font-size:19px;font-weight:800;color:var(--navy);margin-top:5px;line-height:1.15}
.lab .was{font-size:12.5px;color:var(--mute);margin-top:3px;font-style:italic}
.lab .duty{font-size:13px;color:var(--teal);font-weight:600;margin-top:5px}
.lab .fix{font-size:12px;color:var(--ink);margin-top:6px;line-height:1.3;border-left:3px solid var(--amber);padding-left:7px}
.eval .row{border-top:0;padding:0}
.foot{display:grid;grid-template-columns:1.25fr 1fr;gap:14px;margin-top:4px}
.box{border:1px solid var(--line);border-radius:12px;padding:12px 16px;font-size:13.5px;line-height:1.45;background:#fff}
.box h3{margin:0 0 6px;font-size:16px;color:var(--navy)}
.box ul{margin:0;padding-left:18px}
.small{font-size:12px;color:var(--mute);margin-top:12px}"""

if "--sync" in sys.argv: sync(MD)
page, cnt = build(parse(MD))
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, "tiles", sum(cnt.values()), cnt)
