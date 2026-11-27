import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquircleIcon = /*#__PURE__*/ forwardRef(function SquircleIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M5.22 2.1H10.78Q12.0723 2.1 12.9862 3.0138Q13.9 3.9277 13.9 5.22V10.78Q13.9 12.0723 12.9862 12.9862Q12.0723 13.9 10.78 13.9H5.22Q3.9277 13.9 3.0138 12.9862Q2.1 12.0723 2.1 10.78V5.22Q2.1 3.9277 3.0138 3.0138Q3.9277 2.1 5.22 2.1Z", "fill": "currentColor"}));
});
