// Behavior for this reference page. Listings are built from the specimens, so the code shown is
// the markup on the page. Icon and vector paths are elided, as in DESIGN.md.
function elide(html) {
  return html.replace(/(<svg class="ds-(vector|icon)"[^>]*>)([\s\S]*?)<\/svg>/g, (_, open, kind, inner) =>
    open + (kind === 'vector' ? (inner.match(/<title>[\s\S]*?<\/title>/) || [''])[0] : '') + `<!-- paths from @hugocxl/${kind}s -->` + '</svg>');
}
function dedent(html) {
  const lines = html.replace(/^\n+|\s+$/g, '').split('\n');
  const indent = Math.min(...lines.filter(line => line.trim()).map(line => line.match(/^ */)[0].length));
  return lines.map(line => line.slice(indent)).join('\n');
}
for (const specimen of document.querySelectorAll('.doc-specimen')) {
  const listing = document.createElement('div');
  listing.className = 'ds-code';
  listing.innerHTML = '<pre tabindex="0"><code></code></pre><button type="button">Copy</button>';
  listing.querySelector('code').textContent = dedent(elide(specimen.innerHTML));
  specimen.after(listing);
}
for (const form of document.querySelectorAll('.doc-specimen form, .doc-example form')) {
  form.addEventListener('submit', event => event.preventDefault());
}

const select = id => document.getElementById(id);
const vectors = [...select('figure').querySelectorAll('.ds-vector')];
const names = vectors.map(vector => vector.querySelector('title').textContent);
let current = 0;
function cycle(index) {
  current = (index + names.length) % names.length;
  vectors.forEach((vector, i) => vector.toggleAttribute('hidden', i !== current));
  select('caption').textContent = 'Fig. 0' + (current + 1) + ' / ' + names[current];
}
select('prev').onclick = () => cycle(current - 1);
select('next').onclick = () => cycle(current + 1);

const query = select('query');
const feedback = select('figure-feedback');
query.oninput = () => {
  query.removeAttribute('aria-invalid');
  delete feedback.dataset.status;
  feedback.textContent = '';
};
select('figure-search').onsubmit = event => {
  event.preventDefault();
  const requested = query.value.trim().toLowerCase();
  if (!requested) {
    query.setAttribute('aria-invalid', 'true');
    feedback.dataset.status = 'error';
    feedback.textContent = 'Enter a vector name.';
    return;
  }
  const index = names.findIndex(name => name.toLowerCase() === requested);
  query.setAttribute('aria-invalid', String(index < 0));
  feedback.dataset.status = index < 0 ? 'error' : 'success';
  feedback.textContent = index < 0 ? 'Choose ' + names.slice(0, -1).join(', ') + ', or ' + names.at(-1) + '.' : 'Showing ' + names[index];
  if (index >= 0) {
    cycle(index);
    select('opening-figure').scrollIntoView({ block: 'center' });
    select('next').focus({ preventScroll: true });
  }
};
