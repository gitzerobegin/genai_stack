#!/usr/bin/env python3
"""Lay out the print edition in LibreOffice (UNO) and export the KDP interior PDF.

Usage: python3 -I tools/print/print_pdf.py <print.docx> <out.pdf> <book.json>

What it does to the pandoc .docx (tools/build_print_edition.py writes it):
- trim size and mirrored margins from book.json (inside margin is the gutter);
- page styles: front matter in lower-case roman numerals, the body in arabic from Part I = page 1;
- every Heading 1 (a Part, or a divider such as "The nine layers") opens on a right-hand (recto) page;
  a blank left-hand page is inserted where needed;
- every layer or control chapter (Heading 2 "1. ...", "C1. ...") starts on a new page;
- running heads: left (verso) pages show the Part, right (recto) pages show the chapter or section;
  page numbers sit at the outside corner; opening pages carry no running head;
- refreshes the table of contents twice (page numbers settle), then exports a PDF with every font
  embedded, lossless images at full resolution and blank pages kept (print needs them).
"""
import json, os, re, subprocess, sys, time, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

src, dst, cfg = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
book = json.load(open(cfg, encoding="utf-8"))
IN = 2540  # 1/100 mm per inch
W, H = [int(round(v * IN)) for v in book["trim_in"]]
MG = {k: int(round(v * IN)) for k, v in book["margins_in"].items()}
NAVY, GOLD, MUTE = 0x0B1B33, 0xD4A13A, 0x5B6B7A
ROMAN_LOWER, ARABIC, PAGE_DESCRIPTOR = 3, 4, 5
CHAPTER_H2 = re.compile(r"^(\d+|C\d)\.\s")

