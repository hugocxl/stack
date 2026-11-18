import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const StrokeLineJoinRoundIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinRoundIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.55 12.35 6.35 3.15C6.6702 2.5346 7.3063 2.1485 8 2.1485C8.6937 2.1485 9.3298 2.5346 9.65 3.15L14.45 12.35L11.65 13.8L8 6.8L4.35 13.8Z", "fill": "currentColor"}));
});
