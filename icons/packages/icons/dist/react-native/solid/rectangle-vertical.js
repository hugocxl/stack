import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const RectangleVerticalIcon = /*#__PURE__*/ forwardRef(function RectangleVerticalIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M4.38 1.14 11.62 1.14Q12.3324 1.14 12.8362 1.6438Q13.34 2.1476 13.34 2.86V13.14Q13.34 13.8524 12.8362 14.3562Q12.3324 14.86 11.62 14.86H4.38Q3.6676 14.86 3.1638 14.3562Q2.66 13.8524 2.66 13.14L2.66 2.86Q2.66 2.1476 3.1638 1.6438Q3.6676 1.14 4.38 1.14Z", "fill": "currentColor"}));
});
