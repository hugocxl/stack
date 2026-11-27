import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const TestimonialsVector = /*#__PURE__*/ forwardRef(function TestimonialsVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Testimonials", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M220.13,110.45 313.53,157.15 M220.13,130.32 341.35,190.93 M220.13,150.19 287.69,183.97 M108.85,130.32 202.24,177.02 M108.85,150.19 230.06,210.80 M108.85,170.06 176.41,203.85"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M284.35,196.21 383.08,245.58 395.00,239.62 395.00,183.97 383.08,166.09 208.21,78.65 196.28,84.62 196.28,140.26 205.10,152.22"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M98.91,190.93 122.76,202.85 120.77,223.72 150.58,216.76 279.74,281.35 291.67,275.38 291.67,207.82 279.74,189.94 96.92,98.53 85.00,104.49 85.00,172.05 98.91,190.93"}));
});
