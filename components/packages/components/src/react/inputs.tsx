import {
  forwardRef,
  useId,
  useRef,
  type ChangeEvent,
  type InputHTMLAttributes,
  type KeyboardEvent,
  type ReactNode,
  type SelectHTMLAttributes,
  type TextareaHTMLAttributes,
} from "react";
import { CheckIcon } from "@hugocxl/icons/react/check";
import { ChevronDownIcon } from "@hugocxl/icons/react/chevron-down";
import { cx, flag, renderIcon } from "./utils.js";

type FieldOwnProps = {
  /** Required. Sentence case, no colon. */
  label: ReactNode;
  /** One muted sentence below the field. */
  help?: ReactNode;
  /** Replaces the help with an error dot and the message. */
  error?: ReactNode;
  className?: string;
};

function useFieldIds(id: string | undefined, help: ReactNode, error: ReactNode) {
  const generated = useId();
  const fieldId = id ?? generated;
  const helpId = help || error ? `${fieldId}-help` : undefined;
  return { fieldId, helpId };
}

function FieldHelp({ id, help, error }: { id?: string; help?: ReactNode; error?: ReactNode }) {
  if (!help && !error) return null;
  return (
    <span id={id} className="dsc-field-help" data-status={error ? "error" : undefined} aria-live={error ? "polite" : undefined}>
      {error || help}
    </span>
  );
}

export type TextFieldProps = FieldOwnProps & {
  /** Grows with its content. */
  multiline?: boolean;
  /** One trailing icon button, such as submit, clear or reveal. */
  action?: ReactNode;
  /** Called with the new value on every change. */
  onValueChange?: (value: string) => void;
} & Omit<InputHTMLAttributes<HTMLInputElement> & TextareaHTMLAttributes<HTMLTextAreaElement>, "className">;

/** Lets people type a value, on a hairline, with its label above and help or an error below. */
export const TextField = forwardRef<HTMLInputElement & HTMLTextAreaElement, TextFieldProps>(function TextField(
  { label, help, error, multiline, action, className, id, disabled, onChange, onValueChange, rows, ...props },
  ref,
) {
  const { fieldId, helpId } = useFieldIds(id, help, error);
  const shared = {
    id: fieldId,
    disabled,
    "aria-invalid": error ? true : undefined,
    "aria-describedby": helpId,
    onChange: (event: ChangeEvent<HTMLInputElement & HTMLTextAreaElement>) => {
      onChange?.(event);
      onValueChange?.(event.target.value);
    },
  };
  return (
    <div className={cx("dsc-field", className)} data-invalid={flag(error)} data-disabled={flag(disabled)}>
      <label className="dsc-field-label" htmlFor={fieldId}>
        {label}
      </label>
      <div className="dsc-field-control">
        {multiline ? (
          <textarea {...(props as TextareaHTMLAttributes<HTMLTextAreaElement>)} {...shared} ref={ref} rows={rows ?? 3} />
        ) : (
          <input {...(props as InputHTMLAttributes<HTMLInputElement>)} {...shared} ref={ref} />
        )}
        {action}
      </div>
      <FieldHelp id={helpId} help={help} error={error} />
    </div>
  );
});

export type SelectOption = { value: string; label: string; disabled?: boolean };

export type SelectProps = FieldOwnProps & {
  options: SelectOption[];
  onValueChange?: (value: string) => void;
  placeholder?: string;
} & Omit<SelectHTMLAttributes<HTMLSelectElement>, "className">;

/** Picks one option from a long list, with the platform's own menu. */
export const Select = forwardRef<HTMLSelectElement, SelectProps>(function Select(
  { label, help, error, options, className, id, disabled, onChange, onValueChange, placeholder, ...props },
  ref,
) {
  const { fieldId, helpId } = useFieldIds(id, help, error);
  return (
    <div className={cx("dsc-field", className)} data-invalid={flag(error)} data-disabled={flag(disabled)}>
      <label className="dsc-field-label" htmlFor={fieldId}>
        {label}
      </label>
      <div className="dsc-field-control">
        <select
          {...props}
          ref={ref}
          id={fieldId}
          disabled={disabled}
          aria-invalid={error ? true : undefined}
          aria-describedby={helpId}
          onChange={(event) => {
            onChange?.(event);
            onValueChange?.(event.target.value);
          }}
        >
          {placeholder !== undefined && (
            <option value="" disabled>
              {placeholder}
            </option>
          )}
          {options.map((option) => (
            <option key={option.value} value={option.value} disabled={option.disabled}>
              {option.label}
            </option>
          ))}
        </select>
        <ChevronDownIcon className="dsc-icon" />
      </div>
      <FieldHelp id={helpId} help={help} error={error} />
    </div>
  );
});

type ChoiceProps = Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "className"> & {
  label: ReactNode;
  description?: ReactNode;
  className?: string;
  onCheckedChange?: (checked: boolean) => void;
};

