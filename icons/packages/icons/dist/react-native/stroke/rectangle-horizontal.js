import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const RectangleHorizontalIcon = /*#__PURE__*/ forwardRef(function RectangleHorizontalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.37 2.3H13.63Q14.3424 2.3 14.8462 2.8038Q15.35 3.3076 15.35 4.02V11.98Q15.35 12.6924 14.8462 13.1962Q14.3424 13.7 13.63 13.7H2.37Q1.6576 13.7 1.1538 13.1962Q0.65 12.6924 0.65 11.98L0.65 4.02Q0.65 3.3076 1.1538 2.8038Q1.6576 2.3 2.37 2.3ZM2.37 3.34Q2.0883 3.34 1.8892 3.5392Q1.69 3.7383 1.69 4.02L1.69 11.98Q1.69 12.2617 1.8892 12.4608Q2.0883 12.66 2.37 12.66H13.63Q13.9117 12.66 14.1108 12.4608Q14.31 12.2617 14.31 11.98V4.02Q14.31 3.7383 14.1108 3.5392Q13.9117 3.34 13.63 3.34Z", "fill": "currentColor"}));
});
