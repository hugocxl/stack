import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const ParentCategoryVector = /*#__PURE__*/ forwardRef(function ParentCategoryVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Parent category", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M105.75,134.68 256.96,171.55 M105.39,90.36 257.33,127.42 M236.36,258.80 374.25,292.43 M236.00,216.88 374.61,250.68"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M180.03,163.64 180.03,203.12 235.65,216.69 M105.39,67.49 105.39,134.59 105.39,145.08 257.33,182.13 257.33,171.64 257.33,121.61 257.33,111.12 181.36,92.60 164.65,71.45 105.39,57.00 105.39,67.49 M236.00,195.80 236.00,258.71 236.00,269.20 374.61,303.00 374.61,292.51 374.61,245.75 374.61,235.27 305.31,218.36 290.06,198.50 236.00,185.32 236.00,195.80"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M310.64,211.91 310.64,140.61 262.66,128.90 M288.04,124.54 262.66,128.90 271.40,141.59"}));
});
