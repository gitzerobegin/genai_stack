// Executive deck: The Enterprise GenAI Stack — the view at end of Q3 2026 (Veyan theme).
// Usage: node tools/deck/build_deck.js <repo_root>
// Writes Enterprise_GenAI_Stack_Oct2026/03_Slides/Executive_Deck.pptx (PDF via LibreOffice afterwards).
const path = require("path");
const pptxgen = require("pptxgenjs");
const root = process.argv[2] || ".";
const tiers = require("./tiers.json");
const SKILL = path.join(__dirname, "apply_theme.js");  // portable theme writer (tools/deck/apply_theme.js)

const THEME = {
  name: "Veyan",
  headFontFace: "Arial",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "0B1B33", lt1: "FFFFFF", dk2: "0B1B33", lt2: "F5F1E8",
    accent1: "2E6DA4", accent2: "0B1B33", accent3: "D4A13A", accent4: "6B7A8F", accent5: "9DBBDB", accent6: "B3474B",
    hlink: "2E6DA4", folHlink: "6B7A8F",
  },
};
const HEX = { navy: "0B1B33", teal: "2E6DA4", amber: "D4A13A", slate: "6B7A8F", ice: "EEF3F8", red: "B3474B", mint: "9DBBDB", ink: "0B1B33", white: "FFFFFF", line: "D5DCE3", gold: "D4A13A", warm: "F5F1E8" };
const BRAND = path.join(root, "brand");
const LOGO = path.join(BRAND, "veyan_logo.png"), LOGO_W = path.join(BRAND, "veyan_logo_white.png"), ICON = path.join(BRAND, "veyan_icon.png");
const HERO = path.join(BRAND, "veyan_hero.png"), CARD = path.join(BRAND, "veyan_brand_card.jpg");
const MARK = path.join(BRAND, "veyan_mark.png"), LOCK = path.join(BRAND, "veyan_lockup.png"), LOCK_W = path.join(BRAND, "veyan_lockup_white.png");
const LOCK_AR = 2074 / 600;
const LOGO_AR = 1778 / 484;
const KICK = { fontSize: 12, charSpacing: 6, color: HEX.gold, bold: false };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.title = "The Enterprise GenAI Stack: the view at end of Q3 2026";
pres.author = "Veyan";
pres.company = "Veyan";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const FOOT = "Veyan · The Enterprise GenAI Stack · The view at end of Q3 2026 · Not a description of any firm's platform";

pres.defineSlideMaster({
  title: "TITLE", background: { color: HEX.navy },
  objects: [{ image: { x: 0, y: 0, w: 5.14, h: 7.5, path: HERO } },
            { image: { x: 5.75, y: 0.6, w: 3.6, h: 3.6 / LOCK_AR, path: LOCK_W } },
            { text: { text: "THE VIEW AT END OF Q3 2026", options: Object.assign({ x: 5.75, y: 1.75, w: 7.0, h: 0.35 }, KICK) } },
            { line: { x: 5.8, y: 2.2, w: 0.7, h: 0, line: { color: HEX.gold, width: 2 } } },
            { placeholder: { options: { name: "title", type: "title", x: 5.75, y: 2.45, w: 7.0, h: 2.0, fontSize: 36, bold: true, color: C.background1, fontFace: THEME.headFontFace, valign: "top", align: "left" }, text: "" } },
            { placeholder: { options: { name: "body", type: "body", x: 5.75, y: 4.5, w: 7.0, h: 1.6, fontSize: 16, color: C.accent5, valign: "top" }, text: "" } },
            { text: { text: "PEOPLE  |  INSIGHTS  |  DECISIONS  |  A BRIGHTER TOMORROW", options: { x: 5.75, y: 6.75, w: 7.0, h: 0.3, fontSize: 9, charSpacing: 3, color: HEX.mint } } }],
});
pres.defineSlideMaster({
  title: "SECTION", background: { color: HEX.navy },
  objects: [{ image: { x: 9.2, y: 0, w: 4.13, h: 7.5, path: path.join(BRAND, "veyan_hero_strip.png") } },
            { image: { x: 0.8, y: 1.3, w: 1.0, h: 1.0, path: MARK } },
            { line: { x: 0.85, y: 3.85, w: 0.7, h: 0, line: { color: HEX.gold, width: 2 } } },
            { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.55, w: 8.0, h: 1.2, fontSize: 34, bold: true, color: C.background1, fontFace: THEME.headFontFace, valign: "bottom", align: "left" }, text: "" } },
            { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.05, w: 8.0, h: 1.2, fontSize: 17, color: C.accent5 }, text: "" } }],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: C.background1 },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 10.4, h: 0.9, fontSize: 26, bold: true, color: C.text2, fontFace: THEME.headFontFace, valign: "middle", align: "left" }, text: "" } },
            { image: { x: 11.15, y: 0.45, w: 1.6, h: 1.6 / LOCK_AR, path: LOCK } },
            { line: { x: 0.62, y: 1.25, w: 0.6, h: 0, line: { color: HEX.gold, width: 2 } } },
            { image: { x: 0.6, y: 7.02, w: 0.26, h: 0.26, path: MARK } },
            { text: { text: FOOT, options: { x: 0.92, y: 7.0, w: 10.2, h: 0.3, fontSize: 9, color: C.accent4 } } }],
  slideNumber: { x: 12.3, y: 7.0, w: 0.5, h: 0.3, fontSize: 9, color: C.accent4 },
});
pres.defineSlideMaster({ title: "BRAND", background: { color: HEX.navy }, objects: [{ image: { x: 0, y: 0, w: 13.33, h: 7.5, path: CARD } }] });

let sec = "";
function slide(master, title, sectionTitle) {
  if (sectionTitle && sectionTitle !== sec) { pres.addSection({ title: sectionTitle }); sec = sectionTitle; }
  const s = pres.addSlide({ masterName: master, sectionTitle: sec });
  if (title) s.addText(title, { placeholder: "title" });
  return s;
}
const T = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, fontSize: 14, color: C.text1, valign: "top", margin: 0.05 }, o));
function card(s, x, y, w, h, head, body, opts = {}) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: opts.fill || C.background2 }, line: { color: opts.fill || C.background2 }, objectName: "card" });
  T(s, head, { x: x + 0.18, y: y + 0.12, w: w - 0.36, h: 0.45, fontSize: opts.headSize || 15, bold: true, color: opts.headColor || C.text2 });
  if (body) T(s, body, { x: x + 0.18, y: y + 0.55, w: w - 0.36, h: h - 0.65, fontSize: opts.bodySize || 13, color: C.text1 });
}
function dot(s, x, y, label, color) {
  s.addShape(pres.shapes.OVAL, { x, y, w: 0.5, h: 0.5, fill: { color: color || C.accent1 }, line: { color: color || C.accent1 } });
  T(s, label, { x, y: y + 0.02, w: 0.5, h: 0.46, fontSize: 13, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0 });
}
function table(s, rows, o) {
  const hdr = rows[0].map((h) => ({ text: h, options: { bold: true, color: HEX.white, fill: { color: HEX.navy }, fontSize: o.fs || 12 } }));
  const body = rows.slice(1).map((r, i) => r.map((c) => (typeof c === "object" ? c : { text: String(c), options: { fontSize: o.fs || 12, fill: { color: i % 2 ? HEX.white : HEX.ice } } })));
  s.addTable([hdr, ...body], { x: o.x, y: o.y, w: o.w, colW: o.colW, border: { type: "solid", pt: 0.5, color: HEX.line }, fontFace: "Calibri", color: HEX.ink, valign: "middle", margin: 0.06, autoPage: false });
}

