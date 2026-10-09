#!/usr/bin/env python3
"""Build the LinkedIn content calendar (XLSX) and the standalone series document (DOCX) from
work/stageC2/linkedin_series.md.

Usage: python3 -I tools/build_linkedin_calendar.py <repo_root> [--start YYYY-MM-DD]
Without --start, dates are left blank ("first Tuesday after CP5 sign-off", CP4b decision) and a
'Date' formula column computes them from a single start-date cell you fill in.
Writes Enterprise_GenAI_Stack_Oct2026/07_LinkedIn/Content_Calendar.xlsx and LinkedIn_Series.docx
"""
import os, re, subprocess, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

root = sys.argv[1]; os.chdir(root)
OUT = "Enterprise_GenAI_Stack_Oct2026/07_LinkedIn"; os.makedirs(OUT, exist_ok=True)
text = open("work/stageC2/linkedin_series.md", encoding="utf-8").read()
posts = re.split(r"(?m)^(?=### Post \d+)", text)[1:]

def sub(block, name):
    m = re.search(r"(?ms)^#### %s\s*\n(.*?)(?=^#### |^### |^## |\Z)" % re.escape(name), block)
    return m.group(1).strip() if m else ""
def field(block, name):
    m = re.search(r"\*\*%s:\*\*\s*(.+)" % re.escape(name), block)
    return m.group(1).strip() if m else ""

rows = []
for b in posts:
    head = b.split("\n", 1)[0]
    m = re.match(r"### Post (\d+)\s*·\s*Week (\d+),\s*(\w+)\s*·\s*(.+)", head)
    if not m: continue
    n, wk, day, theme = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4).strip()
    full = sub(b, "Full post")
    hook = next((l.strip() for l in full.split("\n") if l.strip()), "")
    rows.append(dict(n=n, week=wk, day=day, theme=theme, pair=field(b, "Pair"), tension=field(b, "Tension"), hook=hook[:300],
                     words=len(re.sub(r"\[[^\]]*\]", "", full).split()), visual=sub(b, "Suggested visual")[:500],
                     tags=sub(b, "Hashtags").replace("\n", " ")[:80], reverify=sub(b, "Re-verify before posting").replace("\n", " ")[:500]))

wb = Workbook(); ws = wb.active; ws.title = "calendar"
ws["A1"] = "Series start date (first Tuesday after CP5 sign-off):"; ws["A1"].font = Font(bold=True)
ws["E1"] = None; ws["E1"].fill = PatternFill("solid", fgColor="FFF2CC")
ws["F1"] = "← enter the start Tuesday (dates and times below compute from it; posting time about 08:00 UK)"
start_arg = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--start"), None)
if start_arg:
    import datetime; ws["E1"] = datetime.date.fromisoformat(start_arg); ws["E1"].number_format = "dd mmm yyyy"
cols = ["#", "Week", "Day", "Date", "Time (UK)", "Theme", "Pair", "Tension", "Hook (first line)", "Words", "Hashtags", "Visual brief",
        "Re-verify before posting", "Status", "Cleared", "Published URL", "Responses / notes", "Full post (master document)"]
ws.append([]); ws.append(cols)
for c in ws[3]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F3864"); c.alignment = Alignment(wrap_text=True, vertical="top")
for r in sorted(rows, key=lambda x: x["n"]):
    i = ws.max_row + 1
    off = (r["week"] - 1) * 7 + (0 if r["day"].lower().startswith("tue") else 2)
    ws.append([r["n"], r["week"], r["day"], '=IF($E$1="","",$E$1+%d)' % off, "08:00", r["theme"], r["pair"], r["tension"], r["hook"], r["words"],
               r["tags"], r["visual"], r["reverify"], "Draft", "Not required (CP4b)", "", "", "Master_Architecture: LinkedIn series, Post %d" % r["n"]])
    ws.cell(i, 4).number_format = "ddd dd mmm yyyy"
widths = [5, 6, 9, 15, 9, 28, 30, 40, 45, 7, 22, 45, 45, 11, 16, 25, 30, 30]
for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=4):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
dv = DataValidation(type="list", formula1='"Draft,Anecdote added,Scheduled,Published,Skipped"', allow_blank=True)
ws.add_data_validation(dv); dv.add("N4:N%d" % max(ws.max_row, 4))
ws.freeze_panes = "F4"
wb.save(os.path.join(OUT, "Content_Calendar.xlsx"))
r = subprocess.run(["pandoc", "work/stageC2/linkedin_series.md", "-f", "markdown-tex_math_dollars-raw_tex", "-o", os.path.join(OUT, "LinkedIn_Series.docx"),
                    "--toc", "--toc-depth=2", "--reference-doc=tools/templates/reference.docx"], capture_output=True, text=True)
print(len(rows), "posts; pandoc", r.returncode)
