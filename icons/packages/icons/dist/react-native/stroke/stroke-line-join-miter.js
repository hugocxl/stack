import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const StrokeLineJoinMiterIcon = /*#__PURE__*/ forwardRef(function StrokeLineJoinMiterIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.096 12.276 8 2.6 13.904 12.276 11.772 13.424 8 7.11 4.228 13.424Z", "fill": "currentColor"}));
});
