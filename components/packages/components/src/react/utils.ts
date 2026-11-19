import { cloneElement, isValidElement, type ReactElement, type ReactNode } from "react";

/** Join class names, skipping empty ones. */
export function cx(...names: Array<string | false | null | undefined>): string {
  return names.filter(Boolean).join(" ");
}

/** An icon from @hugocxl/icons/react, such as `<ArrowRightIcon />`. */
export type IconElement = ReactElement<{ className?: string }>;

/** Give an icon element the shared icon class, so the component sizes and colors it. */
export function renderIcon(icon: ReactNode): ReactNode {
  if (!isValidElement<{ className?: string }>(icon)) return icon;
  return cloneElement(icon, { className: cx("dsc-icon", icon.props.className) });
}

/** Boolean data attributes: present when true, absent otherwise. */
export const flag = (value: unknown): "" | undefined => (value ? "" : undefined);
