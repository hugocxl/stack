import { createElement, forwardRef } from "react";
export const SquareStarIcon = /*#__PURE__*/ forwardRef(function SquareStarIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.25 1.45H12.75Q13.4956 1.45 14.0228 1.9772Q14.55 2.5044 14.55 3.25V12.75Q14.55 13.4956 14.0228 14.0228Q13.4956 14.55 12.75 14.55H3.25Q2.5044 14.55 1.9772 14.0228Q1.45 13.4956 1.45 12.75V3.25Q1.45 2.5044 1.9772 1.9772Q2.5044 1.45 3.25 1.45ZM8 4.75 7 6.85 4.75 7.15 6.4 8.75 6 11 8 9.9 10 11 9.6 8.75 11.25 7.15 9 6.85Z", "fill": "currentColor"}));
});
