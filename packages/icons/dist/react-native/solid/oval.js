import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const OvalIcon = /*#__PURE__*/ forwardRef(function OvalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M0.9 8Q0.9 6.9025 1.4922 5.9085Q2.0488 4.9743 3.0501 4.2635Q4.0303 3.5676 5.2923 3.1887Q6.5866 2.8 8 2.8Q9.4134 2.8 10.7077 3.1887Q11.9697 3.5676 12.9499 4.2635Q13.9512 4.9743 14.5078 5.9085Q15.1 6.9025 15.1 8Q15.1 9.0975 14.5078 10.0915Q13.9512 11.0257 12.9499 11.7365Q11.9697 12.4324 10.7077 12.8113Q9.4134 13.2 8 13.2Q6.5866 13.2 5.2923 12.8113Q4.0303 12.4324 3.0501 11.7365Q2.0488 11.0257 1.4922 10.0915Q0.9 9.0975 0.9 8Z", "fill": "currentColor"}));
});
