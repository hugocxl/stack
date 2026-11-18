import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquareStopIcon = /*#__PURE__*/ forwardRef(function SquareStopIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M4 1.375H12Q13.0873 1.375 13.8562 2.1438Q14.625 2.9127 14.625 4V12Q14.625 13.0873 13.8562 13.8562Q13.0873 14.625 12 14.625H4Q2.9127 14.625 2.1438 13.8562Q1.375 13.0873 1.375 12V4Q1.375 2.9127 2.1438 2.1438Q2.9127 1.375 4 1.375ZM5.6 5C5.2686 5 5 5.2686 5 5.6V10.4C5 10.7314 5.2686 11 5.6 11H10.4C10.7314 11 11 10.7314 11 10.4V5.6C11 5.2686 10.7314 5 10.4 5Z", "fill": "currentColor"}));
});
