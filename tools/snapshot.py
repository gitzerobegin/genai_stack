#!/usr/bin/env python3
"""Save a source to the reference archive.

Usage: python3 -I tools/snapshot.py <SOURCE_ID> <URL> <OUT_DIR>

- PDFs (and other openly downloadable binary originals) are saved to <OUT_DIR>/../../originals/
  when the server serves them openly.
- HTML pages are saved as a plain-text snapshot with a header recording URL and access date.
- Blocked / paywalled / login responses (401, 402, 403, 451, 429) are NOT worked around: the
  script records "link-only" and exits 2 so the caller cites the source by link only.
Prints one JSON line: {"id","url","status","path","bytes","access_status"}.
"""
import datetime, json, os, re, sys
import requests
from bs4 import BeautifulSoup

MAX_TEXT = 250_000
MAX_BIN = 25_000_000
UA = "Mozilla/5.0 (research-archive; enterprise-genai-stack review) Python-requests"

def main():
    sid, url, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(out_dir, exist_ok=True)
    today = datetime.date.today().isoformat()
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", sid)
    rec = {"id": sid, "url": url, "accessed": today}
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=40, allow_redirects=True)
    except Exception as e:  # network failure: link only
        rec.update(access_status="link-only (fetch failed: %s)" % type(e).__name__, path=None)
        print(json.dumps(rec)); sys.exit(2)
    rec["http_status"] = r.status_code
    if r.status_code in (401, 402, 403, 407, 429, 451) or r.status_code >= 400:
        rec.update(access_status="link-only (HTTP %d, not worked around)" % r.status_code, path=None)
        print(json.dumps(rec)); sys.exit(2)
    ctype = r.headers.get("content-type", "").lower()
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        odir = os.path.join(out_dir, "..", "..", "originals")
        os.makedirs(odir, exist_ok=True)
        if len(r.content) > MAX_BIN:
            rec.update(access_status="link-only (original too large to archive)", path=None)
            print(json.dumps(rec)); sys.exit(2)
        p = os.path.normpath(os.path.join(odir, safe + ".pdf"))
        with open(p, "wb") as f:
            f.write(r.content)
        rec.update(access_status="original", path=p, bytes=len(r.content))
        print(json.dumps(rec)); return
    soup = BeautifulSoup(r.text, "html.parser")
    for t in soup(["script", "style", "noscript", "svg", "nav", "footer", "form", "iframe"]):
        t.decompose()
    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    text = soup.get_text("\n")
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    if len(text) < 200:
        rec["note"] = "very little text extracted (likely JS-rendered); keep URL as primary citation"
    text = text[:MAX_TEXT]
    p = os.path.join(out_dir, safe + ".txt")
    with open(p, "w", encoding="utf-8") as f:
        f.write("SOURCE ID: %s\nURL: %s\nFINAL URL: %s\nTITLE: %s\nACCESSED: %s\nTYPE: text snapshot (extracted, not the original page)\n%s\n\n%s\n"
                % (sid, url, r.url, title, today, "=" * 72, text))
    rec.update(access_status="snapshot", path=p, bytes=len(text), title=title)
    print(json.dumps(rec))

if __name__ == "__main__":
    main()
