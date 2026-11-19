import { forwardRef, type AnchorHTMLAttributes, type ButtonHTMLAttributes, type ComponentPropsWithoutRef, type ReactNode } from "react";
import { ArrowUpRightIcon } from "@hugocxl/icons/react/arrow-up-right";
import { cx, flag, renderIcon } from "./utils.js";

export type ButtonVariant = "primary" | "secondary" | "ghost";

type ButtonOwnProps = {
  variant?: ButtonVariant;
  /** An icon from @hugocxl/icons/react, shown before the label. */
  icon?: ReactNode;
  fullWidth?: boolean;
  children?: ReactNode;
};

export type ButtonProps = ButtonOwnProps &
  Omit<ButtonHTMLAttributes<HTMLButtonElement>, "children"> & {
    /** Render a link that looks like a button. */
    href?: string;
    target?: AnchorHTMLAttributes<HTMLAnchorElement>["target"];
    rel?: string;
  };

/** Starts an action. One primary button per view. */
export const Button = forwardRef<HTMLButtonElement & HTMLAnchorElement, ButtonProps>(function Button(
  { variant = "primary", icon, fullWidth, className, children, href, target, rel, type = "button", disabled, ...props },
  ref,
) {
  const shared = {
    className: cx("dsc-button", className),
    "data-variant": variant,
    "data-full-width": flag(fullWidth),
  };
  if (href !== undefined) {
    return (
      <a
        {...(props as AnchorHTMLAttributes<HTMLAnchorElement>)}
        {...shared}
        ref={ref}
        href={disabled ? undefined : href}
        target={target}
        rel={rel ?? (target === "_blank" ? "noopener noreferrer" : undefined)}
        aria-disabled={disabled || undefined}
      >
        {renderIcon(icon)}
        {children}
      </a>
    );
  }
  return (
    <button {...props} {...shared} ref={ref} type={type} disabled={disabled}>
      {renderIcon(icon)}
      {children}
    </button>
  );
});

export type ButtonGroupProps = ComponentPropsWithoutRef<"div"> & { align?: "start" | "end" };

/** Buttons side by side: secondary first, primary last. */
export function ButtonGroup({ align = "start", className, ...props }: ButtonGroupProps) {
  return <div {...props} className={cx("dsc-button-group", className)} data-align={align} />;
}

export type IconButtonProps = Omit<ButtonHTMLAttributes<HTMLButtonElement>, "children"> & {
  /** An icon from @hugocxl/icons/react. */
  icon: ReactNode;
  /** Required: read by assistive technology and shown as a tooltip. */
  label: string;
  variant?: "outline" | "ghost";
};

/** An action shown only as an icon, in a 44px circle. */
export const IconButton = forwardRef<HTMLButtonElement, IconButtonProps>(function IconButton(
  { icon, label, variant = "outline", className, type = "button", title, ...props },
  ref,
) {
  return (
    <button {...props} ref={ref} type={type} className={cx("dsc-icon-button", className)} data-variant={variant} aria-label={label} title={title ?? label}>
      {renderIcon(icon)}
    </button>
  );
});

export type LinkProps = AnchorHTMLAttributes<HTMLAnchorElement> & {
  variant?: "inline" | "standalone";
  icon?: ReactNode;
  /** Open in a new tab, with an arrow after the words. */
  external?: boolean;
};

/** Takes people somewhere, inline in a sentence or standalone in navigation. */
export const Link = forwardRef<HTMLAnchorElement, LinkProps>(function Link(
  { variant = "inline", icon, external, className, children, target, rel, ...props },
  ref,
) {
  return (
    <a
      {...props}
      ref={ref}
      className={cx("dsc-link", className)}
      data-variant={variant}
      target={target ?? (external ? "_blank" : undefined)}
      rel={rel ?? (external ? "noopener noreferrer" : undefined)}
    >
      {renderIcon(icon)}
      {children}
      {external && (
        <>
          {" "}
          <ArrowUpRightIcon className="dsc-icon" style={{ fontSize: ".75em", verticalAlign: "0" }} />
          <span className="dsc-visually-hidden">(opens in a new tab)</span>
        </>
      )}
    </a>
  );
});
