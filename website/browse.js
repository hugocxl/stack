// Icon browser: search, filter, preview and copy. Artwork is fetched per icon
// (svg/<style>/<name>.svg) only when its cell scrolls near the viewport.
const $ = id => document.getElementById(id);
const STYLES = ['duotone', 'solid', 'stroke'];
const STYLE_NAMES = { duotone: 'Duotone', solid: 'Solid', stroke: 'Stroke' };
const ALL = 'All';

const icons = JSON.parse($('ui-catalog').textContent).map(([name, category, tags, everyStyle]) => ({
  name,
  category,
  styles: everyStyle ? STYLES : ['duotone'],
  text: `${name.replaceAll('-', ' ')} ${name} ${category} ${tags}`.toLowerCase(),
}));
const byName = new Map(icons.map(icon => [icon.name, icon]));
const state = { style: 'duotone', size: '24', category: ALL, query: [], platform: 'react', selected: null };

const search = $('ui-search');
const results = $('ui-results');
const count = $('ui-count');
const empty = $('ui-empty');
const detail = $('ui-detail');
const feedback = $('ui-feedback');

// ─── Artwork ────────────────────────────────────────────────────────────
const cache = new Map();
const url = (style, name) => `svg/${style}/${name}.svg`;
export function artwork(style, name) {
  const key = `${style}/${name}`;
  if (!cache.has(key)) {
    const request = fetch(url(style, name)).then(response => {
      if (!response.ok) throw new Error(`${response.status} ${key}`);
      return response.text();
    });
    request.catch(() => cache.delete(key));
    cache.set(key, request);
  }
  return cache.get(key);
}

function paint(element, style, name) {
  const key = `${style}/${name}`;
  element.dataset.key = key;
  artwork(style, name).then(svg => {
    if (element.dataset.key !== key) return;
    element.innerHTML = svg;
    const drawing = element.querySelector('svg');
    drawing?.setAttribute('aria-hidden', 'true');
    drawing?.setAttribute('focusable', 'false');
  }, () => {
    if (element.dataset.key === key) element.replaceChildren();
  });
}

const observer = 'IntersectionObserver' in window
  ? new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        observer.unobserve(entry.target);
        paint(entry.target, state.style, entry.target.dataset.name);
      }
    }, { rootMargin: '600px 0px' })
  : null;

// ─── Results ────────────────────────────────────────────────────────────
const number = new Intl.NumberFormat('en');
const categoryButtons = [...document.querySelectorAll('[data-category]')];

function matches(icon, withCategory = true) {
  if (!icon.styles.includes(state.style)) return false;
  if (withCategory && state.category !== ALL && icon.category !== state.category) return false;
  return state.query.every(word => icon.text.includes(word));
}

function render() {
  const found = icons.filter(icon => matches(icon));
  if (state.query.length) {
    // Names that start with the first word come first, then other name matches.
    const [first] = state.query;
    const rank = icon => icon.name.startsWith(first) ? 0 : icon.name.split('-').some(part => part.startsWith(first)) ? 1 : icon.name.includes(first) ? 2 : 3;
    found.sort((a, b) => rank(a) - rank(b));
  }
  observer?.disconnect();
  const fragment = document.createDocumentFragment();
  for (const icon of found) {
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.className = 'site-item';
    link.href = `#${icon.name}`;
    const art = document.createElement('span');
    art.className = 'site-art';
    art.dataset.name = icon.name;
    const label = document.createElement('span');
    label.className = 'site-name';
    label.textContent = icon.name;
    link.append(art, label);
    item.append(link);
    fragment.append(item);
    if (observer) observer.observe(art);
    else paint(art, state.style, icon.name);
  }
  results.replaceChildren(fragment);
  empty.hidden = found.length > 0;
  const where = state.category === ALL ? '' : ` in ${state.category}`;
  count.textContent = `${number.format(found.length)} ${found.length === 1 ? 'icon' : 'icons'}${where}`;

  // Category counts follow the search and style, so empty categories drop out.
  for (const button of categoryButtons) {
    const category = button.dataset.category;
    const total = icons.filter(icon => (category === ALL || icon.category === category) && matches(icon, false)).length;
    button.querySelector('span').textContent = number.format(total);
    button.hidden = total === 0 && category !== ALL && category !== state.category;
  }
}

function press(attribute, value) {
  for (const button of document.querySelectorAll(`[${attribute}]`)) {
    button.setAttribute('aria-pressed', String(button.getAttribute(attribute) === value));
  }
}

let pending = 0;
search.addEventListener('input', () => {
  cancelAnimationFrame(pending);
  pending = requestAnimationFrame(() => {
    state.query = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    render();
  });
});
$('ui-search-form').addEventListener('submit', event => {
  event.preventDefault();
  results.querySelector('a')?.focus();
});

