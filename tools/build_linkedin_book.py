#!/usr/bin/env python3
"""Assemble the LinkedIn series book (Stage F) from its chapters, ready for tools/build_print_edition.py.

Usage: python3 -I tools/build_linkedin_book.py <repo_root> [--no-print]
Reads  work/stageF/linkedin_book/chapters/ch00.md … ch32.md   (one chapter per post; brief: work/stage0/12_stageF_linkedin_book_brief.md;
                                                               ch25-ch32 = Part IV, "One stack, seven lenses", included when present)
       work/stageC2/worked_example_build.json                 (adds "In the worked example" to every chapter, and Appendix A)
       work/stageF/linkedin_book/glossary.md, about_author.md  (back matter)
Writes work/stageF/linkedin_book/book.md          (inline claim tags, for editing and review)
       work/stageF/linkedin_book/book.pandoc.md   (tags as footnotes: the source for the print and Kindle build)
Then, unless --no-print, runs tools/build_print_edition.py --config tools/print/linkedin_book.json, which writes
Enterprise_GenAI_Stack_Oct2026/07_LinkedIn/Book/ (Interior.docx, cover, EPUB, Build_Summary.md; Interior.pdf only with --pdf).
"""
import json, os, re, subprocess, sys
root = sys.argv[1]; os.chdir(root); sys.path.insert(0, "tools")
from tagfmt import load_index, convert_markdown

D = "work/stageF/linkedin_book"
ch = lambda n: open(os.path.join(D, "chapters", "ch%02d.md" % n), encoding="utf-8").read().strip() + "\n"
WX = json.load(open("work/stageC2/worked_example_build.json", encoding="utf-8"))
steps = {s["post"]: s for s in WX["steps"]}

def worked_example(n):
    s = steps.get(n)
    if not s:
        return ""
    if n == 0:
        return ("### In the worked example\n\n**The brief.** %s The design file starts empty; each chapter adds one piece, "
                "and Appendix A lists every step [AJ].\n\n" % s["adds"])
    return ("### In the worked example\n\n**Step %d: %s.** %s [AJ]\n\n- **Now works:** %s [AJ]\n- **Must never:** %s [AJ]\n"
            "- **Evidence added:** %s [AJ]\n- **Signal:** %s [AJ]\n\n" % (n, s["stage"].lower(), s["adds"], s["now_works"], s["boundary"], s["evidence"], s["metric"]))

def chapter(n):
    t = ch(n)
    t = re.sub(r"(?m)^### In the worked example\n.*?(?=^### )", "", t, flags=re.S)        # idempotent
    t = re.sub(r"(?m)^(?=### Objections worth taking seriously)", lambda m: worked_example(n), t, count=1)
    return t

def one_line(n):
    m = re.search(r"(?ms)^### In one line\s*\n(.*?)(?=^### |\Z)", ch(n))
    return re.sub(r"\s*\[[^\]]*\]", "", m.group(1)).strip().replace("\n", " ") if m else ""

def title(n):
    m = re.search(r"(?m)^## (.+)$", ch(n)); return m.group(1).strip() if m else "Chapter %d" % n

parts = ["# Part I: The argument\n", chapter(0),
         "# Part II: Nine layers and the controls that make them safe\n"] + [chapter(n) for n in range(1, 19)] + \
        ["# Part III: Putting it together\n"] + [chapter(n) for n in range(19, 25)]
LENS = [n for n in range(25, 33) if os.path.exists(os.path.join(D, "chapters", "ch%02d.md" % n))]   # "One stack, seven lenses"
if LENS:
    parts += ["# Part IV: One stack, seven lenses\n"] + [chapter(n) for n in LENS]
appA = ["# Appendix A: The worked example, step by step\n", WX["use_case"] + " The series teaches the stack in layer order; "
        "the real build order (evaluation and governance first) is set out at step 20 [AJ].\n",
        "| Step | Stage | What it adds | Must never |", "|---|---|---|---|"]
appA += ["| %d | %s | %s | %s |" % (s["post"], s["stage"], s["adds"], s["boundary"]) for s in WX["steps"]]
appB = ["\n# Appendix B: The book at a glance\n", "| Chapter | In one line |", "|---|---|"]
appB += ["| %s | %s |" % (title(n), one_line(n)) for n in list(range(0, 25)) + LENS]
back = [open(os.path.join(D, f), encoding="utf-8").read().strip() + "\n" for f in ("glossary.md", "about_author.md") if os.path.exists(os.path.join(D, f))]
book = "\n\n".join(parts + ["\n".join(appA), "\n".join(appB)] + back)
book = book.replace("{width=4.4in}", "{width=4.2in}")       # fits the 6 x 9 in text block with room for the caption
open(os.path.join(D, "book.md"), "w", encoding="utf-8").write(book)
open(os.path.join(D, "book.pandoc.md"), "w", encoding="utf-8").write(convert_markdown(book, *load_index(".")))
print(json.dumps({"words": len(re.sub(r"\[[^\]]*\]", "", book).split()), "chapters": 25 + len(LENS)}))
if "--no-print" not in sys.argv:
    r = subprocess.run([sys.executable, "-I", "tools/build_print_edition.py", ".", "--config", "tools/print/linkedin_book.json"] +
                       [a for a in sys.argv[2:] if a.startswith("--no-") or a in ("--cover-only", "--pdf")], text=True)
    sys.exit(r.returncode)
