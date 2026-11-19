import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const BrickWallIcon = /*#__PURE__*/ forwardRef(function BrickWallIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M2.85 1.55H13.15Q13.8956 1.55 14.4228 2.0772Q14.95 2.6044 14.95 3.35V12.65Q14.95 13.3956 14.4228 13.9228Q13.8956 14.45 13.15 14.45H2.85Q2.1044 14.45 1.5772 13.9228Q1.05 13.3956 1.05 12.65L1.05 3.35Q1.05 2.6044 1.5772 2.0772Q2.1044 1.55 2.85 1.55ZM1.95 9.45 1.95 10.55H4.8V13.55H5.9V10.55H10.1V13.55H11.2V10.55H14.05V9.45H8.55V6.55H14.05V5.45H11.2V2.45H10.1V5.45H5.9V2.45H4.8V5.45H1.95L1.95 6.55H7.45V9.45Z", "fill": "currentColor"}));
});
