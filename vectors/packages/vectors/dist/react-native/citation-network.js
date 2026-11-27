import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const CitationNetworkVector = /*#__PURE__*/ forwardRef(function CitationNetworkVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Citation network", ...props, ref},
    createElement(Path, {"strokeOpacity": ".55", "d": "M144.22,127.85 144.22,149.75 166.12,149.75 M99.49,199.56 137.15,199.56 M373.10,67.01 373.10,88.91 395.00,88.91 M328.36,138.71 366.03,138.71 M373.10,197.38 373.10,219.29 395.00,219.29 M328.36,269.09 366.03,269.09"}),
    createElement(Path, {"strokeOpacity": ".9", "d": "M166.47,177.10 221.17,177.10 270.42,240.84 308.08,240.84 M288.42,250.67 308.08,240.84 288.42,231.01 M85.00,223.46 166.12,223.46 166.12,149.75 144.22,127.85 85.00,127.85 85.00,223.46 M313.88,162.62 395.00,162.62 395.00,88.91 373.10,67.01 313.88,67.01 313.88,162.62 M328.36,114.81 377.62,114.81 M313.88,292.99 395.00,292.99 395.00,219.29 373.10,197.38 313.88,197.38 313.88,292.99 M328.36,245.19 377.62,245.19"}),
    createElement(Path, {"strokeOpacity": "1", "d": "M166.47,177.10 221.17,177.10 270.42,110.47 308.08,110.47 M288.42,120.30 308.08,110.47 288.42,100.63 M99.49,175.65 148.74,175.65"}));
});
