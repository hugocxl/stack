import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const InviteSentVector = /*#__PURE__*/ forwardRef(function InviteSentVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Invite sent", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".43", "d": "M209.63,108.62 267.40,137.51 M201.99,127.35 274.67,163.69 M89.24,212.05 193.60,222.86 M264.42,299.65 223.42,237.77"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M167.51,140.86 174.46,138.78 M298.35,101.61 307.28,98.93 309.54,107.20 M327.44,172.67 342.69,228.45 280.29,285.18 M164.46,143.63 167.51,140.86 M217.45,89.80 310.64,136.39 M163.78,142.73 202.92,236.84 338.96,230.32 260.69,303.00 85.51,215.41 163.78,142.73 M327.78,122.23 394.49,122.23 M360.23,132.51 394.49,122.23 360.23,111.95"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M181.78,185.27 277.23,233.00 M302.75,231.77 346.42,125.95 208.51,57.00 168.62,153.64"}));
});
