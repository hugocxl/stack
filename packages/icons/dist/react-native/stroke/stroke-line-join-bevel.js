import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const StrokeLineJoinBevelIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinBevelIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1 12 6.5 2.5H9.5L15 12L12.5 13.5L8 5.8L3.5 13.5Z", "fill": "currentColor"}));
});
