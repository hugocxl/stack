import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SpreadsheetIcon = /*#__PURE__*/ forwardRef(function SpreadsheetIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.12 2.1 12.88 2.1Q13.8824 2.1 14.5912 2.8088Q15.3 3.5176 15.3 4.52V11.48Q15.3 12.4824 14.5912 13.1912Q13.8824 13.9 12.88 13.9H3.12Q2.1176 13.9 1.4088 13.1912Q0.7 12.4824 0.7 11.48V4.52Q0.7 3.5176 1.4088 2.8088Q2.1176 2.1 3.12 2.1ZM1.6 9.28V10.32H7.48V13H8.52V10.32H14.4V9.28H8.52V6.72H14.4V5.68H8.52V3H7.48V5.68H1.6V6.72H7.48V9.28Z", "fill": "currentColor"}));
});
