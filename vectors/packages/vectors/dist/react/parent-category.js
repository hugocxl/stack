import { createElement, forwardRef } from "react";
export const ParentCategoryVector = /*#__PURE__*/ forwardRef(function ParentCategoryVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Parent category"),
    createElement("desc", null, "Two folder levels form a short category path, with an upward arrow pointing back to the parent folder."),
    createElement("path", {"strokeOpacity": ".55", "d": "M105.75,134.68 256.96,171.55 M105.39,90.36 257.33,127.42 M236.36,258.80 374.25,292.43 M236.00,216.88 374.61,250.68", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"strokeOpacity": ".9", "d": "M180.03,163.64 180.03,203.12 235.65,216.69 M105.39,67.49 105.39,134.59 105.39,145.08 257.33,182.13 257.33,171.64 257.33,121.61 257.33,111.12 181.36,92.60 164.65,71.45 105.39,57.00 105.39,67.49 M236.00,195.80 236.00,258.71 236.00,269.20 374.61,303.00 374.61,292.51 374.61,245.75 374.61,235.27 305.31,218.36 290.06,198.50 236.00,185.32 236.00,195.80", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"strokeOpacity": "1", "d": "M310.64,211.91 310.64,140.61 262.66,128.90 M288.04,124.54 262.66,128.90 271.40,141.59", "xmlns": "http://www.w3.org/2000/svg"}));
});
