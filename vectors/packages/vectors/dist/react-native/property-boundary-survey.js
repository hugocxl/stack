import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const PropertyBoundarySurveyVector = /*#__PURE__*/ forwardRef(function PropertyBoundarySurveyVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Property boundary survey", ...props, ref},
    createElement(Path, {"strokeOpacity": ".55", "d": "M230.03,109.75 211.90,135.13 133.95,174.11 M246.35,112.47 226.40,138.76 141.20,181.36 M266.29,162.32 297.11,177.73 278.98,186.80 289.85,192.24 273.54,200.39 231.84,179.55 266.29,162.32"}),
    createElement(Path, {"strokeOpacity": ".9", "d": "M201.02,98.87 85.00,156.89 85.00,169.58 215.53,245.72 286.23,261.13 376.87,215.80 395.00,190.42 395.00,177.73 266.29,113.38 201.02,98.87 M201.02,98.87 266.29,113.38 395.00,177.73 376.87,203.11 286.23,248.44 215.53,233.03 85.00,156.89 201.02,98.87 M249.97,130.60 268.10,139.66 M268.10,130.60 249.97,139.66 M342.43,173.20 360.56,182.27 M360.56,173.20 342.43,182.27 M275.35,221.24 293.48,230.31 M293.48,221.24 275.35,230.31 M161.14,176.83 179.27,185.89 M179.27,176.83 161.14,185.89"}),
    createElement(Path, {"strokeOpacity": "1", "d": "M259.04,135.13 351.49,177.73 284.42,225.77 170.20,181.36 259.04,135.13"}));
});
