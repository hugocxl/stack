import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const ToolOutputHandoffVector = /*#__PURE__*/ forwardRef(function ToolOutputHandoffVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Tool output handoff", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M281.68,94.17 275.20,128.24 306.04,137.18"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M180.95,57.00 174.78,63.17 136.80,263.06 274.52,303.00 280.69,296.83 312.20,131.01 287.85,88.00 180.95,57.00 M136.80,263.06 274.52,303.00 306.04,137.18 281.68,94.17 174.78,63.17 136.80,263.06 M188.76,115.15 248.38,132.44 M183.15,144.68 271.54,170.32 M177.97,171.94 256.09,194.60 M172.79,199.20 230.35,215.89"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M223.98,238.01 343.20,238.01 M315.30,251.96 343.20,238.01 315.30,224.06"}));
});
