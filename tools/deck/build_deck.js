// Executive deck for the Enterprise GenAI Full-Stack Architecture review (October 2026).
// Usage: node tools/deck/build_deck.js <repo_root>
// Writes Enterprise_GenAI_Stack_Oct2026/03_Slides/Executive_Deck.pptx (PDF via LibreOffice afterwards).
const path = require("path");
const pptxgen = require("pptxgenjs");
const root = process.argv[2] || ".";
const tiers = require("./tiers.json");
const SKILL = "/root/.claude/skills/synced/4b999aaf-5960-40d2-8a19-a0619a4258dd_572bbe3b-9ae9-4d89-903d-a663b77e2e61/pptx/scripts/apply_theme.js";

const THEME = {
  name: "Regulated GenAI",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "16202E", lt1: "FFFFFF", dk2: "1B2A41", lt2: "EEF2F5",
    accent1: "0E7C7B", accent2: "1B2A41", accent3: "C9822B", accent4: "6B7A8F", accent5: "8FB9B8", accent6: "B3474B",
    hlink: "0E7C7B", folHlink: "6B7A8F",
  },
};
const HEX = { navy: "1B2A41", teal: "0E7C7B", amber: "C9822B", slate: "6B7A8F", ice: "EEF2F5", red: "B3474B", mint: "8FB9B8", ink: "16202E", white: "FFFFFF", line: "D5DCE3" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.title = "Enterprise GenAI Stack, October 2026";
pres.author = "Prepared for Bing Zhang (personal research)";
pres.company = "Personal research";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const FOOT = "Enterprise GenAI stack review · October 2026 · Personal research, not a description of any firm's platform";

pres.defineSlideMaster({
  title: "TITLE", background: { color: C.text2 },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.1, w: 11.7, h: 1.6, fontSize: 40, bold: true, color: C.background1, fontFace: THEME.headFontFace, valign: "bottom" }, text: "" } },
            { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.9, w: 11.7, h: 1.6, fontSize: 18, color: C.background2, valign: "top" }, text: "" } }],
});
pres.defineSlideMaster({
  title: "SECTION", background: { color: C.text2 },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.6, w: 11.7, h: 1.2, fontSize: 36, bold: true, color: C.background1, fontFace: THEME.headFontFace }, text: "" } },
            { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.9, w: 11.7, h: 1.0, fontSize: 18, color: C.accent5 }, text: "" } }],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: C.background1 },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.9, fontSize: 28, bold: true, color: C.text2, fontFace: THEME.headFontFace, valign: "middle" }, text: "" } },
            { text: { text: FOOT, options: { x: 0.6, y: 7.0, w: 10.5, h: 0.3, fontSize: 9, color: C.accent4 } } }],
  slideNumber: { x: 12.3, y: 7.0, w: 0.5, h: 0.3, fontSize: 9, color: C.accent4 },
});

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
let s = slide("TITLE", "The enterprise GenAI stack, October 2026", "Opening");
s.addText("What changed since the popular stack diagram, what a regulated asset manager should select, and what to deliberately not build yet", { placeholder: "body" });
T(s, "Reference architecture review · 9 layers · 8 enterprise controls · 140 products · Personal research", { x: 0.8, y: 6.3, w: 11.7, h: 0.4, fontSize: 12, color: C.accent5 });
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
s = slide("CONTENT", "What we reviewed, and how much had moved", "Opening");
const stats = [["80", "tiles in the original graphic", C.text2], ["39", "of 80 tiles out of date: acquired, renamed, mislabelled or unverifiable", C.accent6], ["140", "products profiled (80 tiles, 48 controls, 12 additions)", C.accent1], ["1,255", "sources logged with URL and access date", C.accent3]];
stats.forEach((st, i) => {
  const x = 0.6 + i * 3.08;
  T(s, st[0], { x, y: 1.7, w: 2.9, h: 1.3, fontSize: 60, bold: true, color: st[2], fontFace: THEME.headFontFace });
  T(s, st[1], { x, y: 3.0, w: 2.8, h: 1.0, fontSize: 14, color: C.text1 });
});
T(s, "How the work was done", { x: 0.6, y: 4.35, w: 12, h: 0.4, fontSize: 16, bold: true, color: C.text2 });
T(s, [{ text: "Eight parallel research streams, primary sources first; two adversarial verifiers re-checked 192 high-risk claims (no fabrications found).", options: { bullet: true, breakLine: true } },
      { text: "Seventeen chapters on a 13-part template, each product scored 1–5 on eight criteria with generic and regulated-FS weights.", options: { bullet: true, breakLine: true } },
      { text: "Reader checkpoints decided the scoring rules and the contested tiers; every claim is labelled verified, reported, judgement or recommendation.", options: { bullet: true } }],
  { x: 0.6, y: 4.8, w: 12, h: 1.9, fontSize: 14, paraSpaceAfter: 6 });
