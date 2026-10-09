#!/usr/bin/env bash
# Rebuild every deliverable from the sources, in dependency order. Run from the repo root:
#   bash tools/rebuild_all.sh            # everything (about 30–45 minutes: three LibreOffice PDF layouts)
#   bash tools/rebuild_all.sh --quick    # no PDFs, no print edition (minutes; for checking text changes)
# Needs: python3 (+ openpyxl, python-docx), pandoc, LibreOffice with python3-uno, Node.js with Playwright
# (npm install -g playwright && npx playwright install chromium), and the two local npm folders:
#   (cd tools/deck && npm install)   (cd tools/diagrams && npm install)
set -euo pipefail
QUICK=${1:-}
PKG=Enterprise_GenAI_Stack_Oct2026
G=$PKG/08_Graphic
export NODE_PATH="$(npm root -g)"
step() { printf '\n=== %s\n' "$*"; }

step "1. Dataset, bibliography, what-changed table (expect 0 issues)"
python3 -I tools/build_dataset.py .
step "2. Claim-tag check on the synthesis and the 17 chapters"
python3 -I tools/check_tags.py . work/stageC/synthesis.md work/stageB/*/section.md | tail -5
step "3. Figures: Mermaid diagrams, LinkedIn post visuals, stack graphic, one-page architecture"
node tools/render_diagrams.js
node tools/render_post_visuals.js
python3 -I tools/build_stack_graphic.py . --sync
node tools/render_graphic.js $G/$PKG.html $G/$PKG
node tools/render_graphic.js $G/Architecture_One_Page.html $G/Architecture_One_Page
step "4. Explorer"
python3 -I tools/build_explorer.py .
step "5. LinkedIn calendar and series document"
python3 -I tools/build_linkedin_calendar.py .
step "6. Deck"
NODE_PATH="$PWD/tools/deck/node_modules" node tools/deck/build_deck.js .
if [ "$QUICK" = "--quick" ]; then
  python3 -I tools/build_master.py . --no-pdf
  python3 -I tools/build_appendix.py . --no-pdf
  echo "Quick build done (no PDFs, no print edition)."; exit 0
fi
python3 -I tools/docx2pdf.py $PKG/03_Slides/Executive_Deck.pptx $PKG/03_Slides/Executive_Deck.pdf
step "7. Master document (Word, PDF)"
python3 -I tools/build_master.py .
step "8. Print and Kindle edition (interior PDF, cover, EPUB, KDP checks)"
python3 -I tools/build_print_edition.py .
step "9. Product technical appendix"
python3 -I tools/build_appendix.py .
step "10. ZIP"
rm -f $PKG/$PKG.zip
zip -qr $PKG/$PKG.zip $PKG -x "$PKG/$PKG.zip" -x "*.tmp" -x "*.render.tmp.html" -x "*/.~lock.*#"
ls -la $PKG/$PKG.zip
echo "All deliverables rebuilt. Review, then: git add -A && git commit && git push"
