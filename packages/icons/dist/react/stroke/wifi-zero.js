import { createElement, forwardRef } from "react";
export const WifiZeroIcon = /*#__PURE__*/ forwardRef(function WifiZeroIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M7.25 13C7.25 12.5858 7.5858 12.25 8 12.25C8.4142 12.25 8.75 12.5858 8.75 13C8.75 13.4142 8.4142 13.75 8 13.75C7.5858 13.75 7.25 13.4142 7.25 13Z", "fill": "currentColor"}));
});
