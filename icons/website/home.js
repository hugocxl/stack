// Cycle the home specimen through the three drawing styles.
const figure = document.getElementById('specimen');
const specimens = [...figure.querySelectorAll('[data-style]')];
const caption = document.getElementById('specimen-caption');
let current = 0;
figure.addEventListener('click', event => {
  const button = event.target.closest('[data-step]');
  if (!button) return;
  current = (current + Number(button.dataset.step) + specimens.length) % specimens.length;
  specimens.forEach((specimen, index) => { specimen.hidden = index !== current });
  caption.textContent = specimens[current].dataset.caption;
});
