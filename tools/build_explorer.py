#!/usr/bin/env python3
"""Build the offline interactive explorer (single self-contained HTML file, CP5-3).

Usage: python3 -I tools/build_explorer.py <repo_root>
Writes Enterprise_GenAI_Stack_Oct2026/04_Explorer/explorer.html
Data: 05_Data/products.json (+ synthesis Parts for the worked example / hypotheses / stacks, rendered with pandoc).
"""
import html, json, os, re, subprocess, sys
root = sys.argv[1]; os.chdir(root)
OUT = "Enterprise_GenAI_Stack_Oct2026/04_Explorer"; os.makedirs(OUT, exist_ok=True)
prods = json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/products.json", encoding="utf-8"))
NAMES = {"L9": "Evaluation & observability", "L8": "Data extraction & ingestion", "L7": "Embeddings & reranking",
         "L6": "Retrieval & knowledge stores", "L5": "Memory", "L4": "Tools, protocols & connectivity",
         "L3": "Agent frameworks & orchestration", "L2": "Inference, serving & model access", "L1": "Foundation models",
         "C1": "AI / LLM gateway", "C2": "Guardrails", "C3": "DLP & PII", "C4": "Identity & access for agents",
         "C5": "Prompt & config management", "C6": "AI FinOps", "C7": "AI security", "C8": "Model risk, governance & audit"}
NAMES = {k: NAMES[k] for k in ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]}  # L1 -> L9
TAG = re.compile(r"\s*\[(VF|R)\s*:\s*[^\]\[]+\]|\s*\[(AJ|Rec|NPV)\]")
def clean(s):
    return TAG.sub(lambda m: " ⟨%s⟩" % (m.group(1) or m.group(2)), str(s or "")).strip()
def v(c):
    if isinstance(c, dict) and "v" in c:
        x = c["v"]; return clean("; ".join(map(str, x)) if isinstance(x, list) else x)
    return ""
rows = []
for p in prods:
    cl = p.get("classification") or {}; sc = p.get("scores") or {}; a = p.get("assessment") or {}
    dep = p.get("deployment") or {}
    rows.append({
        "id": p["id"], "layer": p["layer"], "name": v(p.get("current_name")) or p["id"], "short": re.split(r"\s*[(;:,]\s*|\s+-\s+", v(p.get("current_name")) or p["id"])[0][:48], "company": v(p.get("company")),
        "tier": cl.get("tier") or "Not scored", "flags": cl.get("flags") or [],
        "rationale": clean(cl.get("rationale")), "scores": sc.get("criteria") or {}, "fs": sc.get("fs_total"), "gen": sc.get("generic_total"),
        "caps": [clean(x) for x in (sc.get("evidence_caps_applied") or [])],
        "licence": v(p.get("licence_model")), "version": v(p.get("version_or_lineup")), "status": v(p.get("status_events")),
        "certs": v(p.get("certifications")), "resid": v(p.get("gdpr_residency")), "access": v(p.get("access_controls")),
        "pricing": v(p.get("pricing")), "what": v(p.get("what_it_does")),
        "deploy": {k: v(x) for k, x in dep.items()} if isinstance(dep, dict) else {},
        "strengths": [clean(x) for x in a.get("strengths") or []], "limits": [clean(x) for x in a.get("limitations_risks") or []],
        "choose": [clean(x) for x in a.get("choose_when") or []], "avoid": [clean(x) for x in a.get("avoid_when") or []],
        "comp": [str(x) for x in a.get("competitors") or []], "fsnote": clean(a.get("fs_note")),
    })

def part(pattern):
    syn = "work/stageC/synthesis.md"
    if not os.path.exists(syn): return "<p><em>Synthesis not yet available.</em></p>"
    parts = re.split(r"(?m)^(?=# )", open(syn, encoding="utf-8").read())
    hit = next((x for x in parts if re.match(r"# .*" + pattern, x, re.I)), "")
    if not hit: return "<p><em>Section not found.</em></p>"
    hit = TAG.sub(lambda m: " ⟨%s⟩" % (m.group(1) or m.group(2)), hit)
    r = subprocess.run(["pandoc", "-f", "markdown-tex_math_dollars-raw_tex", "-t", "html"], input=hit, capture_output=True, text=True)
    return r.stdout
extras = {"trace": part("Worked example"), "hyp": part("hypothes"), "stacks": part("reference stacks"), "final": part("Final recommended")}