s.addNotes("Numbers from the dataset build (05_Data/products.json, bibliography.xlsx). Limitation: no vendor audit report was read; many facts come from dated search extracts because the research environment blocked direct fetching of most vendor sites.");

// 4 Ten findings
s = slide("CONTENT", "Ten findings that change the picture", "What changed");
const f = [["Catalogue → control system", "None of the eight enterprise controls appears in the graphic."], ["Neutral tools were bought", "Arize, Langfuse, Promptfoo, Portkey, Lakera, Voyage, Jina and others changed hands."],
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
s = slide("CONTENT", "Independence can no longer be assumed from a product's origins", "What changed");
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
s = slide("CONTENT", "The regulatory anchors moved in 2026", "What changed");
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
s.addText("Eight hypotheses tested; nine layers renamed, split or merged; one control plane added", { placeholder: "body" });

// 8 Revised model
s = slide("CONTENT", "Four planes under one firm-owned control plane", "The architecture");
const planes = [["CONTROL PLANE (firm-owned)", "C1 AI traffic gateway · C2 guardrails · C3 privacy service · C4 identity · C5 configuration of record · C6 FinOps · C7 AI security · C8 governance and evidence store", C.text2, C.background1],
                ["EVALUATION AND OBSERVABILITY PLANE (L9)", "Firm OpenTelemetry collector · platform of record · CI and online evaluations · two red-team tools", C.accent1, C.background1],
                ["AGENT PLANE (L3, L4)", "Workflows by default · bounded agent steps · durable execution · tools behind a governance sub-layer", C.background2, C.text2],
                ["KNOWLEDGE PLANE (L8, L7, L6 + L5)", "Ingestion envelope · retrieval optimisation (embed + rerank) · derived, entitlement-filtered stores · memory service last", C.background2, C.text2],
                ["MODEL PLANE (L2, L1)", "In-region model access · vLLM exit route · two-vendor portfolio + small + open-weight", C.background2, C.text2]];
planes.forEach((p, i) => { const y = 1.4 + i * 1.08;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y, w: 8.4, h: 0.95, rectRadius: 0.06, fill: { color: p[2] }, line: { color: p[2] } });
  T(s, p[0], { x: 0.8, y: y + 0.07, w: 8.0, h: 0.35, fontSize: 13, bold: true, color: p[3] });
  T(s, p[1], { x: 0.8, y: y + 0.42, w: 8.0, h: 0.5, fontSize: 12, color: p[3] }); });
card(s, 9.3, 1.4, 3.4, 5.25, "How to read it", "The control plane governs every call and holds the evidence. Planes beneath it are built from replaceable products.\n\nLayer numbers are kept for traceability; names changed where the evidence required it.", { bodySize: 14 });
s.addNotes("Synthesis Part IV.1 (revised layer model and diagram).");

// 9 Hypotheses
s = slide("CONTENT", "Hypothesis verdicts: what the evidence did to the nine layers", "The architecture");
table(s, [["#", "Hypothesis", "Verdict"],
  ["H1", "Split inference; promote the gateway", "Split L2 into access, serving, optimisation; gateway becomes C1 (model, tool and agent traffic)"],
  ["H2", "Agent framework is not one layer", "Split: deterministic workflows (default), bounded agent steps, durable execution"],
  ["H3", "Identity and tool governance", "Keep: a tool-governance sub-layer in L4; C4 and C7 make the decisions"],
  ["H4", "Memory vs retrieval", "Merge into the stores layer as a governed memory service; build it last"],
  ["H5", "Rename vector databases", "Rename L6 'Retrieval, knowledge and memory stores'"],
  ["H6", "Embeddings + reranking", "Merge into L7 'Retrieval optimisation'"],
  ["H7", "Ingestion needs lineage, DLP, ACLs", "Keep, widened: a built ingestion envelope around replaceable parsers"],
  ["H8", "Evaluation is cross-cutting", "Reposition L9 as an evidence plane; one evidence store with C8"]],
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
    showTitle: true, title: "Products by tier, layer (L9→L1) and control (C1→C8)", titleFontSize: 13, titleColor: HEX.navy, titleFontFace: "+mn-lt" });
