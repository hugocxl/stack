import { createElement, forwardRef } from "react";
export const LayoutTemplateIcon = /*#__PURE__*/ forwardRef(function LayoutTemplateIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M2.4 2.08 13.6 2.08Q14.3124 2.08 14.8162 2.5838Q15.32 3.0876 15.32 3.8V12.2Q15.32 12.9124 14.8162 13.4162Q14.3124 13.92 13.6 13.92H2.4Q1.6876 13.92 1.1838 13.4162Q0.68 12.9124 0.68 12.2L0.68 3.8Q0.68 3.0876 1.1838 2.5838Q1.6876 2.08 2.4 2.08ZM1.58 6.82H5.48V13.02H6.52V6.82H14.42V5.78H1.58Z", "fill": "currentColor"}));
});
