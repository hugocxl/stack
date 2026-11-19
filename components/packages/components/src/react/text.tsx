import type { ComponentPropsWithoutRef, ElementType, ReactNode } from "react";
import { cx } from "./utils.js";

export type TextVariant = "reading" | "heading" | "title" | "small" | "label" | "mono";
export type TextTone = "ink" | "muted" | "accent";

const defaultElement: Record<TextVariant, ElementType> = {
  reading: "p",
  heading: "h3",
  title: "h1",
  small: "p",
  label: "span",
  mono: "span",
};

export type TextProps = Omit<ComponentPropsWithoutRef<"p">, "color"> & {
  variant?: TextVariant;
  tone?: TextTone;
  /** The element to render. Defaults to the one that suits the variant. */
  as?: ElementType;
  children?: ReactNode;
};

/** Copy in one of the system's type styles. */
export function Text({ variant = "reading", tone, as, className, ...props }: TextProps) {
  const Element = as ?? defaultElement[variant];
  return <Element {...props} className={cx("dsc-text", className)} data-variant={variant} data-tone={tone} />;
}

/** A muted supporting sentence after the main one, inside the same paragraph. */
export function Muted({ className, ...props }: ComponentPropsWithoutRef<"span">) {
  return <span {...props} className={cx("dsc-muted", className)} />;
}

/** The accent phrase, at title size only. */
export function Accent({ className, ...props }: ComponentPropsWithoutRef<"span">) {
  return <span {...props} className={cx("dsc-accent", className)} />;
}
