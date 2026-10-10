#!/usr/bin/env python3
"""Record a source whose host could not be fetched directly in the research environment.

Usage: python3 -I tools/save_extract.py <SOURCE_ID> <URL> <OUT_DIR> "<search query or how found>" < extract.txt

Writes <OUT_DIR>/<SOURCE_ID>.extract.txt containing the URL, access date, the query used and the
text extract returned by the web-search tool (stdin). This is NOT a copy of the original page: it
is a dated record of what the search tool reported the page to say. The URL remains the citation.
"""
import datetime, json, os, re, sys

sid, url, out_dir, how = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
os.makedirs(out_dir, exist_ok=True)
safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", sid)
text = sys.stdin.read().strip()
today = datetime.date.today().isoformat()
p = os.path.join(out_dir, safe + ".extract.txt")
with open(p, "w", encoding="utf-8") as f:
    f.write("SOURCE ID: %s\nURL: %s\nACCESSED: %s\nTYPE: search-tool extract (direct fetch blocked by research-environment egress policy; not the original page)\nFOUND VIA: %s\n%s\n\n%s\n"
            % (sid, url, today, how, "=" * 72, text))
print(json.dumps({"id": sid, "url": url, "accessed": today, "access_status": "extract", "path": p}))
