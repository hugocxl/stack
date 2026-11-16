import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const StrokeLineJoinMiterIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinMiterIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M0.8 13.2 8 1.4 15.2 13.2 12.6 14.6 8 6.9 3.4 14.6Z", "fill": "currentColor"}));
});
