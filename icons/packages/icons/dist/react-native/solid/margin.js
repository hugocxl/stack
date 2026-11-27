import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const MarginIcon = /*#__PURE__*/ forwardRef(function MarginIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.82 2.1 12.18 2.1Q12.8924 2.1 13.3962 2.6038Q13.9 3.1076 13.9 3.82V12.18Q13.9 12.8924 13.3962 13.3962Q12.8924 13.9 12.18 13.9H3.82Q3.1076 13.9 2.6038 13.3962Q2.1 12.8924 2.1 12.18L2.1 3.82Q2.1 3.1076 2.6038 2.6038Q3.1076 2.1 3.82 2.1ZM6.35 5.75C6.0186 5.75 5.75 6.0186 5.75 6.35V9.65C5.75 9.9814 6.0186 10.25 6.35 10.25H9.65C9.9814 10.25 10.25 9.9814 10.25 9.65V6.35C10.25 6.0186 9.9814 5.75 9.65 5.75Z", "fill": "currentColor"}));
});
