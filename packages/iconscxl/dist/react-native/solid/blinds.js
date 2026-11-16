import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const BlindsIcon = /*#__PURE__*/ forwardRef(function BlindsIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3 1.375H13Q13.6731 1.375 14.149 1.851Q14.625 2.3269 14.625 3V11Q14.625 11.6731 14.149 12.149Q13.6731 12.625 13 12.625H3Q2.3269 12.625 1.851 12.149Q1.375 11.6731 1.375 11V3Q1.375 2.3269 1.851 1.851Q2.3269 1.375 3 1.375ZM2.275 7.45V8.55H10.45V11.725H11.55V8.55H13.725V7.45H11.55V5.55H13.725V4.45H11.55V2.275H10.45V4.45H2.275V5.55H10.45V7.45Z", "fill": "currentColor"}));
});
