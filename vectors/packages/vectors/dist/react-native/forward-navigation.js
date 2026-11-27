import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const ForwardNavigationVector = /*#__PURE__*/ forwardRef(function ForwardNavigationVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Forward navigation", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M270.58,113.75 381.63,212.75 M85.46,116.66 270.17,159.73 270.17,143.12"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M85.00,116.56 85.00,171.07 270.17,214.25 270.17,260.58 381.97,213.05 395.00,199.08 283.20,99.42 270.17,113.39 270.17,142.72 98.03,102.58 85.00,116.56"}));
});
