import { createElement, forwardRef } from "react";
export const FavoritesVector = /*#__PURE__*/ forwardRef(function FavoritesVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement("svg", {...{"viewBox": "0 0 480 360", "role": "img", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round", "xmlns": "http://www.w3.org/2000/svg"}, width: size, height: size * 360 / 480, color, ...props, ref},
    createElement("title", null, "Favorites"),
    createElement("desc", null, "A five-point favorite star has one clean silhouette and a shallow side wall."),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M233.19,70.65 269.81,155.56 370.34,186.94 M308.29,211.56 292.56,217.69 318.05,302.34 M95.80,113.95 196.17,135.98 204.07,121.86", "xmlns": "http://www.w3.org/2000/svg"}),
    createElement("path", {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M95.03,113.78 109.06,100.59 204.28,121.50 232.99,70.19 247.01,57.00 283.83,142.37 384.97,173.94 370.94,187.13 308.66,211.41 332.27,289.81 318.25,303.00 232.99,236.52 147.73,257.67 173.42,186.02 95.03,113.78", "xmlns": "http://www.w3.org/2000/svg"}));
});
