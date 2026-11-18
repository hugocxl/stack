import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquaresUniteIcon = /*#__PURE__*/ forwardRef(function SquaresUniteIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.7 1.15H8.9Q9.542 1.15 9.996 1.604Q10.45 2.058 10.45 2.7V5.55H13.3Q13.942 5.55 14.396 6.004Q14.85 6.458 14.85 7.1V13.3Q14.85 13.942 14.396 14.396Q13.942 14.85 13.3 14.85H7.1Q6.458 14.85 6.004 14.396Q5.55 13.942 5.55 13.3V10.45H2.7Q2.058 10.45 1.604 9.996Q1.15 9.542 1.15 8.9V2.7Q1.15 2.058 1.604 1.604Q2.058 1.15 2.7 1.15Z", "fill": "currentColor"}));
});
