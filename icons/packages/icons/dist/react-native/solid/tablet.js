import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const TabletIcon = /*#__PURE__*/ forwardRef(function TabletIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.8626 0.6354 12.1374 0.6354Q12.8693 0.6354 13.3868 1.1529Q13.9043 1.6705 13.9043 2.4023V13.5977Q13.9043 14.3295 13.3868 14.8471Q12.8693 15.3646 12.1374 15.3646H3.8626Q3.1307 15.3646 2.6132 14.8471Q2.0957 14.3296 2.0957 13.5977L2.0957 2.4023Q2.0957 1.6704 2.6132 1.1529Q3.1307 0.6354 3.8626 0.6354ZM7.3672 12.3808C7.3672 12.7303 7.6505 13.0136 8 13.0136C8.3495 13.0136 8.6328 12.7303 8.6328 12.3808C8.6328 12.0313 8.3495 11.748 8 11.748C7.6505 11.748 7.3672 12.0313 7.3672 12.3808Z", "fill": "currentColor"}));
});
