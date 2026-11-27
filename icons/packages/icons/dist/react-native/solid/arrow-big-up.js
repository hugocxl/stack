import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const ArrowBigUpIcon = /*#__PURE__*/ forwardRef(function ArrowBigUpIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M6.65 14.77Q6.0204 14.77 5.5752 14.3248Q5.13 13.8796 5.13 13.25V8.8Q5.13 8.7875 5.1212 8.7788Q5.1125 8.77 5.1 8.77H4.171Q3.4105 8.77 3.0704 8.0898Q2.7303 7.4096 3.1866 6.8012L6.784 2.0047Q7.24 1.3967 8 1.3967Q8.76 1.3967 9.216 2.0047L12.8134 6.8012Q13.2697 7.4096 12.9296 8.0898Q12.5895 8.77 11.829 8.77H10.9Q10.8875 8.77 10.8788 8.7788Q10.87 8.7875 10.87 8.8V13.25Q10.87 13.8796 10.4248 14.3248Q9.9796 14.77 9.35 14.77Z", "fill": "currentColor"}));
});
