import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const GuidePointIcon = /*#__PURE__*/ forwardRef(function GuidePointIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M1.4 8C1.4 7.144 2.094 6.45 2.95 6.45C3.6236 6.45 4.1969 6.8797 4.4106 7.48H11.5894C11.8031 6.8797 12.3764 6.45 13.05 6.45C13.906 6.45 14.6 7.144 14.6 8C14.6 8.856 13.906 9.55 13.05 9.55C12.3764 9.55 11.8031 9.1203 11.5894 8.52H4.4106C4.1969 9.1203 3.6236 9.55 2.95 9.55C2.094 9.55 1.4 8.856 1.4 8Z", "fill": "currentColor"}));
});
