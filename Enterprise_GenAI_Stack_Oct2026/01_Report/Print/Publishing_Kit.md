# Publishing kit: The Enterprise GenAI Stack (print and Kindle)

This folder is the master document prepared as a book you can sell on Amazon (KDP) or print through any print-on-demand service. Everything here is generated from the same sources as `01_Report/Master_Architecture`, so a refresh rebuilds the book too.

**Check the figures before upload.** The KDP specifications below were gathered on 9 October 2026 from KDP's help pages through web-search extracts; KDP's site could not be opened directly from the research environment. Check each figure on kdp.amazon.com before you upload.

## 1. What is in this folder

| File | Use |
|---|---|
| `Interior.pdf` | **Not built by default** (no PDF from any Word document; user decision, 10 October 2026); when you are ready to upload, run `python3 -I tools/build_print_edition.py . --pdf`, which also sets the exact page count for the spine. It is not committed. **Paperback interior.** 8.5 × 11 in trim with mirrored margins (the inside margin is the gutter). Parts open on right-hand pages; every chapter starts on a new page. Running heads show the Part on left-hand pages and the chapter on right-hand pages. Front matter is numbered in roman numerals; Part I starts at page 1. All fonts are embedded, and images are lossless at full resolution. |
| `Interior.docx` | The same content as an editable Word file. Page styles, running heads and right-hand openings are applied in LibreOffice when the PDF is made, so lay out the PDF from this script rather than from Word. |
| `Cover_Paperback.pdf` | **Full-wrap paperback cover:** back, spine and front, with 0.125 in bleed. The spine width is computed from the interior's page count. A white box marks where KDP prints the barcode. |
| `cover.html` | Editable cover source. Change `tools/print/book.json` (blurb, author, title) and rebuild. |
| `Cover_Front.jpg` | Front cover, 1600 × 2560 px, for the Kindle edition and the store page. |
| `Ebook.epub` | Reflowable EPUB 3 for Kindle (KDP accepts EPUB uploads) and other stores. It has full colour figures, a linked contents and footnotes. |
| `Build_Summary.md` | Page count, spine width, cover size and each KDP check (gutter, outside margin, fonts, page limits), written by the build. |

Rebuild everything in one go:

```bash
python3 -I tools/build_master.py . --no-pdf
python3 -I tools/build_print_edition.py .        # about 10–20 minutes: the interior is laid out in LibreOffice
```

## 2. Which formats to publish

| Format | Recommendation | Why |
|---|---|---|
| **Paperback, black-and-white interior, white paper, 8.5 × 11 in** | Publish | The page count fits KDP's black-and-white limit for this trim. The interior was designed to read in greyscale: navy, gold and blue keep enough contrast. Order a proof and check the figures. |
| Paperback, colour interior | Not as one volume | KDP's colour limits for 8.5 × 11 in (premium 24–590 pages, standard 72–600) are below this book's length. For colour in print, split the book into two volumes. Volume 1 would hold the front matter, Parts I–II and Parts III–XII; Volume 2 the 17 layer and control chapters. Each volume then needs its own ISBN and cover. |
| Hardcover | Check first | KDP's hardcover trims and page limits differ from paperback. Search extracts disagreed on whether 8.5 × 11 in is offered, so check KDP's hardcover table before choosing. |
| **Kindle eBook** | Publish | Upload `Ebook.epub` and `Cover_Front.jpg`. The EPUB is about 28 MB because of the figures. Under KDP's 70% royalty option a delivery cost is charged per megabyte, so check the current rate and decide between 35% and 70%, or compress the figures. |

## 3. Before you publish: checklist

- [ ] **Author and copyright holder.** `book.json` names Bing Zhang, the author named in the LinkedIn series. Confirm or change it, then rebuild.
- [ ] **ISBNs.** Use KDP's free ISBN or your own; a paperback, a hardcover and an ebook each need their own. Enter them in `book.json`. They print on the copyright page and go into the EPUB metadata. Rebuild afterwards.
- [ ] **AI disclosure in KDP.** KDP asks at set-up whether the content is AI-generated. Its guidelines treat text created by an AI tool as AI-generated even after substantial human editing. This book's text was researched and drafted with Claude, an AI model made by Anthropic, under your direction. **Answer "yes" for text.** The copyright page already says how the book was made.
- [ ] **Brand and imagery.** The cover uses the Veyan brand image and lockup. Confirm you hold the rights to use them commercially.
- [ ] **The background diagram.** The book says once, in Part II, that the work began from a popular public stack diagram; it sets a new baseline of its own and does not describe or reproduce that diagram. Keep it that way, or get the owner's permission before adding any image of it.
- [ ] **Facts still current.** The evidence date is 9 October 2026. If you publish more than a few weeks later, run the quarterly refresh (`REFRESH_QUARTERLY.md`) or at least the R0 monitor sweep. Then rebuild, so the book matches the evidence date it states.
- [ ] **Order a printed proof.** Check:
  - greyscale contrast in the diagrams and LinkedIn cards;
  - small type in the tall decision trees (L3-2 and C7-2 are the densest);
  - that the gutter is not swallowing text.
