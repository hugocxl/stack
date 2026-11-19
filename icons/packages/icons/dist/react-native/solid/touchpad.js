import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TouchpadIcon = /*#__PURE__*/ forwardRef(function TouchpadIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.05 1.95 12.95 1.95Q13.6956 1.95 14.2228 2.4772Q14.75 3.0044 14.75 3.75V12.25Q14.75 12.9956 14.2228 13.5228Q13.6956 14.05 12.95 14.05H3.05Q2.3044 14.05 1.7772 13.5228Q1.25 12.9956 1.25 12.25V3.75Q1.25 3.0044 1.7772 2.4772Q2.3044 1.95 3.05 1.95ZM2.15 10.55H7.45V13Q7.45 13.0542 7.4606 13.1073Q7.4649 13.1289 7.4708 13.15H8.5292Q8.5351 13.1289 8.5394 13.1073Q8.55 13.0542 8.55 13V10.55H13.85V9.45H2.15Z", "fill": "currentColor"}));
});
