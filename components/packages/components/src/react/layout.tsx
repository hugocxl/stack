import type { ComponentPropsWithoutRef, CSSProperties, ReactNode } from "react";
import { ThemeToggle } from "./theme.js";
import { cx } from "./utils.js";

export type PageProps = Omit<ComponentPropsWithoutRef<"div">, "children"> & {
  /** field adds the textured panel, for a personal home page only. */
  layout?: "plain" | "field";
  /** The image behind the field panel, such as @hugocxl/design-system/system/images/gray-folds.png. */
  fieldImage?: string;
  masthead?: ReactNode;
  footer?: ReactNode;
  /** Wrap the content in the reading column with the opening space. Defaults to true. */
  column?: boolean;
  children?: ReactNode;
};

/** The canvas, gutter and reading column every page sits in. */
export function Page({ layout = "plain", fieldImage, masthead, footer, column = true, className, style, children, ...props }: PageProps) {
  const pageStyle = fieldImage ? ({ "--dsc-field-image": `url("${fieldImage}")`, ...style } as CSSProperties) : style;
  return (
    <div {...props} className={cx("dsc-page", className)} data-layout={layout} style={pageStyle}>
      {masthead}
      <main>{column ? <article className="dsc-column dsc-opening">{children}</article> : children}</main>
      {footer}
    </div>
  );
}

export type NavLink = { label: ReactNode; href: string; current?: boolean };

export type MastheadProps = Omit<ComponentPropsWithoutRef<"header">, "children"> & {
  wordmark: ReactNode;
  href?: string;
  /** Up to three. */
  links?: NavLink[];
  /** A row of mono links above the wordmark, such as the other sites of a family. */
  nav?: { label: string; links: NavLink[] };
  /** Defaults to true. */
  themeToggle?: boolean;
  /** Extra items at the end, before the theme toggle. */
  children?: ReactNode;
};

/** The wordmark, up to three links and the theme toggle. */
export function Masthead({ wordmark, href = "/", links = [], nav, themeToggle = true, className, children, ...props }: MastheadProps) {
  return (
    <header {...props} className={cx("dsc-masthead", className)}>
      {nav && (
        <nav className="dsc-masthead-nav" aria-label={nav.label}>
          {nav.links.map((link) => (
            <a key={link.href} href={link.href} aria-current={link.current ? "page" : undefined}>
              {link.label}
            </a>
          ))}
        </nav>
      )}
      <a className="dsc-wordmark" href={href}>
        {wordmark}
      </a>
      {links.map((link) => (
        <a key={link.href} href={link.href} aria-current={link.current ? "page" : undefined}>
          {link.label}
        </a>
      ))}
      {children}
      {themeToggle && <ThemeToggle />}
    </header>
  );
}

export type FooterProps = Omit<ComponentPropsWithoutRef<"footer">, "children"> & {
  /** The project's own pages. */
  links: NavLink[];
  /** Elsewhere: npm, GitHub, the author. */
  secondary?: NavLink[];
};

/** Two groups of mono links on either side of a hairline. */
export function Footer({ links, secondary = [], className, ...props }: FooterProps) {
  const group = (items: NavLink[]) => (
    <ul>
      {items.map((link) => (
        <li key={link.href}>
          <a href={link.href}>{link.label}</a>
        </li>
      ))}
    </ul>
  );
  return (
    <footer {...props} className={cx("dsc-footer", className)}>
      {group(links)}
      {secondary.length > 0 && group(secondary)}
    </footer>
  );
}
