import { createElement, forwardRef } from "react";
export const GuidePointIcon = /*#__PURE__*/ forwardRef(function GuidePointIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M1.4 8C1.4 7.144 2.094 6.45 2.95 6.45C3.6124 6.45 4.1777 6.8655 4.3996 7.45H11.6004C11.8223 6.8655 12.3876 6.45 13.05 6.45C13.906 6.45 14.6 7.144 14.6 8C14.6 8.856 13.906 9.55 13.05 9.55C12.3876 9.55 11.8223 9.1345 11.6004 8.55H4.3996C4.1777 9.1345 3.6124 9.55 2.95 9.55C2.094 9.55 1.4 8.856 1.4 8Z", "fill": "currentColor"}));
});
