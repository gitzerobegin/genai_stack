#!/usr/bin/env python3
"""Convert a .docx to PDF through LibreOffice UNO, refreshing the table of contents first
(plain `soffice --convert-to pdf` leaves pandoc's TOC field empty).

Usage: python3 -I tools/docx2pdf.py <in.docx> <out.pdf>
"""
import os, subprocess, sys, time, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

src, dst = map(os.path.abspath, sys.argv[1:3])
port = 2002 + os.getpid() % 1000
office = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore", "--nologo",
                           "--accept=socket,host=127.0.0.1,port=%d;urp;" % port],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    resolver = uno.getComponentContext().ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", uno.getComponentContext())
    for _ in range(120):
        try:
            ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext" % port); break
        except Exception:
            time.sleep(1)
    desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), "_blank", 0, (prop("Hidden", True),))
    idx = doc.getDocumentIndexes()
    for i in range(idx.getCount()):
        idx.getByIndex(i).update()
    doc.refresh()
    for i in range(idx.getCount()):  # second pass: page numbers settle after the TOC itself takes space
        idx.getByIndex(i).update()
    n = idx.getCount()
    doc.storeToURL(uno.systemPathToFileUrl(dst), (prop("FilterName", "writer_pdf_Export"),))
    doc.close(True)
    print("pdf ok, indexes:", n)
finally:
    office.terminate()
    try: office.wait(30)
    except Exception: office.kill()