// 1 Title
let s = slide("TITLE", "The Enterprise GenAI Stack", "Opening");
s.addText("A new baseline for the enterprise GenAI stack, set by this research: the reference architecture, what to select, what to deliberately not build yet, and how the advice changes for seven kinds of reader.", { placeholder: "body" });
T(s, "Reference architecture · 9 layers · 8 enterprise controls · 140 products · 1,255 sources", { x: 5.75, y: 6.2, w: 7.0, h: 0.4, fontSize: 11, color: C.accent5 });
s.addNotes("Purpose: give the leadership team one decision-ready view of the 2026 GenAI stack. The full evidence (about 230,000 words, 1,255 sources) sits in the master document and appendix. Disclosure: researched and drafted with an Anthropic model; Anthropic items were scored on the same rubric, borderline calls resolved against them, and tiers set by the reader are marked.");

// 2 The answer
s = slide("CONTENT", "The answer in one sentence", "Opening");
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.45, w: 12.1, h: 1.9, rectRadius: 0.1, fill: { color: C.text2 }, line: { color: C.text2 } });
T(s, "Build a firm-owned control and evidence plane first. Run regulated work as deterministic workflows with one bounded model step and a human approval gate. Consume models as a two-vendor portfolio. Treat every product beneath the plane as replaceable.",
  { x: 0.95, y: 1.65, w: 11.4, h: 1.55, fontSize: 21, color: C.background1, fontFace: THEME.headFontFace, valign: "middle" });
const ans = [["Control first", "Gateway, identity, privacy, configuration, evaluation and one evidence store are the firm's own. They make exit a configuration change."],
             ["Workflows, not free agents", "Every serious framework now separates deterministic workflows from agent loops. Regulated work defaults to the workflow."],
             ["Products are components", "Ownership of 'neutral' tools changed hands repeatedly in 2025–26. Independence and exit must be designed in, not assumed."]];
ans.forEach((a, i) => card(s, 0.6 + i * 4.1, 3.7, 3.9, 2.9, a[0], a[1], { bodySize: 14 }));
s.addNotes("Source: synthesis Part I.2. Rationale for each point: Part I.1 findings 1, 2 and 4.");

// 3 What we reviewed
s = slide("CONTENT", "A new baseline, set by this research", "Opening");
const stats = [["17", "layers and controls: nine stack layers (L1–L9) and eight enterprise controls (C1–C8)", C.text2], ["140", "products profiled: 92 in the stack layers, 48 in the controls; 138 scored", C.accent1], ["192", "high-risk claims re-checked by two adversarial verifiers", C.accent6], ["1,255", "sources logged with URL and access date", C.accent3]];
stats.forEach((st, i) => {
  const x = 0.6 + i * 3.08;
  T(s, st[0], { x, y: 1.7, w: 2.9, h: 1.3, fontSize: 60, bold: true, color: st[2], fontFace: THEME.headFontFace });
  T(s, st[1], { x, y: 3.0, w: 2.8, h: 1.0, fontSize: 14, color: C.text1 });
});
T(s, "How the work was done", { x: 0.6, y: 4.35, w: 12, h: 0.4, fontSize: 16, bold: true, color: C.text2 });
T(s, [{ text: "Eight parallel research streams, primary sources first; two adversarial verifiers re-checked the high-risk claims (no fabrications found). The result is the baseline every later edition is measured against.", options: { bullet: true, breakLine: true } },
      { text: "Seventeen chapters on a 13-part template, each product scored 1–5 on eight criteria with generic and regulated-FS weights.", options: { bullet: true, breakLine: true } },
      { text: "Reader checkpoints decided the scoring rules and the contested tiers; every claim is labelled verified, reported, judgement or recommendation.", options: { bullet: true } }],
  { x: 0.6, y: 4.8, w: 12, h: 1.9, fontSize: 14, paraSpaceAfter: 6 });
s.addNotes("This review sets a new baseline: the stack as it stands at the end of Q3 2026, on its own terms, and the reference point for the next quarterly edition. Numbers from the dataset build (05_Data/products.json, bibliography.xlsx) and the verification logs (192 checks). Limitation: no vendor audit report was read; many facts come from dated search extracts because the research environment blocked direct fetching of most vendor sites.");

// 4 Ten findings
s = slide("CONTENT", "Ten findings that shape the stack", "The view at end of Q3 2026");
const f = [["Catalogue → control system", "The eight enterprise controls are where GenAI risk is managed."], ["Neutral tools were bought", "Arize, Langfuse, Promptfoo, Portkey, Lakera, Voyage, Jina and others changed hands."],
           ["Models are tiered families", "Gated top tiers and short lives: model choice is a lifecycle discipline."], ["Workflows vs agents", "Every serious framework now ships both; this is the key design choice."],
           ["Protocols under foundations", "MCP and A2A now sit in a Linux Foundation project; agent identity is a product category."], ["Vector DB is a feature", "Hybrid search ships in most stores; retrieval is a governed index."],
           ["Memory layer is thinning", "Open editions narrowed; hyperscalers ship memory in their runtimes."], ["Supply chain is attack surface", "A gateway package was compromised; a tool broker leaked tokens."],
           ["Regulatory anchors moved", "SR 26-2 excludes GenAI; EU high-risk duties now 2 Dec 2027."], ["'Open source' often is not", "Source-available, AGPL, non-commercial and threshold licences."]];
f.forEach((x, i) => { const col = i % 2, row = Math.floor(i / 2); const xx = 0.6 + col * 6.15, yy = 1.4 + row * 1.1;
  dot(s, xx, yy + 0.12, String(i + 1), i === 8 ? C.accent3 : C.accent1);
  T(s, x[0], { x: xx + 0.65, y: yy, w: 5.3, h: 0.4, fontSize: 15, bold: true, color: C.text2 });
  T(s, x[1], { x: xx + 0.65, y: yy + 0.4, w: 5.3, h: 0.6, fontSize: 13 }); });
s.addNotes("Synthesis Part I.1, findings 1–10, each tagged to sources in the master document.");

// 5 Ownership
s = slide("CONTENT", "Independence can no longer be assumed from a product's origins", "The view at end of Q3 2026");
table(s, [["Product (layer)", "New owner", "Status (as of 8 October 2026)"],
  ["Arize Phoenix and AX (evaluation)", "Dynatrace", "Completed 1 October 2026"], ["Langfuse (evaluation)", "ClickHouse", "Announced 16 January 2026"],
  ["Promptfoo (red-teaming)", "OpenAI", "Announced 9 March 2026; closing not published"], ["Voyage AI (embeddings)", "MongoDB", "Closed February 2025"],
  ["Jina AI (embeddings)", "Elastic", "Completed 9 October 2025"], ["Tavily (search API)", "Nebius", "Closed 19 February 2026"],
  ["OpenRouter (model router)", "Stripe", "Agreed 19 August 2026; pending"], ["Portkey (gateway), Protect AI (security)", "Palo Alto Networks", "Completed 2025–26"],
  ["Lakera (guardrails)", "Check Point", "Completed 22 October 2025"], ["Guardrails AI; Helicone", "Harvey; Mintlify", "Completed; Helicone in maintenance mode"]],
  { x: 0.6, y: 1.4, w: 7.6, colW: [3.0, 1.9, 2.7], fs: 13 });
