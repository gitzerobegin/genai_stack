// Write a THEME's name, fonts and colours into a .pptx theme part (pptxgenjs cannot write theme colours itself).
// Used by build_deck.js; portable (needs only the jszip that pptxgenjs installs).
//   const { applyTheme } = require("./apply_theme.js"); await applyTheme("deck.pptx", THEME);
const fs = require("fs");
const JSZip = require("jszip");
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
async function applyTheme(file, T) {
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  const parts = Object.keys(zip.files).filter((f) => /^ppt\/theme\/theme\d+\.xml$/.test(f));
  for (const p of parts) {
    let x = await zip.file(p).async("string");
    x = x.replace(/(<a:theme [^>]*name=")[^"]*(")/, `$1${esc(T.name)}$2`);
    x = x.replace(/(<a:clrScheme name=")[^"]*(")/, `$1${esc(T.name)}$2`);
    for (const [k, v] of Object.entries(T.colors || {})) {
      const re = new RegExp(`(<a:${k}>)[\\s\\S]*?(</a:${k}>)`);
      x = x.replace(re, `$1<a:srgbClr val="${String(v).replace("#", "").toUpperCase()}"/>$2`);
    }
    if (T.headFontFace) x = x.replace(/(<a:majorFont>\s*<a:latin typeface=")[^"]*(")/, `$1${esc(T.headFontFace)}$2`);
    if (T.bodyFontFace) x = x.replace(/(<a:minorFont>\s*<a:latin typeface=")[^"]*(")/, `$1${esc(T.bodyFontFace)}$2`);
    zip.file(p, x);
  }
  fs.writeFileSync(file, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
  return parts.length;
}
module.exports = { applyTheme };
