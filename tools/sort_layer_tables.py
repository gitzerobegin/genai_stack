#!/usr/bin/env python3
"""Sort the rows of layer-keyed Markdown tables into the house order: L1 -> L9, then C1 -> C8, then rows with no code.

Usage: python3 -I tools/sort_layer_tables.py <file.md> [--dry-run]
A table is sorted only if its key column (first column whose header is one of KEY_HEADERS) holds a layer or
control code (L1-L9, C1-C8, in any form such as "L6 stores", "Gateway (C1)", "L2 / L1") in at least 70% of rows.
Sorting is stable, so rows with the same key keep their order. Numbered tables (decision guides, steps) are skipped.
"""
import re, sys
KEY_HEADERS = {"layer / control", "ref", "#", "layer", "component", "layer / control "}
CODE = re.compile(r"\b([LC])([1-9])\b")

def key(cell):
    codes = [(0 if l == "L" else 10) + int(n) for l, n in CODE.findall(cell)]
    return min(codes) if codes else 99

def sort_tables(text):
    lines = text.split("\n"); out = []; i = 0; changed = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"): j += 1
            hdr = [c.strip().lower() for c in lines[i].strip().strip("|").split("|")]
            rows = lines[i + 2:j]
            col = next((k for k, h in enumerate(hdr) if h in KEY_HEADERS), None)
            if col is not None and rows:
                cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
                coded = sum(1 for c in cells if len(c) > col and key(c[col]) < 99)
                if coded / len(rows) >= 0.7:
                    new = [r for _, r in sorted(zip([key(c[col]) if len(c) > col else 99 for c in cells], rows), key=lambda t: t[0])]
                    if new != rows: changed += 1
                    rows = new
            out += lines[i:i + 2] + rows; i = j
        else:
            out.append(lines[i]); i += 1
    return "\n".join(out), changed

if __name__ == "__main__":
    p = sys.argv[1]; s = open(p, encoding="utf-8").read()
    new, n = sort_tables(s)
    print("%s: %d tables reordered" % (p, n))
    if "--dry-run" not in sys.argv: open(p, "w", encoding="utf-8").write(new)
