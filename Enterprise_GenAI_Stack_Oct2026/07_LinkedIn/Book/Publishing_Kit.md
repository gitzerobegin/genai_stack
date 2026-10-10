# Publishing kit: The Enterprise GenAI Stack, Layer by Layer (the LinkedIn series as a book)

This folder holds the LinkedIn series as a 6 × 9 in trade book, ready for Amazon KDP or another print-on-demand service. The master document's kit (`01_Report/Print/Publishing_Kit.md`) covers the KDP specifications and their sources; the items below are specific to this book.

| File | Use |
|---|---|
| `Interior.docx` | **The editable Word master.** KDP accepts .docx, but upload the PDF for print: it carries the right-hand Part openings, the running heads and the roman front matter, which LibreOffice applies when the PDF is made. |
| `Interior.pdf` | Paperback interior, 6 × 9 in, mirrored margins, fonts embedded |
| `Cover_Paperback.pdf` / `cover.html` | Full-wrap cover, with the spine width taken from the page count |
| `Cover_Front.jpg` | Kindle and store-page cover |
| `Ebook.epub` | Kindle eBook |
| `Build_Summary.md` | Page count, spine width and KDP checks |

**Rebuild:** run `python3 -I tools/build_linkedin_book.py .`. It assembles the chapters in `work/stageF/linkedin_book/chapters/`, adds the worked-example steps, then lays out the book with `tools/build_print_edition.py --config tools/print/linkedin_book.json`. Metadata, the blurb and the cover text live in `tools/print/linkedin_book.json`.

## Before you publish

- [ ] **Author, copyright and "About the author"** (`work/stageF/linkedin_book/about_author.md`): confirm the wording, which was written from your LinkedIn profile description.
- [ ] **ISBNs:** this book needs its own ISBNs, separate from the master book's. Enter them in `linkedin_book.json` and rebuild.
- [ ] **AI disclosure in KDP:** answer "yes" for text. The chapters were drafted with Claude under your direction; the copyright page and the preface say so.
- [ ] **The posts as published:** each chapter opens with the post's fallback version. If you change a post before publishing it on LinkedIn, change it in `work/stageC2/linkedin_series.md` and in the chapter, then rebuild.
- [ ] **Timing:** if the book comes out after the series ends, the posts' own references to the series ("over the next twelve weeks") still read as the series' words. Adjust them if you prefer the book to stand apart from the series.
- [ ] **Proof copy:** check the figures in greyscale and the footnote density. The footnotes carry full source URLs; a shorter citation style is a one-line change in `tools/tagfmt.py` if you prefer it.
- [ ] **Price:** check KDP's royalty calculator for 255 pages at 6 × 9 in, black ink.

## Store listing (draft)

**Title:** The Enterprise GenAI Stack, Layer by Layer
**Subtitle:** A Thought-Leadership Series on Building GenAI That Regulated Firms Can Trust
**Description:** the three blurb paragraphs and five points in `linkedin_book.json` (printed on the back cover).
**Keywords:** enterprise AI architecture · generative AI governance · AI agents in financial services · LLM gateway · AI model risk · RAG architecture · AI leadership
**Categories:** Computers & Technology (Artificial Intelligence; Software Architecture) and Business & Money (Management & Leadership; Financial Services). Choose the closest matches in KDP's browser.
