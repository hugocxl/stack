import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const VideoCallIcon = /*#__PURE__*/ forwardRef(function VideoCallIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.75 3.45H9.25Q9.9956 3.45 10.5228 3.9772Q11.05 4.5044 11.05 5.25V5.9714L14.5 4V12L11.05 10.0286V10.75Q11.05 11.4956 10.5228 12.0228Q9.9956 12.55 9.25 12.55H2.75Q2.0044 12.55 1.4772 12.0228Q0.95 11.4956 0.95 10.75V5.25Q0.95 4.5044 1.4772 3.9772Q2.0044 3.45 2.75 3.45Z", "fill": "currentColor"}));
});
