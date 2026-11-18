import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const LayersIcon = /*#__PURE__*/ forwardRef(function LayersIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.55 5.5 8 1.95 14.45 5.5 8 9.05ZM1.55 9.35 8 12.9 14.45 9.35V11.15L8 14.7L1.55 11.15Z", "fill": "currentColor"}));
});
