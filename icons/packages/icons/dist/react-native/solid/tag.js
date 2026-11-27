import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TagIcon = /*#__PURE__*/ forwardRef(function TagIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M14.42 3.6V7.55Q14.42 8.4154 13.8177 9.0177L8.5177 14.3177Q7.8654 14.97 7.15 14.97Q6.4346 14.97 5.7823 14.3177L1.6823 10.2177Q1.03 9.5654 1.03 8.85Q1.03 8.1346 1.6823 7.4823L6.9823 2.1823Q7.5846 1.58 8.45 1.58H12.4Q13.3654 1.58 13.8927 2.1073Q14.42 2.6346 14.42 3.6ZM9.9 5.1C9.9 5.6523 10.3477 6.1 10.9 6.1C11.4523 6.1 11.9 5.6523 11.9 5.1C11.9 4.5477 11.4523 4.1 10.9 4.1C10.3477 4.1 9.9 4.5477 9.9 5.1Z", "fill": "currentColor"}));
});
