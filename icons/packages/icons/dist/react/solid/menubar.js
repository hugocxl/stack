import { createElement, forwardRef } from "react";
export const MenubarIcon = /*#__PURE__*/ forwardRef(function MenubarIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.145 2.33 12.855 2.33Q13.8574 2.33 14.5662 3.0388Q15.275 3.7476 15.275 4.75V11.25Q15.275 12.2524 14.5662 12.9612Q13.8574 13.67 12.855 13.67H3.145Q2.1426 13.67 1.4338 12.9612Q0.725 12.2524 0.725 11.25L0.725 4.75Q0.725 3.7476 1.4338 3.0388Q2.1426 2.33 3.145 2.33ZM1.765 5.97H14.235V4.93H1.765Z", "fill": "currentColor"}));
});
