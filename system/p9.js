// P9DS runtime: mounts [data-figure] drawings and wires .p9-code copy buttons.
import * as figures from './figures/index.js';

const mounted = new Map();

export function show(element, name) {
  mounted.get(element)?.destroy();
  element.dataset.figure = name;
  mounted.set(element, figures[name](element));
}

export function mountFigures(root = document) {
  for (const element of root.querySelectorAll('[data-figure]')) {
    if (!mounted.has(element) && figures[element.dataset.figure]) show(element, element.dataset.figure);
  }
}

document.addEventListener('click', async event => {
  const button = event.target.closest('.p9-code button');
  if (!button) return;
  try {
    await navigator.clipboard.writeText(button.closest('.p9-code').querySelector('pre').textContent);
    button.textContent = 'Copied';
  } catch {
    button.textContent = 'Select to copy';
  }
  setTimeout(() => { button.textContent = 'Copy' }, 1600);
});

mountFigures();
