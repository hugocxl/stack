// The vector browser: search, category filters, lazy artwork and a deep-linkable detail view.
const $ = id => document.getElementById(id);
const data = JSON.parse($('browse-data').textContent);
const byName = new Map(data.map((item, index) => [item.name, { ...item, index }]));
const items = [...$('results').children];
const haystacks = data.map(item =>
  [item.name.replaceAll('-', ' '), item.title, item.category, item.placement, item.description].join(' ').toLowerCase());
const number = new Intl.NumberFormat('en');
const svgs = new Map();
let category = '';
let visible = data.map((_, index) => index);

const fetchSvg = name => {
  if (!svgs.has(name)) svgs.set(name, fetch(`figures/${name}.svg`).then(response => {
    if (!response.ok) throw new Error(`Could not load ${name}`);
    return response.text();
  }));
  return svgs.get(name);
};
const inline = (text, decorative) => {
  const svg = text.replace(' xmlns="http://www.w3.org/2000/svg"', ' class="ds-vector"').replace(/ color="[^"]*"/, '');
  return decorative ? svg.replace('<svg ', '<svg aria-hidden="true" focusable="false" ') : svg;
};
const escapeHtml = text => text.replace(/[&<>"]/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[char]);

// Artwork loads only when a result scrolls near the viewport.
const observer = new IntersectionObserver(entries => {
  for (const entry of entries) {
    if (!entry.isIntersecting) continue;
    observer.unobserve(entry.target);
    const art = entry.target.querySelector('.browse-art');
    fetchSvg(entry.target.id).then(text => { art.innerHTML = inline(text, true); }).catch(() => {});
  }
}, { rootMargin: '600px 0px' });
for (const item of items) observer.observe(item);

// Search and filter.
const query = $('browse-query');
function filter() {
  const words = query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
  visible = [];
  data.forEach((item, index) => {
    const match = (!category || item.categoryId === category) && words.every(word => haystacks[index].includes(word));
    items[index].hidden = !match;
    if (match) visible.push(index);
  });
  const count = visible.length;
  $('browse-count').textContent = `${number.format(count)} ${count === 1 ? 'vector' : 'vectors'}`;
  $('browse-empty').hidden = count > 0;
}
query.addEventListener('input', filter);
$('browse-form').addEventListener('submit', event => {
  event.preventDefault();
  const first = items[visible[0]];
  if (first) first.querySelector('a').focus();
});
const filters = [...document.querySelectorAll('[data-category]')];
for (const button of filters) {
  button.addEventListener('click', () => {
    category = button.dataset.category;
    for (const other of filters) other.setAttribute('aria-pressed', String(other === button));
    $('browse-category-name').textContent = button.textContent;
    filter();
  });
}
if (matchMedia('(max-width: 760px)').matches) $('browse-categories').open = false;

// Detail view.
const dialog = $('browse-detail');
const swiftName = item => item.export[0].toLowerCase() + item.export.slice(1, -'Vector'.length);
function snippets(item) {
  return [
    ['SVG', `<img src="${item.name}.svg" alt="${escapeHtml(item.description)}" width="480" height="360">`],
    ['JavaScript', `import { ${item.export} } from '@hugocxl/vectors/js/${item.name}';\n\nelement.innerHTML = ${item.export};`],
    ['React', `import { ${item.export} } from '@hugocxl/vectors/react/${item.name}';\n\n<${item.export} size={320} />`],
    ['React Native', `import { ${item.export} } from '@hugocxl/vectors/react-native/${item.name}';\n\n<${item.export} size={320} color="#171717" />`],
    ['Swift', `import Vectors\n\nVector.${swiftName(item)}.image\n    .resizable()\n    .aspectRatio(4 / 3, contentMode: .fit)`],
  ];
}

let shown = null;
async function open(name) {
  const item = byName.get(name);
  shown = item;
  $('detail-title').textContent = item.title;
  $('detail-category').textContent = item.category;
  $('detail-caption').textContent = `Fig. ${String(item.index + 1).padStart(4, '0')} / ${item.title}`;
  $('detail-description').textContent = item.description;
  $('detail-placement').textContent = item.placement;
  $('detail-download').href = `figures/${item.name}.svg`;
  $('detail-download').setAttribute('download', `${item.name}.svg`);
  $('detail-copy').textContent = 'Copy SVG';
  const code = $('detail-code');
  code.replaceChildren(code.firstElementChild);
  for (const [label, text] of snippets(item)) {
    const heading = document.createElement('h3');
    heading.className = 'ds-label';
    heading.textContent = label;
    const block = document.createElement('div');
    block.className = 'ds-code';
    block.innerHTML = '<pre tabindex="0"><code></code></pre><button type="button">Copy</button>';
    block.querySelector('code').textContent = text;
    code.append(heading, block);
  }
  const media = $('detail-media');
  media.replaceChildren();
  if (!dialog.open) {
    dialog.showModal();
    dialog.scrollTop = 0;
  }
  document.title = `${item.title} — Vectors`;
  try {
    const text = await fetchSvg(item.name);
    if (shown === item) media.innerHTML = inline(text, false);
  } catch {
    if (shown === item) media.textContent = 'The preview could not be loaded.';
  }
}

const baseTitle = document.title;
function route() {
  const name = decodeURIComponent(location.hash.slice(1));
  if (byName.has(name)) open(name);
  else if (dialog.open) dialog.close();
}
addEventListener('hashchange', route);
dialog.addEventListener('close', () => {
  document.title = baseTitle;
  const name = shown?.name;
  shown = null;
  if (byName.has(decodeURIComponent(location.hash.slice(1)))) {
    history.replaceState(null, '', location.pathname + location.search);
  }
  if (name) $(name)?.querySelector('a').focus();
});
$('detail-close').addEventListener('click', () => dialog.close());

function step(offset) {
  if (!shown) return;
  const order = visible.length && visible.includes(shown.index) ? visible : data.map((_, index) => index);
  const position = order.indexOf(shown.index);
  const next = data[order[(position + offset + order.length) % order.length]];
  history.replaceState(null, '', `#${next.name}`);
  open(next.name);
}
$('detail-prev').addEventListener('click', () => step(-1));
$('detail-next').addEventListener('click', () => step(1));

$('detail-copy').addEventListener('click', async event => {
  const button = event.currentTarget;
  try {
    await navigator.clipboard.writeText(await fetchSvg(shown.name));
    button.textContent = 'Copied';
  } catch {
    button.textContent = 'Copy failed. Use Download SVG instead.';
  }
  setTimeout(() => { button.textContent = 'Copy SVG'; }, 1600);
});

route();
