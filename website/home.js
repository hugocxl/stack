// Cycle the opening figure through a few vectors. The first one is inlined at build time.
const figures = JSON.parse(document.getElementById('home-figures').textContent);
const media = document.getElementById('home-media');
const caption = document.getElementById('home-caption');
const cache = new Map();
let current = 0;

export const inline = text => text
  .replace(' xmlns="http://www.w3.org/2000/svg"', ' class="p9-vector"')
  .replace(/ color="[^"]*"/, '');

async function show(index) {
  current = (index + figures.length) % figures.length;
  const { name, title } = figures[current];
  const requested = current;
  if (!cache.has(name)) cache.set(name, fetch(`figures/${name}.svg`).then(response => response.text()));
  const svg = await cache.get(name);
  if (requested !== current) return;
  media.innerHTML = inline(svg);
  caption.textContent = `Fig. ${String(current + 1).padStart(2, '0')} / ${title}`;
}

document.getElementById('home-prev').addEventListener('click', () => show(current - 1));
document.getElementById('home-next').addEventListener('click', () => show(current + 1));
