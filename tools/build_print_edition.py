#!/usr/bin/env python3
"""Build the print and ebook editions of the master document (for KDP or any print-on-demand service).

Usage: python3 -I tools/build_print_edition.py <repo_root> [--no-pdf] [--no-epub] [--no-cover]
Run tools/build_master.py first (it writes work/stageD/Master_Architecture.pandoc.md, the source used here).
Settings and metadata: tools/print/book.json (title, author, ISBNs, trim size, margins, paper, blurb).

Writes Enterprise_GenAI_Stack_Oct2026/01_Report/Print/:
  Interior.pdf          print interior: trim size, mirrored margins, recto Part openers, running heads, fonts embedded
  Interior.docx         the same content as an editable Word file (layout features are applied in LibreOffice)
  Cover_Paperback.pdf   full-wrap cover (back, spine, front, 0.125 in bleed), spine width from the interior's page count
  Cover_Front.jpg       front cover for the ebook and the store page (1600 x 2560)
  Ebook.epub            reflowable EPUB 3 for Kindle (upload the EPUB to KDP) and other stores
  cover.html            the editable cover source (re-render with this script)
The publishing checklist and the specification notes are in Print/Publishing_Kit.md.
"""
import json, os, re, shutil, subprocess, sys, zipfile

root = sys.argv[1]; os.chdir(root)
B = json.load(open("tools/print/book.json", encoding="utf-8"))
OUT = "Enterprise_GenAI_Stack_Oct2026/01_Report/Print"; WORK = "work/stageD/print"
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
SRC = "work/stageD/Master_Architecture.pandoc.md"
if not os.path.exists(SRC):
    sys.exit("Run tools/build_master.py first: %s is missing" % SRC)
FMT = "markdown+pipe_tables+bracketed_spans+footnotes+fenced_divs+raw_attribute-implicit_figures-tex_math_dollars-raw_tex-tex_math_single_backslash"

# ---------------------------------------------------------------- 1. print reference document
def make_reference():
    ref = os.path.join(WORK, "reference_print.docx")
    zin = zipfile.ZipFile("tools/templates/reference.docx")
    zout = zipfile.ZipFile(ref, "w", zipfile.ZIP_DEFLATED)
    sizes = {"Normal": 20, "BodyText": 20, "FirstParagraph": 20, "Compact": 17, "FootnoteText": 14,
             "Heading1": 44, "Heading2": 32, "Heading3": 24, "Heading4": 21}
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/styles.xml":
            s = data.decode("utf-8")
            for sid, sz in sizes.items():
                m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, s, re.S)
                if m:
                    blk = re.sub(r'<w:sz w:val="\d+"/>', '<w:sz w:val="%d"/>' % sz, m.group(0))
                    blk = re.sub(r'<w:szCs w:val="\d+"/>', '<w:szCs w:val="%d"/>' % sz, blk)
                    s = s.replace(m.group(0), blk)
            data = s.encode("utf-8")
        elif item.filename == "word/document.xml":
            s = data.decode("utf-8")
            s = re.sub(r"<w:headerReference [^>]*/>|<w:footerReference [^>]*/>", "", s)
            tw = lambda inch: int(round(inch * 1440))
            w, h = B["trim_in"]; m = B["margins_in"]
            s = re.sub(r"<w:pgSz [^>]*/>", '<w:pgSz w:w="%d" w:h="%d"/>' % (tw(w), tw(h)), s)
            s = re.sub(r"<w:pgMar [^>]*/>", '<w:pgMar w:top="%d" w:right="%d" w:bottom="%d" w:left="%d" w:header="432" w:footer="432" w:gutter="0"/>'
                       % (tw(m["top"]), tw(m["outside"]), tw(m["bottom"]), tw(m["inside"])), s)
            data = s.encode("utf-8")
        elif item.filename == "word/settings.xml":
            s = data.decode("utf-8")
            if "<w:mirrorMargins/>" not in s:
                s = s.replace("<w:zoom", "<w:mirrorMargins/><w:evenAndOddHeaders/><w:zoom", 1)
            data = s.encode("utf-8")
        zout.writestr(item, data)
    zout.close()
    return ref

