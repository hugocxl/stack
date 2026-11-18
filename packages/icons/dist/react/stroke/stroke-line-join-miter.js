import { createElement, forwardRef } from "react";
export const StrokeLineJoinMiterIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinMiterIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M0.8 13.2 8 1.4 15.2 13.2 12.6 14.6 8 6.9 3.4 14.6Z", "fill": "currentColor"}));
});
