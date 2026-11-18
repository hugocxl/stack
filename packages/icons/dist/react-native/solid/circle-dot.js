import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const CircleDotIcon = /*#__PURE__*/ forwardRef(function CircleDotIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.45 8Q1.45 6.6678 1.965 5.4503Q2.4622 4.2747 3.3685 3.3684Q4.2747 2.4622 5.4503 1.965Q6.6678 1.45 8 1.45Q9.3322 1.45 10.5497 1.965Q11.7253 2.4622 12.6315 3.3685Q13.5378 4.2747 14.035 5.4503Q14.55 6.6678 14.55 8Q14.55 9.3322 14.035 10.5497Q13.5378 11.7253 12.6315 12.6315Q11.7253 13.5378 10.5497 14.035Q9.3322 14.55 8 14.55Q6.6678 14.55 5.4503 14.035Q4.2747 13.5378 3.3685 12.6315Q2.4622 11.7253 1.965 10.5497Q1.45 9.3322 1.45 8ZM6.5 8C6.5 8.8284 7.1716 9.5 8 9.5C8.8284 9.5 9.5 8.8284 9.5 8C9.5 7.1716 8.8284 6.5 8 6.5C7.1716 6.5 6.5 7.1716 6.5 8Z", "fill": "currentColor"}));
});
