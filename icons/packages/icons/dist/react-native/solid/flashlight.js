import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const FlashlightIcon = /*#__PURE__*/ forwardRef(function FlashlightIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M5.55 0.78H10.45Q10.9654 0.78 11.2677 1.0823Q11.57 1.3846 11.57 1.9V4.1Q11.57 4.7733 11.166 5.312L10.22 6.6185L10.22 14.1Q10.22 14.6154 9.9177 14.9177Q9.6154 15.22 9.1 15.22H6.9Q6.3846 15.22 6.0823 14.9177Q5.78 14.6154 5.78 14.1V6.6185L4.8288 5.305Q4.43 4.7733 4.43 4.1V1.9Q4.43 1.3846 4.7323 1.0823Q5.0346 0.78 5.55 0.78ZM5.33 3.67H10.67V2.63H5.33ZM8 8.4C7.641 8.4 7.35 8.691 7.35 9.05V10.25C7.35 10.609 7.641 10.9 8 10.9C8.359 10.9 8.65 10.609 8.65 10.25V9.05C8.65 8.691 8.359 8.4 8 8.4Z", "fill": "currentColor"}));
});
