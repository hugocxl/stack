import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const AspectRatioIcon = /*#__PURE__*/ forwardRef(function AspectRatioIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M11.1 13.4H2.75Q2.0044 13.4 1.4772 12.8728Q0.95 12.3456 0.95 11.6V6.8H10.85Q11.0222 6.8 11.0611 6.8389Q11.1 6.8778 11.1 7.05V13.4ZM2.75 2.6H13.25Q13.9956 2.6 14.5228 3.1272Q15.05 3.6544 15.05 4.4V11.6Q15.05 12.3456 14.5228 12.8728Q13.9956 13.4 13.25 13.4H12.2V7.05Q12.2 6.4222 11.8389 6.0611Q11.4778 5.7 10.85 5.7H0.95V4.4Q0.95 3.6544 1.4772 3.1272Q2.0044 2.6 2.75 2.6Z", "fill": "currentColor"}));
});