card(s, 8.6, 1.4, 4.1, 2.4, "What it means", "A model vendor now owns a red-team tool; security vendors own gateways. Effective challenge and exit planning have to be designed, not inherited.", { bodySize: 14 });
card(s, 8.6, 4.0, 4.1, 2.6, "What we do about it", "Keep evaluation datasets, routes and policies in Git; keep two red-team tools, one independent of the model vendor; re-run due diligence on every change of control.", { bodySize: 14 });
s.addNotes("Synthesis Part I.1 finding 2; filing figures only for deal values (press values are deliberately not used). Source IDs in the master document.");

// 6 Regulation timeline
s = slide("CONTENT", "The regulatory anchors moved in 2026", "The view at end of Q3 2026");
const ev = [["17 Apr 2026", "SR 26-2 replaces SR 11-7", "Generative and agentic AI are out of scope: firms must write their own GenAI standard"],
            ["2 Aug 2026", "EU AI Act GPAI enforcement", "Commission powers over general-purpose model providers start"],
            ["18 Mar 2027", "PRA PS7/26 · FCA PS26/2", "Material third-party notifications and registers begin"],
            ["2 Dec 2027", "EU AI Act Annex III", "High-risk duties deferred by Regulation (EU) 2026/1744"]];
s.addShape(pres.shapes.LINE, { x: 0.9, y: 2.55, w: 11.6, h: 0, line: { color: C.accent4, width: 2 } });
ev.forEach((e, i) => { const x = 0.7 + i * 3.05;
  s.addShape(pres.shapes.OVAL, { x: x + 0.2, y: 2.37, w: 0.36, h: 0.36, fill: { color: i === 0 ? C.accent6 : C.accent1 }, line: { color: C.background1, width: 2 } });
  T(s, e[0], { x, y: 1.55, w: 2.9, h: 0.5, fontSize: 18, bold: true, color: C.text2, fontFace: THEME.headFontFace });
  T(s, e[1], { x, y: 2.95, w: 2.85, h: 0.6, fontSize: 15, bold: true, color: C.accent1 });
  T(s, e[2], { x, y: 3.55, w: 2.85, h: 1.3, fontSize: 13 }); });
card(s, 0.6, 5.15, 12.1, 1.55, "Concentration sits with the clouds, not the model vendors",
  "DORA's first critical-provider list and the UK CTP designations name hyperscalers and no model vendor. PRA SS1/23 and the EU AI Act are now the operative model-risk anchors.", { bodySize: 14 });
s.addNotes("Synthesis Part I.1 finding 9 and Part V; every date tagged to regulator sources (regulatory_facts.json R-US-MRM, R-EUAIA, R-EU-OMNIBUS-AI, R-PRA-SS221, R-FCA-SYSC8, R-DORA, R-UK-CTP).");

// 7 Section
s = slide("SECTION", "The architecture", "The architecture");
s.addText("Eight hypotheses tested; nine stack layers under one firm-owned control plane of eight controls", { placeholder: "body" });

// 8 Revised model
s = slide("CONTENT", "Four planes under one firm-owned control plane", "The architecture");
const planes = [["CONTROL PLANE (firm-owned)", "C1 AI traffic gateway · C2 guardrails · C3 privacy service · C4 identity · C5 configuration of record · C6 FinOps · C7 AI security · C8 governance and evidence store", C.text2, C.background1],
                ["MODEL PLANE (L1, L2)", "Two-vendor portfolio + small + open-weight · in-region model access · vLLM exit route", C.background2, C.text2],
                ["AGENT PLANE (L3, L4)", "Workflows by default · bounded agent steps · durable execution · tools behind a governance sub-layer", C.background2, C.text2],
                ["KNOWLEDGE PLANE (L5, L6, L7, L8)", "Memory service (built last) · derived, entitlement-filtered stores · retrieval optimisation · ingestion envelope", C.background2, C.text2],
                ["EVALUATION AND OBSERVABILITY PLANE (L9)", "Firm OpenTelemetry collector · platform of record · CI and online evaluations · two red-team tools", C.accent1, C.background1]];
planes.forEach((p, i) => { const y = 1.4 + i * 1.08;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y, w: 8.4, h: 0.95, rectRadius: 0.06, fill: { color: p[2] }, line: { color: p[2] } });
  T(s, p[0], { x: 0.8, y: y + 0.07, w: 8.0, h: 0.35, fontSize: 13, bold: true, color: p[3] });
  T(s, p[1], { x: 0.8, y: y + 0.42, w: 8.0, h: 0.5, fontSize: 12, color: p[3] }); });
card(s, 9.3, 1.4, 3.4, 5.25, "How to read it", "The control plane governs every call and holds the evidence. Planes beneath it are built from replaceable products.\n\nL1–L9 and C1–C8 are the baseline's identifiers in every document, the explorer and the dataset.", { bodySize: 14 });
s.addNotes("Synthesis Part IV.1 (revised layer model and diagram).");

// 9 Hypotheses
s = slide("CONTENT", "Hypothesis verdicts: how evidence shaped the layers", "The architecture");
table(s, [["#", "Hypothesis", "Verdict"],
  ["H1", "Inference is several jobs; the gateway is a control", "L2 covers model access, serving and optimisation; the gateway is C1 (model, tool and agent traffic)"],
  ["H2", "Agent framework is not one layer", "L3 holds deterministic workflows (default), bounded agent steps and durable execution"],
  ["H3", "Identity and tool governance", "Keep: a tool-governance sub-layer in L4; C4 and C7 make the decisions"],
  ["H4", "Memory vs retrieval", "Memory is a governed service on the stores layer; build it last"],
  ["H5", "Vector databases are retrieval stores", "L6 is 'Retrieval, knowledge and memory stores'"],
  ["H6", "Embeddings + reranking", "Together they are L7 'Retrieval optimisation'"],
  ["H7", "Ingestion needs lineage, DLP, ACLs", "Keep, widened: a built ingestion envelope around replaceable parsers"],
  ["H8", "Evaluation is cross-cutting", "L9 is an evidence plane, sharing one evidence store with C8"]],
  { x: 0.6, y: 1.5, w: 12.1, colW: [0.7, 3.6, 7.8], fs: 16 });
s.addNotes("Synthesis Part III, H1–H8, with evidence from the 17 chapters.");

// 10 Twelve decisions
s = slide("CONTENT", "Twelve decisions that define the architecture", "The architecture");
const dec = ["One gateway of record for all model, MCP and agent traffic; two deployments, in region, failing closed",
  "Evaluation and observability from day one; datasets in Git; two red-team tools",
  "A firm-owned, immutable evidence store keyed by trace ID",
  "A two-vendor model portfolio in region, plus a small model and a self-hosted exit route",
  "Deterministic workflows by default, with approval gates only a named human can resume",
  "Read-only tools for authoritative data, behind a governed tool gateway",
  "Every agent a registered identity acting on behalf of a human, deny by default",
  "One privacy service at six enforcement points",
  "Retrieval inside platforms already run, as a rebuildable, entitlement-filtered index",
  "Git as the configuration of record for prompts, pins and policies",
  "Capability separation as the first security control",
  "Memory last, as a governed record class"];
dec.forEach((d, i) => { const col = Math.floor(i / 6), row = i % 6; const x = 0.6 + col * 6.15, y = 1.4 + row * 0.88;
  dot(s, x, y + 0.08, String(i + 1), C.accent1); T(s, d, { x: x + 0.65, y: y + 0.02, w: 5.3, h: 0.8, fontSize: 14, valign: "middle" }); });
s.addNotes("Synthesis Part I.2, 'Twelve decisions'. MCP originated at Anthropic; OpenAPI tools behind the same gateway are the independent alternative.");