# ---------------------------------------------------------------- 2. book markdown
def esc(s): return s.replace("*", "\\*")
isbn = lambda k, label: ("ISBN %s (%s)" % (B[k], label)) if B.get(k) else "ISBN (%s): to be assigned" % label
TOC = ('```{=openxml}\n<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
       '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click and update the table of contents.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>\n```\n')
front = f"""::: {{custom-style="HalfTitle"}}
{esc(B['title'])}
:::

::: {{custom-style="BookTitle"}}
{esc(B['title'])}
:::

::: {{custom-style="BookSubtitle"}}
{esc(B['subtitle'])}
:::

::: {{custom-style="BookAuthor"}}
{esc(B['author'])}
:::

::: {{custom-style="BookLogo"}}
![{B['publisher']}](brand/veyan_lockup.png){{width=2.4in}}
:::

::: {{custom-style="Copyright"}}
**{esc(B['title'])}: {esc(B['short_subtitle'])}**

Copyright © {B['year']} {esc(B['copyright_holder'])}. All rights reserved. No part of this book may be reproduced, stored in a retrieval system or transmitted in any form or by any means without the prior written permission of the publisher, except for brief quotations in reviews and articles.

Published by {B['publisher']}. {B['edition']}. Evidence as of {B['evidence_date']}.

{isbn('isbn_paperback', 'paperback')} · {isbn('isbn_hardcover', 'hardcover')} · {isbn('isbn_ebook', 'ebook')}

**Not advice, and not a description of any firm.** This book sets out a reference architecture and the author's assessment of products and regulation. It is not investment, legal, regulatory or tax advice. It does not describe any firm's actual platform, vendor choices or internal systems. The worked example is generic and illustrative. Product facts, prices, certifications, ownership and regulatory dates are stated as at the dates given and change frequently; verify them before relying on them.

**Trademarks.** Product and company names are trademarks or registered trademarks of their respective owners. Their mention does not imply endorsement by, or affiliation with, those owners.

**How this book was made.** The research and drafting were carried out with Claude, an AI model made by Anthropic, under the author's direction, with the author's decisions recorded at five review checkpoints. Anthropic's products are assessed on the same rubric as every other vendor's; the disclosure after the contents explains how the conflict of interest was handled.

Cover and interior design: {B['publisher']}.
:::

::: {{custom-style="ContentsTitle"}}
Contents
:::

{TOC}
# About this book

Most enterprise GenAI diagrams are shelves of product logos. This book presents the enterprise GenAI stack as it stands at the end of Q3 2026: nine layers, from foundation models (L1) to evaluation and observability (L9), under a firm-owned control plane of eight components (C1 to C8). The popular stack diagram was its inspiration and baseline; Part XII sets out what changed since that diagram [AJ].

It is written for the people who must make GenAI work inside a regulated firm: enterprise and solution architects, technology and data leaders, model-risk, compliance and operational-resilience teams, and the engineers who build the platform [AJ].

| Part | What it covers |
|---|---|
| Disclosure and final tiers | The conflict-of-interest disclosure and the final tier decisions |
| Part I | Executive summary: ten findings, the architecture on one page, how to read the tiers |
| Part II | Method, evidence base, claim labels, scorecard and limitations |
| Chapters 1 to 9 | The nine layers, L1 to L9 |
| Chapters C1 to C8 | The eight cross-cutting enterprise controls |
| Parts III to XI | Hypotheses, reference architecture, the financial-services view, the worked example, four reference stacks, build versus buy, lock-in, the roadmap and the final recommended stack |
| Part XII | What changed since the popular stack diagram |
| Annex | Sources, data and companion files |

# How to read this book

**If you have thirty minutes,** read Part I. **If you design platforms,** read Parts I, IV and VII, then the chapters for the layers you own. **If you own risk or compliance,** read Part V, chapter C8 and the worked example in Part VI. **If you build,** start with each chapter's decision tree (section x.9) and worked-example slice (x.12) [AJ].

Every chapter follows the same thirteen sections, so any two chapters can be read side by side [AJ]:

| Section | Content | Section | Content |
|---|---|---|---|
| x.1 | Responsibility | x.8 | Comparison table |
| x.2 | Why it matters | x.9 | Decision tree |
| x.3 | Goals and KPIs | x.10 | Lock-in classification |
| x.4 | How it works | x.11 | Regulated financial-services lens |
| x.5 | Enterprise design principles | x.12 | Worked-example slice |
| x.6 | Product selection criteria | x.13 | What changed since the popular stack diagram |
| x.7 | Product deep dives | | |

**Claim labels.** Every substantive sentence carries a label: verified fact (VF), reported (R), architectural judgement (AJ), recommendation (Rec) or not publicly verified (NPV). Verified and reported facts have a footnote naming the source and its access date. Part II explains the labels and the scoring rubric [AJ].

**Dates.** The evidence is as of {B['evidence_date']}. Versions, owners, prices and regulatory dates move monthly; the review is refreshed each quarter [AJ].

"""

