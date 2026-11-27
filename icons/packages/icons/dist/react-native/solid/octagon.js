import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const OctagonIcon = /*#__PURE__*/ forwardRef(function OctagonIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M14.0808 4.8528 14.0816 4.8536Q14.5252 5.2975 14.5252 5.9268V10.0732Q14.5252 10.703 14.0799 11.1481L11.148 14.08Q10.703 14.5252 10.0732 14.5252H5.9268Q5.297 14.5252 4.8519 14.0799L1.92 11.148Q1.4748 10.703 1.4748 10.0732L1.4748 5.9268Q1.4748 5.297 1.9201 4.8519L4.852 1.92Q5.297 1.4748 5.9268 1.4748L10.0732 1.4748Q10.703 1.4748 11.1481 1.9201L14.08 4.852Z", "fill": "currentColor"}));
});
