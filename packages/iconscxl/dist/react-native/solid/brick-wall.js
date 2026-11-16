import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const BrickWallIcon = /*#__PURE__*/ forwardRef(function BrickWallIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.638 1.5914H14.362Q14.7905 1.5914 15.0815 1.8824Q15.3725 2.1734 15.3725 2.602V13.398Q15.3725 13.8266 15.0815 14.1176Q14.7905 14.4086 14.362 14.4086H1.638Q1.2095 14.4086 0.9185 14.1176Q0.6275 13.8266 0.6275 13.398V2.602Q0.6275 2.1735 0.9185 1.8824Q1.2095 1.5914 1.638 1.5914ZM1.5275 9.3977V10.458H3.6141V13.5086H4.6744V10.458H11.3256V13.5086H12.3859V10.458H14.4725V9.3977H8.5302V6.6023H14.4725V5.542H11.422V2.4914H10.3616V5.542H5.6384V2.4914H4.578V5.542H1.5275V6.6023H7.4698V9.3977Z", "fill": "currentColor"}));
});
