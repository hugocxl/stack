import {
  readFileSync,
  writeFileSync,
  mkdirSync,
  cpSync,
  rmSync,
} from "node:fs";
import { marked } from "marked";
const out = "_site";
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
const read = (p) => readFileSync(p, "utf8");
cpSync("website/assets", `${out}/assets`, { recursive: true });
cpSync("website/styles.css", `${out}/styles.css`);
cpSync("website/assets/preview.png", `${out}/preview.png`);
const catalog = JSON.parse(read("catalog.json"));
const icon = (name, style = "duotone") =>
  read(
    `icons/${style === "duotone" ? "" : `styles/${style}/`}${name}.svg`,
  ).replace("<svg ", '<svg aria-hidden="true" ');
const header = `<a class="skip" href="#main">Skip to content</a><header class="site-header wrap"><a class="wordmark" href="./">Icons<span>CXL</span></a><nav aria-label="Main navigation"><a href="icons.html">Icons</a><a href="guide.html">Guide</a><a href="https://github.com/hugocxl/iconscxl">GitHub ↗</a></nav></header>`;
const footer = `<footer class="wrap"><span>Made by <a href="https://github.com/hugocxl">Hugo</a>. Also behind <a href="https://hugocxl.github.io/tab/">Tab ↗</a></span><span>Free &amp; open source · <a href="guide.html#license-and-attribution">License &amp; attribution</a></span></footer>`;
function page(title, body, file) {
  writeFileSync(
    `${out}/${file}`,
    `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title} — IconsCXL</title><meta name="description" content="A family of rounded icons for apps and websites. Explore Duotone, Solid, and Stroke, with guides for web, React, React Native, and Swift."><meta name="theme-color" content="#f5f3ed"><link rel="canonical" href="https://hugocxl.github.io/iconscxl/${file === "index.html" ? "" : file}"><meta property="og:image" content="https://hugocxl.github.io/iconscxl/preview.png"><link rel="stylesheet" href="styles.css"><link rel="preload" href="assets/fonts/Junicode-Regular-latin.woff2" as="font" type="font/woff2" crossorigin></head><body>${header}${body}${footer}</body></html>`,
  );
}
const names = [
  "home",
  "search",
  "heart",
  "star",
  "bell",
  "calendar",
  "camera",
  "music",
  "cloud",
  "folder",
  "mail",
  "message-circle",
  "settings",
  "globe",
  "map-pin",
  "sun",
  "moon",
  "zap",
  "coffee",
  "gift",
  "bookmark",
  "clock",
  "compass",
  "layers",
  "palette",
  "pencil",
  "sparkles",
  "terminal",
  "umbrella",
  "wallet",
];
page(
  "Rounded icons for the things you build",
  `<main id="main"><section class="hero wrap"><p class="eyebrow">One family. Every interface.</p><h1>Small details.<br>A whole lot<br><span>of character.</span></h1><div class="hero-bottom"><div><p class="description">Rounded icons for the things you build.<br>A little warmth. A shared rhythm. Right at home in your next app.</p><div class="actions"><a class="button" href="icons.html">Explore the icons ↗</a><a href="guide.html">Get started →</a></div></div><p class="small">${catalog.length.toLocaleString("en")} icons / 3 styles<br>Free &amp; open source</p></div></section><figure class="wrap" style="margin-block:0"><div class="specimen" role="img" aria-label="Thirty IconsCXL symbols, from navigation and communication to creative tools">${names.map((n) => `<div>${icon(n)}</div>`).join("")}</div><figcaption class="caption small"><span>A small taste of a much bigger collection.</span><a href="icons.html">Find your next icon →</a></figcaption></figure><section class="section wrap"><p class="eyebrow">01 / Find your expression</p><div class="section-heading"><h2>Same family.<br>Different feeling.</h2><p>Keep a consistent character across your interface. Add depth, bring emphasis, or keep things light.</p></div><div class="styles">${[
    [
      "duotone",
      "A quiet sense of depth. A second tone where it adds something.",
    ],
    ["solid", "A confident presence for the moments that need emphasis."],
    ["stroke", "An airy, understated companion to your content."],
  ]
    .map(
      ([style, description]) =>
        `<article class="style-card"><div class="style-art">${["home", "heart", "camera"].map((n) => icon(n, style)).join("")}</div><h3>${style[0].toUpperCase() + style.slice(1)}</h3><p>${description}</p></article>`,
    )
    .join(
      "",
    )}</div><p class="small" style="margin-top:20px">2,117 interface icons in all three styles. Plus 81 brand marks in their default style.</p></section><section class="section wrap"><p class="eyebrow">02 / Bring them with you</p><div class="section-heading"><h2>Wherever<br>you build.</h2><p>From a website to a native app, use the same familiar shapes. Pick your platform and make them yours.</p></div><div class="platforms">${[
    ["SVG", "raw-svgs"],
    ["JavaScript", "javascript-no-framework"],
    ["React", "react"],
    ["React Native / Expo", "react-native--expo"],
    ["Swift / SwiftUI", "swift--swiftui"],
  ]
    .map(([name, id]) => `<a href="guide.html#${id}">${name} ↗</a>`)
    .join(
      "",
    )}</div><p class="small">Use the icon browser to try sizes and colors, copy SVGs, and download individual icons.</p></section></main>`,
  "index.html",
);
const slug = (s) =>
  s
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .replace(/\s/g, "-");
const renderer = new marked.Renderer();
renderer.heading = function ({ tokens, depth, text }) {
  return `<h${depth} id="${slug(text)}">${this.parser.parseInline(tokens)}</h${depth}>`;
};
let guide =
  read("docs/USAGE.md") +
  "\n" +
  read("README.md").split("## License and attribution")[1];
guide = guide.replace(
  "\nOriginal IconsCXL artwork",
  "\n## License and attribution\n\nOriginal IconsCXL artwork",
);
guide = guide
  .replace(
    /\]\(\.\.\/([^)]+)\)/g,
    "](https://github.com/hugocxl/iconscxl/blob/main/$1)",
  )
  .replace(
    /\]\((LICENSE|NOTICE|THIRD_PARTY_LICENSES.md)\)/g,
    "](https://github.com/hugocxl/iconscxl/blob/main/$1)",
  );
page(
  "Getting started",
  `<main class="wrap docs-layout" id="main"><aside class="docs-nav" aria-label="On this page">${[...guide.matchAll(/^## (.+)$/gm)].map((m) => `<a href="#${slug(m[1])}">${m[1]}</a>`).join("")}</aside><article class="prose">${marked.parse(guide, { renderer })}</article></main>`,
  "guide.html",
);
let gallery = read("index.html").replaceAll("website/assets/", "assets/");
writeFileSync(`${out}/icons.html`, gallery);
writeFileSync(`${out}/.nojekyll`, "");
console.log(`Built site with ${catalog.length} icons.`);
