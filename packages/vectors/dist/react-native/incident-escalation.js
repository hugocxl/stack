import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const IncidentEscalationVector = /*#__PURE__*/ forwardRef(function IncidentEscalationVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Incident escalation", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M227.17,57.00 217.24,61.97 109.63,195.40 324.84,303.00 334.77,298.03 227.17,57.00 M109.63,195.40 324.84,303.00 217.24,61.97 109.63,195.40 M345.53,292.65 345.53,110.55 M370.37,164.36 345.53,110.55 320.70,139.52"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M217.20,114.41 217.20,181.82 M217.20,211.77 217.20,219.26"}));
});
