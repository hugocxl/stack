import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const StrokeLineJoinBevelIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinBevelIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.26 12.03 6.77 4.24H9.23L13.74 12.03L11.69 13.26L8 6.946L4.31 13.26Z", "fill": "currentColor"}));
});