// 11 Section
s = slide("SECTION", "What to select", "What to select");
s.addText("138 products scored on eight criteria · 58 Strategic · 67 Tactical · 13 Experimental", { placeholder: "body" });

// 12 Tier chart
s = slide("CONTENT", "Where the Strategic choices are", "What to select");
s.addChart(pres.charts.BAR, [{ name: "Strategic", labels: tiers.labels, values: tiers.Strategic }, { name: "Tactical", labels: tiers.labels, values: tiers.Tactical }, { name: "Experimental", labels: tiers.labels, values: tiers.Experimental }],
  { x: 0.6, y: 1.35, w: 8.2, h: 5.45, barDir: "col", barGrouping: "stacked", chartColors: [HEX.teal, HEX.slate, HEX.amber], showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: "+mn-lt",
    catAxisLabelColor: HEX.ink, valAxisLabelColor: HEX.ink, catAxisLabelFontSize: 11, valAxisLabelFontSize: 11, catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt",
    valGridLine: { color: HEX.line, size: 0.5 }, catGridLine: { style: "none" }, showValue: true, dataLabelPosition: "ctr", dataLabelColor: HEX.white, dataLabelFontSize: 10, dataLabelFormatCode: "0;;;",
    showTitle: true, title: "Products by tier, layer (L1→L9) and control (C1→C8)", titleFontSize: 13, titleColor: HEX.navy, titleFontFace: "+mn-lt" });
card(s, 9.1, 1.35, 3.6, 2.5, "A Strategic tier carries a condition", "18 of the 58 apply only where a given cloud is primary, or where a platform is already operated. The condition is the decision.", { bodySize: 13 });
card(s, 9.1, 4.05, 3.6, 2.75, "What drives the tiers", "Regulated-FS weights favour deployment flexibility and low lock-in, so open, self-hostable components take most Strategic slots. No commercial governance tool reached Strategic on public evidence.", { bodySize: 13 });
s.addNotes("Data: 05_Data/products.json after CP4. Strategic counts by area from the scorecard; tiers are judgements under rules 9–13, not thresholds.");

// 13 Cloud-neutral core
s = slide("CONTENT", "The cloud-neutral core we would select today", "What to select");
table(s, [["Layer / control", "Selection", "Independent alternative or note"],
  ["L1 models", "Two vendors from OpenAI, Anthropic, Mistral, Gemini; Gemma 4 or Mistral self-hosted", "For Claude: GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5"],
  ["L2 inference", "Primary cloud's in-region model service + vLLM exit route", "SGLang as backup engine once its CVE fix is confirmed"],
  ["L3 orchestration", "LangGraph on Temporal", "Microsoft Agent Framework, ADK, Pydantic AI"],
  ["L4 tools", "Read-only MCP tools behind a governed gateway", "OpenAPI tools (MCP originated at Anthropic)"],
  ["L6 / L7 retrieval", "pgvector (or Elasticsearch where run) + Sentence Transformers", "Qdrant or Milvus after a failed load test"],
  ["L8 ingestion", "Docling + Unstructured inside a built envelope", "Specialist parsers for hard documents"],
  ["L9 evaluation", "Langfuse or MLflow + firm OpenTelemetry collector", "Two red-team tools, one vendor-independent"],
  ["C1 gateway", "LiteLLM Enterprise (hardened, pinned) or Kong AI Gateway", "Cloud gateway where that cloud is primary"],
  ["C3 privacy / C4 identity", "Presidio behind a privacy API · workforce IdP + OPA + SPIFFE", "Cloud DLP / Entra Agent ID per cloud"],
  ["C5 configuration", "Git as configuration of record; prompts as code", "Vendor registries are caches only"]],
  { x: 0.6, y: 1.4, w: 12.1, colW: [2.3, 5.4, 4.4], fs: 14 });
s.addNotes("Synthesis Part XI.7 and Part I.2. Anthropic's tier (Strategic, conditional) was set by the reader at Checkpoint 4 on neutral-rubric scores; an independent alternative is always named.");

// 14 Model portfolio
s = slide("CONTENT", "Treat models as a portfolio, not a bet", "What to select");
const pf = [["Primary mid-tier", "One vendor through the primary cloud's in-region model service", C.accent1], ["Second mid-tier", "An unrelated vendor qualified on the same evaluation suite", C.accent1],
            ["Small model", "Classification, routing and judging at low cost", C.accent4], ["Open-weight exit route", "Gemma 4 or Mistral on vLLM: the stressed-exit drill", C.accent3]];
pf.forEach((p, i) => { const x = 0.6 + i * 3.08;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.45, w: 2.9, h: 2.4, rectRadius: 0.08, fill: { color: p[2] }, line: { color: p[2] } });
  T(s, p[0], { x: x + 0.2, y: 1.6, w: 2.5, h: 0.5, fontSize: 17, bold: true, color: C.background1 });
  T(s, p[1], { x: x + 0.2, y: 2.15, w: 2.5, h: 1.6, fontSize: 14, color: C.background1 }); });
T(s, [{ text: "Top tiers are gated and lifetimes are short: one Gemini Flash version lives about five months. Re-qualification is routine work, not an event.", options: { bullet: true, breakLine: true } },
      { text: "Chinese-origin families: decide the route, not the brand. Self-hosted weights by explicit policy or in-tenant hosting; never the vendor's own API for client data.", options: { bullet: true, breakLine: true } },
      { text: "Numbers are never generated by the model; they come from the attribution engine through read-only tools.", options: { bullet: true } }],
  { x: 0.6, y: 4.2, w: 12.1, h: 2.5, fontSize: 14, paraSpaceAfter: 8 });
s.addNotes("Chapter 1 (foundation models) and synthesis Part I.3. Disclosure: the drafting model is Anthropic's; Anthropic was scored on the same rubric and its tier was set by the reader.");

// 15 Keep/remove/missing
s = slide("CONTENT", "The new baseline: 17 layers and controls, 140 products", "What to select");
const krm = [["Nine stack layers", "L1 models as a pinned portfolio · L2 access, serving, optimisation · L3 workflows and bounded agents · L4 tools behind a governed gateway · L5 memory as a governed record class · L6 retrieval stores · L7 retrieval optimisation · L8 ingestion envelope · L9 evaluation and observability", C.accent1],
             ["Eight enterprise controls", "C1 AI traffic gateway · C2 guardrails as policy · C3 privacy service · C4 agent identity and authorisation · C5 configuration of record · C6 AI FinOps · C7 AI security · C8 model risk, governance and evidence store", C.text2],
             ["Facts as at Q3 2026", "Current lines: Gemma 4, Z.ai GLM-5.x, Mistral Medium 3.5 · archived or closing: TGI, OpenAI Agent Builder; Helicone in maintenance · not verifiable: EthicalAgents, Ragoos · a router is not the access layer; desktop runtimes stay out of production", C.accent6]];
krm.forEach((k, i) => { const x = 0.6 + i * 4.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.4, w: 3.9, h: 0.6, rectRadius: 0.06, fill: { color: k[2] }, line: { color: k[2] } });
  T(s, k[0], { x: x + 0.2, y: 1.45, w: 3.5, h: 0.5, fontSize: 17, bold: true, color: C.background1, valign: "middle" });
  T(s, k[1].split(" · ").map((t, j, arr) => ({ text: t, options: { bullet: true, breakLine: j < arr.length - 1 } })), { x: x + 0.1, y: 2.15, w: 3.7, h: 4.6, fontSize: 14, paraSpaceAfter: 4 }); });
