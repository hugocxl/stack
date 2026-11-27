import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const InviteSentVector = /*#__PURE__*/ forwardRef(function InviteSentVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Invite sent", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M209.63,108.62 267.40,137.51 M201.99,127.35 274.67,163.69 M89.24,212.05 193.60,222.86 M264.42,299.65 223.42,237.77"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M167.51,140.86 174.37,138.81 M298.45,101.58 307.28,98.93 309.52,107.11 M327.47,172.78 342.69,228.45 285.21,280.71 M164.52,143.58 167.51,140.86 M217.45,89.80 310.64,136.39 M163.78,142.73 202.92,236.84 338.96,230.32 260.69,303.00 85.51,215.41 163.78,142.73 M327.78,122.23 394.49,122.23 M367.08,135.93 394.49,122.23 367.08,108.52"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M181.87,185.32 277.10,232.93 M302.78,231.70 346.42,125.95 208.51,57.00 168.66,153.55"}));
});
