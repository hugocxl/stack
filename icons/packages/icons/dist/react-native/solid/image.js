import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const ImageIcon = /*#__PURE__*/ forwardRef(function ImageIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.12 2.3 12.88 2.3Q13.8824 2.3 14.5912 3.0088Q15.3 3.7176 15.3 4.72V11.28Q15.3 12.2824 14.5912 12.9912Q13.8824 13.7 12.88 13.7H3.12Q2.1176 13.7 1.4088 12.9912Q0.7 12.2824 0.7 11.28V4.72Q0.7 3.7176 1.4088 3.0088Q2.1176 2.3 3.12 2.3ZM14.26 10.4882 11.6 7.75Q11.35 7.475 11.1 7.475Q10.85 7.475 10.6 7.75L8.65 10.25L6.65 8.6Q6.1 8.15 5.55 8.6L1.7778 11.5846C1.9242 12.2013 2.4785 12.66 3.14 12.66H12.86C13.6332 12.66 14.26 12.0332 14.26 11.26ZM3.7 6.3C3.7 7.0456 4.3044 7.65 5.05 7.65C5.7956 7.65 6.4 7.0456 6.4 6.3C6.4 5.5544 5.7956 4.95 5.05 4.95C4.3044 4.95 3.7 5.5544 3.7 6.3Z", "fill": "currentColor"}));
});