document.addEventListener('click', event => {
  const button = event.target.closest('button[data-style], button[data-size], button[data-category], button[data-platform]');
  if (!button) return;
  const { style, size, category, platform } = button.dataset;
  if (style) setStyle(style);
  if (size) {
    state.size = size;
    results.dataset.size = size;
    press('data-size', size);
  }
  if (category) {
    state.category = category;
    press('data-category', category);
    render();
  }
  if (platform) {
    state.platform = platform;
    press('data-platform', platform);
    if (state.selected) fill(state.selected);
  }
});

function setStyle(style) {
  if (!STYLES.includes(style)) return;
  state.style = style;
  press('data-style', style);
  render();
  if (state.selected) fill(state.selected);
}

document.addEventListener('keydown', event => {
  if (event.key !== '/' || event.metaKey || event.ctrlKey || event.altKey || detail.open) return;
  if (event.target.closest('input, textarea, select, [contenteditable]')) return;
  event.preventDefault();
  search.focus();
});

// ─── Detail ─────────────────────────────────────────────────────────────
const symbol = name => name.split('-').map(part => part[0].toUpperCase() + part.slice(1)).join('') + 'Icon';
const swiftCase = name => {
  const base = symbol(name).slice(0, -4);
  const member = base[0].toLowerCase() + base.slice(1);
  return ['init', 'self', 'Type', 'Protocol'].includes(member) || /^\d/.test(member) ? `\`${member}\`` : member;
};

export function snippet(platform, style, name) {
  const sub = style === 'duotone' ? '' : `/${style}`;
  const component = symbol(name);
  switch (platform) {
    case 'svg':
      return `curl -O https://raw.githubusercontent.com/hugocxl/icons/main/icons/${style === 'duotone' ? '' : `styles/${style}/`}${name}.svg`;
    case 'js':
      return `import { ${component} } from '@hugocxl/icons/js${sub}/${name}';\n\nelement.innerHTML = ${component};`;
    case 'react':
      return `import { ${component} } from '@hugocxl/icons/react${sub}/${name}';\n\n<${component} size={24} />`;
    case 'react-native':
      return `import { ${component} } from '@hugocxl/icons/react-native${sub}/${name}';\n\n<${component} size={24} />`;
    case 'swift':
      return `import Icons\n\n${style === 'duotone' ? 'Icon' : STYLE_NAMES[style] + 'Icon'}.${swiftCase(name)}.image`;
  }
  return '';
}

function fill(icon) {
  const style = icon.styles.includes(state.style) ? state.style : 'duotone';
  $('ui-detail-name').textContent = icon.name;
  $('ui-detail-category').textContent = icon.styles.length === 1 ? `${icon.category} · Duotone only` : icon.category;
  $('ui-preview').setAttribute('aria-label', `${icon.name} in the ${STYLE_NAMES[style]} style`);
  paint($('ui-preview'), style, icon.name);
  for (const art of $('ui-sizes').querySelectorAll('.site-art')) paint(art, style, icon.name);
  for (const button of detail.querySelectorAll('[data-style]')) {
    button.hidden = !icon.styles.includes(button.dataset.style);
    button.setAttribute('aria-pressed', String(button.dataset.style === style));
  }
  $('ui-snippet').textContent = snippet(state.platform, style, icon.name);
  const download = $('ui-download');
  download.href = url(style, icon.name);
  download.download = `${icon.name}${style === 'duotone' ? '' : `-${style}`}.svg`;
  feedback.textContent = '';
}

function open(icon) {
  state.selected = icon;
  fill(icon);
  if (!detail.open) detail.showModal();
}

function close() {
  if (detail.open) detail.close();
}

detail.addEventListener('close', () => {
  const name = state.selected?.name;
  state.selected = null;
  if (location.hash) history.replaceState(null, '', location.pathname + location.search);
  if (name) results.querySelector(`a[href="#${CSS.escape(name)}"]`)?.focus();
});
$('ui-close').addEventListener('click', close);
detail.addEventListener('click', event => {
  if (event.target === detail) close();
});

$('ui-copy-svg').addEventListener('click', async () => {
  const icon = state.selected;
  if (!icon) return;
  const style = icon.styles.includes(state.style) ? state.style : 'duotone';
  try {
    await navigator.clipboard.writeText(await artwork(style, icon.name));
    feedback.textContent = `Copied the ${STYLE_NAMES[style]} SVG for ${icon.name}.`;
  } catch {
    feedback.textContent = 'Copying is not available here. Use Download SVG instead.';
  }
});

function route() {
  const icon = byName.get(decodeURIComponent(location.hash.slice(1)));
  if (icon) open(icon);
  else close();
}
window.addEventListener('hashchange', route);

render();
route();
