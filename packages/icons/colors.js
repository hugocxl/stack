// Color is independent of drawing style. Omitting appearance follows the web theme.
import { hues, palette } from './dist/colors.js';

export function defaultColor(name, appearance) {
  if (!Object.hasOwn(hues, name)) return undefined;
  const hue = hues[name];
  const { light, dark } = palette[hue];
  if (appearance === 'light') return light;
  if (appearance === 'dark') return dark;
  return `var(--ds-${hue}, light-dark(${light}, ${dark}))`;
}
