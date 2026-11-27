import { createElement, forwardRef } from "react";
export const AdjustableReadingSpacingVector = /*#__PURE__*/ forwardRef(function AdjustableReadingSpacingVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Adjustable reading spacing"),
    createElement("desc", null, "A double-headed vertical arrow spans the gap between text lines on a reading folio."),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M128.11,228.49 200.40,57.00 323.05,118.33 336.47,159.20 276.08,302.47 128.11,228.49 M156.85,221.83 209.41,248.12 M176.98,174.08 241.23,206.20 M197.11,126.32 263.30,159.42 M201.24,57.03 215.82,57.53 338.47,118.85 351.89,159.73 291.50,303.00 276.45,302.49 M208.09,100.27 264.55,128.50 M258.65,180.80 285.63,180.80 M258.65,241.49 285.63,241.49 M323.05,118.33 311.16,146.55 336.47,159.20", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M262.03,197.66 272.14,187.54 282.26,197.66 M262.03,224.63 272.14,234.75 282.26,224.63 M272.14,187.54 272.14,234.75", "xmlns": "http://www.w3.org/2000/svg"}));
});
