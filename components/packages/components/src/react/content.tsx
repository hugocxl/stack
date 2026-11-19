import { useEffect, useRef, useState, type ComponentPropsWithoutRef, type ReactNode } from "react";
import { ArrowLeftIcon } from "@hugocxl/icons/react/arrow-left";
import { ArrowRightIcon } from "@hugocxl/icons/react/arrow-right";
import { ChevronRightIcon } from "@hugocxl/icons/react/chevron-right";
import { IconButton } from "./actions.js";
import { cx, flag } from "./utils.js";

export type TitleProps = Omit<ComponentPropsWithoutRef<"hgroup">, "children"> & {
  children: ReactNode;
  byline?: ReactNode;
};

/** The name of the page in ink, with an optional muted byline. */
export function Title({ children, byline, className, ...props }: TitleProps) {
  return (
    <hgroup {...props} className={cx("dsc-title", className)}>
      <h1>{children}</h1>
      {byline && <p>{byline}</p>}
    </hgroup>
  );
}

export type StatementProps = ComponentPropsWithoutRef<"h1"> & {
  /** The last two or three words, in the accent. */
  accent?: ReactNode;
};

/** One sentence at title size that opens a home page. */
export function Statement({ children, accent, className, ...props }: StatementProps) {
  return (
    <h1 {...props} className={cx("dsc-statement", className)}>
      {children}
      {accent && (
        <>
          {" "}
          <span className="dsc-accent">{accent}</span>
        </>
      )}
    </h1>
  );
}

export type MetaProps = Omit<ComponentPropsWithoutRef<"ul">, "children"> & {
  /** One to three labels: status first, then version or date. */
  items: ReactNode[];
};

