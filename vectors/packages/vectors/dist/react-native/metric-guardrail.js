import { createElement, forwardRef } from "react";
import { Svg, Path } from "react-native-svg";
export const MetricGuardrailVector = /*#__PURE__*/ forwardRef(function MetricGuardrailVector({size = 480, color = "currentColor", ...props}, ref) {
  return createElement(Svg, {...{"viewBox": "0 0 480 360", "fill": "none", "stroke": "currentColor", "strokeWidth": "3.6", "strokeLinecap": "round", "strokeLinejoin": "round"}, width: size, height: size * 360 / 480, color, accessible: true, accessibilityRole: "image", accessibilityLabel: "Metric guardrail", ...props, ref},
    createElement(Path, {"strokeOpacity": ".55", "d": "M129.19,143.60 114.29,238.68 320.85,238.68"}),
    createElement(Path, {"strokeOpacity": ".9", "d": "M136.28,85.81 111.25,98.33 85.00,265.85 85.00,274.19 343.72,274.19 395.00,248.55 395.00,85.81 136.28,85.81 M85.00,265.85 343.72,265.85 369.96,98.33 111.25,98.33 85.00,265.85 M343.72,265.85 343.72,274.19 M125.52,206.99 153.04,191.14 184.65,202.46 214.30,173.03 241.38,186.61 277.60,168.50 319.28,182.09 M307.64,123.23 329.92,114.17 349.37,123.23 343.74,145.87 333.62,157.19 322.12,163.98 312.75,157.19 306.18,145.87 307.64,123.23"}),
    createElement(Path, {"strokeOpacity": "1", "d": "M128.13,150.39 299.21,150.39"}));
});
