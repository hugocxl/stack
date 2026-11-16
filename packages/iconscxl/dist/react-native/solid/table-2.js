import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const Table2Icon = /*#__PURE__*/ forwardRef(function Table2Icon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3 1.375H13Q13.6731 1.375 14.149 1.851Q14.625 2.3269 14.625 3V13Q14.625 13.6731 14.149 14.149Q13.6731 14.625 13 14.625H3Q2.3269 14.625 1.851 14.149Q1.375 13.6731 1.375 13V3Q1.375 2.3269 1.851 1.851Q2.3269 1.375 3 1.375ZM2.275 6.55H5.45V9.45H2.275V10.55H5.45V13.725H6.55V10.55H13.725V9.45H6.55V6.55H13.725V5.45H2.275Z", "fill": "currentColor"}));
});
