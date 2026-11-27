import { createElement, forwardRef } from "react";
export const DotIcon = /*#__PURE__*/ forwardRef(function DotIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.65 8C3.65 5.5976 5.5976 3.65 8 3.65C10.4024 3.65 12.35 5.5976 12.35 8C12.35 10.4024 10.4024 12.35 8 12.35C5.5976 12.35 3.65 10.4024 3.65 8Z", "fill": "currentColor"}));
});
