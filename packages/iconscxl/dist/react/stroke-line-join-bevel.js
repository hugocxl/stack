import { createElement, forwardRef } from "react";
export const StrokeLineJoinBevelIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinBevelIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M1 12 6.5 2.5H9.5L15 12L12.5 13.5L8 5.8L3.5 13.5Z", "fill": "currentColor"}));
});
