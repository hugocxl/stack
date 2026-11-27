import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const CircleStarIcon = /*#__PURE__*/ forwardRef(function CircleStarIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.48 8Q1.48 6.6739 1.9926 5.462Q2.4875 4.2918 3.3897 3.3897Q4.2918 2.4875 5.462 1.9926Q6.6739 1.48 8 1.48Q9.3261 1.48 10.538 1.9926Q11.7082 2.4875 12.6103 3.3897Q13.5125 4.2918 14.0074 5.462Q14.52 6.6739 14.52 8Q14.52 9.3261 14.0074 10.538Q13.5125 11.7082 12.6103 12.6103Q11.7082 13.5125 10.538 14.0074Q9.3261 14.52 8 14.52Q6.6739 14.52 5.462 14.0074Q4.2918 13.5125 3.3897 12.6103Q2.4875 11.7082 1.9926 10.538Q1.48 9.3261 1.48 8ZM8 4.36 6.88 6.712 4.36 7.048 6.208 8.84 5.76 11.36 8 10.128 10.24 11.36 9.792 8.84 11.64 7.048 9.12 6.712Z", "fill": "currentColor"}));
});
