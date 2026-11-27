import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const DotIcon = /*#__PURE__*/ forwardRef(function DotIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.65 8C3.65 5.5976 5.5976 3.65 8 3.65C10.4024 3.65 12.35 5.5976 12.35 8C12.35 10.4024 10.4024 12.35 8 12.35C5.5976 12.35 3.65 10.4024 3.65 8Z", "fill": "currentColor"}));
});
