import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const DiamondIcon = /*#__PURE__*/ forwardRef(function DiamondIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M6.607 1.4076Q7.184 0.8306 8 0.8306Q8.816 0.8306 9.393 1.4076L14.5924 6.607Q15.1694 7.184 15.1694 8Q15.1694 8.816 14.5924 9.393L9.393 14.5924Q8.816 15.1694 8 15.1694Q7.184 15.1694 6.607 14.5924L1.4076 9.393Q0.8306 8.816 0.8306 8Q0.8306 7.184 1.4076 6.607Z", "fill": "currentColor"}));
});
