import { readFileSync } from 'node:fs';
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { parse } from 'yaml';

const design = readFileSync(new URL('../DESIGN.md', import.meta.url), 'utf8');
const { colors, typography, spacing, rounded } = parse(design.split('---')[1]);

test('the opening paragraph links to sections of the same article', async ({ page }) => {
  await page.goto('/');
  const article = page.getByRole('article');
  await expect(article).toHaveCount(1);
  const links = article.locator('.cxl-introduction + p a');
  await expect(links).toHaveCount(6);
  for (const link of await links.all()) {
    const fragment = await link.getAttribute('href');
    expect(fragment).toMatch(/^#[a-z-]+$/);
    await expect(article.locator(fragment)).toHaveCount(1);
    await link.click();
    await expect(page).toHaveURL(new RegExp(fragment + '$'));
    await expect(article.locator(fragment).getByRole('heading')).toBeInViewport();
  }

  const [download] = await Promise.all([
    page.waitForEvent('download'),
    page.getByRole('link', { name: 'Download DESIGN.md' }).click(),
  ]);
  expect(download.suggestedFilename()).toBe('DESIGN.md');
});

for (const width of [320, 646, 760, 761, 1440]) {
  test(`editorial layout at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);
    const reading = page.getByRole('article');
    const metrics = await reading.evaluate(article => {
      const main = article.closest('main').getBoundingClientRect();
      const column = article.getBoundingClientRect();
      const figure = article.querySelector('figure').getBoundingClientRect();
      const style = getComputedStyle(article);
      const intro = getComputedStyle(article.querySelector('.cxl-introduction'));
      const section = getComputedStyle(article.querySelector('section'));
      const rootSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
      return {
        scrollWidth: document.documentElement.scrollWidth,
        mainWidth: main.width,
        columnWidth: column.width,
        maxWidth: parseFloat(style.maxWidth),
        centerOffset: column.left + column.width / 2 - (main.left + main.width / 2),
        figureWidth: figure.width,
        figureOffset: figure.left + figure.width / 2 - (main.left + main.width / 2),
        paragraphMargin: parseFloat(intro.marginBottom) / rootSize,
        sectionMargin: parseFloat(section.marginTop) / rootSize,
        readingLineHeight: parseFloat(style.lineHeight) / parseFloat(style.fontSize),
        readingSize: parseFloat(style.fontSize),
        headingSize: parseFloat(getComputedStyle(article.querySelector('h2')).fontSize),
        textureWidth: parseFloat(getComputedStyle(document.body, '::after').width),
      };
    });

    expect(metrics.scrollWidth).toBe(width);
    expect(metrics.columnWidth).toBeCloseTo(Math.min(metrics.maxWidth, metrics.mainWidth), 0);
    expect(metrics.centerOffset).toBeCloseTo(0, 0);
    expect(metrics.figureWidth).toBeCloseTo(Math.min(metrics.mainWidth, 1280), 0);
    expect(metrics.figureOffset).toBeCloseTo(0, 0);
    expect(metrics.paragraphMargin).toBe(parseFloat(spacing.paragraph));
    expect(metrics.sectionMargin).toBe(parseFloat(spacing.section));
    expect(metrics.readingLineHeight).toBeCloseTo(typography.reading.lineHeight, 2);
    expect(metrics.readingSize).toBeCloseTo(Math.min(16 + width * 0.0036, 16 * 1.54), 2);
    expect(metrics.headingSize).toBe(metrics.readingSize);
    expect(metrics.textureWidth).toBeCloseTo(width <= 760 ? 12 : Math.max(240, width * 0.23) - 10, 0);
  });
}

for (const mode of ['light', 'dark']) {
  test(`${mode} tokens, type and accessibility`, async ({ page }) => {
    await page.setViewportSize({ width: 646, height: 900 });
    await page.emulateMedia({ colorScheme: mode });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (!response.ok() && response.status() !== 304) errors.push(`${response.status()} ${response.url()}`);
    });
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);

    const canvas = mode === 'light' ? colors.paper : colors.primary;
    const foreground = mode === 'light' ? colors.primary : colors.paper;
    const root = page.locator('html');
    await expect(root).toHaveAttribute('data-theme', mode);
    const tokens = await root.evaluate(element => {
      const style = getComputedStyle(element);
      const names = ['bg', 'text', 'muted', 'surface', 'line', 'graphite', 'radius'];
      return Object.fromEntries(names.map(name => [name, style.getPropertyValue('--cxl-' + name).trim()]));
    });
    expect(tokens).toEqual({
      bg: canvas,
      text: foreground,
      muted: colors[mode].muted,
      surface: colors[mode].surface,
      line: mode === 'light' ? colors.ring : colors.dark.line,
      graphite: colors.graphite,
      radius: rounded.control,
    });
    await expect(page.getByRole('article')).toHaveCSS('font-weight', String(typography.reading.fontWeight));
    await expect(page.locator('.cxl-introduction')).toHaveCSS('font-weight', String(typography.introduction.fontWeight));
    await expect(page.locator('#site-building strong').first()).toHaveCSS('font-weight', String(typography.emphasis.fontWeight));
    await expect(page.locator('#caption')).toHaveCSS('font-size', typography.caption.fontSize);
    await expect(page.getByRole('button', { name: 'Preview' })).toHaveCSS('font-size', typography.control.fontSize);
    await expect(page.getByRole('button', { name: 'Preview' })).toHaveCSS('border-radius', rounded.control);
    await expect(page.locator('.cxl-pager')).toHaveCSS('border-radius', rounded.material);
    await expect(page.getByRole('button', { name: 'Next figure' })).toHaveCSS('height', spacing.target);
    const loadedFonts = await page.evaluate(() => Array.from(document.fonts)
      .filter(font => font.status === 'loaded').map(font => font.family));
    expect(loadedFonts).toEqual(expect.arrayContaining([typography.reading.fontFamily, typography.caption.fontFamily]));

    const { violations } = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();
    expect(violations.map(({ id, nodes }) => ({ id, targets: nodes.map(node => node.target) }))).toEqual([]);
    expect(errors).toEqual([]);
  });
}

test('keyboard figure browsing and search feedback', async ({ page }) => {
  await page.goto('/');
  const caption = page.locator('#caption');
  const next = page.getByRole('button', { name: 'Next figure' });
  await expect(caption).toContainText('Keyboard');
  await next.focus();
  await page.keyboard.press('Enter');
  await expect(caption).toContainText('Terrain');

  const search = page.getByLabel('Find a figure');
  await search.fill('Unknown');
  await search.press('Enter');
  await expect(page.locator('form output')).toHaveText('Choose Keyboard, Terrain, or Dish.');
  await expect(search).toHaveAttribute('aria-invalid', 'true');
  await expect(search).toHaveValue('Unknown');
  await search.fill('dish');
  await search.press('Enter');
  await expect(caption).toContainText('Dish');
  await expect(page.locator('form output')).toHaveText('Showing Dish');
  await expect(next).toBeFocused();
});

test('theme selection persists on the reference page', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'light' });
  await page.goto('/');
  await page.getByRole('button', { name: 'Switch theme' }).click();
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
});

test('the old guide URL forwards to the article', async ({ page }) => {
  await page.goto('/system/interface-guidelines.html');
  await expect(page).toHaveURL('/#guidelines');
  await expect(page.getByRole('heading', { name: 'Interface guidelines' })).toBeInViewport();
});