def book_body():
    s = open(SRC, encoding="utf-8").read()
    s = s[s.index("# About this document"):]                       # drop the report's own title block
    s = s.replace("# About this document: disclosure and final tiers", "# Disclosure and final tiers", 1)
    s = re.sub(r" Editable source: `[^`]+`\.", "", s)              # figure sources live in the companion files
    s = re.sub(r"\{height=8\.8in\}", "{height=7.6in}", s)          # fit the print text block
    s = re.sub(r"\{width=100%\}", "{width=100%}", s)
    s = re.sub(r"\s\(plan §[\d.]+(?:,[^)]*)?\)", "", s)            # internal brief references
    s = re.sub(r"\bplan §[\d.]+", "the review brief", s)
    return s

ref = make_reference()
md = front + book_body()
open(os.path.join(WORK, "Interior.md"), "w", encoding="utf-8").write(md)
docx = os.path.join(OUT, "Interior.docx")
r = subprocess.run(["pandoc", os.path.join(WORK, "Interior.md"), "-f", FMT, "-o", docx, "--reference-doc=" + ref,
                    "--metadata", "title=" + B["title"], "--metadata", "lang=" + B["language"]], capture_output=True, text=True)
print("pandoc docx:", r.returncode, r.stderr[-400:])
# pandoc writes the title metadata as a Title paragraph only when the YAML has it; --metadata title adds docProps only
pages = None
if "--no-pdf" not in sys.argv and r.returncode == 0:
    pdf = os.path.join(OUT, "Interior.pdf")
    r2 = subprocess.run([sys.executable, "-I", "tools/print/print_pdf.py", docx, pdf, "tools/print/book.json"],
                        capture_output=True, text=True, timeout=7200)
    print("interior pdf:", r2.returncode, (r2.stdout + r2.stderr)[-500:])