s.addNotes("The baseline this review sets, stated on its own terms. Layer and control definitions: synthesis Part IV; product status (current, retired, renamed, acquired, unverifiable) in each record of 05_Data/products.json and the product technical appendix.");

// 16 Avoid
s = slide("CONTENT", "Deliberately not selected, on evidence", "What to select");
table(s, [["Avoid", "Why"],
  ["Archived or deprecated: TGI, OpenAI Agent Builder, AutoGen for new code, Helicone, Zep Community Edition", "Archived, shut down, superseded or in maintenance mode"],
  ["EthicalAgents, Ragoos", "Could not be verified as real products"],
  ["A third-party broker holding client tokens (Composio managed cloud)", "Unresolved token-exposure incident, May 2026"],
  ["Jina weights, MinerU above thresholds, a modified AGPL Firecrawl server", "Licence blockers without a commercial licence"],
  ["LM Studio as a service; training-on-data model tiers", "Terms blockers"]],
  { x: 0.6, y: 1.4, w: 12.1, colW: [7.2, 4.9], fs: 15 });
T(s, "Moved to monitor by the reader (CP5): Chinese-origin vendors' own APIs for client data (the route rule still applies) and billing intermediation. Not avoided but not yet: memory, autonomous agents with write tools, multi-agent delegation, fine-tuning, own-GPU fleets, dedicated vector databases without a failed load test.", { x: 0.6, y: 5.3, w: 12.1, h: 1.3, fontSize: 13, italic: true, color: C.text2 });
s.addNotes("Synthesis Part XI.5 (evidence-based avoid list, CP4-7; two routes moved to monitor at CP5) and Stack A 'do not build yet'.");

// 17 Section
s = slide("SECTION", "The regulated firm's view", "Regulated view");
s.addText("What supervisors will ask for, and the worked example that makes it concrete", { placeholder: "body" });

// 18 Evidence
s = slide("CONTENT", "What a supervisor or validator will ask to see", "Regulated view");
const evd = [["Model risk (SS1/23)", "A GenAI model-risk standard, inventory entry, independent validation report, monitoring results, change records"],
             ["EU AI Act", "Use-case classification, AI literacy records, Article 26 logs (six months or more) and oversight assignments for any high-risk use"],
             ["Third parties (PS7/26, DORA)", "Provider assessments, notifications from 18 March 2027, register entries, tested exit plans including a stressed exit"],
             ["Data", "Processing-region evidence per call, transfer risk assessments, erasure runbooks covering vectors, caches and backups"],
             ["Audit trail", "Per-output evidence pack: prompt and model versions, data snapshot, tool calls, evaluation results, approver identity"],
             ["Security (OWASP 2026)", "Red-team results mapped to the LLM and Agentic Top 10 lists; supply-chain gate records"]];
evd.forEach((e, i) => { const col = i % 2, row = Math.floor(i / 2); card(s, 0.6 + col * 6.15, 1.4 + row * 1.8, 5.95, 1.65, e[0], e[1], { bodySize: 13 }); });
s.addNotes("Synthesis Part V and V.8 (consolidated evidence register).");

// 19 Worked example trace
s = slide("CONTENT", "Worked example: the attribution-commentary agent", "Regulated view");
const steps = [["1", "Analyst request", "Identity and policy check (C4)"], ["2", "Workflow graph", "Deterministic; one drafting step (L3)"], ["3", "Read-only data", "Attribution engine via governed tools (L4)"],
               ["4", "House style", "Retrieval of prior commentary (L6–L8)"], ["5", "Draft", "Model via the gateway, in region (C1, L2, L1)"], ["6", "Evaluate", "Every figure matches the engine (L9, C2)"],
               ["7", "Approve", "Named portfolio manager (C4)"], ["8", "Evidence pack", "Stored, immutable, reproducible (C8)"]];
steps.forEach((st, i) => { const col = i % 4, row = Math.floor(i / 4); const x = 0.6 + col * 3.08, y = 1.45 + row * 2.0;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 2.85, h: 1.7, rectRadius: 0.08, fill: { color: i === 5 || i === 6 ? C.accent1 : C.background2 }, line: { color: C.background2 } });
  T(s, st[0] + "  " + st[1], { x: x + 0.15, y: y + 0.15, w: 2.6, h: 0.5, fontSize: 16, bold: true, color: i === 5 || i === 6 ? C.background1 : C.text2 });
  T(s, st[2], { x: x + 0.15, y: y + 0.7, w: 2.6, h: 0.9, fontSize: 13, color: i === 5 || i === 6 ? C.background1 : C.text1 }); });
T(s, "A multi-asset fund, Brinson-style attribution (allocation, selection, currency). Generic and illustrative: not any firm's platform.", { x: 0.6, y: 5.6, w: 12.1, h: 0.5, fontSize: 13, italic: true, color: C.accent4 });
s.addNotes("Synthesis Part VI.1–VI.4. Cloud-neutral; AWS, Azure and Google Cloud equivalents are in the master document.");

// 20 Must never
s = slide("CONTENT", "What the agent must never do matters more than what it can do", "Regulated view");
const nv = [["Generate or alter a number", "Every figure comes from the approved attribution output and is traceable"], ["Present inference as data", "Commentary distinguishes the engine's figures from the narrative"],
            ["Publish without approval", "Only a named, entitled person can resume the approval gate"], ["Leave no record", "Outputs are reproducible; evaluation evidence is retained"]];
nv.forEach((n, i) => { const x = 0.6 + i * 3.08;
  s.addShape(pres.shapes.OVAL, { x: x + 1.0, y: 1.6, w: 0.9, h: 0.9, fill: { color: C.accent6 }, line: { color: C.accent6 } });
  T(s, "✕", { x: x + 1.0, y: 1.62, w: 0.9, h: 0.86, fontSize: 28, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0 });
  T(s, n[0], { x, y: 2.75, w: 2.9, h: 0.8, fontSize: 17, bold: true, color: C.text2, align: "center" });
  T(s, n[1], { x: x + 0.1, y: 3.6, w: 2.7, h: 1.5, fontSize: 14, align: "center" }); });
card(s, 0.6, 5.35, 12.1, 1.35, "The control that catches the one failure that matters", "A wrong number in a client commentary is caught by a deterministic numeric-faithfulness check: an evaluation scorer reused inline as a guardrail.", { bodySize: 14 });
s.addNotes("Plan §11.3 boundaries; synthesis Part VI.3 and X.3 reason 7.");

// 21 Section
s = slide("SECTION", "Delivery", "Delivery");
s.addText("Four reference stacks · build vs buy · lock-in · an 18-month roadmap", { placeholder: "body" });

// 22 Four stacks
s = slide("CONTENT", "Four reference stacks: Stack A leads", "Delivery");
const stk = [["A · Regulated enterprise", "LEAD", "Private deployment, governance and evidence before speed; tested exit for every material dependency", C.text2],
             ["B · Cloud-native managed", "", "The primary cloud's lead service in each category; firm-owned evidence and configuration keep exit possible", C.accent1],
             ["C · Open-source first", "", "Open licence and self-hosted route for every component; the cloud as infrastructure, not platform", C.accent4],
             ["D · Minimal start-small", "", "Stack A cut to one use case, with an explicit 'do not build yet' list", C.accent3]];
stk.forEach((k, i) => { const x = 0.6 + i * 3.08;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.4, w: 2.9, h: 3.4, rectRadius: 0.08, fill: { color: k[3] }, line: { color: k[3] } });
  T(s, k[0], { x: x + 0.18, y: 1.55, w: 2.55, h: 0.8, fontSize: 17, bold: true, color: C.background1 });
  if (k[1]) T(s, k[1], { x: x + 0.18, y: 2.3, w: 1.2, h: 0.35, fontSize: 11, bold: true, color: C.accent3 });
  T(s, k[2], { x: x + 0.18, y: 2.7, w: 2.55, h: 2.0, fontSize: 14, color: C.background1 }); });
