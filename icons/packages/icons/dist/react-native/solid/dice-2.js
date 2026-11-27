import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const Dice2Icon = /*#__PURE__*/ forwardRef(function Dice2Icon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.82 2.1 12.18 2.1Q12.8924 2.1 13.3962 2.6038Q13.9 3.1076 13.9 3.82V12.18Q13.9 12.8924 13.3962 13.3962Q12.8924 13.9 12.18 13.9H3.82Q3.1076 13.9 2.6038 13.3962Q2.1 12.8924 2.1 12.18L2.1 3.82Q2.1 3.1076 2.6038 2.6038Q3.1076 2.1 3.82 2.1ZM9.85 5.25C9.85 5.7471 10.2529 6.15 10.75 6.15C11.2471 6.15 11.65 5.7471 11.65 5.25C11.65 4.7529 11.2471 4.35 10.75 4.35C10.2529 4.35 9.85 4.7529 9.85 5.25ZM4.35 10.75C4.35 11.2471 4.7529 11.65 5.25 11.65C5.7471 11.65 6.15 11.2471 6.15 10.75C6.15 10.2529 5.7471 9.85 5.25 9.85C4.7529 9.85 4.35 10.2529 4.35 10.75Z", "fill": "currentColor"}));
});
