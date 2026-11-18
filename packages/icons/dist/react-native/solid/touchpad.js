import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TouchpadIcon = /*#__PURE__*/ forwardRef(function TouchpadIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.2 1.875 12.8 1.875Q13.6388 1.875 14.2319 2.4681Q14.825 3.0612 14.825 3.9V12.1Q14.825 12.9388 14.2319 13.5319Q13.6388 14.125 12.8 14.125H3.2Q2.3612 14.125 1.7681 13.5319Q1.175 12.9388 1.175 12.1V3.9Q1.175 3.0612 1.7681 2.4681Q2.3612 1.875 3.2 1.875ZM2.075 10.55H7.45V13Q7.45 13.0542 7.4606 13.1073Q7.4711 13.1604 7.4919 13.2105Q7.4949 13.2178 7.4981 13.225H8.5019Q8.5051 13.2178 8.5081 13.2105Q8.5289 13.1604 8.5394 13.1073Q8.55 13.0542 8.55 13V10.55H13.925V9.45H2.075Z", "fill": "currentColor"}));
});
