import { createElement, forwardRef } from "react";
export const PauseBarsIcon = /*#__PURE__*/ forwardRef(function PauseBarsIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M10.75 2H11.25C11.9404 2 12.5 2.5596 12.5 3.25V12.75C12.5 13.4404 11.9404 14 11.25 14H10.75C10.0596 14 9.5 13.4404 9.5 12.75V3.25C9.5 2.5596 10.0596 2 10.75 2ZM4.75 2H5.25C5.9404 2 6.5 2.5596 6.5 3.25V12.75C6.5 13.4404 5.9404 14 5.25 14H4.75C4.0596 14 3.5 13.4404 3.5 12.75V3.25C3.5 2.5596 4.0596 2 4.75 2Z", "fill": "currentColor"}));
});
