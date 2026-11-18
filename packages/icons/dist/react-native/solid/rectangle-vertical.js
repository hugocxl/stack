import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const RectangleVerticalIcon = /*#__PURE__*/ forwardRef(function RectangleVerticalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M5.25 1.25H10.75Q11.4956 1.25 12.0228 1.7772Q12.55 2.3044 12.55 3.05V12.95Q12.55 13.6956 12.0228 14.2228Q11.4956 14.75 10.75 14.75H5.25Q4.5044 14.75 3.9772 14.2228Q3.45 13.6956 3.45 12.95V3.05Q3.45 2.3044 3.9772 1.7772Q4.5044 1.25 5.25 1.25Z", "fill": "currentColor"}));
});
