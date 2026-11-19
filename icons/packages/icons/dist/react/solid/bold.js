import { createElement, forwardRef } from "react";
export const BoldIcon = /*#__PURE__*/ forwardRef(function BoldIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.1 1.65H8.65C13.15 1.65 14 6.1 11.2 7.65C14.85 9.1 13.95 14.35 9.25 14.35H3.1ZM5.9 9.05V11.9H8.8C11.45 11.9 11.45 9.05 8.8 9.05ZM5.9 4.1V6.65H8.25C10.75 6.65 10.75 4.1 8.25 4.1Z", "fill": "currentColor"}));
});
