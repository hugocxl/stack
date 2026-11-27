import { createElement, forwardRef } from "react";
export const BoldIcon = /*#__PURE__*/ forwardRef(function BoldIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M4.024 3.301H8.131C11.461 3.301 12.09 6.594 10.018 7.741C12.719 8.814 12.053 12.699 8.575 12.699H4.024ZM6.096 8.777V10.886H8.242C10.203 10.886 10.203 8.777 8.242 8.777ZM6.096 5.114V7.001H7.835C9.685 7.001 9.685 5.114 7.835 5.114Z", "fill": "currentColor"}));
});
