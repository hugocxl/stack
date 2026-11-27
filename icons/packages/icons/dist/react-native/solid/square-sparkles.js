import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const SquareSparklesIcon = /*#__PURE__*/ forwardRef(function SquareSparklesIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M3.82 2.1 12.18 2.1Q12.8924 2.1 13.3962 2.6038Q13.9 3.1076 13.9 3.82V12.18Q13.9 12.8924 13.3962 13.3962Q12.8924 13.9 12.18 13.9H3.82Q3.1076 13.9 2.6038 13.3962Q2.1 12.8924 2.1 12.18L2.1 3.82Q2.1 3.1076 2.6038 2.6038Q3.1076 2.1 3.82 2.1ZM7.47 4.797Q7.041 7.761 5.052 8.346Q7.041 8.931 7.47 10.92Q7.899 8.931 9.888 8.346Q7.899 7.761 7.47 4.797ZM10.512 4.524Q10.278 5.499 9.342 5.772Q10.278 6.045 10.512 7.02Q10.746 6.045 11.682 5.772Q10.746 5.499 10.512 4.524Z", "fill": "currentColor"}));
});
