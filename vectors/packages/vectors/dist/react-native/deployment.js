import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const DeploymentVector = /*#__PURE__*/ forwardRef(function DeploymentVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Deployment", ...props, ref},
    createElement(Path, {"strokeOpacity": ".55", "d": "M277.67,128.80 178.79,178.23 178.79,192.36 M301.21,140.57 202.33,190.00 202.33,204.13"}),
    createElement(Path, {"strokeOpacity": ".9", "d": "M221.17,100.55 357.31,168.62 M122.69,149.79 221.17,100.55 M357.70,253.56 259.18,302.82 M259.14,218.10 357.70,168.82 357.70,253.56 M122.30,234.73 258.83,303.00 258.83,218.25 122.30,149.99 122.30,234.73 M159.96,201.78 138.78,207.66 159.96,234.73 M181.15,247.68 199.98,219.43 M221.17,232.38 242.35,259.45 221.17,265.33"}),
    createElement(Path, {"strokeOpacity": "1", "d": "M270.60,174.70 270.60,57.00 M296.97,96.55 270.60,57.00 244.24,70.18"}));
});
