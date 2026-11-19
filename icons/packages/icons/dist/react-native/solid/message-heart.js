import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const MessageHeartIcon = /*#__PURE__*/ forwardRef(function MessageHeartIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M4 1.45H12Q13.2278 1.45 13.8889 2.1111Q14.55 2.7722 14.55 4V10Q14.55 11.2278 13.8889 11.8889Q13.2278 12.55 12 12.55H7.1298L3.6512 14.2893Q3.5781 14.3259 3.4992 14.3475Q3.4204 14.3691 3.3388 14.3749Q3.2573 14.3807 3.1762 14.3704Q3.0951 14.3602 3.0175 14.3344Q2.94 14.3085 2.869 14.268Q2.7979 14.2275 2.7362 14.174Q2.6744 14.1204 2.6243 14.0558Q2.5742 13.9913 2.5376 13.9181Q2.45 13.7429 2.45 13.547V12.4449Q2.0148 12.2594 1.7581 11.746Q1.45 11.1298 1.45 10V4Q1.45 2.7722 2.1111 2.1111Q2.7722 1.45 4 1.45ZM8 10 11 7.5C12.5 6 10 4 8 6C6 4 3.5 6 5 7.5Z", "fill": "currentColor"}));
});
