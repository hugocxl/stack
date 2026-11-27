import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const MouseIcon = /*#__PURE__*/ forwardRef(function MouseIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M8 1Q8.9152 1 9.7518 1.3538Q10.5594 1.6955 11.182 2.318Q11.8045 2.9406 12.1462 3.7482Q12.5 4.5848 12.5 5.5V10.5Q12.5 11.4152 12.1462 12.2518Q11.8045 13.0594 11.182 13.682Q10.5594 14.3045 9.7518 14.6462Q8.9152 15 8 15Q7.0848 15 6.2482 14.6462Q5.4406 14.3045 4.818 13.682Q4.1955 13.0594 3.8538 12.2518Q3.5 11.4152 3.5 10.5V5.5Q3.5 4.5848 3.8538 3.7482Q4.1955 2.9406 4.818 2.318Q5.4406 1.6955 6.2482 1.3538Q7.0848 1 8 1ZM8 1.9Q7.7358 1.9 7.48 1.9368V5.83H4.4V6.87H11.6V5.83H8.52V1.9368Q8.2642 1.9 8 1.9Z", "fill": "currentColor"}));
});