# ---- Seven views (Stage E, Parts XIII-XVIII): re-weighted scores and fit from 05_Data/views.json (tools/build_views.py)
VJ = json.load(open("Enterprise_GenAI_Stack_Oct2026/05_Data/views.json", encoding="utf-8"))
PARTS = {"FS": "Parts I–XII", "TS": "Part XIII", "SW": "Part XIV", "SU": "Part XV", "AT": "Part XVI", "DV": "Part XVII", "AG": "Part XVIII"}
def view_part(vid):
    f = "work/stageE/views/%s/view.md" % vid
    if not os.path.exists(f): return "<p><em>Part not yet available.</em></p>"
    t = TAG.sub(lambda m: " ⟨%s⟩" % (m.group(1) or m.group(2)), open(f, encoding="utf-8").read())
    return subprocess.run(["pandoc", "-f", "markdown-tex_math_dollars-raw_tex", "-t", "html", "--shift-heading-level-by=1"], input=t, capture_output=True, text=True).stdout
VIEWS = [{"id": v["id"], "name": v["name"], "short": v["short"], "weights": v["weights"], "profile": v.get("profile", ""),
          "why": v.get("why_weights", ""), "part": PARTS.get(v["id"], ""), "core": sum(1 for r in VJ["products"] if r["fit"][v["id"]] == "Core candidate"),
          "html": "" if v["id"] == "FS" else view_part(v["id"])} for v in VJ["views"]]
VFIT = {r["id"]: {"s": r["scores"], "f": {k: (1 if x == "Core candidate" else 0) for k, x in r["fit"].items()}, "r": r["rank"]} for r in VJ["products"]}
for r in rows:
    if r["id"] in VFIT: r["v"] = VFIT[r["id"]]
VMETA = {"scored": len(VJ["products"]), "rule": VJ["fit_rules"]["rule"], "th": VJ["fit_rules"]["core_threshold"]}

