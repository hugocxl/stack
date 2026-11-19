import { readFileSync } from 'node:fs';
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { parse } from 'yaml';

const read = path => readFileSync(new URL('../' + path, import.meta.url), 'utf8');
const design = read('DESIGN.md');
const { colors, typography, spacing, rounded } = parse(design.split('---')[1]);
const schema = JSON.parse(read('system/plan.schema.json'));
const px = value => parseFloat(value);

test('the opening paragraph links to every section of the article', async ({ page }) => {
  await page.goto('/');
  const links = page.locator('.ds-opening > .ds-section').first().locator('a');
  await expect(links).toHaveCount(11);
  for (const link of await links.all()) {
    const fragment = await link.getAttribute('href');
    expect(fragment).toMatch(/^#[a-z]+$/);
    await link.click();
    await expect(page).toHaveURL(new RegExp(fragment + '$'));
    await expect(page.locator(fragment + ' > h2')).toBeInViewport();
  }
});

test('DESIGN.md, the schema and the page name the same thirteen components', async ({ page }) => {
  await page.goto('/');
  const specimens = await page.locator('.doc-specimen').evaluateAll(nodes => nodes.map(node => node.dataset.component));
  const documented = [...design.matchAll(/^### `([a-z-]+)`$/gm)].map(match => match[1]);
  expect(specimens).toHaveLength(13);
  expect(documented).toEqual(specimens);
  expect(schema.$defs.block.properties.component.enum).toEqual(specimens);
  for (const id of specimens) expect(schema.$defs[id].properties.component.const).toBe(id);
});

for (const layout of ['plain', 'field']) for (const width of [320, 760, 761, 1440]) {
  test(`${layout} layout geometry at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/');
    await page.evaluate(layout => { document.body.dataset.layout = layout }, layout);
    await page.evaluate(() => document.fonts.ready);
    const metrics = await page.evaluate(() => {
      const article = document.querySelector('.ds-opening');
      const main = document.querySelector('main').getBoundingClientRect();
      const column = article.getBoundingClientRect();
      const figure = document.querySelector('#opening-figure').getBoundingClientRect();
      const style = getComputedStyle(article);
      const field = getComputedStyle(document.body, '::after');
      return {
        scrollWidth: document.documentElement.scrollWidth,
        mainLeft: main.left,
        mainWidth: main.width,
        columnLeft: column.left,
        columnWidth: column.width,
        measure: parseFloat(style.fontSize) * 30,
        figureLeft: figure.left,
        figureWidth: figure.width,
        readingSize: parseFloat(style.fontSize),
        lineHeight: parseFloat(style.lineHeight) / parseFloat(style.fontSize),
        titleSize: parseFloat(getComputedStyle(document.querySelector('.ds-title h1')).fontSize),
        headingSize: parseFloat(getComputedStyle(document.querySelector('.ds-section > h2')).fontSize),
        paragraphGap: parseFloat(getComputedStyle(document.querySelector('.ds-section p + p')).marginTop),
        sectionGap: parseFloat(getComputedStyle(document.querySelector('#principles')).marginTop),
        fieldWidth: parseFloat(field.width),
      };
    });

    expect(metrics.scrollWidth).toBe(width);
    const columnWidth = Math.min(metrics.measure, metrics.mainWidth);
    const figureWidth = Math.min(metrics.mainWidth, 1280);
    expect(metrics.columnWidth).toBeCloseTo(columnWidth, 0);
    expect(metrics.columnLeft).toBeCloseTo(metrics.mainLeft + (layout === 'plain' ? (metrics.mainWidth - columnWidth) / 2 : 0), 0);
    expect(metrics.figureLeft).toBeCloseTo(metrics.mainLeft + (layout === 'plain' ? (metrics.mainWidth - figureWidth) / 2 : 0), 0);
    expect(metrics.figureWidth).toBeCloseTo(Math.min(metrics.mainWidth, 1280), 0);
    expect(metrics.readingSize).toBeCloseTo(Math.min(16 + width * 0.0036, 16 * 1.54), 2);
    expect(metrics.lineHeight).toBeCloseTo(typography.reading.lineHeight, 2);
    expect(metrics.titleSize).toBeCloseTo(metrics.readingSize * 1.4, 1);
    expect(metrics.headingSize).toBe(metrics.readingSize);
    expect(metrics.paragraphGap).toBe(px(spacing.paragraph));
    expect(metrics.sectionGap).toBe(px(spacing.section));
    const gutter = Math.min(Math.max(20, width * 0.045), 64);
    const field = width <= 760 ? 20 : Math.min(Math.max(width * 0.3, width - 2 * gutter - 47.6 * 16), width * 0.4);
    if (layout === 'field') expect(metrics.fieldWidth).toBeCloseTo(width <= 760 ? 12 : field - 12, 0);
    else expect(Number.isNaN(metrics.fieldWidth) || metrics.fieldWidth === 0).toBe(true);
  });
}

for (const mode of ['light', 'dark']) {
  test(`${mode} tokens, type and accessibility`, async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 900 });
    await page.emulateMedia({ colorScheme: mode });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (!response.ok() && response.status() !== 304) errors.push(`${response.status()} ${response.url()}`);
    });
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);
    await expect(page.locator('html')).toHaveAttribute('data-theme', mode);

    const tokens = await page.evaluate(names => {
      const style = getComputedStyle(document.documentElement);
      return Object.fromEntries(names.map(name => [name, style.getPropertyValue('--ds-' + name).trim()]));
    }, Object.keys(colors[mode]));
    expect(tokens).toEqual(colors[mode]);
    expect(await page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--ds-accent').trim())).toBe(colors.accent);

    await expect(page.getByRole('article')).toHaveCSS('font-weight', String(typography.reading.fontWeight));
    await expect(page.locator('.ds-opening > .ds-title h1')).toHaveCSS('font-weight', String(typography.title.fontWeight));
    await expect(page.locator('#principles > h2')).toHaveCSS('font-weight', String(typography.heading.fontWeight));
    await expect(page.locator('#caption')).toHaveCSS('font-size', typography.label.fontSize);
    await expect(page.locator('body > .ds-footer a').first()).toHaveCSS('font-size', typography.mono.fontSize);
    await expect(page.locator('#c-button .ds-button')).toHaveCSS('font-size', typography.control.fontSize);
    await expect(page.locator('#c-button .ds-button')).toHaveCSS('border-radius', rounded.control);
    const button = await page.locator('#c-button .ds-button').evaluate(node => [getComputedStyle(node).color, getComputedStyle(node).backgroundColor]);
    const rgb = hex => `rgb(${hex.slice(1).match(/../g).map(pair => parseInt(pair, 16)).join(', ')})`;
    expect(button).toEqual([rgb(colors[mode].canvas), rgb(colors[mode].ink)]);
    await expect(page.locator('#opening-figure .ds-media')).toHaveCSS('border-radius', rounded.media);
    await expect(page.locator('.ds-pager')).toHaveCSS('border-radius', rounded.pill);
    await expect(page.getByRole('button', { name: 'Next figure' })).toHaveCSS('height', spacing.target);
    const loadedFonts = await page.evaluate(() => Array.from(document.fonts).filter(font => font.status === 'loaded').map(font => font.family));
    expect(loadedFonts).toEqual(expect.arrayContaining(['Geist Sans', 'Geist Mono']));

    const { violations } = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();
    expect(violations.map(({ id, nodes }) => ({ id, targets: nodes.map(node => node.target) }))).toEqual([]);
    expect(errors).toEqual([]);
  });
}

test('the example home page follows its recipe and accent budget', async ({ page }) => {
  await page.goto('/');
  const example = page.locator('.doc-example-page');
  const sequence = await example.evaluate(root => {
    const names = {
      'ds-masthead': 'masthead', 'ds-statement': 'statement', 'ds-meta': 'meta', 'ds-section': 'section',
      'ds-grid': 'figure-grid', 'ds-form': 'form', 'ds-footer': 'footer', 'ds-button': 'button',
    };
    const blocks = [root.querySelector('.ds-masthead'), ...root.querySelector('.ds-column').children, root.querySelector('.ds-footer')];
    return blocks.map(block => names[[...block.classList].find(name => names[name])]);
  });
  expect(sequence.join(' ')).toMatch(/^masthead statement( meta)? section (figure-wide|figure-grid)( section)*( button| form)? footer$/);
  await expect(example.locator('.ds-accent, .ds-dot')).toHaveCount(2);
  await expect(example.locator('.ds-button')).toHaveCount(0);
  const accent = await example.locator('.ds-accent').evaluate(node => getComputedStyle(node).color);
  expect(accent).toBe('rgb(206, 119, 85)');
});

test('component listings show the specimen markup', async ({ page }) => {
  await page.goto('/');
  const listings = page.locator('.doc-specimen + .ds-code code');
  await expect(listings).toHaveCount(13);
  await expect(listings.nth(1)).toHaveText('<hgroup class="ds-title">\n  <h1>Public testing is beginning</h1>\n  <p>Fieldwork team</p>\n</hgroup>');
  for (const listing of await listings.all()) await expect(listing).not.toContainText('<path');
});

test('icons and vectors draw in the text color at their documented sizes', async ({ page }) => {
  await page.goto('/');
  for (const theme of ['light', 'dark']) {
    await page.evaluate(theme => { document.documentElement.dataset.theme = theme }, theme);
    const icon = await page.locator('#icon-example a:not(.ds-button) .ds-icon').evaluate(node => {
      const link = getComputedStyle(node.closest('a'));
      const box = node.getBoundingClientRect();
      return { width: box.width, size: parseFloat(link.fontSize), color: getComputedStyle(node).color, linkColor: link.color, hidden: node.getAttribute('aria-hidden') };
    });
    expect(icon.width).toBeCloseTo(icon.size, 0);
    expect(icon.color).toBe(icon.linkColor);
    expect(icon.hidden).toBe('true');
    const vector = await page.locator('#vector-example .ds-vector').evaluate(node => {
      const box = node.getBoundingClientRect();
      return { ratio: box.width / box.height, color: getComputedStyle(node).color, ink: getComputedStyle(document.body).color, title: node.querySelector('title')?.textContent };
    });
    expect(vector.ratio).toBeCloseTo(4 / 3, 1);
    expect(vector.color).toBe(vector.ink);
    expect(vector.title).toBeTruthy();
  }
});

test('hues and status colors reach 3:1 and color only their marks', async ({ page }) => {
  const hues = ['red', 'orange', 'yellow', 'green', 'teal', 'sky', 'blue', 'violet', 'purple', 'pink', 'brown'];
  const roles = { success: 'green', warning: 'yellow', error: 'red', info: 'blue', neutral: 'muted' };
  const luminance = hex => {
    const [r, g, b] = hex.slice(1, 7).match(/../g).map(pair => parseInt(pair, 16) / 255).map(c => c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  };
  const contrast = (a, b) => { const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05) };
  const rgb = hex => `rgb(${hex.slice(1).match(/../g).map(pair => parseInt(pair, 16)).join(', ')})`;
  await page.goto('/');
  for (const mode of ['light', 'dark']) {
    const palette = colors[mode];
    for (const hue of hues) for (const ground of ['canvas', 'surface']) expect(contrast(palette[hue], palette[ground]), `${mode} ${hue} on ${ground}`).toBeGreaterThanOrEqual(3);
    for (const [role, hue] of Object.entries(roles)) expect(palette[role], `${mode} ${role}`).toBe(palette[hue]);

    await page.evaluate(theme => { document.documentElement.dataset.theme = theme }, mode);
    const dots = await page.locator('#status-example .ds-dot').evaluateAll(nodes => nodes.map(node => [node.dataset.status, getComputedStyle(node).backgroundColor, getComputedStyle(node.parentElement).color]));
    expect(dots.map(([status]) => status)).toEqual(Object.keys(roles));
    for (const [status, background, text] of dots) {
      expect(background).toBe(rgb(palette[status]));
      expect(text).toBe(rgb(palette.muted));
    }
    for (const icon of await page.locator('#colored-icon-example .ds-icon').all()) {
      const { name, color, text } = await icon.evaluate(node => ({ name: node.dataset.color ?? node.dataset.status, color: getComputedStyle(node).color, text: getComputedStyle(node.parentElement).color }));
      expect(color).toBe(rgb(palette[name]));
      expect(text).toBe(rgb(palette.ink));
    }
  }
});

test('keyboard vector browsing and search feedback', async ({ page }) => {
  await page.goto('/');
  const caption = page.locator('#caption');
  const visible = page.locator('#figure .ds-vector:visible');
  const next = page.getByRole('button', { name: 'Next figure' });
  await expect(caption).toHaveText('Fig. 01 / Product launch');
  await expect(visible).toHaveCount(1);
  await next.focus();
  await page.keyboard.press('Enter');
  await expect(caption).toHaveText('Fig. 02 / Modular design');
  await expect(visible).toHaveAttribute('data-vector', 'modular-design');

  const search = page.getByLabel('Find a vector');
  const feedback = page.locator('#figure-feedback');
  await search.press('Enter');
  await expect(feedback).toHaveText('Enter a vector name.');
  await expect(feedback).toHaveAttribute('data-status', 'error');
  await search.fill('Unknown');
  await expect(feedback).toHaveText('');
  await expect(feedback).not.toHaveAttribute('data-status');
  await search.press('Enter');
  await expect(feedback).toHaveText('Choose Product launch, Modular design, or Fast performance.');
  await expect(search).toHaveAttribute('aria-invalid', 'true');
  await expect(search).toHaveValue('Unknown');
  await search.fill(' fast performance ');
  await expect(search).not.toHaveAttribute('aria-invalid');
  await search.press('Enter');
  await expect(caption).toHaveText('Fig. 03 / Fast performance');
  await expect(feedback).toHaveText('Showing Fast performance');
  await expect(feedback).toHaveAttribute('data-status', 'success');
  await expect(next).toBeFocused();
});

test('only @hugocxl icons and vectors draw on the page', async ({ page }) => {
  await page.goto('/');
  const stray = await page.evaluate(() => {
    const glyphs = /[◐←→↩↑↓↗]/;
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const found = [];
    for (let node; (node = walker.nextNode());) {
      if (node.parentElement.closest('pre, code, li, .doc-stack-example')) continue;
      if (glyphs.test(node.textContent)) found.push(node.textContent.trim());
    }
    const svgs = [...document.querySelectorAll('svg')].filter(svg => !svg.matches('.ds-icon, .ds-vector') && !svg.closest('.ds-icon, .ds-vector'));
    return { found, svgs: svgs.length, figures: document.querySelectorAll('[data-figure]').length };
  });
  expect(stray).toEqual({ found: [], svgs: 0, figures: 0 });
  for (const button of await page.locator('.ds-theme, .ds-pager button, .ds-input button').all()) {
    await expect(button.locator('svg.ds-icon')).toHaveCount(1);
    await expect(button).toHaveAttribute('aria-label', /.+/);
  }
});

test('theme selection persists across visits', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'light' });
  await page.goto('/');
  await page.locator('body > .ds-masthead .ds-theme').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
});

test('the old guide URL forwards to the article', async ({ page }) => {
  await page.goto('/system/interface-guidelines.html');
  await expect(page).toHaveURL('/#principles');
  await expect(page.locator('#principles > h2')).toBeInViewport();
});
