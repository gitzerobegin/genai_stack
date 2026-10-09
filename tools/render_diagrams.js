// Render the editable Mermaid diagrams to PNG (for the Word/PDF documents) and HTML (for viewing in a browser).
// Source files: Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/*.md — each has a "# Title" line, optional
// "Caption: ..." line, and one ```mermaid block. Edit the .md, then run:
//   NODE_PATH=$(npm root -g) node tools/render_diagrams.js [file.md ...]      (no arguments = all diagrams)
// Needs: cd tools/diagrams && npm install mermaid@11.17.2   (and Playwright, as for render_graphic.js)
const fs = require("fs"), path = require("path");
const { chromium } = require("playwright");
const DIR = "Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams";
const MERMAID = path.resolve("tools/diagrams/node_modules/mermaid/dist/mermaid.min.js");
const CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.min.js";
const INIT = { startOnLoad: false, theme: "base", securityLevel: "strict",
  themeVariables: { fontFamily: "Inter, Arial, sans-serif", fontSize: "15px", primaryColor: "#EEF3F8", primaryBorderColor: "#2E6DA4",
    primaryTextColor: "#0B1B33", secondaryColor: "#F5F1E8", secondaryBorderColor: "#D4A13A", tertiaryColor: "#FBF4E4",
    tertiaryBorderColor: "#D4A13A", lineColor: "#0B1B33", clusterBkg: "#F5F1E8", clusterBorder: "#D4A13A", edgeLabelBackground: "#FFFFFF" },
  flowchart: { htmlLabels: true, curve: "basis", wrappingWidth: 240, nodeSpacing: 36, rankSpacing: 44, padding: 10 } };

function parse(file) {
  const t = fs.readFileSync(file, "utf8");
  const title = (t.match(/^#\s+(.+)$/m) || [, path.basename(file, ".md")])[1].trim();
  const cap = (t.match(/^Caption:\s*(.+)$/m) || [, ""])[1].trim();
  const m = t.match(/```mermaid\s*\n([\s\S]*?)```/);
  if (!m) throw new Error(file + ": no ```mermaid block");
  return { title, cap, code: m[1] };
}
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
function page(d, script) {
  return `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>${esc(d.title)}</title>
<!-- Generated from the .md file of the same name by tools/render_diagrams.js. Edit the .md (Mermaid), not this file. -->
<style>body{margin:0;font-family:Inter,Arial,sans-serif;color:#0B1B33;background:#fff}
#fig{display:inline-block;padding:18px 22px 14px;background:#fff}
.k{font-size:11px;letter-spacing:4px;color:#D4A13A;text-transform:uppercase}.t{font-size:19px;font-weight:800;margin:4px 0 2px}
.r{width:48px;height:3px;background:#D4A13A;margin:6px 0 12px}.c{font-size:12.5px;color:#5B6B7A;margin-top:8px;max-width:1100px}
.mermaid{max-width:1300px}</style>
<script src="${script}"></script></head><body><div id="fig"><div class="k">Veyan · the view at end of Q3 2026</div><div class="t">${esc(d.title)}</div><div class="r"></div>
<pre class="mermaid">${esc(d.code)}</pre>${d.cap ? `<div class="c">${esc(d.cap)}</div>` : ""}</div>
<script>mermaid.initialize(${JSON.stringify(INIT)});mermaid.run().then(()=>{document.body.dataset.done="1"}).catch(e=>{document.body.dataset.err=String(e && e.message || e)});</script></body></html>`;
}
(async () => {
  let files = process.argv.slice(2);
  if (!files.length) files = fs.readdirSync(DIR).filter((f) => f.endsWith(".md")).sort().map((f) => path.join(DIR, f));
  const browser = await chromium.launch();
  const pg = await browser.newPage({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: 2 });
  let bad = 0;
  for (const f of files) {
    const d = parse(f), base = f.replace(/\.md$/, "");
    fs.writeFileSync(base + ".html", page(d, CDN));
    await pg.setContent(page(d, "file://" + MERMAID), { waitUntil: "load" });
    await pg.addScriptTag({ path: MERMAID }).catch(() => {});
    await pg.evaluate((init) => { if (!document.body.dataset.done) { mermaid.initialize(init); return mermaid.run().then(() => { document.body.dataset.done = "1"; }).catch((e) => { document.body.dataset.err = String(e && e.message || e); }); } }, INIT);
    await pg.waitForFunction(() => document.body.dataset.done || document.body.dataset.err, null, { timeout: 20000 });
    const err = await pg.evaluate(() => document.body.dataset.err);
    if (err) { console.log("ERROR", f, err.slice(0, 300)); bad++; continue; }
    await (await pg.$("#fig")).screenshot({ path: base + ".png" });
    console.log("ok", base + ".png");
  }
  await browser.close();
  if (bad) process.exit(1);
})();
