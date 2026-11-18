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
select('theme').onclick = () => {
  localStorage.setItem('cxl-theme', document.documentElement.dataset.theme === 'light' ? 'dark' : 'light');
  applyTheme();
};
for (const name of ['Paper','Silver','Graphite','Ink']) {
  const token = '--cxl-' + name.toLowerCase();
  const hex = getComputedStyle(document.documentElement).getPropertyValue(token).trim();
  const swatch = document.createElement('div');
  swatch.innerHTML = '<span class="chip"></span>' + name + '<small>' + hex.toUpperCase() + '</small>';
  swatch.firstChild.style.background = 'var(' + token + ')';
  document.querySelector('.swatches').append(swatch);
}
document.querySelector('form').onsubmit = event => {
  event.preventDefault();
  const query = select('query').value.trim().toLowerCase();
  const index = figures.findIndex(([name]) => name.toLowerCase() === query);
  document.querySelector('output').textContent = index < 0 ? 'Choose Keyboard, Terrain, or Dish.' : 'Showing ' + figures[index][0];
  if (index >= 0) {
    show(index);
    document.querySelector('figure').scrollIntoView({block:'center'});
    select('next').focus({preventScroll:true});
  }
};
