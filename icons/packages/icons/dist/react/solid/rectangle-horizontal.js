import { createElement, forwardRef } from "react";
export const RectangleHorizontalIcon = /*#__PURE__*/ forwardRef(function RectangleHorizontalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.05 3.45H12.95Q13.6956 3.45 14.2228 3.9772Q14.75 4.5044 14.75 5.25V10.75Q14.75 11.4956 14.2228 12.0228Q13.6956 12.55 12.95 12.55H3.05Q2.3044 12.55 1.7772 12.0228Q1.25 11.4956 1.25 10.75V5.25Q1.25 4.5044 1.7772 3.9772Q2.3044 3.45 3.05 3.45Z", "fill": "currentColor"}));
});
