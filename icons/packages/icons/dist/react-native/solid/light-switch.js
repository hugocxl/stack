import { createElement, forwardRef } from "react";
import { Svg, Path, Circle, Rect, G } from "react-native-svg";
export const LightSwitchIcon = /*#__PURE__*/ forwardRef(function LightSwitchIcon({size = 16, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"fill": "none", "viewBox": "0 0 16 16"}, width: size, height: size, color, ...props, ref} ,createElement(Path, {"d": "M6.0941 0.6382H9.9059Q11.012 0.6382 11.7941 1.4203Q12.5762 2.2025 12.5762 3.3085V12.6915Q12.5762 13.7975 11.7941 14.5797Q11.012 15.3618 9.9059 15.3618H6.0941Q4.988 15.3618 4.2059 14.5797Q3.4238 13.7976 3.4238 12.6915V3.3085Q3.4238 2.2024 4.2059 1.4203Q4.988 0.6382 6.0941 0.6382ZM6.1918 3.113C5.814 3.113 5.5076 3.4193 5.5076 3.7972V6.2407C5.5076 6.6186 5.814 6.9249 6.1918 6.9249H9.8082C10.186 6.9249 10.4924 6.6186 10.4924 6.2407V3.7972C10.4924 3.4193 10.186 3.113 9.8082 3.113Z", "fill": "currentColor"}));
});
