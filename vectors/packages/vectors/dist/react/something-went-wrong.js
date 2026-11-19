import { createElement, forwardRef } from "react";
export const SomethingWentWrongVector = /*#__PURE__*/ forwardRef(function SomethingWentWrongVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Something went wrong"),
    createElement("desc", null, "A single upright warning triangle surrounds a large exclamation mark."),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M242.89,57.00 237.11,59.89 128.58,194.47 345.64,303.00 351.42,300.11 242.89,57.00 M128.58,194.47 345.64,303.00 237.11,59.89 128.58,194.47", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M237.08,112.78 237.08,180.76 M237.08,210.98 237.08,218.53", "xmlns": "http://www.w3.org/2000/svg"}));
});
