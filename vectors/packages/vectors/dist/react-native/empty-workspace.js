import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const EmptyWorkspaceVector = /*#__PURE__*/ forwardRef(function EmptyWorkspaceVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "1.05", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Empty workspace", ...props, ref},
    createElement(Path, {"vectorEffect": "non-scaling-stroke", "strokeOpacity": ".9", "d": "M107.78,121.52 113.27,116.39 304.30,211.90 352.06,297.87 346.57,303.00 155.54,207.49 107.78,121.52 M107.78,121.52 155.54,207.49 346.57,303.00 298.81,217.04 107.78,121.52 M350.71,299.61 350.55,301.01 349.68,300.57 350.55,301.01 356.46,298.77 372.22,160.87 252.82,101.18 242.56,80.58 200.77,59.69 194.86,61.92 193.41,62.63 182.14,57.00 176.23,59.24 166.69,142.71 176.23,59.24 188.17,65.21 194.86,61.92 236.65,82.82 246.91,103.41 366.31,163.11 351.17,295.55"}));
});