port = 2002 + os.getpid() % 1000
office = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore", "--nologo",
                           "--accept=socket,host=127.0.0.1,port=%d;urp;" % port],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    for _ in range(120):
        try:
            ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext" % port); break
        except Exception:
            time.sleep(1)
    desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), "_blank", 0, (prop("Hidden", True),))
    E = lambda t, v: uno.Enum(t, v)
    doc.lockControllers(); doc.addActionLock()   # re-paginate once at the end, not after every style change

    # ---------- page styles
    fam = doc.StyleFamilies.getByName("PageStyles")
    def text_line(xtext, align, parts):
        xtext.setString("")
        cur = xtext.createTextCursor()
        cur.ParaAdjust = E("com.sun.star.style.ParagraphAdjust", align)
        cur.CharFontName = "Arial"; cur.CharHeight = 8; cur.CharColor = MUTE
        for p in parts:
            if isinstance(p, str):
                xtext.insertString(cur, p, False)
            else:
                xtext.insertTextContent(cur, p, False)
    def chapter_field(level):
        f = doc.createInstance("com.sun.star.text.TextField.Chapter"); f.ChapterFormat = 0; f.Level = level; return f
    def page_field():
        f = doc.createInstance("com.sun.star.text.TextField.PageNumber")
        f.NumberingType = PAGE_DESCRIPTOR; f.SubType = E("com.sun.star.text.PageNumberType", "CURRENT"); return f
    def style(name, layout, numbering, head, foot, follow):
        if not fam.hasByName(name):
            fam.insertByName(name, doc.createInstance("com.sun.star.style.PageStyle"))
        s = fam.getByName(name)
        s.Width, s.Height = W, H
        s.PageStyleLayout = E("com.sun.star.style.PageStyleLayout", layout)
        s.LeftMargin, s.RightMargin = MG["inside"], MG["outside"]   # mirrored: left = inner on recto, mirrored on verso
        s.TopMargin, s.BottomMargin = MG["top"], MG["bottom"]
        s.NumberingType = numbering
        s.HeaderIsOn = bool(head); s.FooterIsOn = bool(foot)
        if head:
            s.HeaderIsShared = False; s.HeaderBodyDistance = int(0.18 * IN); s.HeaderHeight = int(0.3 * IN)
            l, r = head
            text_line(s.HeaderTextLeft, "LEFT", l); text_line(s.HeaderText, "RIGHT", r)
        if foot:
            s.FooterIsShared = False; s.FooterBodyDistance = int(0.18 * IN); s.FooterHeight = int(0.3 * IN)
            text_line(s.FooterTextLeft, "LEFT", [page_field()]); text_line(s.FooterText, "RIGHT", [page_field()])
        s.FollowStyle = follow
        return s
    title = book["title"]
    style("FrontPlain", "ALL", ROMAN_LOWER, None, None, "FrontPlain")
    style("FrontPlainR", "RIGHT", ROMAN_LOWER, None, None, "FrontPlain")
    style("FrontMatter", "MIRRORED", ROMAN_LOWER, ([title.upper()], [chapter_field(0)]), True, "FrontMatter")
    style("FrontOpen", "RIGHT", ROMAN_LOWER, None, True, "FrontMatter")
    style("BookBody", "MIRRORED", ARABIC, ([chapter_field(0)], [chapter_field(1)]), True, "BookBody")
    style("ChapterOpen", "RIGHT", ARABIC, None, True, "BookBody")

    # ---------- paragraph styles for the front matter (pandoc custom styles)
    pst = doc.StyleFamilies.getByName("ParagraphStyles")
    def pstyle(name, **kw):
        if pst.hasByName(name):
            s = pst.getByName(name)
            for k, v in kw.items():
                setattr(s, k, E("com.sun.star.style.ParagraphAdjust", v) if k == "ParaAdjust" else v)
    C = "CENTER"
    pstyle("HalfTitle", CharFontName="Arial", CharHeight=24, CharWeight=150, CharColor=NAVY, ParaAdjust=C, ParaTopMargin=int(3.2 * IN))
    pstyle("BookTitle", CharFontName="Arial", CharHeight=36, CharWeight=150, CharColor=NAVY, ParaAdjust=C, ParaTopMargin=int(2.0 * IN), ParaBottomMargin=int(0.25 * IN))
    pstyle("BookSubtitle", CharFontName="Arial", CharHeight=15, CharColor=NAVY, ParaAdjust=C, ParaBottomMargin=int(0.6 * IN))
    pstyle("BookAuthor", CharFontName="Arial", CharHeight=16, CharWeight=150, CharColor=NAVY, ParaAdjust=C, ParaBottomMargin=int(1.6 * IN))
    pstyle("BookLogo", ParaAdjust=C)
    pstyle("Copyright", CharHeight=8.5, ParaBottomMargin=int(0.08 * IN))
    pstyle("ContentsTitle", CharFontName="Arial", CharHeight=24, CharWeight=150, CharColor=NAVY, ParaTopMargin=int(0.9 * IN), ParaBottomMargin=int(0.3 * IN))
    for h, top in (("Heading 1", 1.3), ("Heading 2", 0.25)):
        if pst.hasByName(h):
            pst.getByName(h).ParaTopMargin = int(top * IN)

    # ---------- walk the body
    PB = E("com.sun.star.style.BreakType", "PAGE_BEFORE")
    en = doc.Text.createEnumeration()
    first, seen_part1, seen_copyright, n_h1, n_ch = True, False, False, 0, 0
    while en.hasMoreElements():
        par = en.nextElement()
        if not par.supportsService("com.sun.star.text.Paragraph"):
            continue
        st, txt = par.ParaStyleName, par.getString().strip()
        if first:
            par.PageDescName = "FrontPlainR"; first = False; continue
        if st == "BookTitle":
            par.PageDescName = "FrontPlainR"
        elif st == "Copyright" and not seen_copyright:
            seen_copyright = True; par.BreakType = PB; par.ParaTopMargin = int(3.6 * IN)
        elif st == "ContentsTitle":
            par.PageDescName = "FrontOpen"
        elif st in ("Heading 1", "Heading1"):
            n_h1 += 1
            if not seen_part1 and txt.startswith("Part I:"):
                seen_part1 = True; par.PageDescName = "ChapterOpen"; par.PageNumberOffset = 1
            else:
                par.PageDescName = "ChapterOpen" if seen_part1 else "FrontOpen"
        elif st in ("Heading 2", "Heading2") and seen_part1 and CHAPTER_H2.match(txt):
            n_ch += 1; par.BreakType = PB; par.CharHeight = 22; par.ParaTopMargin = int(0.5 * IN); par.ParaBottomMargin = int(0.2 * IN)

    doc.removeActionLock(); doc.unlockControllers()
    # ---------- table of contents: refresh twice so the numbers settle after the layout changes
    idx = doc.getDocumentIndexes(); n_idx = idx.getCount()
    for _ in range(2):
        for i in range(n_idx):
            idx.getByIndex(i).update()
        doc.refresh()

    fd = uno.Any("[]com.sun.star.beans.PropertyValue", tuple([
        prop("UseLosslessCompression", True), prop("ReduceImageResolution", False), prop("ExportBookmarks", True),
        prop("IsSkipEmptyPages", False), prop("EmbedStandardFonts", True), prop("ExportNotes", False),
        prop("ExportFormFields", False), prop("UseTaggedPDF", True)]))
    doc.storeToURL(uno.systemPathToFileUrl(dst), (prop("FilterName", "writer_pdf_Export"), prop("FilterData", fd)))
    pages = doc.CurrentController.PageCount if hasattr(doc, "CurrentController") and doc.CurrentController else -1
    doc.close(True)
    print(json.dumps({"pdf": dst, "h1": n_h1, "chapters": n_ch, "indexes": n_idx, "part1_found": seen_part1}))
finally:
    office.terminate()
    try: office.wait(30)
    except Exception: office.kill()