card(s, 9.1, 1.35, 3.6, 2.5, "A Strategic tier carries a condition", "18 of the 58 apply only where a given cloud is primary, or where a platform is already operated. The condition is the decision.", { bodySize: 13 });
card(s, 9.1, 4.05, 3.6, 2.75, "What drives the tiers", "Regulated-FS weights favour deployment flexibility and low lock-in, so open, self-hostable components take most Strategic slots. No commercial governance tool reached Strategic on public evidence.", { bodySize: 13 });
s.addNotes("Data: 05_Data/products.json after CP4. Strategic counts by area from the scorecard; tiers are judgements under rules 9–13, not thresholds.");

// 13 Cloud-neutral core
s = slide("CONTENT", "The cloud-neutral core we would select today", "What to select");
table(s, [["Layer / control", "Selection", "Independent alternative or note"],
  ["C1 gateway", "LiteLLM Enterprise (hardened, pinned) or Kong AI Gateway", "Cloud gateway where that cloud is primary"],
  ["L9 evaluation", "Langfuse or MLflow + firm OpenTelemetry collector", "Two red-team tools, one vendor-independent"],
  ["C3 privacy / C4 identity", "Presidio behind a privacy API · workforce IdP + OPA + SPIFFE", "Cloud DLP / Entra Agent ID per cloud"],
  ["C5 configuration", "Git as configuration of record; prompts as code", "Vendor registries are caches only"],
  ["L8 ingestion", "Docling + Unstructured inside a built envelope", "Specialist parsers for hard documents"],
  ["L7 / L6 retrieval", "Sentence Transformers + pgvector (or Elasticsearch where run)", "Qdrant or Milvus after a failed load test"],
  ["L4 tools", "Read-only MCP tools behind a governed gateway", "OpenAPI tools (MCP originated at Anthropic)"],
  ["L3 orchestration", "LangGraph on Temporal", "Microsoft Agent Framework, ADK, Pydantic AI"],
  ["L2 inference", "Primary cloud's in-region model service + vLLM exit route", "SGLang as backup engine once its CVE fix is confirmed"],
  ["L1 models", "Two vendors from OpenAI, Anthropic, Mistral, Gemini; Gemma 4 or Mistral self-hosted", "For Claude: GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5"]],
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
s.addNotes("Chapter 1 (foundation models) and synthesis Part I.4. Disclosure: the drafting model is Anthropic's; Anthropic was scored on the same rubric and its tier was set by the reader.");

// 15 Keep/remove/missing
s = slide("CONTENT", "Keep, remove, add", "What to select");
const krm = [["Keep", "The nine-layer spine as a teaching device · vLLM · LangGraph · Docling · pgvector, Qdrant, Milvus, Elasticsearch · Langfuse, LangSmith · MCP and A2A behind a governed gateway · the portfolio model vendors", C.accent1],
             ["Remove or demote", "Labels that do not exist (Gemma 2.9, QI4) · unverifiable tiles (EthicalAgents, Ragoos) · archived TGI · a router as 'the' access layer · memory as its own infrastructure layer · desktop runtimes in production", C.accent6],
             ["Add", "AI traffic gateway · guardrails as policy · privacy service · agent identity and tool governance · configuration of record · FinOps · AI security · governance and evidence store · durable execution · ingestion envelope", C.accent3]];
krm.forEach((k, i) => { const x = 0.6 + i * 4.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.4, w: 3.9, h: 0.6, rectRadius: 0.06, fill: { color: k[2] }, line: { color: k[2] } });
  T(s, k[0], { x: x + 0.2, y: 1.45, w: 3.5, h: 0.5, fontSize: 17, bold: true, color: C.background1, valign: "middle" });
  T(s, k[1], { x: x + 0.1, y: 2.15, w: 3.7, h: 4.5, fontSize: 14 }); });
s.addNotes("Synthesis Part I.3.");

