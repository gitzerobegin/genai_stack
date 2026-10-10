"""The current edition, read from edition.json at the repo root (written by tools/new_edition.py).

    from edition import E, PKG, fill
    E["view_label"]  -> "The view at end of Q3 2026"
    PKG              -> "Enterprise_GenAI_Stack_Oct2026"
    fill(text)       -> replaces {PKG}, {VIEW_LABEL}, {VIEW_LABEL_LC}, {VIEW_LABEL_UC}, {AS_AT}, {QUARTER},
                        {MONTH_YEAR}, {EVIDENCE_DATE}, {EVIDENCE_ISO}, {EDITION}, {ROADMAP_START},
                        {YEAR}, and {N_PRODUCTS}, {N_SCORED}, {N_SOURCES}, {N_REGULATORY} from the dataset
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = json.load(open(os.path.join(ROOT, "edition.json"), encoding="utf-8"))
PKG = E["package"]


SMALL = {"a", "an", "and", "at", "by", "for", "in", "of", "on", "or", "the", "to"}


def title_case(s):
    """'The view at end of Q3 2026' -> 'The View at End of Q3 2026'."""
    out = []
    for i, w in enumerate(s.split()):
        out.append(w if (w[:1].isdigit() or w.isupper() or (i and w.lower() in SMALL)) else w[:1].upper() + w[1:])
    return " ".join(out)


def tokens():
    v = E["view_label"]
    return {"{PKG}": PKG, "{VIEW_LABEL}": v, "{VIEW_LABEL_LC}": v[0].lower() + v[1:], "{VIEW_LABEL_UC}": v.upper(),
            "{VIEW_LABEL_TC}": title_case(v),
            "{AS_AT}": E["as_at"], "{QUARTER}": E["quarter"], "{MONTH_YEAR}": E["month_year"],
            "{EVIDENCE_DATE}": E["evidence_date"], "{EVIDENCE_ISO}": E["evidence_iso"], "{EDITION}": E["edition"],
            "{ROADMAP_START}": E["roadmap_start"], "{YEAR}": E["evidence_iso"][:4], **dataset_tokens()}


def dataset_tokens():
    """{N_PRODUCTS}, {N_SCORED}, {N_SOURCES}, {N_REGULATORY} from <PKG>/05_Data/dataset_stats.json (tools/build_dataset.py)."""
    p = os.path.join(ROOT, PKG, "05_Data", "dataset_stats.json")
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding="utf-8"))
    return {"{N_PRODUCTS}": "%d" % d["products"], "{N_SCORED}": "%d" % d["scored"],
            "{N_SOURCES}": "{:,}".format(d["sources"]), "{N_REGULATORY}": "%d" % d["regulatory"]}


def fill(text):
    """Replace edition tokens in a string (configs, front matter); other text is left as written."""
    if not isinstance(text, str):
        return text
    for k, v in tokens().items():
        text = text.replace(k, v)
    return text


def fill_all(obj):
    if isinstance(obj, dict):
        return {k: fill_all(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [fill_all(v) for v in obj]
    return fill(obj)


if __name__ == "__main__":  # used by rebuild_all.sh: python3 -I tools/edition.py package
    import sys
    print(E[sys.argv[1]] if len(sys.argv) > 1 else PKG)
