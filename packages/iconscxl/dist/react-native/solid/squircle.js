import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquircleIcon = /*#__PURE__*/ forwardRef(function SquircleIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M8 1.075Q10.4222 1.075 11.5296 1.2515Q13.0236 1.4897 13.7669 2.2331Q14.5103 2.9764 14.7485 4.4704Q14.925 5.5778 14.925 8Q14.925 10.4222 14.7485 11.5296Q14.5103 13.0236 13.7669 13.7669Q13.0236 14.5103 11.5296 14.7485Q10.4222 14.925 8 14.925Q5.5778 14.925 4.4704 14.7485Q2.9764 14.5103 2.2331 13.7669Q1.4897 13.0236 1.2515 11.5296Q1.075 10.4222 1.075 8Q1.075 5.5778 1.2515 4.4704Q1.4897 2.9764 2.2331 2.2331Q2.9764 1.4897 4.4704 1.2515Q5.5778 1.075 8 1.075Z", "fill": "currentColor"}));
});