card(s, 0.6, 5.05, 12.1, 1.65, "Same control-plane minimum in every stack", "Gateway, evaluation harness, evidence store, privacy API, agent identity, Git configuration, budgets that fail closed. Stacks differ in who runs the components, not in whether they exist.", { bodySize: 14 });
s.addNotes("Synthesis Part VII. Every stack table shows AWS, Azure and Google Cloud equivalents side by side (cloud-neutral by the reader's decision).");

// 23 Build vs buy
s = slide("CONTENT", "Build the control statement; buy the commodity", "Delivery");
table(s, [["Component", "Decision", "What the firm owns"],
  ["Models (L1)", "Buy; adopt open weights", "Portfolio policy, qualification suite, retirement calendar"],
  ["Stores (L6)", "Reuse what is run", "Retrieval interface and rebuild pipeline"],
  ["Ingestion (L8)", "Build the envelope", "No product emits lineage; parsers adopted"],
  ["Evaluation (L9)", "Hybrid", "Datasets and scorers in Git; platform replaceable"],
  ["Gateway (C1), guardrails (C2), privacy (C3)", "Hybrid", "Routes, policies, test sets, keys; the product is replaceable"],
  ["Identity (C4)", "Buy the IdP, build the policy", "Agent registration, policies in Git"],
  ["Configuration (C5), FinOps (C6)", "Build (thin)", "Release manifest, evaluation gate, allocation rules"],
  ["Governance (C8)", "Build the store, buy the workflow", "Evidence store and inventory outlive any tool"],
  ["Fine-tuning", "Do not build yet", "May turn a deployer into a provider under the AI Act"]],
  { x: 0.6, y: 1.4, w: 12.1, colW: [3.8, 3.0, 5.3], fs: 15 });
s.addNotes("Synthesis Part VIII.");

// 24 Lock-in
s = slide("CONTENT", "Which lock-in is acceptable, and which is not", "Delivery");
table(s, [["Area", "Acceptable", "Unacceptable without an exit"],
  ["Models (L1)", "Open weights the firm holds", "A single proprietary vendor for an important service"],
  ["Orchestration (L3)", "Open frameworks", "Vendor-hosted agent state for regulated workflows"],
  ["Tools (L4)", "MCP and A2A as open specifications", "Credential custody in a third party's multi-tenant cloud"],
  ["Stores (L6)", "A vector index rebuildable from source", "Entitlement logic only in proprietary syntax"],
  ["Evaluation (L9)", "Production APM module", "Datasets only in a vendor UI"],
  ["Configuration (C5)", "Pins in a manifest", "Prompt text or change history only in a vendor registry"],
  ["Governance (C8)", "Policy packs, OpenLineage", "An evidence store held only by a vendor"]],
  { x: 0.6, y: 1.4, w: 12.1, colW: [2.4, 4.3, 5.4], fs: 16 });
T(s, "The pattern: own the data, the policy and the evidence; let the engines be bought and replaced.", { x: 0.6, y: 6.1, w: 12.1, h: 0.6, fontSize: 15, bold: true, color: C.accent1 });
s.addNotes("Synthesis Part IX.4 (lock-in by layer and control).");

// 25 Roadmap
s = slide("CONTENT", "An 18-month roadmap, governance first and memory last", "Delivery");
const ph = [["0 Governance", 0, 2], ["1 Evaluation", 1, 3], ["2 Gateway and models", 2, 5], ["3 Retrieval", 4, 7], ["4 Workflows", 6, 9], ["5 Tools", 9, 12], ["6 Memory", 12, 15], ["7 Optimisation", 15, 18]];
const gx = 3.0, gw = 9.6, gy = 1.75, rh = 0.52;
for (let m = 0; m <= 18; m += 3) { const x = gx + (m / 18) * gw; T(s, "M" + m, { x: x - 0.3, y: 1.3, w: 0.6, h: 0.3, fontSize: 10, color: C.accent4, align: "center" });
  s.addShape(pres.shapes.LINE, { x, y: 1.65, w: 0, h: rh * 8 + 0.1, line: { color: HEX.line, width: 0.75 } }); }
ph.forEach((p, i) => { const y = gy + i * rh;
  T(s, p[0], { x: 0.6, y, w: 2.3, h: rh - 0.08, fontSize: 13, bold: true, color: C.text2, valign: "middle" });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: gx + (p[1] / 18) * gw, y: y + 0.07, w: ((p[2] - p[1]) / 18) * gw, h: rh - 0.16, rectRadius: 0.05, fill: { color: i < 3 ? C.accent1 : i < 6 ? C.accent4 : C.accent3 }, line: { color: C.background1 } }); });
[["18 Mar 2027 · PS7/26", 5.5], ["2 Dec 2027 · AI Act Annex III", 14]].forEach(([lab, m]) => { const x = gx + (m / 18) * gw;
  s.addShape(pres.shapes.LINE, { x, y: 1.65, w: 0, h: rh * 8 + 0.1, line: { color: HEX.red, width: 1.5, dashType: "dash" } });
  T(s, lab, { x: x - 1.4, y: 6.05, w: 2.8, h: 0.35, fontSize: 11, bold: true, color: C.accent6, align: "center" }); });
T(s, "October 2026 to March 2028. Phases overlap; each starts when its predecessor's exit criteria are in sight. The exit drill (model switched by configuration only) must pass before March 2027.", { x: 0.6, y: 6.4, w: 12.1, h: 0.55, fontSize: 12, color: C.text1 });
s.addNotes("Synthesis Part X.1–X.2. Phase 2 exit criteria include the exit drill and provider assessments before 18 March 2027; the synthesis notes this timing may be tight.");

// 26 Evals from day one
s = slide("CONTENT", "Why evaluation comes before the first model call", "Delivery");
const why = [["It is the validation evidence", "Without a suite there is nothing for a validator to re-perform and nothing to approve"], ["It is what makes exit possible", "A replacement model is qualified only by running the same suite"],
             ["Every later change is a model change", "Model, prompt, embedding and tool changes all need a regression baseline"], ["Evidence cannot be recreated", "Free tiers keep traces for weeks; an unrecorded output has no reproducible record"]];
why.forEach((w, i) => { const col = i % 2, row = Math.floor(i / 2); const x = 0.6 + col * 6.15, y = 1.7 + row * 2.6;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x - 0.1, y: y - 0.2, w: 6.0, h: 2.3, rectRadius: 0.08, fill: { color: C.background2 }, line: { color: C.background2 } });
  dot(s, x + 0.1, y + 0.05, String(i + 1), C.accent1); T(s, w[0], { x: x + 0.8, y, w: 5.0, h: 0.6, fontSize: 18, bold: true, color: C.text2 }); T(s, w[1], { x: x + 0.8, y: y + 0.7, w: 5.0, h: 1.2, fontSize: 16 }); });
s.addNotes("Synthesis Part X.3 (seven reasons, condensed to four).");