// 16 Avoid
s = slide("CONTENT", "Deliberately not selected, on evidence", "What to select");
table(s, [["Avoid", "Why"],
  ["Archived or deprecated: TGI, OpenAI Agent Builder, AutoGen for new code, Helicone, Zep Community Edition", "Archived, shut down, superseded or in maintenance mode"],
  ["EthicalAgents, Ragoos", "Could not be verified as real products"],
  ["A third-party broker holding client tokens (Composio managed cloud)", "Unresolved token-exposure incident, May 2026"],
  ["Any Chinese-origin vendor's own API for client data", "PRC storage and unremediated regulatory findings"],
  ["Jina weights, MinerU above thresholds, a modified AGPL Firecrawl server", "Licence blockers without a commercial licence"],
  ["LM Studio as a service; training-on-data model tiers", "Terms blockers"],
  ["Billing intermediation through a gateway or router", "Puts a vendor between the firm and its model contract"]],
  { x: 0.6, y: 1.4, w: 12.1, colW: [7.2, 4.9], fs: 15 });
T(s, "Not avoided but not yet: memory, autonomous agents with write tools, multi-agent delegation, fine-tuning, own-GPU fleets, dedicated vector databases without a failed load test.", { x: 0.6, y: 5.9, w: 12.1, h: 0.8, fontSize: 14, italic: true, color: C.text2 });
s.addNotes("Synthesis Part XI.5 (evidence-based avoid list, CP4-7) and Stack A 'do not build yet'.");

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
               ["4", "House style", "Retrieval of prior commentary (L8–L6)"], ["5", "Draft", "Model via the gateway, in region (C1, L2, L1)"], ["6", "Evaluate", "Every figure matches the engine (L9, C2)"],
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
  ["Gateway (C1), guardrails (C2), privacy (C3)", "Hybrid", "Routes, policies, test sets, keys; the product is replaceable"],
  ["Identity (C4)", "Buy the IdP, build the policy", "Agent registration, policies in Git"],
  ["Configuration (C5), FinOps (C6)", "Build (thin)", "Release manifest, evaluation gate, allocation rules"],
  ["Governance (C8)", "Build the store, buy the workflow", "Evidence store and inventory outlive any tool"],
  ["Evaluation (L9)", "Hybrid", "Datasets and scorers in Git; platform replaceable"],
  ["Ingestion (L8)", "Build the envelope", "No product emits lineage; parsers adopted"],
  ["Stores (L6)", "Reuse what is run", "Retrieval interface and rebuild pipeline"],
  ["Models (L1)", "Buy; adopt open weights", "Portfolio policy, qualification suite, retirement calendar"],
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

// 27 Decisions
s = slide("CONTENT", "Decisions for the leadership team", "Close");
const asks = [["Adopt the reference architecture", "Control plane first; Stack A as the target; the lock-in rules as design policy"], ["Name the accountable owner", "An SMF for GenAI model risk and a GenAI standard to SS1/23 quality"],
              ["Fund Phases 0–2 now", "Governance, evaluation harness, gateway and two-vendor model access, with the exit drill before 18 March 2027"], ["Choose the first use case", "The attribution commentary: clear boundaries, checkable numbers, a named approver"]];
asks.forEach((a, i) => card(s, 0.6 + (i % 2) * 6.15, 1.4 + Math.floor(i / 2) * 2.55, 5.95, 2.35, a[0], a[1], { headSize: 18, bodySize: 15 }));
s.addNotes("Synthesis Part X Phase 0 scope and Part XI.7.");

// 28 Close
s = slide("TITLE", "Own the control plane. Rent the components.", "Close");
s.addText("Full evidence: master document (Word/PDF), product technical appendix (138 scored products), offline explorer, dataset and source archive. Every claim is labelled and sourced. Researched and drafted with an Anthropic model; Anthropic items scored on the same rubric, with tiers set by the reader marked.", { placeholder: "body" });

const out = path.join(root, "Enterprise_GenAI_Stack_Oct2026/03_Slides/Executive_Deck.pptx");
require("fs").mkdirSync(path.dirname(out), { recursive: true });
pres.writeFile({ fileName: out }).then(async () => {
  const { applyTheme } = require(SKILL);
  await applyTheme(out, THEME);
  console.log("written", out);
});
