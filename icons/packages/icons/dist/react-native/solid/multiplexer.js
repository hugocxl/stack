import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const MultiplexerIcon = /*#__PURE__*/ forwardRef(function MultiplexerIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M6.25 4.45H13.25Q13.9956 4.45 14.5228 4.9772Q15.05 5.5044 15.05 6.25V13.25Q15.05 13.9956 14.5228 14.5228Q13.9956 15.05 13.25 15.05H6.25Q5.5044 15.05 4.9772 14.5228Q4.45 13.9956 4.45 13.25V6.25Q4.45 5.5044 4.9772 4.9772Q5.5044 4.45 6.25 4.45ZM2.75 0.95H9.75Q10.4956 0.95 11.0228 1.4772Q11.55 2.0044 11.55 2.75V3.9H6.25Q5.2766 3.9 4.5883 4.5883Q3.9 5.2766 3.9 6.25V11.55H2.75Q2.0044 11.55 1.4772 11.0228Q0.95 10.4956 0.95 9.75V2.75Q0.95 2.0044 1.4772 1.4772Q2.0044 0.95 2.75 0.95ZM5.35 9.45V10.55H9.45V14.15H10.55V10.55H14.15V9.45H10.55V5.35H9.45V9.45Z", "fill": "currentColor"}));
});
