import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const SomethingWentWrongVector = /*#__PURE__*/ forwardRef(function SomethingWentWrongVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Something went wrong", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M242.89,57.00 237.11,59.89 128.58,194.47 345.64,303.00 351.42,300.11 242.89,57.00 M128.58,194.47 345.64,303.00 237.11,59.89 128.58,194.47"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M237.08,112.78 237.08,180.76 M237.08,210.98 237.08,218.53"}));
});
