import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const ChessPawnIcon = /*#__PURE__*/ forwardRef(function ChessPawnIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M5.3294 7.951Q3.9148 6.4573 3.6498 5.1327Q3.3351 3.559 4.5682 2.3259Q6.2462 0.6479 8 0.6479Q9.7538 0.6479 11.4318 2.3259Q12.6649 3.559 12.3502 5.1327Q12.0852 6.4573 10.6706 7.951L11.5022 12.1089H12.5844Q13.0187 12.1089 13.3134 12.4036Q13.6081 12.6983 13.6081 13.1325V14.3285Q13.6081 14.7627 13.3134 15.0574Q13.0187 15.3521 12.5844 15.3521H3.4156Q2.9813 15.3521 2.6866 15.0574Q2.3919 14.7627 2.3919 14.3285V13.1325Q2.3919 12.6983 2.6866 12.4036Q2.9813 12.1089 3.4156 12.1089H4.4978Z", "fill": "currentColor"}));
});