function Choice({ kind, label, description, className, disabled, onChange, onCheckedChange, id, ...props }: ChoiceProps & { kind: "checkbox" | "switch" }) {
  const generated = useId();
  const inputId = id ?? generated;
  const descriptionId = description ? `${inputId}-description` : undefined;
  return (
    <label className={cx("dsc-choice", className)} data-kind={kind} data-disabled={flag(disabled)} htmlFor={inputId}>
      <input
        {...props}
        id={inputId}
        type="checkbox"
        role={kind === "switch" ? "switch" : undefined}
        disabled={disabled}
        aria-describedby={descriptionId}
        onChange={(event) => {
          onChange?.(event);
          onCheckedChange?.(event.target.checked);
        }}
      />
      {kind === "checkbox" ? (
        <span className="dsc-check-box" aria-hidden="true">
          <CheckIcon className="dsc-icon" />
        </span>
      ) : (
        <span className="dsc-switch-track" aria-hidden="true" />
      )}
      <span className="dsc-choice-text">
        <span>{label}</span>
        {description && (
          <span id={descriptionId} className="dsc-choice-description">
            {description}
          </span>
        )}
      </span>
    </label>
  );
}

export type CheckboxProps = ChoiceProps;
/** Turns one option on or off when the choice is applied later, as in a form. */
export function Checkbox(props: CheckboxProps) {
  return <Choice {...props} kind="checkbox" />;
}

export type SwitchProps = ChoiceProps;
/** Turns a setting on or off immediately. */
export function Switch(props: SwitchProps) {
  return <Choice {...props} kind="switch" />;
}

export type RadioOption = { value: string; label: ReactNode; description?: ReactNode; disabled?: boolean };

export type RadioGroupProps = {
  label: ReactNode;
  options: RadioOption[];
  value?: string;
  defaultValue?: string;
  name?: string;
  disabled?: boolean;
  onValueChange?: (value: string) => void;
  className?: string;
};

/** Picks exactly one option from two to six that are all worth reading. */
export function RadioGroup({ label, options, value, defaultValue, name, disabled, onValueChange, className }: RadioGroupProps) {
  const generated = useId();
  const groupName = name ?? generated;
  return (
    <fieldset className={cx("dsc-radio-group", className)} disabled={disabled}>
      <legend>{label}</legend>
      {options.map((option) => {
        const inputId = `${groupName}-${option.value}`;
        const descriptionId = option.description ? `${inputId}-description` : undefined;
        return (
          <label key={option.value} className="dsc-choice" data-kind="radio" data-disabled={flag(disabled || option.disabled)} htmlFor={inputId}>
            <input
              id={inputId}
              type="radio"
              name={groupName}
              value={option.value}
              disabled={option.disabled}
              aria-describedby={descriptionId}
              {...(value !== undefined ? { checked: value === option.value } : { defaultChecked: defaultValue === option.value })}
              onChange={(event) => event.target.checked && onValueChange?.(option.value)}
            />
            <span className="dsc-check-box" aria-hidden="true" />
            <span className="dsc-choice-text">
              <span>{option.label}</span>
              {option.description && (
                <span id={descriptionId} className="dsc-choice-description">
                  {option.description}
                </span>
              )}
            </span>
          </label>
        );
      })}
    </fieldset>
  );
}

export type SegmentedOption = { value: string; label: ReactNode; icon?: ReactNode; disabled?: boolean };

export type SegmentedControlProps = {
  /** Required: names the control for assistive technology. */
  label: string;
  options: SegmentedOption[];
  value: string;
  onValueChange: (value: string) => void;
  className?: string;
};

/** Switches between two to five views or modes, in a hairline pill. */
export function SegmentedControl({ label, options, value, onValueChange, className }: SegmentedControlProps) {
  const refs = useRef<Array<HTMLButtonElement | null>>([]);
  const enabled = options.filter((option) => !option.disabled);
  function onKeyDown(event: KeyboardEvent<HTMLDivElement>) {
    const step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
    if (!step) return;
    event.preventDefault();
    const current = enabled.findIndex((option) => option.value === value);
    const next = enabled[(current + step + enabled.length) % enabled.length];
    onValueChange(next.value);
    refs.current[options.indexOf(next)]?.focus();
  }
  return (
    <div className={cx("dsc-segmented", className)} role="radiogroup" aria-label={label} onKeyDown={onKeyDown}>
      {options.map((option, index) => {
        const selected = option.value === value;
        return (
          <button
            key={option.value}
            ref={(element) => {
              refs.current[index] = element;
            }}
            type="button"
            role="radio"
            aria-checked={selected}
            tabIndex={selected ? 0 : -1}
            disabled={option.disabled}
            onClick={() => onValueChange(option.value)}
          >
            {renderIcon(option.icon)}
            {option.label}
          </button>
        );
      })}
    </div>
  );
}
