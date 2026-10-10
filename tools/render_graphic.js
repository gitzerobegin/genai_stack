// Render the stack graphic HTML to PNG (2x, 3200 px wide) and PDF (single tall page).
// Usage: NODE_PATH=$(npm root -g) node tools/render_graphic.js <in.html> <out_basename>
//   e.g. <package>/08_Graphic/<package>.html  <package>/08_Graphic/<package>   (package from edition.json)
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 2 });
  await page.goto("file://" + path.resolve(inp));
  await page.evaluate(() => document.fonts.ready);
  const h = await page.evaluate(() => document.body.scrollHeight);
  await page.screenshot({ path: out + ".png", fullPage: true });
  await page.pdf({ path: out + ".pdf", width: "1600px", height: (h + 2) + "px", printBackground: true, pageRanges: "1" });
  console.log("rendered", out, "height", h);
  await browser.close();
})();
