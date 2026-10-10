#!/usr/bin/env python3
"""Write the worked example's build step into each LinkedIn post's first comment (idempotent).

Usage: python3 -I tools/sync_worked_example.py <repo_root>
Source: work/stageC2/worked_example_build.json (one step per post). Edits work/stageC2/linkedin_series.md in place:
the line starting "- **Worked example" in each "#### First comment" is replaced (or added). Run after editing the JSON;
the post visuals pick the same file up when rendered (tools/render_post_visuals.js) and the book uses it too.
"""
import json, os, re, sys
os.chdir(sys.argv[1])
B = json.load(open("work/stageC2/worked_example_build.json", encoding="utf-8"))
steps = {s["post"]: s for s in B["steps"]}
p = "work/stageC2/linkedin_series.md"; t = open(p, encoding="utf-8").read()
def line(n):
    s = steps[n]
    if n == 0:
        return ("- **Worked example: the brief.** %s Each post adds one piece of the design; the strip at the foot of every "
                "visual shows how far the build has come. The series teaches the stack in layer order; the real build order "
                "(evaluation and governance first) comes in Post 20." % s["adds"])
    return "- **Worked example, step %d (%s).** Adds: %s Now: %s Never: %s" % (n, s["stage"].lower(), s["adds"], s["now_works"], s["boundary"])
out, n_done = [], 0
for block in re.split(r"(?m)^(?=### Post \d+ )", t):
    m = re.match(r"### Post (\d+) ", block)
    if m and int(m.group(1)) in steps:
        n = int(m.group(1))
        def fix(mm):
            body = re.sub(r"(?m)^- \*\*Worked example[^\n]*\n?", "", mm.group(2)).rstrip("\n")
            return mm.group(1) + body + "\n" + line(n) + "\n\n"
        block, k = re.subn(r"(?ms)(^#### First comment\s*\n)(.*?)(?=^#### )", fix, block, count=1)
        n_done += k
    out.append(block)
open(p, "w", encoding="utf-8").write("".join(out))
print("first comments updated:", n_done)
