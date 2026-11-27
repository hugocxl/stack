import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const DamagedDeliveryVector = /*#__PURE__*/ forwardRef(function DamagedDeliveryVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Damaged delivery", ...props, ref},
    createElement(Path, {"strokeOpacity": ".55", "d": "M193.01,156.51 253.82,181.38 314.63,156.51 M267.64,213.17 281.46,222.84 292.52,214.55 M270.40,79.11 154.31,137.16 154.31,159.27 M289.75,88.79 173.66,146.83 173.66,168.94"}),
    createElement(Path, {"strokeOpacity": ".9", "d": "M226.18,57.00 369.52,128.67 M314.13,156.51 193.42,156.51 M110.48,114.85 226.18,57.00 M110.09,115.04 193.01,156.51 206.83,180.00 217.89,182.76 231.71,211.79 253.59,244.61 M253.47,302.82 110.09,231.13 110.09,115.04 M369.91,128.87 314.63,156.51 292.52,178.62 281.46,181.38 267.64,213.17 253.82,244.96 253.82,303.00 369.91,244.96 369.91,128.87"}),
    createElement(Path, {"strokeOpacity": "1", "d": "M231.71,211.79 217.89,213.17 206.83,202.11 195.78,218.70"}));
});
