import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TouchpadIcon = /*#__PURE__*/ forwardRef(function TouchpadIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3 1.98 13 1.98Q13.7124 1.98 14.2162 2.4838Q14.72 2.9876 14.72 3.7V12.3Q14.72 13.0124 14.2162 13.5162Q13.7124 14.02 13 14.02H3Q2.2876 14.02 1.7838 13.5162Q1.28 13.0124 1.28 12.3V3.7Q1.28 2.9876 1.7838 2.4838Q2.2876 1.98 3 1.98ZM2.18 10.52H7.48V13Q7.48 13.0512 7.49 13.1014Q7.4918 13.1108 7.494 13.12H8.506Q8.5082 13.1108 8.51 13.1014Q8.52 13.0512 8.52 13V10.52H13.82V9.48H2.18Z", "fill": "currentColor"}));
});
