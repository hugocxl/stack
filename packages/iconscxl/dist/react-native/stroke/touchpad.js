import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TouchpadIcon = /*#__PURE__*/ forwardRef(function TouchpadIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.2 1.875 12.8 1.875Q13.6388 1.875 14.2319 2.4681Q14.825 3.0612 14.825 3.9V12.1Q14.825 12.9388 14.2319 13.5319Q13.6388 14.125 12.8 14.125H3.2Q2.3612 14.125 1.7681 13.5319Q1.175 12.9388 1.175 12.1V3.9Q1.175 3.0612 1.7681 2.4681Q2.3612 1.875 3.2 1.875ZM3.2 3.125Q2.879 3.125 2.652 3.352Q2.425 3.579 2.425 3.9V9.45H13.575V3.9Q13.575 3.579 13.348 3.352Q13.121 3.125 12.8 3.125ZM2.425 10.55V12.1Q2.425 12.421 2.652 12.648Q2.879 12.875 3.2 12.875H7.45V10.55H2.425ZM8.55 12.875H12.8Q13.121 12.875 13.348 12.648Q13.575 12.421 13.575 12.1V10.55H8.55V12.875Z", "fill": "currentColor"}));
});
