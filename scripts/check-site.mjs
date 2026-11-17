import { readFileSync, existsSync } from "node:fs";
import assert from "node:assert/strict";
import { JSDOM } from "jsdom";
const docs = new Map(
  ["index.html", "guide.html", "icons.html"].map((name) => [
    name,
    new JSDOM(readFileSync(`_site/${name}`, "utf8")).window.document,
  ]),
);
for (const [name, doc] of docs) {
  for (const a of doc.querySelectorAll("a[href]")) {
    const href = a.getAttribute("href");
    if (/^(https?:|mailto:)/.test(href)) continue;
    const [path, hash] = href.split("#");
    const target = path === "./" ? "index.html" : path || name;
    assert.ok(existsSync(`_site/${target}`), `${name}: missing ${href}`);
    if (hash)
      assert.ok(
        docs.get(target)?.getElementById(hash),
        `${name}: missing anchor ${href}`,
      );
  }
  for (const el of doc.querySelectorAll("[src],link[href]")) {
    const p = el.getAttribute("src") || el.getAttribute("href");
    if (!p.startsWith("http"))
      assert.ok(existsSync(`_site/${p}`), `${name}: missing asset ${p}`);
  }
}
assert.equal(
  docs.get("index.html").querySelectorAll(".specimen svg").length,
  30,
);
console.log(
  "Site navigation, guide anchors, assets, and 30 preview icons verified.",
);
