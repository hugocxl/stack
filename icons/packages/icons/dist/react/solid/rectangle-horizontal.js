import { createElement, forwardRef } from "react";
export const RectangleHorizontalIcon = /*#__PURE__*/ forwardRef(function RectangleHorizontalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M2.37 2.3H13.63Q14.3424 2.3 14.8462 2.8038Q15.35 3.3076 15.35 4.02V11.98Q15.35 12.6924 14.8462 13.1962Q14.3424 13.7 13.63 13.7H2.37Q1.6576 13.7 1.1538 13.1962Q0.65 12.6924 0.65 11.98L0.65 4.02Q0.65 3.3076 1.1538 2.8038Q1.6576 2.3 2.37 2.3Z", "fill": "currentColor"}));
});
