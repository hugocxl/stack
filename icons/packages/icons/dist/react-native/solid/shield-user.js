import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const ShieldUserIcon = /*#__PURE__*/ forwardRef(function ShieldUserIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M8.2659 1.6624 12.3728 3.1096Q12.8471 3.2827 13.0986 3.6419Q13.35 4.0011 13.35 4.5V8.95Q13.35 10.6693 11.9014 11.6738L8.9075 13.8693Q8.4733 14.195 8 14.195Q7.5267 14.195 7.088 13.866L4.0972 11.6728Q2.65 10.6716 2.65 8.95V4.5Q2.65 4.0011 2.9014 3.6419Q3.1529 3.2827 3.6217 3.1115L7.7341 1.6623Q8 1.5687 8.2659 1.6624ZM5.738 9.968H10.262Q10.262 7.979 8 7.979Q5.738 7.979 5.738 9.968ZM6.791 6.107C6.791 6.7747 7.3323 7.316 8 7.316C8.6677 7.316 9.209 6.7747 9.209 6.107C9.209 5.4393 8.6677 4.898 8 4.898C7.3323 4.898 6.791 5.4393 6.791 6.107Z", "fill": "currentColor"}));
});
