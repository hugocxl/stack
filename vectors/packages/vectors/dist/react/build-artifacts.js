import { createElement, forwardRef } from "react";
export const BuildArtifactsVector = /*#__PURE__*/ forwardRef(function BuildArtifactsVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Build artifacts"),
    createElement("desc", null, "A downward download arrow marks the front of a sealed release package."),
    createElement("path", {"strokeOpacity": ".55", "d": "M285.77,91.33 165.63,151.40 165.63,168.56 M314.37,105.63 194.23,165.70 194.23,182.86", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"strokeOpacity": ".9", "d": "M217.12,57.00 382.63,139.76 M97.37,116.87 217.12,57.00 M383.02,242.93 263.23,302.83 M263.20,199.87 383.02,139.95 383.02,242.93 M96.98,220.05 262.88,303.00 262.88,200.02 96.98,117.07 96.98,220.05", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"strokeOpacity": "1", "d": "M179.90,181.44 179.90,250.10 M159.31,219.20 179.90,250.10 200.50,239.80", "xmlns": "http://www.w3.org/2000/svg"}));
});
