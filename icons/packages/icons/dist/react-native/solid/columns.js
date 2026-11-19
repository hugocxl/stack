import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const ColumnsIcon = /*#__PURE__*/ forwardRef(function ColumnsIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.25 1.45H12.75Q13.4956 1.45 14.0228 1.9772Q14.55 2.5044 14.55 3.25V12.75Q14.55 13.4956 14.0228 14.0228Q13.4956 14.55 12.75 14.55H3.25Q2.5044 14.55 1.9772 14.0228Q1.45 13.4956 1.45 12.75V3.25Q1.45 2.5044 1.9772 1.9772Q2.5044 1.45 3.25 1.45ZM7.45 13.65H8.55V2.35H7.45Z", "fill": "currentColor"}));
});
