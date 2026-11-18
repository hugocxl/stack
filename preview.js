// Behavior for this reference page. Listings are built from the specimens before figures mount,
// so the code shown is exactly the markup on the page.
function dedent(html) {
  const lines = html.replace(/^\n+|\s+$/g, '').split('\n');
  const indent = Math.min(...lines.filter(line => line.trim()).map(line => line.match(/^ */)[0].length));
  return lines.map(line => line.slice(indent)).join('\n');
}
for (const specimen of document.querySelectorAll('.doc-specimen')) {
  const listing = document.createElement('div');
  listing.className = 'p9-code';
  listing.innerHTML = '<pre tabindex="0"><code></code></pre><button type="button">Copy</button>';
  listing.querySelector('code').textContent = dedent(specimen.innerHTML);
  specimen.after(listing);
}
for (const form of document.querySelectorAll('.doc-specimen form, .doc-example form')) {
  form.addEventListener('submit', event => event.preventDefault());
}

const { show } = await import('./system/p9.js?v=2');

const names = ['Keyboard', 'Terrain', 'Dish'];
const select = id => document.getElementById(id);
const figure = select('figure');
let current = 0;
function cycle(index) {
  current = (index + names.length) % names.length;
  show(figure, names[current].toLowerCase());
  figure.setAttribute('aria-label', 'Isometric ' + names[current].toLowerCase() + ' drawing');
  select('caption').textContent = 'Fig. 0' + (current + 1) + ' / ' + names[current];
}
select('prev').onclick = () => cycle(current - 1);
select('next').onclick = () => cycle(current + 1);

const query = select('query');
const feedback = select('figure-feedback');
query.oninput = () => {
  query.removeAttribute('aria-invalid');
  feedback.textContent = '';
};
select('figure-search').onsubmit = event => {
  event.preventDefault();
  const requested = query.value.trim().toLowerCase();
  if (!requested) {
    query.setAttribute('aria-invalid', 'true');
    feedback.textContent = 'Enter a figure name.';
    return;
  }
  const index = names.findIndex(name => name.toLowerCase() === requested);
  query.setAttribute('aria-invalid', String(index < 0));
  feedback.textContent = index < 0 ? 'Choose Keyboard, Terrain, or Dish.' : 'Showing ' + names[index];
  if (index >= 0) {
    cycle(index);
    select('opening-figure').scrollIntoView({ block: 'center' });
    select('next').focus({ preventScroll: true });
  }
};
