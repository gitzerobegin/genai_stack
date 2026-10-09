// Render the LinkedIn post visuals: one editable Markdown source per post, rendered to HTML, PNG and PDF.
// Sources: Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md (P00 = series introduction).
// Each source has:
//   # Title                                   (headline on the card)
//   Post: 1 · Week 1, Tuesday · L1 Foundation models
//   Caption: one-line footer (what the reader should take away; say "illustrative" where it is)
//   Source: L1 §1.9 and §1.12                 (where the content comes from in the review)
//   Format: portrait | square | landscape     (optional; default portrait 1080x1350, LinkedIn's 4:5 feed size)
// and ONE fenced block: ```html (a fragment using the classes in CSS below, plus an optional <style>) or ```mermaid.
// Edit the .md, then run:
//   NODE_PATH=$(npm root -g) node tools/render_post_visuals.js [P01.md ...]      (no arguments = all)
// Output next to the source: P<NN>.html (stand-alone, open in a browser), P<NN>.png (2x, for posting and the
// documents) and P<NN>.pdf (one page, vector). Vendor-neutral: no vendor or product names on the cards.
const fs = require("fs"), path = require("path");
const { chromium } = require("playwright");
const DIR = "Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin";
const MERMAID = path.resolve("tools/diagrams/node_modules/mermaid/dist/mermaid.min.js");
const CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.min.js";
const SIZES = { portrait: [1080, 1350], square: [1080, 1080], landscape: [1200, 675] };
const INIT = { startOnLoad: false, theme: "base", securityLevel: "strict",
  themeVariables: { fontFamily: "Inter, Arial, sans-serif", fontSize: "20px", primaryColor: "#FFFFFF", primaryBorderColor: "#2E6DA4",
    primaryTextColor: "#0B1B33", secondaryColor: "#F5F1E8", secondaryBorderColor: "#D4A13A", tertiaryColor: "#FBF4E4",
    tertiaryBorderColor: "#D4A13A", lineColor: "#0B1B33", clusterBkg: "#FFFFFF", clusterBorder: "#D4A13A", edgeLabelBackground: "#F5F1E8" },
  flowchart: { htmlLabels: true, curve: "basis", wrappingWidth: 260, nodeSpacing: 30, rankSpacing: 36, padding: 12 } };

// Component library shared by every card. Colours: Veyan navy, gold, blue, sky, warm; green/amber/red for status.
const CSS = `
:root{--navy:#0B1B33;--gold:#D4A13A;--blue:#2E6DA4;--sky:#9DBBDB;--warm:#F5F1E8;--mute:#5B6B7A;--line:#D9D2C3;
 --green:#2F7D5B;--greenbg:#E5F2EC;--amber:#B07A1A;--amberbg:#FBF0DA;--red:#B3474B;--redbg:#F7E3E3;--bluebg:#EAF1F8}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;color:var(--navy);background:#fff}
.card{width:var(--w);height:var(--h);background:var(--warm);display:flex;flex-direction:column;padding:54px 60px 40px;position:relative;overflow:hidden}
.card:before{content:"";position:absolute;right:-140px;top:-140px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(212,161,58,.18),rgba(212,161,58,0) 70%)}
.hd{display:flex;justify-content:space-between;align-items:flex-start;gap:24px}
.kick{font-size:17px;letter-spacing:5px;color:var(--gold);text-transform:uppercase;font-weight:700}
.title{font-size:44px;line-height:1.12;font-weight:800;letter-spacing:-.5px;margin:12px 0 0}
.rule{width:72px;height:4px;background:var(--gold);margin:18px 0 0}
.logo{height:46px;flex:none;margin-top:2px}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;margin:26px 0 18px;min-height:0;font-size:21px;line-height:1.3}
.ft{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;border-top:2px solid var(--line);padding-top:14px;font-size:16px;color:var(--mute);line-height:1.35}
.ft .cap{max-width:80%}.ft .src{text-align:right;white-space:nowrap}
/* building blocks */
.row{display:flex;gap:16px;align-items:stretch}.col{display:flex;flex-direction:column;gap:12px}.grow{flex:1}
.center{align-items:center;justify-content:center;text-align:center}
.box{background:#fff;border:2px solid var(--line);border-radius:16px;padding:16px 18px}
.box.navy{background:var(--navy);color:#fff;border-color:var(--navy)}.box.navy .sub{color:var(--sky)}
.box.gold{border-color:var(--gold);background:#FBF4E4}.box.blue{border-color:var(--blue);background:var(--bluebg)}
.box.green{border-color:var(--green);background:var(--greenbg)}.box.amber{border-color:var(--amber);background:var(--amberbg)}
.box.red{border-color:var(--red);background:var(--redbg)}.box.grey{border-style:dashed;color:#8792A0;background:#F3F1EC}
.box.dash{border-style:dashed}
.h{font-weight:800;font-size:23px}.sub{font-size:18px;color:var(--mute);margin-top:4px}.small{font-size:16px}.big{font-size:56px;font-weight:800;line-height:1}
.lab{font-size:15px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:var(--blue)}
.code{display:inline-block;background:var(--navy);color:#fff;font-weight:800;border-radius:7px;padding:2px 9px;font-size:17px;margin-right:8px}
.code.g{background:var(--gold);color:var(--navy)}
.chip{display:inline-block;border-radius:999px;padding:4px 13px;font-size:16px;font-weight:600;background:var(--bluebg);color:var(--navy);margin:3px 4px 3px 0}
.chip.green{background:var(--greenbg);color:var(--green)}.chip.amber{background:var(--amberbg);color:#7A5410}.chip.red{background:var(--redbg);color:var(--red)}
.chip.navy{background:var(--navy);color:#fff}.chip.gold{background:var(--gold);color:var(--navy)}
.arrow{color:var(--blue);font-size:30px;line-height:1;text-align:center;font-weight:700}
.arrow.r:after{content:"\\2192"}.arrow.d:after{content:"\\2193"}.arrow.l:after{content:"\\2190"}.arrow.u:after{content:"\\2191"}
.flow{display:flex;flex-direction:column;gap:6px}.flow>.arrow{margin:-2px 0}
.hflow{display:flex;align-items:center;gap:8px}
.tag{font-size:14px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--gold)}
.note{font-size:17px;color:var(--mute);font-style:italic}
table.t{border-collapse:separate;border-spacing:0;width:100%;font-size:17px;background:#fff;border:2px solid var(--line);border-radius:14px;overflow:hidden}
table.t th{background:var(--navy);color:#fff;text-align:left;padding:10px 12px;font-size:16px}
table.t td{padding:8px 12px;border-top:1px solid #ECE6DA;vertical-align:top}
.mermaid{display:flex;justify-content:center}.mermaid svg{max-width:100%;max-height:100%}
`;