// 27a-27i One stack, seven lenses (the seven views: FS = Parts I–XII; TS, SW, SU, AT, DV, AG = Parts XIII–XVIII)
// Weights and core-candidate counts are read from 05_Data/views.json (tools/build_views.py); the decisions condense
// each view Part's "In brief", findings (x.2) and checklist (x.11).
const VJ = JSON.parse(require("fs").readFileSync(path.join(root, "Enterprise_GenAI_Stack_Oct2026/05_Data/views.json"), "utf8"));
const VCORE = {}; VJ.views.forEach((v) => { VCORE[v.id] = VJ.products.filter((r) => r.fit[v.id] === "Core candidate").length; });
const VSCORED = VJ.products.length;
const VW = (id, k) => VJ.views.find((v) => v.id === id).weights[k];
const PARTN = { FS: "Parts I–XII", TS: "Part XIII", SW: "Part XIV", SU: "Part XV", AT: "Part XVI", DV: "Part XVII", AG: "Part XVIII" };
s = slide("SECTION", "One stack, seven lenses", "Seven lenses");
s.addText(`The same ${VSCORED} scored products and criterion scores, re-weighted for six further readers (Parts XIII–XVIII)`, { placeholder: "body" });
s.addNotes("The regulated-FS view (this deck so far, Parts I–XII) is one of seven. Each further view keeps every fact and criterion score and changes only the weights (architectural judgement, published in 05_Data/views.xlsx), then adds view-specific evidence on regulation, commercial terms and agent standards.");

s = slide("CONTENT", "Seven readers, one stack, different weights", "Seven lenses");
const lensRows = [
  ["FS", "Regulated asset manager deploying GenAI for itself", `Security and compliance ${VW("FS", "security_compliance")}%`],
  ["TS", "Runs GenAI inside services it operates for customers", `Reliability ${VW("TS", "reliability_maturity")}% and cost ${VW("TS", "cost_tco")}%; lock-in ${VW("TS", "lockin_portability")}%`],
  ["SW", "Ships GenAI inside software customers install and run", `Deployment flexibility ${VW("SW", "deployment_flexibility")}%`],
  ["SU", "Early-stage company building an AI-native product", `Technical ${VW("SU", "technical")}%, cost ${VW("SU", "cost_tco")}%`],
  ["AT", "Start-up selling AI tools into the enterprise stack", `Technical ${VW("AT", "technical")}%; ecosystem ${VW("AT", "ecosystem")}%`],
  ["DV", "Start-up selling agentic SDLC tools to developers", `Technical ${VW("DV", "technical")}%; ecosystem and cost ${VW("DV", "ecosystem")}% each`],
  ["AG", "Start-up selling agents to enterprises", `Technical ${VW("AG", "technical")}%; enterprise, security, deployment, ecosystem ${VW("AG", "ecosystem")}% each`]];
table(s, [["View", "Reader", "Weighted most", "Part"], ...lensRows.map((r) => [{ text: r[0], options: { bold: true, fontSize: 13, color: HEX.navy } }, r[1], r[2], PARTN[r[0]]])],
  { x: 0.6, y: 1.4, w: 8.55, colW: [0.75, 3.55, 3.05, 1.2], fs: 12 });
s.addChart(pres.charts.BAR, [{ name: "Core candidates", labels: lensRows.map((r) => r[0]), values: lensRows.map((r) => VCORE[r[0]]) }],
  { x: 9.35, y: 1.3, w: 3.4, h: 4.45, barDir: "bar", chartColors: [HEX.teal], catAxisOrientation: "maxMin", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HEX.navy, dataLabelFontSize: 12, valAxisMinVal: 0, valAxisMaxVal: 75,
    showTitle: true, title: `Core candidates of ${VSCORED}`, titleFontSize: 13, titleColor: HEX.navy, titleFontFace: "+mn-lt", showLegend: false, barGapWidthPct: 60 });
card(s, 0.6, 5.85, 12.1, 0.95, "Same facts and criterion scores; only the weights change",
  null, { headSize: 15 });
T(s, "A core candidate scores at least 3.6 under the view's weights, has no criterion at 1 and is not Experimental. The master tiers and their conditions still stand.", { x: 0.78, y: 6.3, w: 11.8, h: 0.45, fontSize: 13 });
s.addNotes(`Weights and counts from 05_Data/views.json (tools/build_views.py): core candidates FS ${VCORE.FS}, TS ${VCORE.TS}, SW ${VCORE.SW}, SU ${VCORE.SU}, AT ${VCORE.AT}, DV ${VCORE.DV}, AG ${VCORE.AG} of ${VSCORED}. Weights are architectural judgement and sum to 100 per view; the fit is computed and indicative, not checkpoint-reviewed. Conflict of interest: under some views Anthropic's Claude family and MCP rise on the same criterion scores; each Part names the independent alternative beside them.`);

const VIEWSLIDES = [
  ["TS", "Service provider: tenant-aware, metered and sold",
   "The same control plane as the regulated firm, but every element is tenant-aware, metered and sold. Tenant isolation, cost per call and service levels replace model-risk validation as the hardest problems.",
   [["Write a tenancy standard first", "Tenant, user and agent in every token; filters injected server-side; every cache, index and store addressed by tenant; a cross-tenant leak test blocks every release."],
    ["Design the margin in", "Every model call is cost of goods sold: batch, prompt caching and a small model in every feature; cost per call reported per tenant and feature against price."],
    ["Make the second vendor a live capacity route", "Sized and drilled for real load, because discount tiers throttle and one tenant's misuse can suspend the whole service."],
    ["Sell a service, not a pass-through model API", "Flow vendor terms down to tenants, list every model route as a subprocessor, and ship an AI assurance pack and NIS2 and CRA incident runbooks."]],
   "Part XIII.2 findings 1–5 and 8, XIII.11 checklist."],
  ["SW", "Software company: own the release plane",
   "The vendor ships into many control planes it does not own. It is a manufacturer and provider: its product plugs into each customer's gateway, identity, telemetry and evidence tools.",
   [["Publish a support matrix", "At least two unrelated hosted vendors, reached through the customer's own account or gateway, plus one Apache 2.0 or MIT model bundled for air-gapped sites."],
    ["Route through the customer's gateway", "One configurable model endpoint; no provider SDKs in feature code; no vendor-run endpoint on the request path of a self-managed product."],
    ["Gate every shipped component", "Redistribution, not use, decides what ships: a licence register and an AI-aware SBOM per release; signed, safetensors-only bundled weights."],
    ["Treat the CRA and PLD as deadlines", "Vulnerability reporting since 11 September 2026; software a PLD product from 9 December 2026; CRA main obligations from 11 December 2027."]],
   "Part XIV In brief, XIV.2 findings 1–5 and 8, XIV.11 checklist."],
  ["SU", "Start-up: speed first, exits kept open cheaply",
   "A fortnight, not a quarter, on the control plane. What is built in the first two weeks decides how cheaply the company can change its mind later.",
   [["Build four things in the first fortnight", "One pinned gateway with a key and budget per customer; a tenant ID on every row, vector and trace; standard tracing; an evaluation set in Git with the prompts."],
    ["Let credits pick the first vendor, not the last", "Credits mostly pay only for the credit-giver's models: qualify a second vendor on the same evaluation set, switchable by configuration."],
    ["Isolation before model risk", "Keeping one customer's data out of another's answers is the first control problem; the users are customers' staff, so use customer identity, not a workforce directory."],
    ["Two things do not bend", "Pin the gateway: a widely used open-source gateway shipped poisoned releases in March 2026. Keep evaluation sets and prompts as the company's own IP."]],
   "Part XV.2 findings 1–3, 6 and 9, XV.11 checklist."],
  ["AT", "AI-tools start-up: easy to adopt, easy to leave",
   "The buyer's architecture already assigns the product's place: a replaceable call-out inside the buyer's control plane, running where the data is and writing evidence into the buyer's stores.",
   [["Publish the integration contract", "Gateway hooks with a latency budget and typed outcomes; spans to the customer's OpenTelemetry collector; verdicts to its evidence store; usage in an open cost format."],
    ["Run where the buyer's data is", "One build as EU SaaS, private-endpoint SaaS and a container in the customer's account; no hidden model dependency; policy as code, not console settings."],
    ["Beat the free baseline on evidence", "Open tools and incumbents' bundles already ship the feature: win on recall, operations or evidence, never on having the feature."],
    ["Pass diligence and plan for a change of owner", "Many 'neutral' tools were acquired: subprocessor list, DORA addendum, exit plan and change-of-control notice; the start-up's own CRA duties apply too."]],
   "Part XVI In brief, XVI.2 findings 1–4, 6 and 7, XVI.11 checklist."],
  ["DV", "Agentic SDLC: trust is earned in the pull request",
   "The crown jewels are source code and the credentials that change it. Two questions decide the deal: where does our code go, and can we see everything the agent did?",
   [["The customer's model endpoint by default", "Every call through the customer's gateway; two unrelated model vendors qualified per task; retention reported route by route, because it depends on the model."],
    ["The pull request is the boundary", "Own branch, isolated sandbox with default-deny egress, short-lived repository-scoped tokens; the agent never merges, a named human does."],
    ["Fill the audit gap", "An evidence record of every model call, tool call and command, written to the customer's store, with pinned OpenTelemetry spans."],
    ["Sell depth, neutrality and evidence", "Incumbents ship breadth and the enterprise baseline. Win on one task done well; cache stable prefixes, the main cost lever."]],
   "Part XVII In brief, XVII.2 findings 1, 2, 4, 5, 6 and 10, XVII.11 checklist."],
  ["AG", "Agent start-up: an ungoverned agent is not bought",
   "The buyer governs every agent through its own control and evidence plane. The start-up sells domain logic, a tested workflow and an evaluation suite, not a second identity plane, gateway or evidence store.",
   [["Run under the customer's identity", "Registered in the customer's directory with a sponsor; on-behalf-of tokens per tool audience; no standing secrets; revocation within 15 minutes."],
    ["Ship the strict profile of incomplete standards", "Tool authorisation on, signed agent cards, short-lived audience-bound tokens, no sub-delegation; tools read-only by default, through the customer's gateway."],
    ["Keep nothing the customer must audit", "Model calls only to a customer-supplied endpoint; one evidence record per output in the customer's store; workflow, prompts and autonomy budget as files."],
    ["Treat governance fit as the product", "Incumbents are building agent platforms. The test: an evidence pack for every output, revoke by one identity, switch model by one route."]],
   "Part XVIII In brief, XVIII.2 findings 1–3 and 8, XVIII.11 checklist."]];