/** One to three mono labels under the title. */
export function Meta({ items, className, ...props }: MetaProps) {
  return (
    <ul {...props} className={cx("dsc-meta", className)}>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}

export type SectionProps = ComponentPropsWithoutRef<"section"> & {
  /** Leave empty for the lead section. */
  heading?: ReactNode;
};

/** A muted heading followed by paragraphs, lists, code or a table. */
export function Section({ heading, className, children, ...props }: SectionProps) {
  return (
    <section {...props} className={cx("dsc-section", className)}>
      {heading && <h2>{heading}</h2>}
      {children}
    </section>
  );
}

/** A 1px hairline between groups. */
export function Divider({ className, ...props }: ComponentPropsWithoutRef<"hr">) {
  return <hr {...props} className={cx("dsc-divider", className)} />;
}

export type CodeBlockProps = Omit<ComponentPropsWithoutRef<"div">, "children"> & {
  /** The exact text that is shown and copied. */
  code: string;
  /** A file name or language. */
  label?: ReactNode;
  /** Hide the copy button. */
  copyable?: boolean;
};

/** Code or commands in mono on the surface, with a copy button. */
export function CodeBlock({ code, label, copyable = true, className, ...props }: CodeBlockProps) {
  const [state, setState] = useState<"idle" | "copied" | "failed">("idle");
  const timer = useRef<ReturnType<typeof setTimeout>>(undefined);
  useEffect(() => () => clearTimeout(timer.current), []);
  async function copy() {
    try {
      await navigator.clipboard.writeText(code);
      setState("copied");
    } catch {
      setState("failed");
    }
    clearTimeout(timer.current);
    timer.current = setTimeout(() => setState("idle"), 1600);
  }
  return (
    <div {...props} className={cx("dsc-code", className)}>
      {label && <span className="dsc-code-label">{label}</span>}
      <pre tabIndex={0}>
        <code>{code}</code>
      </pre>
      {copyable && (
        <button type="button" className="dsc-code-copy" onClick={copy} aria-live="polite">
          {state === "copied" ? "Copied" : state === "failed" ? "Select to copy" : "Copy"}
        </button>
      )}
    </div>
  );
}

export type ListItem = {
  key?: string;
  /** A date, a version or a short kind. */
  label?: ReactNode;
  title: ReactNode;
  description?: ReactNode;
  /** A value or a status at the end of the row. */
  trailing?: ReactNode;
  /** Makes the whole row a link. */
  href?: string;
  /** Makes the whole row a button. */
  onClick?: () => void;
};

export type ListProps = Omit<ComponentPropsWithoutRef<"ul">, "children"> & {
  items: ListItem[];
  density?: "regular" | "compact";
};

/** Rows between hairlines that people scan. */
export function List({ items, density = "regular", className, ...props }: ListProps) {
  const labels = items.some((item) => item.label !== undefined);
  return (
    <ul {...props} className={cx("dsc-list", className)} data-labels={flag(labels)} data-density={density}>
      {items.map((item, index) => {
        const action = item.href !== undefined || item.onClick !== undefined;
        const row = (
          <div className="dsc-list-row">
            {labels && <span className="dsc-list-label">{item.label}</span>}
            <div>
              <h3 className="dsc-list-title">{item.title}</h3>
              {item.description && <p className="dsc-list-description">{item.description}</p>}
            </div>
            {(item.trailing || action) && (
              <span className="dsc-list-trailing">
                {item.trailing}
                {action && <ChevronRightIcon className="dsc-icon" />}
              </span>
            )}
          </div>
        );
        return (
          <li key={item.key ?? index}>
            {item.href !== undefined ? (
              <a className="dsc-list-action" href={item.href}>
                {row}
              </a>
            ) : item.onClick ? (
              <button type="button" className="dsc-list-action" onClick={item.onClick}>
                {row}
              </button>
            ) : (
              row
            )}
          </li>
        );
      })}
    </ul>
  );
}

export type TableColumn = { label: ReactNode; align?: "start" | "end" };

export type TableProps = Omit<ComponentPropsWithoutRef<"table">, "children"> & {
  columns: TableColumn[];
  /** The first cell of each row is its header. */
  rows: ReactNode[][];
  /** Read by assistive technology. */
  caption?: ReactNode;
};

/** Rows and columns of data on hairlines. */
export function Table({ columns, rows, caption, className, ...props }: TableProps) {
  return (
    <div className="dsc-table-scroll">
      <table {...props} className={cx("dsc-table", className)}>
        {caption && <caption className="dsc-visually-hidden">{caption}</caption>}
        <thead>
          <tr>
            {columns.map((column, index) => (
              <th key={index} scope="col" data-align={column.align}>
                {column.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, index) =>
                index === 0 ? (
                  <th key={index} scope="row" data-align={columns[index]?.align}>
                    {cell}
                  </th>
                ) : (
                  <td key={index} data-align={columns[index]?.align}>
                    {cell}
                  </td>
                ),
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export type FigureProps = Omit<ComponentPropsWithoutRef<"figure">, "children"> & {
  /** A vector from @hugocxl/vectors/react, or an <img> with alt text. */
  children: ReactNode;
  /** Written “Fig. 01 / Name”. */
  caption?: ReactNode;
  /** Extend past the reading column. */
  wide?: boolean;
  /** Only when the figure cycles. */
  pager?: { onPrevious: () => void; onNext: () => void };
};

/** One vector or screenshot on the surface at 3:2, with a caption. */
export function Figure({ children, caption, wide = true, pager, className, ...props }: FigureProps) {
  return (
    <figure {...props} className={cx("dsc-figure", wide && "dsc-wide", className)}>
      <div className="dsc-media">{children}</div>
      {(caption || pager) && (
        <figcaption className="dsc-caption">
          <span>{caption}</span>
          {pager && (
            <span className="dsc-pager">
              <IconButton variant="ghost" label="Previous" icon={<ArrowLeftIcon />} onClick={pager.onPrevious} />
              <IconButton variant="ghost" label="Next" icon={<ArrowRightIcon />} onClick={pager.onNext} />
            </span>
          )}
        </figcaption>
      )}
    </figure>
  );
}

export type FigureGridItem = { label?: ReactNode; media: ReactNode; title: ReactNode; text?: ReactNode };

export type FigureGridProps = Omit<ComponentPropsWithoutRef<"ul">, "children"> & {
  /** Two to four. */
  items: FigureGridItem[];
  wide?: boolean;
};

/** Two to four vectors side by side between hairlines. */
export function FigureGrid({ items, wide = true, className, style, ...props }: FigureGridProps) {
  return (
    <ul {...props} className={cx("dsc-grid", wide && "dsc-wide", className)} style={{ ["--dsc-cols" as string]: items.length, ...style }}>
      {items.map((item, index) => (
        <li key={index}>
          <span className="dsc-grid-label">{item.label ?? `Fig 0.${index + 1}`}</span>
          <div className="dsc-grid-media">{item.media}</div>
          <h3>{item.title}</h3>
          {item.text && <p>{item.text}</p>}
        </li>
      ))}
    </ul>
  );
}
