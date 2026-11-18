import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const InviteSentVector = /*#__PURE__*/ forwardRef(function InviteSentVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Invite sent", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".43", "d": "M233.66,108.62 291.44,137.51 M226.02,127.35 298.70,163.69 M113.27,212.05 217.64,222.86 M288.45,299.65 247.45,237.77"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M191.55,140.86 198.49,138.78 M322.39,101.61 331.32,98.93 333.58,107.20 M351.48,172.67 366.73,228.45 304.32,285.18 M188.50,143.63 191.55,140.86 M241.49,89.80 334.67,136.39 M187.82,142.73 226.95,236.84 363.00,230.32 284.73,303.00 109.55,215.41 187.82,142.73"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M205.81,185.27 301.27,233.00 M326.78,231.77 370.45,125.95 232.55,57.00 192.66,153.64"}));
});
