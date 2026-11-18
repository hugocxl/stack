import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const FootprintsIcon = /*#__PURE__*/ forwardRef(function FootprintsIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M9.312 7.8927 9.0963 6.2622C8.6923 4.7962 8.5255 3.1761 10.1964 2.0489C11.8776 0.8727 14.1286 2.0668 14.1113 4.3123C14.0825 5.8908 13.4845 7.5017 12.6377 8.5996ZM6.688 10.5427 3.3623 11.2496C2.5155 10.1517 1.9175 8.5408 1.8887 6.9623C1.8714 4.7168 4.1224 3.5227 5.8036 4.6989C7.4745 5.8261 7.3077 7.4462 6.9037 8.9122ZM3.8282 12.4796 6.9093 11.8247 7.1234 13.3127C7.3821 15.2513 4.8878 15.7815 4.318 14.0624ZM12.1718 9.8296 11.682 11.4124C11.1122 13.1315 8.6179 12.6013 8.8766 10.6627L9.0907 9.1747Z", "fill": "currentColor"}));
});
