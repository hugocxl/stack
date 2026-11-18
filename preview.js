import {keyboard, terrain, dish} from './system/figures/index.js?v=gray';
const figures = Object.entries({Keyboard:keyboard, Terrain:terrain, Dish:dish});
const select = id => document.getElementById(id);
let current = 0;
let illustration;
function show(index) {
  current = (index + figures.length) % figures.length;
  illustration?.destroy();
  const [name, draw] = figures[current];
  illustration = draw(select('figure'));
  select('caption').textContent = 'FIG. 0' + (current + 1) + ' / ' + name;
}
show(0);
select('prev').onclick = () => show(current - 1);
select('next').onclick = () => show(current + 1);
for (const [name, token] of Object.entries({Canvas:'--cxl-ink', Foreground:'--cxl-paper', Graphite:'--cxl-graphite', Ring:'--cxl-silver'})) {
  const hex = getComputedStyle(document.documentElement).getPropertyValue(token).trim();
  const swatch = document.createElement('div');
  swatch.innerHTML = '<span class="chip"></span>' + name + '<small>' + hex.toUpperCase() + '</small>';
  swatch.firstChild.style.background = 'var(' + token + ')';
  document.querySelector('.swatches').append(swatch);
}
const query = select('query');
const feedback = select('figure-feedback');
query.oninput = () => {
  query.removeAttribute('aria-invalid');
  feedback.textContent = '';
};
query.form.onsubmit = event => {
  event.preventDefault();
  const requested = query.value.trim().toLowerCase();
  const index = figures.findIndex(([name]) => name.toLowerCase() === requested);
  query.setAttribute('aria-invalid', String(index < 0));
  feedback.textContent = index < 0 ? 'Choose Keyboard, Terrain, or Dish.' : 'Showing ' + figures[index][0];
  if (index >= 0) {
    show(index);
    document.querySelector('figure').scrollIntoView({block:'center'});
    select('next').focus({preventScroll:true});
  }
};

select('copy-snippet').onclick = async () => {
  try {
    await navigator.clipboard.writeText(select('stylesheet-snippet').textContent);
    select('copy-result').textContent = 'Copied stylesheet links.';
  } catch {
    select('copy-result').textContent = 'Select the snippet to copy it manually.';
  }
};