if os.path.exists(os.path.join(OUT, "Interior.pdf")):
    info = subprocess.run(["pdfinfo", os.path.join(OUT, "Interior.pdf")], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    print("interior pages:", pages)

# ---------------------------------------------------------------- 3. cover (full wrap) and front cover
def cover_html(pages, mode):
    tw, th = B["trim_in"]; bl = B["bleed_in"]
    spine = round(pages * B["paper_spine_in_per_page"][B["paper"]], 3) if pages else 0.5
    W = bl + tw + spine + tw + bl; H = bl + th + bl
    pts = "".join("<li>%s</li>" % p for p in B["back_points"])
    blurb = "".join("<p>%s</p>" % p for p in B["blurb"])
    spine_txt = (f'<div class="spine"><span class="st">{B["title"]}</span><span class="sa">{B["author"]}</span>'
                 f'<img src="../../../brand/veyan_mark.png"></div>') if pages and pages > 79 else '<div class="spine"></div>'
    front = f'''<div class="front"><img class="hero" src="../../../brand/veyan_hero.png">
 <div class="ftxt"><div class="kick">{B["short_subtitle"]}</div><div class="t">{B["title"]}</div><div class="rule"></div>
 <div class="s">Reference architecture, product assessment and the regulated financial-services view</div>
 <div class="facts">{"".join("<span>%s</span>" % f for f in B["cover_facts"])}</div>
 <div class="a">{B["author"]}</div></div><img class="lock" src="../../../brand/veyan_lockup_white.png"></div>'''
    if mode == "front":
        return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
 body{{width:1600px;height:2560px}} .front{{position:absolute;left:0;top:0;width:1600px;height:2560px;font-size:290%}}</style></head>
 <body>{front}</body></html>''', None
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>Cover</title>
<!-- Full-wrap paperback cover. Generated by tools/build_print_edition.py from tools/print/book.json; size = bleed + back + spine + front + bleed.
     Trim {tw} x {th} in, {pages} pages, spine {spine} in ({B["paper"]} paper), bleed {bl} in. -->
<style>{CSS}
@page{{size:{W}in {H}in;margin:0}} body{{width:{W}in;height:{H}in}}
.back{{position:absolute;left:0;top:0;width:{bl + tw}in;height:{H}in;padding:{bl + 0.6}in 0.7in {bl + 0.5}in {bl + 0.6}in}}
.spinewrap{{position:absolute;left:{bl + tw}in;top:0;width:{spine}in;height:{H}in}}
.front{{position:absolute;left:{bl + tw + spine}in;top:0;width:{tw + bl}in;height:{H}in;font-size:100%}}
</style></head><body>
<div class="back"><div class="kick">The view at end of Q3 2026</div><div class="bt">Run GenAI like the regulated system it is</div><div class="rule"></div>
{blurb}<ul>{pts}</ul><div class="bfoot"><img src="../../../brand/veyan_lockup_white.png"><div class="barcode">Barcode area<br>(left clear for the printer)</div></div></div>
<div class="spinewrap">{spine_txt}</div>
{front}
</body></html>''', (W, H, spine)

CSS = """*{box-sizing:border-box}html,body{margin:0;padding:0}body{position:relative;background:#0B1B33;font-family:Inter,Arial,sans-serif;color:#fff;overflow:hidden}
.kick{font-size:11pt;letter-spacing:4pt;text-transform:uppercase;color:#D4A13A;font-weight:700}
.rule{width:0.8in;height:3pt;background:#D4A13A;margin:14pt 0 18pt}
.back p{font-size:11.5pt;line-height:1.45;color:#E4EAF2;margin:0 0 10pt}.bt{font-size:24pt;font-weight:800;line-height:1.15;margin-top:10pt}
.back ul{margin:8pt 0 0;padding-left:16pt;font-size:11pt;line-height:1.45;color:#fff}.back li{margin-bottom:5pt}.back li::marker{color:#D4A13A}
.bfoot{position:absolute;left:0.75in;right:0.8in;bottom:0.85in;display:flex;justify-content:space-between;align-items:flex-end}
.bfoot img{height:0.55in}.barcode{width:2in;height:1.2in;background:#fff;color:#999;font-size:8pt;display:flex;align-items:center;justify-content:center;text-align:center}
.spinewrap{background:#0B1B33;border-left:1px solid rgba(212,161,58,.5);border-right:1px solid rgba(212,161,58,.5)}
.spine{position:absolute;inset:0.5in 0;display:flex;flex-direction:column;align-items:center;justify-content:space-between}
.spine .st,.spine .sa{writing-mode:vertical-rl;font-weight:800;white-space:nowrap}.spine .st{font-size:15pt}.spine .sa{font-size:11pt;color:#D4A13A;margin-top:0.4in;flex:1}
.spine img{width:0.42in;border-radius:6pt}
.front{overflow:hidden;background:#0B1B33}.hero{position:absolute;right:0;top:0;height:100%;opacity:.95}
.front:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#0B1B33 0%,#0B1B33 38%,rgba(11,27,51,.75) 62%,rgba(11,27,51,.15) 100%)}
.ftxt{position:absolute;z-index:2;left:0.75in;top:1.35in;width:5.6in}
.front .t{font-size:44pt;line-height:1.02;font-weight:800;margin-top:12pt;letter-spacing:-0.5pt}
.front .s{font-size:15pt;line-height:1.35;color:#C9D6E6}.facts{margin-top:22pt;display:flex;gap:8pt;flex-wrap:wrap}
.facts span{border:1.2pt solid #D4A13A;border-radius:20pt;padding:4pt 11pt;font-size:10.5pt;color:#fff}
.front .a{margin-top:1.1in;font-size:17pt;font-weight:700;letter-spacing:1pt}
.lock{position:absolute;z-index:2;left:0.75in;bottom:0.85in;height:0.6in}"""

if "--no-cover" not in sys.argv:
    html, dims = cover_html(pages, "wrap")
    open(os.path.join(OUT, "cover.html"), "w", encoding="utf-8").write(html)
    fhtml, _ = cover_html(pages, "front")
    open(os.path.join(WORK, "cover_front.html"), "w", encoding="utf-8").write(fhtml.replace("../../../brand/", os.path.abspath("brand") + "/"))
    js = os.path.join(WORK, "render_cover.js")
    open(js, "w").write("""const {chromium}=require('playwright');const path=require('path');(async()=>{const b=await chromium.launch();
const [wrap,out,front,jpg,W,H]=process.argv.slice(2);let p=await b.newPage();await p.goto('file://'+path.resolve(wrap));await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:out,width:W+'in',height:H+'in',printBackground:true,pageRanges:'1'});
p=await b.newPage({viewport:{width:1600,height:2560}});await p.goto('file://'+path.resolve(front));await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:jpg,type:'jpeg',quality:92});await b.close();})();""")
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    r3 = subprocess.run(["node", js, os.path.join(OUT, "cover.html"), os.path.join(OUT, "Cover_Paperback.pdf"),
                         os.path.join(WORK, "cover_front.html"), os.path.join(OUT, "Cover_Front.jpg"), str(dims[0]), str(dims[1])],
                        capture_output=True, text=True, env=dict(os.environ, NODE_PATH=npm_root))
    print("cover:", r3.returncode, r3.stderr[-300:], "size in: %.3f x %.3f, spine %.3f" % dims)

# ---------------------------------------------------------------- 4. EPUB (Kindle and other stores)
if "--no-epub" not in sys.argv:
    css = os.path.join(WORK, "epub.css")
    open(css, "w").write("""body{font-family:serif;line-height:1.45}h1,h2,h3,h4{font-family:sans-serif;color:#0B1B33}h1{border-bottom:2px solid #D4A13A;padding-bottom:.2em}
table{border-collapse:collapse;font-size:.8em;margin:1em 0}td,th{border:1px solid #ccc;padding:.25em .4em;vertical-align:top}th{background:#0B1B33;color:#fff}
img{max-width:100%}.Claim-Label,[data-custom-style="Claim Label"]{font-size:.7em;color:#8792A0}blockquote{border-left:3px solid #D4A13A;margin-left:0;padding-left:1em}""")
    meta = os.path.join(WORK, "epub_meta.yaml")
    open(meta, "w", encoding="utf-8").write(
        "---\ntitle:\n- type: main\n  text: \"%s\"\n- type: subtitle\n  text: \"%s\"\ncreator:\n- role: author\n  text: \"%s\"\npublisher: \"%s\"\nrights: \"Copyright © %s %s. All rights reserved.\"\nlang: %s\ndate: \"2026-10-09\"\n%s---\n"
        % (B["title"], B["subtitle"], B["author"], B["publisher"], B["year"], B["copyright_holder"], B["language"],
           ("identifier:\n- scheme: ISBN-13\n  text: \"%s\"\n" % B["isbn_ebook"]) if B.get("isbn_ebook") else ""))
    emd = md.replace(TOC, "")
    emd = re.sub(r'(?ms)^::: \{custom-style="(HalfTitle|BookTitle|BookSubtitle|BookAuthor|BookLogo|ContentsTitle)"\}.*?^:::\n', "", emd)
    emd = emd.replace('::: {custom-style="Copyright"}', '# Copyright\n\n::: {custom-style="Copyright"}', 1)
    open(os.path.join(WORK, "Ebook.md"), "w", encoding="utf-8").write(emd)
    cover = os.path.join(OUT, "Cover_Front.jpg")
    cmd = ["pandoc", meta, os.path.join(WORK, "Ebook.md"), "-f", FMT, "-t", "epub3", "-o", os.path.join(OUT, "Ebook.epub"),
           "--toc", "--toc-depth=2", "--split-level=2", "--css", css, "--resource-path=."]
    if os.path.exists(cover): cmd.append("--epub-cover-image=" + cover)
    r4 = subprocess.run(cmd, capture_output=True, text=True)
    print("epub:", r4.returncode, r4.stderr[-300:])
# ---------------------------------------------------------------- 5. build summary with the KDP checks
if pages:
    K = B["kdp_checks"]; m = B["margins_in"]
    need = next((g for lo, hi, g in K["gutter_min_in_by_pages"] if lo <= pages <= hi), None)
    fonts = subprocess.run(["pdffonts", os.path.join(OUT, "Interior.pdf")], capture_output=True, text=True).stdout.splitlines()[2:]
    not_emb = [f for f in fonts if f.split() and len(f.split()) > 4 and f.split()[-5] != "yes"]
    spine = round(pages * B["paper_spine_in_per_page"][B["paper"]], 3)
    tw, th = B["trim_in"]; bl = B["bleed_in"]
    rows = [("Interior pages", pages),
            ("Trim size", "%s x %s in" % (tw, th)),
            ("Inside margin (gutter)", "%s in; KDP minimum for %d pages: %s in -> %s" % (m["inside"], pages, need, "OK" if need and m["inside"] >= need else "CHECK")),
            ("Outside margin", "%s in; minimum %s in -> %s" % (m["outside"], K["outside_min_in_no_bleed"], "OK" if m["outside"] >= K["outside_min_in_no_bleed"] else "CHECK")),
            ("Fonts embedded", "all %d fonts embedded" % len(fonts) if not not_emb else "NOT EMBEDDED: %s" % not_emb),
            ("Black-and-white page limit (8.5 x 11)", "%s -> %s" % (K["max_pages_8.5x11"]["black_white"], "OK" if pages <= K["max_pages_8.5x11"]["black_white"] else "TOO LONG")),
            ("Premium colour page limit (8.5 x 11)", "%s -> %s" % (K["max_pages_8.5x11"]["premium_colour"], "OK" if pages <= K["max_pages_8.5x11"]["premium_colour"] else "too long for one colour volume")),
            ("Spine width (%s paper)" % B["paper"], "%s in; spine text %s" % (spine, "printed" if pages >= K["spine_text_min_pages"] else "omitted (under 80 pages)")),
            ("Full-wrap cover size", "%.3f x %.3f in (with %s in bleed)" % (2 * bl + 2 * tw + spine, 2 * bl + th, bl))]
    summ = "# Print build summary\n\nGenerated by `tools/build_print_edition.py`. KDP figures: %s\n\n| Check | Result |\n|---|---|\n" % K["_source"]
    summ += "".join("| %s | %s |\n" % r for r in rows)
    open(os.path.join(OUT, "Build_Summary.md"), "w", encoding="utf-8").write(summ)
    print(summ)
print(json.dumps({"pages": pages}))
