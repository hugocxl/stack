import { createElement, forwardRef } from "react";
export const DeploymentVector = /*#__PURE__*/ forwardRef(function DeploymentVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Deployment"),
    createElement("desc", null, "An upward arrow launches from the top of a sealed software carton."),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".43", "d": "M277.67,128.80 178.79,178.23 178.79,192.36 M301.21,140.57 202.33,190.00 202.33,204.13", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".76", "d": "M221.17,100.55 357.31,168.62 M122.69,149.79 221.17,100.55 M357.70,253.56 259.19,302.82 M259.15,218.10 357.70,168.82 357.70,253.56 M122.30,234.73 258.83,303.00 258.83,218.25 122.30,149.99 122.30,234.73 M159.96,201.78 138.78,207.66 159.96,234.73 M181.15,247.68 199.98,219.43 M221.17,232.38 242.35,259.45 221.17,265.33", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M270.60,174.70 270.60,57.00 M290.38,99.84 270.60,57.00 250.83,80.07", "xmlns": "http://www.w3.org/2000/svg"}));
});
