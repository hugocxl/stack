import { createElement, forwardRef } from "react";
export const BookmarkIcon = /*#__PURE__*/ forwardRef(function BookmarkIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M5 1.13 11 1.13Q11.7554 1.13 12.2877 1.6623Q12.82 2.1946 12.82 2.95V13.35Q12.82 14.1216 12.1459 14.449Q11.4768 14.774 10.8807 14.3105L8 12.1049L5.1161 14.3129Q4.5232 14.774 3.8541 14.449Q3.18 14.1216 3.18 13.35L3.18 2.95Q3.18 2.1946 3.7123 1.6623Q4.2446 1.13 5 1.13Z", "fill": "currentColor"}));
});
