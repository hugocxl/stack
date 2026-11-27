import { createElement, forwardRef } from "react";
export const PanelRightIcon = /*#__PURE__*/ forwardRef(function PanelRightIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, "aria-hidden": props["aria-label"] || props["aria-labelledby"] ? undefined : true, ...props, ref} ,createElement("path", {"d": "M3.12 2.3 12.88 2.3Q13.8824 2.3 14.5912 3.0088Q15.3 3.7176 15.3 4.72V11.28Q15.3 12.2824 14.5912 12.9912Q13.8824 13.7 12.88 13.7H3.12Q2.1176 13.7 1.4088 12.9912Q0.7 12.2824 0.7 11.28V4.72Q0.7 3.7176 1.4088 3.0088Q2.1176 2.3 3.12 2.3ZM9.88 12.8H10.92V3.2L9.88 3.2Z", "fill": "currentColor"}));
});
