import { useEffect, useId, useRef, type ComponentPropsWithoutRef, type ReactNode } from "react";
import { CircleCheckIcon } from "@hugocxl/icons/react/circle-check";
import { CircleInfoIcon } from "@hugocxl/icons/react/circle-info";
import { CircleXIcon } from "@hugocxl/icons/react/circle-x";
import { CloseIcon } from "@hugocxl/icons/react/close";
import { TriangleAlertIcon } from "@hugocxl/icons/react/triangle-alert";
import { IconButton } from "./actions.js";
import { cx, flag } from "./utils.js";

export type StatusTone = "accent" | "success" | "warning" | "error" | "info" | "neutral";

const statusIcons = {
  success: CircleCheckIcon,
  warning: TriangleAlertIcon,
  error: CircleXIcon,
  info: CircleInfoIcon,
} as const;

function StatusIcon({ tone }: { tone: StatusTone }) {
  const Icon = tone in statusIcons ? statusIcons[tone as keyof typeof statusIcons] : null;
  return Icon ? <Icon className="dsc-icon" /> : <span className="dsc-status-dot" aria-hidden="true" />;
}

export type StatusProps = ComponentPropsWithoutRef<"span"> & {
  tone?: StatusTone;
  /** A dot, or the status icon (success, warning, error and info only). */
  mark?: "dot" | "icon";
  /** label is mono uppercase; text follows the surrounding type. */
  appearance?: "label" | "text";
};

/** Names a state with words and a mark in the state's color. */
export function Status({ tone = "accent", mark = "dot", appearance = "label", className, children, ...props }: StatusProps) {
  return (
    <span {...props} className={cx("dsc-status", className)} data-tone={tone} data-appearance={appearance}>
      {mark === "icon" ? <StatusIcon tone={tone} /> : <span className="dsc-status-dot" aria-hidden="true" />}
      {children}
    </span>
  );
}

export type NoticeProps = Omit<ComponentPropsWithoutRef<"div">, "title"> & {
  tone?: Exclude<StatusTone, "accent">;
  /** Required. One short sentence. */
  title: ReactNode;
  /** One ghost button. */
  action?: ReactNode;
  /** Shows a close button that calls this. */
  onDismiss?: () => void;
};

/** A short message about the page or a task, in a hairline frame with a status icon. */
export function Notice({ tone = "info", title, action, onDismiss, className, children, ...props }: NoticeProps) {
  const urgent = tone === "error" || tone === "warning";
  return (
    <div {...props} className={cx("dsc-notice", className)} data-tone={tone} role={urgent ? "alert" : "status"}>
      {tone === "neutral" ? <CircleInfoIcon className="dsc-icon" /> : <StatusIcon tone={tone} />}
      <div className="dsc-notice-body">
        <p className="dsc-notice-title">{title}</p>
        {children && <div className="dsc-notice-text">{children}</div>}
        {action && <div className="dsc-notice-action">{action}</div>}
      </div>
      {onDismiss && <IconButton variant="ghost" label="Dismiss" icon={<CloseIcon />} onClick={onDismiss} />}
    </div>
  );
}

export type DialogProps = {
  open: boolean;
  /** Called when the dialog asks to close: Escape, the close button or a cancel action. */
  onClose: () => void;
  title: ReactNode;
  description?: ReactNode;
  /** Buttons, secondary first and primary last. */
  actions?: ReactNode;
  children?: ReactNode;
  className?: string;
};

/** Asks for a decision or a few values before going on, above a veil of the canvas. */
export function Dialog({ open, onClose, title, description, actions, children, className }: DialogProps) {
  const ref = useRef<HTMLDialogElement>(null);
  const titleId = useId();
  const descriptionId = useId();
  useEffect(() => {
    const dialog = ref.current;
    if (!dialog) return;
    if (open && !dialog.open) dialog.showModal();
    if (!open && dialog.open) dialog.close();
  }, [open]);
  return (
    <dialog
      ref={ref}
      className={cx("dsc-dialog", className)}
      aria-labelledby={titleId}
      aria-describedby={description ? descriptionId : undefined}
      onCancel={(event) => {
        event.preventDefault();
        onClose();
      }}
      onClick={(event) => {
        if (event.target === ref.current) onClose();
      }}
    >
      <h2 id={titleId} className="dsc-dialog-title">
        {title}
      </h2>
      {description && (
        <p id={descriptionId} className="dsc-dialog-description">
          {description}
        </p>
      )}
      {children && <div className="dsc-dialog-content">{children}</div>}
      {actions && <div className="dsc-dialog-actions dsc-button-group" data-align="end">{actions}</div>}
      <IconButton className="dsc-dialog-close" variant="ghost" label="Close" icon={<CloseIcon />} onClick={onClose} />
    </dialog>
  );
}

export type ProgressProps = Omit<ComponentPropsWithoutRef<"div">, "children"> & {
  /** From 0 to 1. Leave empty when the length is unknown. */
  value?: number;
  label?: ReactNode;
  /** Show the percentage next to the label. */
  showValue?: boolean;
};

/** Shows how far a task has come, or that it is working, on a hairline track. */
export function Progress({ value, label, showValue = true, className, ...props }: ProgressProps) {
  const indeterminate = value === undefined;
  const clamped = indeterminate ? 0 : Math.min(1, Math.max(0, value));
  const percent = Math.round(clamped * 100);
  return (
    <div
      {...props}
      className={cx("dsc-progress", className)}
      data-indeterminate={flag(indeterminate)}
      role="progressbar"
      aria-valuemin={0}
      aria-valuemax={100}
      aria-valuenow={indeterminate ? undefined : percent}
      aria-label={typeof label === "string" ? label : props["aria-label"]}
    >
      {label && (
        <div className="dsc-progress-header">
          <span>{label}</span>
          {showValue && !indeterminate && <span>{percent}%</span>}
        </div>
      )}
      <div className="dsc-progress-track">
        <div className="dsc-progress-fill" style={indeterminate ? undefined : { width: `${percent}%` }} />
      </div>
    </div>
  );
}
