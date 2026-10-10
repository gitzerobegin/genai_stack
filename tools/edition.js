// The current edition, read from edition.json at the repo root (written by tools/new_edition.py).
// const ED = require("./edition.js");  ED.package, ED.view_label, ED.viewLc, ED.viewUc, ED.fill(text)
const fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, "..");
const ED = JSON.parse(fs.readFileSync(path.join(ROOT, "edition.json"), "utf8"));
ED.viewLc = ED.view_label[0].toLowerCase() + ED.view_label.slice(1);
ED.viewUc = ED.view_label.toUpperCase();
module.exports = ED;
