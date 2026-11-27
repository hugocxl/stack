import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquareSplitHorizontalIcon = /*#__PURE__*/ forwardRef(function SquareSplitHorizontalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.82 2.1 12.18 2.1Q12.8924 2.1 13.3962 2.6038Q13.9 3.1076 13.9 3.82V12.18Q13.9 12.8924 13.3962 13.3962Q12.8924 13.9 12.18 13.9H3.82Q3.1076 13.9 2.6038 13.3962Q2.1 12.8924 2.1 12.18L2.1 3.82Q2.1 3.1076 2.6038 2.6038Q3.1076 2.1 3.82 2.1ZM3 8.52H13V7.48H3Z", "fill": "currentColor"}));
});
