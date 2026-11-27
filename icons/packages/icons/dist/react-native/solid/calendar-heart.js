import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const CalendarHeartIcon = /*#__PURE__*/ forwardRef(function CalendarHeartIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M14.4 5.97V11.44Q14.4 12.4424 13.6912 13.1512Q12.9824 13.86 11.98 13.86H4.02Q3.0176 13.86 2.3088 13.1512Q1.6 12.4424 1.6 11.44L1.6 5.97H14.4ZM4.02 2.14 11.98 2.14Q12.9824 2.14 13.6912 2.8488Q14.4 3.5576 14.4 4.56V4.93H1.6V4.56Q1.6 3.5576 2.3088 2.8488Q3.0176 2.14 4.02 2.14ZM8 11.3957C8.3196 11.1217 10.1 9.8435 10.1 8.6109C10.1 6.9574 8.044 6.7913 8 8.1553C7.956 6.7913 5.9 6.9574 5.9 8.6109C5.9 9.8435 7.6804 11.1217 8 11.3957Z", "fill": "currentColor"}));
});
