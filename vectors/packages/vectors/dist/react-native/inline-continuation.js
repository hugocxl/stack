import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const InlineContinuationVector = /*#__PURE__*/ forwardRef(function InlineContinuationVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Inline continuation", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M156.83,156.89 319.08,184.47 M243.20,213.56 260.98,216.58 M272.09,218.47 287.65,221.12 M298.76,223.01 320.99,226.78 M371.40,101.97 358.33,134.33 389.44,139.62"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M140.96,196.18 212.08,208.27 M171.77,119.90 276.23,137.66 M296.50,150.99 308.26,158.91 305.39,177.20 316.70,160.35 332.95,157.18 321.18,149.26 324.06,130.97 312.74,147.82 296.50,150.99 M85.00,258.30 162.48,66.45 168.03,60.89 376.95,96.41 395.00,134.06 330.59,293.55 325.03,299.11 85.00,258.30 M85.00,258.30 162.48,66.45 371.40,101.97 389.44,139.62 325.03,299.11 85.00,258.30"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M216.09,233.65 234.75,187.42"}));
});