TEMPLATE = r"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GenAI Stack Explorer</title>
<style>
:root{--bg:#F7F5F0;--panel:#fff;--ink:#0B1B33;--muted:#5B6B7A;--line:#E3E1DA;--accent:#0B1B33;--strat:#2E6DA4;--tact:#5B6B7A;--exp:#B07A1A;--ns:#888;--chip:#EEF3F8;--gold:#D4A13A}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#11151c;--panel:#1a2029;--ink:#e6e9ef;--muted:#9aa3b2;--line:#2a313c;--accent:#8fb3ff;--strat:#4fc98a;--tact:#e0b04a;--exp:#d58bd9;--chip:#232a35}}
:root[data-theme=dark]{--bg:#11151c;--panel:#1a2029;--ink:#e6e9ef;--muted:#9aa3b2;--line:#2a313c;--accent:#8fb3ff;--strat:#4fc98a;--tact:#e0b04a;--exp:#d58bd9;--chip:#232a35}
*{box-sizing:border-box}body{margin:0;font:14px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:14px 16px;border-bottom:1px solid var(--line);background:var(--panel);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
h1{font-size:17px;margin:0;color:var(--accent)}.sub{color:var(--muted);font-size:12px}
nav.tabs{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}nav.tabs button{border:1px solid var(--line);background:var(--chip);color:var(--ink);padding:6px 10px;border-radius:6px;cursor:pointer}
nav.tabs button.on{background:var(--accent);color:var(--panel);border-color:var(--accent)}
main{display:grid;grid-template-columns:260px 1fr;gap:0;min-height:calc(100vh - 60px)}
aside{border-right:1px solid var(--line);background:var(--panel);padding:10px;overflow:auto;max-height:calc(100vh - 60px);position:sticky;top:0}
aside .grp{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:10px 6px 4px}
aside button{display:block;width:100%;text-align:left;border:0;background:none;color:var(--ink);padding:6px 8px;border-radius:6px;cursor:pointer;font-size:13px}
aside button.on{background:var(--chip);font-weight:600}aside button small{color:var(--muted)}
section.view{padding:16px;max-width:1200px}.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
.filters select,.filters input{background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:6px 8px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px;cursor:pointer}
.card h3{margin:0 0 4px;font-size:15px}.meta{color:var(--muted);font-size:12px}
.tier{display:inline-block;font-size:11px;font-weight:700;padding:1px 7px;border-radius:10px;color:#fff}
.Strategic{background:var(--strat)}.Tactical{background:var(--tact)}.Experimental{background:var(--exp)}.Not.scored,.Not{background:var(--ns)}
.chip{display:inline-block;background:var(--chip);border-radius:10px;padding:0 7px;font-size:11px;margin:2px 3px 0 0}
.bar{height:6px;background:var(--chip);border-radius:3px;overflow:hidden;margin-top:6px}.bar i{display:block;height:100%;background:var(--accent)}
.detail{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px;margin-top:12px}
table{border-collapse:collapse;width:100%;margin:8px 0}td,th{border-bottom:1px solid var(--line);padding:5px 6px;text-align:left;vertical-align:top;font-size:13px}
th{color:var(--muted);font-weight:600}.num{text-align:right;font-variant-numeric:tabular-nums}
.cmp{margin:0 0 0 auto}.cmpbox{position:sticky;bottom:0;background:var(--panel);border-top:1px solid var(--line);padding:8px 16px;display:none}
label.ck{font-size:12px;color:var(--muted);float:right}.prose{max-width:900px}.prose pre{white-space:pre-wrap;background:var(--chip);padding:10px;border-radius:8px;font-size:12px}
.note{color:var(--muted);font-size:12px}
@media (max-width:760px){main{grid-template-columns:1fr}aside{position:static;max-height:none;border-right:0;border-bottom:1px solid var(--line)}section.view{padding:16px}}
</style></head><body>
<header><picture><source srcset="__LOCKUPW__" media="(prefers-color-scheme: dark)"><img src="__LOCKUP__" alt="Veyan" style="height:40px"></picture><div><h1>The Enterprise GenAI Stack Explorer</h1><div class="sub">The view at end of Q3 2026 · __N__ products · scores 1–5 (generic / regulated-FS weights) · ⟨VF⟩ verified ⟨R⟩ reported ⟨AJ⟩ judgement ⟨Rec⟩ recommendation ⟨NPV⟩ not publicly verified</div></div>
<nav class="tabs"><button data-t="products" class="on">Products</button><button data-t="compare">Compare</button><button data-t="trace">Worked example</button><button data-t="hyp">Hypotheses</button><button data-t="stacks">Reference stacks</button><button data-t="final">Final stack</button><button id="theme" title="Toggle theme">◐</button></nav></header>
<main><aside id="nav"></aside><section class="view" id="view"></section></main>
<div class="cmpbox" id="cmpbox"></div>
<script>
const D=__DATA__, X=__EXTRAS__, N=__NAMES__;
const C=[["technical","Technical"],["enterprise_readiness","Enterprise"],["security_compliance","Security"],["deployment_flexibility","Deployment"],["ecosystem","Ecosystem"],["reliability_maturity","Maturity"],["cost_tco","Cost/TCO"],["lockin_portability","Lock-in"]];
let st={tab:"products",layer:"all",tier:"all",q:"",dep:"all",sel:null,cmp:[]};
try{const s=JSON.parse(localStorage.getItem("gx")||"{}");Object.assign(st,{cmp:s.cmp||[]})}catch(e){}
const save=()=>{try{localStorage.setItem("gx",JSON.stringify({cmp:st.cmp}))}catch(e){}};
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const tierCls=t=>t.replace(" ",".");
function nav(){const L=Object.keys(N);let h='<button data-l="all" class="'+(st.layer=="all"?"on":"")+'">All layers &amp; controls <small>('+D.length+')</small></button>';
 h+='<div class="grp">Stack layers (L1 → L9)</div>';for(const k of L.filter(x=>x[0]=="L")){const n=D.filter(p=>p.layer==k).length;h+=`<button data-l="${k}" class="${st.layer==k?"on":""}">${k} ${esc(N[k])} <small>(${n})</small></button>`}
 h+='<div class="grp">Enterprise controls</div>';for(const k of L.filter(x=>x[0]=="C")){const n=D.filter(p=>p.layer==k).length;h+=`<button data-l="${k}" class="${st.layer==k?"on":""}">${k} ${esc(N[k])} <small>(${n})</small></button>`}
 document.getElementById("nav").innerHTML=h;document.querySelectorAll("#nav button").forEach(b=>b.onclick=()=>{st.layer=b.dataset.l;st.sel=null;st.tab="products";render()})}
function list(){let r=D.filter(p=>(st.layer=="all"||p.layer==st.layer)&&(st.tier=="all"||p.tier==st.tier)&&(st.dep=="all"||/^Yes/i.test((p.deploy||{})[st.dep]||""))&&(!st.q||JSON.stringify(p).toLowerCase().includes(st.q.toLowerCase())));
 r.sort((a,b)=>(b.fs||0)-(a.fs||0));return r}
function card(p){const ck=st.cmp.includes(p.id)?"checked":"";return `<div class="card" data-id="${p.id}"><label class="ck" onclick="event.stopPropagation()"><input type="checkbox" data-c="${p.id}" ${ck}> compare</label>
 <h3 title="${esc(p.name)}">${esc(p.short)}</h3><div class="meta">${p.layer} · ${esc(p.company).slice(0,60)}</div>
 <div style="margin-top:6px"><span class="tier ${tierCls(p.tier)}">${esc(p.tier)}</span> ${p.flags.map(f=>`<span class="chip">${esc(f)}</span>`).join("")}</div>
 ${p.fs!=null?`<div class="meta" style="margin-top:6px">FS ${p.fs.toFixed(2)} · generic ${p.gen.toFixed(2)}</div><div class="bar"><i style="width:${(p.fs/5*100).toFixed(0)}%"></i></div>`:'<div class="meta">Not scored</div>'}</div>`}
function detail(p){const sc=C.map(([k,l])=>`<tr><td>${l}</td><td class="num">${p.scores[k]??"–"}</td></tr>`).join("");
 const li=(t,a)=>a&&a.length?`<h4>${t}</h4><ul>${a.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`:"";
 const dep=Object.entries(p.deploy||{}).map(([k,v])=>`<span class="chip">${esc(k)}: ${esc(v).slice(0,40)}</span>`).join("");
 return `<div class="detail"><h2 style="margin:0">${esc(p.name)} <span class="tier ${tierCls(p.tier)}">${esc(p.tier)}</span></h2><div class="meta">${p.id} · ${esc(p.company)}${p.orig?" · label in the popular stack diagram: "+esc(p.orig):" · not in the popular stack diagram"}</div>
 <p>${esc(p.rationale)}</p><div style="display:grid;grid-template-columns:minmax(220px,300px) 1fr;gap:16px">
 <div><table><tr><th>Criterion</th><th class="num">Score</th></tr>${sc}<tr><th>FS total</th><th class="num">${p.fs!=null?p.fs.toFixed(2):"–"}</th></tr><tr><th>Generic total</th><th class="num">${p.gen!=null?p.gen.toFixed(2):"–"}</th></tr></table>
 ${p.caps.length?`<p class="note">Evidence rules: ${p.caps.map(esc).join("; ")}</p>`:""}</div>
 <div><p>${esc(p.what)}</p><table><tr><td>Version / lineup</td><td>${esc(p.version)}</td></tr><tr><td>Licence</td><td>${esc(p.licence)}</td></tr><tr><td>Status events</td><td>${esc(p.status)}</td></tr><tr><td>Certifications</td><td>${esc(p.certs)}</td></tr><tr><td>Residency</td><td>${esc(p.resid)}</td></tr><tr><td>Access controls</td><td>${esc(p.access)}</td></tr><tr><td>Pricing</td><td>${esc(p.pricing)}</td></tr></table><div>${dep}</div></div></div>
 ${li("Strengths",p.strengths)}${li("Limitations and risks",p.limits)}${li("Choose when",p.choose)}${li("Avoid when",p.avoid)}
 ${p.comp.length?`<p><b>Nearest competitors:</b> ${p.comp.map(esc).join(", ")}</p>`:""}${p.fsnote?`<p><b>Regulated-FS note.</b> ${esc(p.fsnote)}</p>`:""}</div>`}
function products(){const deps=["saas","managed_cloud","vpc_byoc","private_cloud","self_hosted","on_prem"];
 let h=`<div class="filters"><input id="q" placeholder="Search products, facts…" value="${esc(st.q)}"><select id="tier">${["all","Strategic","Tactical","Experimental","Not scored"].map(t=>`<option ${st.tier==t?"selected":""} value="${t}">${t=="all"?"All tiers":t}</option>`).join("")}</select>
 <select id="dep"><option value="all">Any deployment</option>${deps.map(d=>`<option ${st.dep==d?"selected":""} value="${d}">${d.replace("_"," ")}</option>`).join("")}</select></div>`;
 const r=list();h+=`<p class="note">${r.length} products · sorted by regulated-FS score · click a card for detail</p><div class="cards">${r.map(card).join("")}</div>`;
 if(st.sel){const p=D.find(x=>x.id==st.sel);if(p)h=detail(p)+`<p><button onclick="st.sel=null;render()">← back to list</button></p>`}
 return h}
function compare(){const ps=st.cmp.map(id=>D.find(p=>p.id==id)).filter(Boolean);if(!ps.length)return '<p>Tick "compare" on up to four product cards, then return here.</p>';
 let h=`<table><tr><th></th>${ps.map(p=>`<th>${esc(p.short)}<br><span class="tier ${tierCls(p.tier)}">${p.tier}</span></th>`).join("")}</tr>`;
 for(const [k,l] of C)h+=`<tr><td>${l}</td>${ps.map(p=>`<td class="num">${p.scores[k]??"–"}</td>`).join("")}</tr>`;
 h+=`<tr><th>FS total</th>${ps.map(p=>`<th class="num">${p.fs!=null?p.fs.toFixed(2):"–"}</th>`).join("")}</tr><tr><th>Generic total</th>${ps.map(p=>`<th class="num">${p.gen!=null?p.gen.toFixed(2):"–"}</th>`).join("")}</tr>`;
 for(const [k,l] of [["licence","Licence"],["certs","Certifications"],["resid","Residency"],["status","Status events"]])h+=`<tr><td>${l}</td>${ps.map(p=>`<td>${esc(p[k]).slice(0,300)}</td>`).join("")}</tr>`;
 return h+`</table><p><button onclick="st.cmp=[];save();render()">Clear comparison</button></p>`}
function render(){nav();document.querySelectorAll("nav.tabs button[data-t]").forEach(b=>b.classList.toggle("on",b.dataset.t==st.tab));
 const v=document.getElementById("view");
 v.innerHTML=st.tab=="products"?products():st.tab=="compare"?compare():`<div class="prose">${X[st.tab]||""}</div>`;
 const q=document.getElementById("q");if(q){q.oninput=e=>{st.q=e.target.value;const pos=e.target.selectionStart;render();const n=document.getElementById("q");n.focus();n.setSelectionRange(pos,pos)}}
 const t=document.getElementById("tier");if(t)t.onchange=e=>{st.tier=e.target.value;render()};const d=document.getElementById("dep");if(d)d.onchange=e=>{st.dep=e.target.value;render()};
 v.querySelectorAll(".card").forEach(c=>c.onclick=()=>{st.sel=c.dataset.id;render();window.scrollTo(0,0)});
 v.querySelectorAll("input[data-c]").forEach(c=>c.onchange=()=>{const id=c.dataset.c;st.cmp=c.checked?[...new Set([...st.cmp,id])].slice(-4):st.cmp.filter(x=>x!=id);save();cb()});cb()}
function cb(){const b=document.getElementById("cmpbox");b.style.display=st.cmp.length?"block":"none";b.innerHTML=`Comparing ${st.cmp.length}/4: ${st.cmp.join(", ")} <button onclick="st.tab='compare';render()">Open comparison</button>`}
document.querySelectorAll("nav.tabs button[data-t]").forEach(b=>b.onclick=()=>{st.tab=b.dataset.t;render()});
document.getElementById("theme").onclick=()=>{const r=document.documentElement;r.dataset.theme=r.dataset.theme=="dark"?"light":"dark"};
render();
</script></body></html>"""
page = TEMPLATE.replace("__DATA__", json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")).replace("__EXTRAS__", json.dumps(extras, ensure_ascii=False).replace("</", "<\\/")) \
               .replace("__NAMES__", json.dumps(NAMES)).replace("__VIEWS__", json.dumps(VIEWS, ensure_ascii=False).replace("</", "<\\/")).replace("__VMETA__", json.dumps(VMETA, ensure_ascii=False)).replace("__LOCKUPW__", "data:image/png;base64," + __import__("base64").b64encode(open("brand/veyan_lockup_white_small.png", "rb").read()).decode()).replace("__LOCKUP__", "data:image/png;base64," + __import__("base64").b64encode(open("brand/veyan_lockup_small.png", "rb").read()).decode()).replace("__N__", str(len(rows)))
open(os.path.join(OUT, "explorer.html"), "w", encoding="utf-8").write(page)
print(len(page), "bytes")
