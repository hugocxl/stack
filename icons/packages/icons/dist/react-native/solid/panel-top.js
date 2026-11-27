import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const PanelTopIcon = /*#__PURE__*/ forwardRef(function PanelTopIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.12 2.3 12.88 2.3Q13.8824 2.3 14.5912 3.0088Q15.3 3.7176 15.3 4.72V11.28Q15.3 12.2824 14.5912 12.9912Q13.8824 13.7 12.88 13.7H3.12Q2.1176 13.7 1.4088 12.9912Q0.7 12.2824 0.7 11.28V4.72Q0.7 3.7176 1.4088 3.0088Q2.1176 2.3 3.12 2.3ZM1.6 6.57H14.4V5.53H1.6Z", "fill": "currentColor"}));
});