- [ ] **Pricing.** Use KDP's royalty calculator: print cost depends on the page count, ink and marketplace. Set a list price that clears it in every marketplace you choose.
- [ ] **Categories and keywords.** Use the suggestions in §5 and choose the closest matches in KDP's category browser.
- [ ] **Look inside / preview.** The first pages are the half title, title page, copyright page and contents, which is standard. Part I starts at page 1.

## 4. Print specification used (and where it comes from)

| Item | Value in this build | KDP rule (search extract, verify) |
|---|---|---|
| Trim | 8.5 × 11 in | Standard KDP paperback trim |
| Inside margin (gutter) | 0.875 in | Minimum rises with page count: 0.375 in (24–150 pages), 0.5 (151–300), 0.625 (301–500), 0.75 (501–700), 0.875 (701–828) |
| Outside, top and bottom margins | 0.6 / 0.75 / 0.7 in | At least 0.25 in without bleed |
| Interior bleed | None (no artwork runs to the page edge) | Bleed only where artwork reaches the edge |
| Cover bleed | 0.125 in on every outside edge | 0.125 in |
| Spine width | Page count × 0.002252 in (white paper) | White 0.002252, cream 0.0025, colour 0.002347 in per page |
| Spine text | Printed | Only on books over 79 pages |
| Fonts | All embedded (`pdffonts` check in `Build_Summary.md`) | Fonts must be embedded |
| Images | Lossless, full resolution; diagrams at 2× and cards at 2160 × 2700 px | At least 300 dpi recommended at printed size |

Sources: [KDP: Trim size](https://kdp.amazon.com/help/topic/G201834560); [KDP: Set trim size, bleed and margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6); [KDP: Cover](https://kdp.amazon.com/help/topic/G201953020). For the AI disclosure, see [The Bookseller: Amazon revises KDP guidelines to compel disclosure of AI content](https://thebookseller.com/news/amazon-revises-kdp-guidelines-to-compel-disclosure-of-ai-content). All of these were read as search extracts on 9 October 2026.

## 5. Store listing (draft)

**Title:** The Enterprise GenAI Stack
**Subtitle:** The View at End of Q3 2026: Reference Architecture, Product Assessment and the Regulated Financial-Services View
**Author:** as in `book.json`
**Description** (paste into KDP; it accepts simple HTML such as `<p>`, `<b>` and `<ul>`):

> Most enterprise GenAI maps are shelves of product logos, and the logos move every quarter. This book sets a new baseline instead: the enterprise GenAI stack as it stands at the end of Q3 2026, built from 1,449 logged sources and checked by two adversarial verifiers.
>
> This book takes a different route. It asks what a regulated asset manager actually needs to run GenAI safely in production, and answers with a reference architecture: nine layers, from foundation models to evaluation, under a firm-owned control plane of eight components (gateway, guardrails, privacy, identity, configuration, FinOps, security and model risk).
>
> Every layer and control gets its own chapter: how it works, design principles, selection criteria, product deep dives, a decision tree, lock-in classification, the regulated financial-services lens and a worked example. 140 products are assessed on one rubric, every claim is labelled and every fact traces to a dated source.
>
> - A reference architecture for regulated firms, layer by layer (L1 to L9) and control by control (C1 to C8)
> - 140 products assessed on one rubric, with Strategic, Tactical and Experimental tiers and their conditions
> - Four reference stacks, a build-versus-buy view, lock-in by layer and an 18-month roadmap
> - EU AI Act, DORA, the UK critical third-party regime and model-risk rules applied to GenAI
> - One worked example throughout: an agent drafting a fund's monthly attribution commentary

**Keywords (seven slots):**
1. enterprise AI architecture
2. generative AI platform
3. LLM gateway and guardrails
4. AI governance and model risk
5. financial services AI regulation
6. RAG and vector database selection
7. agentic AI in production

**Categories:** choose the closest matches in KDP's browser under Computers & Technology (Artificial Intelligence; Enterprise Applications; Software Architecture) and Business & Money (Financial Services; Risk Management).

## 6. Keeping the book current

The book is rebuilt from the review's sources. Each quarterly refresh (`REFRESH_QUARTERLY.md`, step 6) runs `build_print_edition.py` and produces a new edition with a new evidence date. KDP lets you upload a revised interior and cover for the same ISBN when the changes are updates. A substantially new edition may need a new ISBN, so check KDP's guidance on new editions.
