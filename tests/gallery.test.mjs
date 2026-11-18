import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { JSDOM, VirtualConsole } from 'jsdom';

const catalog = JSON.parse(readFileSync('catalog.json', 'utf8'));
const settle = () => new Promise(resolve => setTimeout(resolve, 20));

before(() => {
  if (!existsSync('_site/browse.html')) execFileSync(process.execPath, ['scripts/build-site.mjs'], { stdio: 'ignore' });
});

// Load a built page and run its site script (modules are inlined as classic scripts for jsdom).
function load(page, script, hash = '') {
  const errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', error => errors.push(error));
  const requests = [];
  const dom = new JSDOM(readFileSync(`_site/${page}`, 'utf8'), {
    url: `https://hugocxl.github.io/icons/${page}${hash}`,
    runScripts: 'outside-only',
    virtualConsole,
  });
  const w = dom.window;
  w.HTMLDialogElement.prototype.showModal = function () { this.setAttribute('open', '') };
  w.HTMLDialogElement.prototype.close = function () {
    if (!this.hasAttribute('open')) return;
    this.removeAttribute('open');
    this.dispatchEvent(new w.Event('close'));
  };
  w.requestAnimationFrame = callback => setTimeout(callback, 0);
  w.cancelAnimationFrame = id => clearTimeout(id);
  w.CSS ??= {};
  w.CSS.escape ??= value => value;
  w.fetch = async path => {
    requests.push(path);
    const file = `_site/${path}`;
    return existsSync(file)
      ? { ok: true, status: 200, text: async () => readFileSync(file, 'utf8') }
      : { ok: false, status: 404, text: async () => '' };
  };
  w.eval(readFileSync(`_site/${script}`, 'utf8').replace(/^export /gm, ''));
  return { w, d: w.document, errors, requests };
}

test('icon browser searches, filters, previews and deep links', async () => {
  const { w, d, errors, requests } = load('browse.html', 'browse.js');
  const $ = id => d.getElementById(id);
  const items = () => d.querySelectorAll('#ui-results .site-item');
  const type = async value => { $('ui-search').value = value; $('ui-search').dispatchEvent(new w.Event('input')); await settle() };
  const click = selector => d.querySelector(selector).click();

  assert.equal(items().length, catalog.length);
  assert.equal($('ui-count').textContent, `${catalog.length.toLocaleString('en')} icons`);
  await settle();
  assert.ok(d.querySelector('#ui-results .site-art svg[aria-hidden="true"]'), 'artwork is painted in place');
  assert.ok(requests.every(path => /^svg\/duotone\/[\w-]+\.svg$/.test(path)));

  await type('calendar');
  assert.ok(items().length >= 7);
  await type('there-is-no-icon-by-this-name');
  assert.equal(items().length, 0);
  assert.equal($('ui-empty').hidden, false);
  assert.equal($('ui-count').textContent, '0 icons');
  await type('');

  click('#ui-browser [data-style="stroke"]');
  assert.equal(items().length, catalog.filter(icon => icon.styles.includes('stroke')).length);
  assert.equal([...items()].some(item => item.textContent === 'github'), false, 'brands only come in Duotone');
  assert.equal(d.querySelector('#ui-browser [data-category="Brands"]').hidden, true);
  await settle();
  assert.ok(requests.some(path => path.startsWith('svg/stroke/')));

  click('#ui-browser [data-category="Health and fitness"]');
  assert.equal(items().length, catalog.filter(icon => icon.category === 'Health and fitness').length);
  assert.match($('ui-count').textContent, /in Health and fitness$/);
  click('#ui-browser [data-category="All"]');

  click('#ui-browser [data-size="48"]');
  assert.equal($('ui-results').dataset.size, '48');
  assert.equal(d.querySelector('#ui-browser [data-size="48"]').getAttribute('aria-pressed'), 'true');

  // Deep link: #name opens the detail view.
  w.location.hash = '#search';
  await settle();
  assert.equal($('ui-detail').open, true);
  assert.equal($('ui-detail-name').textContent, 'search');
  assert.equal($('ui-snippet').textContent, "import { SearchIcon } from '@hugocxl/icons/react/stroke/search';\n\n<SearchIcon size={24} />");
  assert.equal($('ui-download').getAttribute('href'), 'svg/stroke/search.svg');
  assert.equal($('ui-download').getAttribute('download'), 'search-stroke.svg');
  await settle();
  assert.ok($('ui-preview').querySelector('svg'));
  assert.equal($('ui-sizes').querySelectorAll('svg').length, 4);

  click('#ui-detail [data-platform="swift"]');
  assert.equal($('ui-snippet').textContent, 'import Icons\n\nStrokeIcon.search.image');
  click('#ui-detail [data-platform="svg"]');
  assert.match($('ui-snippet').textContent, /icons\/styles\/stroke\/search\.svg$/);
  click('#ui-detail [data-style="duotone"]');
  assert.match($('ui-snippet').textContent, /\/main\/icons\/search\.svg$/);
  click('#ui-detail [data-platform="js"]');
  assert.equal($('ui-snippet').textContent, "import { SearchIcon } from '@hugocxl/icons/js/search';\n\nelement.innerHTML = SearchIcon;");

  $('ui-close').click();
  assert.equal($('ui-detail').open, false);
  assert.equal(w.location.hash, '');

  // A brand opens in Duotone and hides the other styles.
  w.location.hash = '#github';
  await settle();
  assert.equal($('ui-detail-name').textContent, 'github');
  assert.match($('ui-detail-category').textContent, /Duotone only/);
  assert.equal(d.querySelector('#ui-detail [data-style="stroke"]').hidden, true);
  w.location.hash = '';
  await settle();
  assert.equal($('ui-detail').open, false);

  assert.deepEqual(errors, []);
  w.close();
});

test('a deep link opens the detail on load', async () => {
  const { w, d, errors } = load('browse.html', 'browse.js', '#calendar');
  assert.equal(d.getElementById('ui-detail').open, true);
  assert.equal(d.getElementById('ui-detail-name').textContent, 'calendar');
  assert.deepEqual(errors, []);
  w.close();
});

test('home specimen cycles through the three styles', () => {
  const { w, d, errors } = load('index.html', 'home.js');
  const visible = () => [...d.querySelectorAll('.site-specimen')].filter(node => !node.hidden).map(node => node.dataset.style);
  assert.deepEqual(visible(), ['duotone']);
  d.querySelector('[data-step="1"]').click();
  assert.deepEqual(visible(), ['solid']);
  assert.equal(d.getElementById('specimen-caption').textContent, 'Fig. 02 / Solid');
  d.querySelector('[data-step="-1"]').click();
  d.querySelector('[data-step="-1"]').click();
  assert.deepEqual(visible(), ['stroke']);
  assert.equal(d.getElementById('specimen-caption').textContent, 'Fig. 03 / Stroke');
  assert.deepEqual(errors, []);
  w.close();
});
