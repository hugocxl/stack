const preference = window.matchMedia('(prefers-color-scheme: dark)');
function applyTheme() {
  document.documentElement.dataset.theme = localStorage.getItem('cxl-theme') || (preference.matches ? 'dark' : 'light');
}
applyTheme();
preference.addEventListener('change', applyTheme);

document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('theme');
  if (!toggle) return;
  toggle.onclick = () => {
    localStorage.setItem('cxl-theme', document.documentElement.dataset.theme === 'light' ? 'dark' : 'light');
    applyTheme();
  };
});