VIEWSLIDES.forEach(([id, title, ribbon, decs, src]) => {
  s = slide("CONTENT", title, "Seven lenses");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.4, w: 12.1, h: 1.0, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.text2 } });
  T(s, id, { x: 0.8, y: 1.52, w: 0.9, h: 0.76, fontSize: 28, bold: true, color: C.accent3, fontFace: THEME.headFontFace, valign: "middle" });
  T(s, ribbon, { x: 1.75, y: 1.47, w: 10.8, h: 0.86, fontSize: 14, color: C.background1, valign: "middle" });
  decs.forEach((d, i) => card(s, 0.6 + (i % 2) * 6.15, 2.6 + Math.floor(i / 2) * 1.85, 5.95, 1.7, d[0], d[1], { headSize: 16, bodySize: 14 }));
  const fsCore = VCORE.FS, vCore = VCORE[id];
  T(s, `Read more: ${PARTN[id]} of the master document · core candidates under this view: ${vCore} of ${VSCORED} (FS ${fsCore})`, { x: 0.6, y: 6.33, w: 12.1, h: 0.4, fontSize: 12, italic: true, color: C.accent4 });
  s.addNotes(`Source: ${src} Each decision is tagged to its sources in the Part. Where a Claude model, MCP or Agent Skills appears in the Part, an independent alternative is named beside it (for example GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5 for a Claude route; OpenAPI-described tools for MCP).`);
});

s = slide("CONTENT", "What holds across all seven lenses", "Seven lenses");
const holds = [["A named person approves", "Anything consequential: a support reply, a merged pull request, a payment run. The model drafts; a person decides."],
               ["Memory comes last", "Long-term memory of customer or client content waits; when built, it is a governed record class with erasure by person."],
               ["Configuration in source control", "Prompts, model pins and policies released through review, in Git, as one manifest."],
               ["An evidence record for every output", "Keyed by a trace ID, in a store the firm or its customer owns, never only in a vendor's."],
               ["A pinned, signed supply chain", "A five-person team is as exposed to a poisoned package as a bank."],
               ["Every model call through a gateway", "The firm's own or the customer's: one route to switch a model, enforce a budget and record the call."]];
holds.forEach((h, i) => card(s, 0.6 + (i % 3) * 4.1, 1.4 + Math.floor(i / 3) * 2.0, 3.9, 1.85, h[0], h[1], { headSize: 16, bodySize: 14 }));
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 5.5, w: 12.1, h: 1.25, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.text2 } });
T(s, "What changes is who owns the control plane, who pays for inference and which rulebook applies: deployer, operator, manufacturer, provider or supplier. Every lens keeps a second, unrelated model vendor qualified on the same evaluation set; only the reason for it changes.",
  { x: 0.85, y: 5.58, w: 11.6, h: 1.1, fontSize: 14, color: C.background1, valign: "middle" });
s.addNotes("Condensed from the checklists (x.11) of Parts XIII–XVIII against Part I.2 of the regulated-FS view. Fund the parts that never change first: they are what every customer, supervisor and acquirer asks about.");

// 27 Decisions
s = slide("CONTENT", "Decisions for the leadership team", "Close");
const asks = [["Adopt the reference architecture", "Control plane first; Stack A as the target; the lock-in rules as design policy"], ["Name the accountable owner", "An SMF for GenAI model risk and a GenAI standard to SS1/23 quality"],
              ["Fund Phases 0–2 now", "Governance, evaluation harness, gateway and two-vendor model access, with the exit drill before 18 March 2027"], ["Choose the first use case", "The attribution commentary: clear boundaries, checkable numbers, a named approver"]];
asks.forEach((a, i) => card(s, 0.6 + (i % 2) * 6.15, 1.4 + Math.floor(i / 2) * 2.55, 5.95, 2.35, a[0], a[1], { headSize: 18, bodySize: 15 }));
s.addNotes("Synthesis Part X Phase 0 scope and Part XI.7.");

// 28 Close
s = slide("TITLE", "Own the control plane. Rent the components.", "Close");
s.addText("Full evidence: master document (seven views, Parts I–XVIII), product technical appendix (138 scored products, fit by view), offline explorer with a view selector, dataset and source archive. Every claim is labelled and sourced. Researched and drafted with an Anthropic model; Anthropic items scored on the same rubric, with tiers set by the reader marked.", { placeholder: "body" });

s = slide("BRAND", null, "Close");
s.addNotes("Veyan. Truth, compounded. hello@veyan.ai");

const out = path.join(root, "Enterprise_GenAI_Stack_Oct2026/03_Slides/Executive_Deck.pptx");
require("fs").mkdirSync(path.dirname(out), { recursive: true });
pres.writeFile({ fileName: out }).then(async () => {
  const { applyTheme } = require(SKILL);
  await applyTheme(out, THEME);
  console.log("written", out);
});
