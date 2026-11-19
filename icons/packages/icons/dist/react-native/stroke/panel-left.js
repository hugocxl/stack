import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const PanelLeftIcon = /*#__PURE__*/ forwardRef(function PanelLeftIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.25 1.45H12.75Q13.4956 1.45 14.0228 1.9772Q14.55 2.5044 14.55 3.25V12.75Q14.55 13.4956 14.0228 14.0228Q13.4956 14.55 12.75 14.55H3.25Q2.5044 14.55 1.9772 14.0228Q1.45 13.4956 1.45 12.75V3.25Q1.45 2.5044 1.9772 1.9772Q2.5044 1.45 3.25 1.45ZM6.55 13.45H12.75Q13.04 13.45 13.245 13.245Q13.45 13.04 13.45 12.75V3.25Q13.45 2.96 13.245 2.755Q13.04 2.55 12.75 2.55H6.55V13.45ZM3.25 2.55Q2.9601 2.55 2.755 2.755Q2.55 2.9601 2.55 3.25V12.75Q2.55 13.04 2.755 13.245Q2.9601 13.45 3.25 13.45H5.45V2.55Z", "fill": "currentColor"}));
});
