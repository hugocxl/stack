import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquareStarIcon = /*#__PURE__*/ forwardRef(function SquareStarIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M4 1.375H12Q13.0873 1.375 13.8562 2.1438Q14.625 2.9127 14.625 4V12Q14.625 13.0873 13.8562 13.8562Q13.0873 14.625 12 14.625H4Q2.9127 14.625 2.1438 13.8562Q1.375 13.0873 1.375 12V4Q1.375 2.9127 2.1438 2.1438Q2.9127 1.375 4 1.375ZM8 4.75 7 6.85 4.75 7.15 6.4 8.75 6 11 8 9.9 10 11 9.6 8.75 11.25 7.15 9 6.85Z", "fill": "currentColor"}));
});