function parse(file) {
  const t = fs.readFileSync(file, "utf8");
  const get = (k) => ((t.match(new RegExp("^" + k + ":\\s*(.+)$", "m")) || [, ""])[1]).trim();
  const title = (t.match(/^#\s+(.+)$/m) || [, path.basename(file, ".md")])[1].trim();
  const m = t.match(/```(html|mermaid)\s*\n([\s\S]*?)```/);
  if (!m) throw new Error(file + ": no ```html or ```mermaid block");
  const fmt = (get("Format") || "portrait").toLowerCase();
  if (!SIZES[fmt]) throw new Error(file + ": unknown Format " + fmt);
  return { title, post: get("Post"), cap: get("Caption"), src: get("Source"), fmt, kind: m[1], code: m[2] };
}
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
function page(d, script, logo) {
  const [w, h] = SIZES[d.fmt];
  const inner = d.kind === "mermaid" ? `<pre class="mermaid">${esc(d.code)}</pre>` : d.code;
  const mm = d.kind === "mermaid" ? `<script src="${script}"></script>` : "";
  const run = d.kind === "mermaid"
    ? `<script>mermaid.initialize(${JSON.stringify(INIT)});mermaid.run().then(()=>{document.body.dataset.done="1"}).catch(e=>{document.body.dataset.err=String(e&&e.message||e)});</script>`
    : `<script>document.body.dataset.done="1"</script>`;
  return `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=${w}">
<title>${esc(d.title)}</title>
<!-- Generated from ${path.basename(d.file)} by tools/render_post_visuals.js. Edit the .md, not this file. -->
<style>${CSS}</style>${mm}</head><body>
<div class="card" id="card" style="--w:${w}px;--h:${h}px">
 <div class="hd"><div><div class="kick">${esc(d.post ? d.post.replace(/ · Week.*?·/, " ·") : "The Enterprise GenAI Stack")}</div>
  <div class="title">${esc(d.title)}</div><div class="rule"></div></div>
  <img class="logo" src="${logo}" alt="Veyan"></div>
 <div class="body">${inner}</div>
 <div class="ft"><div class="cap">${esc(d.cap)}</div><div class="src">Veyan · the view at end of Q3 2026${d.src ? "<br>Source: " + esc(d.src) : ""}</div></div>
</div>${run}</body></html>`;
}
(async () => {
  let files = process.argv.slice(2);
  if (!files.length) files = fs.readdirSync(DIR).filter((f) => /^P\d+\.md$/.test(f)).sort().map((f) => path.join(DIR, f));
  const browser = await chromium.launch();
  let bad = 0;
  for (const f of files) {
    let d;
    try { d = parse(f); } catch (e) { console.log("ERROR", e.message); bad++; continue; }
    d.file = f;
    const base = f.replace(/\.md$/, ""), [w, h] = SIZES[d.fmt];
    fs.writeFileSync(base + ".html", page(d, CDN, "../veyan_lockup.png"));
    const tmp = base + ".render.tmp.html";
    fs.writeFileSync(tmp, page(d, "file://" + MERMAID, "../veyan_lockup.png"));
    const pg = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await pg.goto("file://" + path.resolve(tmp), { waitUntil: "load" });
    await pg.waitForFunction(() => document.body.dataset.done || document.body.dataset.err, null, { timeout: 20000 }).catch(() => {});
    await pg.evaluate(() => document.fonts.ready);
    const err = await pg.evaluate(() => document.body.dataset.err);
    // overflow check: the body region must not be clipped
    const over = await pg.evaluate(() => { const b = document.querySelector(".body"); return b.scrollHeight - b.clientHeight; });
    if (err) { console.log("ERROR", f, err.slice(0, 300)); bad++; fs.unlinkSync(tmp); await pg.close(); continue; }
    await (await pg.$("#card")).screenshot({ path: base + ".png" });
    await pg.pdf({ path: base + ".pdf", width: w + "px", height: h + "px", printBackground: true, pageRanges: "1" });
    fs.unlinkSync(tmp);
    console.log(over > 2 ? "WARN overflow " + over + "px" : "ok", base + ".png");
    if (over > 2) bad++;
    await pg.close();
  }
  await browser.close();
  if (bad) process.exit(1);
})();
