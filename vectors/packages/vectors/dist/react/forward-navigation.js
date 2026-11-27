import { createElement, forwardRef } from "react";
export const ForwardNavigationVector = /*#__PURE__*/ forwardRef(function ForwardNavigationVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Forward navigation"),
    createElement("desc", null, "A broad right-pointing navigation arrow has a clean head and shallow isometric depth."),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M381.63,212.75 270.58,113.75 M270.17,143.12 270.17,159.73 85.46,116.66", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M85.00,116.56 85.00,171.07 270.17,214.25 270.17,260.58 381.97,213.05 395.00,199.08 283.20,99.42 270.17,113.39 270.17,142.72 98.03,102.58 85.00,116.56", "xmlns": "http://www.w3.org/2000/svg"}));
});
