import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const FileDownloadReadyVector = /*#__PURE__*/ forwardRef(function FileDownloadReadyVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "File download ready", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".55", "d": "M187.24,179.01 244.36,207.57 M199.23,151.60 265.87,184.91 M211.23,124.18 261.20,149.17"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M211.13,64.73 139.17,229.23 253.40,286.34 M211.13,64.73 214.70,62.95 302.76,106.98 314.27,153.57 256.97,284.56 253.40,286.34 M211.13,64.73 298.87,108.60 M218.66,64.54 220.65,59.97 M220.65,59.97 226.60,57.00 340.83,114.12 268.87,278.61 262.92,281.58 M220.65,59.97 334.88,117.09 262.92,281.58 M253.40,286.34 310.56,155.68 M259.42,279.83 262.92,281.58 M284.53,142.27 299.19,108.76 310.70,155.36 284.53,142.27"}),
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": "1", "d": "M184.86,278.73 201.04,303.00 217.23,294.91 M201.04,243.50 201.04,303.00"}));
});
