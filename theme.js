const preference = window.matchMedia('(prefers-color-scheme: dark)');
function applyTheme() {
  document.documentElement.dataset.theme = localStorage.getItem('cxl-theme') || (preference.matches ? 'dark' : 'light');
}
applyTheme();
preference.addEventListener('change', applyTheme);
