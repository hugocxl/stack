import {
  useCallback,
  useId,
  useRef,
  useState,
  type ComponentPropsWithoutRef,
  type KeyboardEvent,
  type PointerEvent,
  type ReactNode,
  type WheelEvent,
} from "react";
import type { StatusTone } from "./feedback.js";
import { cx, flag } from "./utils.js";

// ─── Shared range behavior ──────────────────────────────────────────────

type RangeProps = {
  value?: number;
  defaultValue?: number;
  onValueChange?: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
  disabled?: boolean;
};

const clamp = (value: number, min: number, max: number) => Math.min(max, Math.max(min, value));
const snap = (value: number, min: number, step: number) => {
  const snapped = Math.round((value - min) / step) * step + min;
  const decimals = (String(step).split(".")[1] ?? "").length;
  return Number(snapped.toFixed(decimals));
};

/** Controlled or uncontrolled value, clamped and snapped, with the keys every range control shares. */
function useRange({ value, defaultValue, onValueChange, min = 0, max = 100, step = 1, disabled }: RangeProps) {
  const [inner, setInner] = useState(defaultValue ?? min);
  const current = clamp(value ?? inner, min, max);
  const set = useCallback(
    (next: number) => {
      const settled = clamp(snap(next, min, step), min, max);
      if (value === undefined) setInner(settled);
      if (settled !== current) onValueChange?.(settled);
    },
    [value, min, max, step, current, onValueChange],
  );
  const onKeyDown = (event: KeyboardEvent) => {
    if (disabled) return;
    const big = Math.max(step, (max - min) / 10);
    const moves: Record<string, number> = {
      ArrowUp: current + step,
      ArrowRight: current + step,
      ArrowDown: current - step,
      ArrowLeft: current - step,
      PageUp: current + big,
      PageDown: current - big,
      Home: min,
      End: max,
    };
    if (!(event.key in moves)) return;
    event.preventDefault();
    set(moves[event.key]);
  };
  const fraction = max === min ? 0 : (current - min) / (max - min);
  return { current, set, onKeyDown, fraction, min, max, step };
}

type ReadingProps = {
  label?: ReactNode;
  /** How the reading is written. Defaults to the number. */
  format?: (value: number) => string;
  /** Hide the reading next to the label. */
  hideValue?: boolean;
};

// ─── Meter ──────────────────────────────────────────────────────────────

export type MeterProps = Omit<ComponentPropsWithoutRef<"div">, "children"> & {
  /** From 0 to 1. */
  value: number;
  label?: ReactNode;
  /** How the reading is written. Defaults to a percentage. */
  format?: (value: number) => string;
  segments?: number;
  variant?: "bars" | "dots";
  tone?: Exclude<StatusTone, "neutral">;
};

/** A level read at a glance: segments that light up to the value. */
export function Meter({ value, label, format, segments = 24, variant = "bars", tone = "accent", className, ...props }: MeterProps) {
  const level = clamp(value, 0, 1);
  const lit = Math.round(level * segments);
  const reading = format ? format(level) : `${Math.round(level * 100)}%`;
  return (
    <div
      {...props}
      className={cx("dsc-meter", className)}
      data-variant={variant}
      data-tone={tone}
      role="meter"
      aria-valuemin={0}
      aria-valuemax={100}
      aria-valuenow={Math.round(level * 100)}
      aria-valuetext={reading}
      aria-label={typeof label === "string" ? label : props["aria-label"]}
    >
      {label !== undefined && (
        <div className="dsc-instrument-header">
          <span>{label}</span>
          <span className="dsc-instrument-reading">{reading}</span>
        </div>
      )}
      <div className="dsc-meter-segments" aria-hidden="true">
        {Array.from({ length: segments }, (_, index) => (
          <span key={index} data-lit={flag(index < lit)} />
        ))}
      </div>
    </div>
  );
}

// ─── Knob ───────────────────────────────────────────────────────────────

const knobSizes = { small: 48, medium: 64, large: 88 } as const;

export type KnobProps = RangeProps &
  ReadingProps &
  Omit<ComponentPropsWithoutRef<"div">, "defaultValue" | "onChange" | "children"> & {
    size?: keyof typeof knobSizes;
  };

/** A flat dial that sets a value by dragging up or down, with a ring of ticks that fills up to it. */
export function Knob({ value, defaultValue, onValueChange, min = 0, max = 100, step = 1, disabled, label, format, hideValue, size = "medium", className, ...props }: KnobProps) {
  const range = useRange({ value, defaultValue, onValueChange, min, max, step, disabled });
  const drag = useRef<{ x: number; y: number; start: number } | null>(null);
  const [dragging, setDragging] = useState(false);
  const labelId = useId();
  const disc = knobSizes[size];
  const pad = 14;
  const box = disc + pad * 2;
  const center = box / 2;
  const ticks = size === "small" ? 21 : size === "large" ? 37 : 29;
  const angle = -135 + range.fraction * 270;
  const point = (degrees: number, radius: number) => {
    const radians = ((degrees - 90) * Math.PI) / 180;
    return [center + radius * Math.cos(radians), center + radius * Math.sin(radians)];
  };
  const [dotX, dotY] = point(angle, disc / 2 - (size === "small" ? 8 : 11));
  const reading = format ? format(range.current) : String(range.current);

  function onPointerDown(event: PointerEvent<HTMLDivElement>) {
    if (disabled || event.button !== 0) return;
    event.currentTarget.setPointerCapture(event.pointerId);
    drag.current = { x: event.clientX, y: event.clientY, start: range.current };
    setDragging(true);
  }
  function onPointerMove(event: PointerEvent<HTMLDivElement>) {
    if (!drag.current) return;
    const travel = event.clientX - drag.current.x - (event.clientY - drag.current.y);
    const perPixel = (max - min) / (event.shiftKey ? 2000 : 200);
    range.set(drag.current.start + travel * perPixel);
  }
  function onPointerUp() {
    drag.current = null;
    setDragging(false);
  }
  function onWheel(event: WheelEvent<HTMLDivElement>) {
    if (disabled || document.activeElement !== event.currentTarget) return;
    range.set(range.current - Math.sign(event.deltaY) * step);
  }

  return (
    <div className={cx("dsc-knob", className)} data-size={size} data-disabled={flag(disabled)} data-dragging={flag(dragging)}>
      <div
        {...props}
        className="dsc-knob-dial"
        role="slider"
        tabIndex={disabled ? -1 : 0}
        aria-labelledby={label !== undefined ? labelId : undefined}
        aria-valuemin={min}
        aria-valuemax={max}
        aria-valuenow={range.current}
        aria-valuetext={reading}
        aria-disabled={disabled || undefined}
        onKeyDown={range.onKeyDown}
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onPointerCancel={onPointerUp}
        onWheel={onWheel}
        onDoubleClick={() => !disabled && defaultValue !== undefined && range.set(defaultValue)}
      >
        <svg width={box} height={box} viewBox={`0 0 ${box} ${box}`} aria-hidden="true">
          {Array.from({ length: ticks }, (_, index) => {
            const tickAngle = -135 + (index / (ticks - 1)) * 270;
            const major = index % 4 === 0 || index === ticks - 1;
            const [x1, y1] = point(tickAngle, disc / 2 + 5);
            const [x2, y2] = point(tickAngle, disc / 2 + (major ? 12 : 9));
            return <line key={index} x1={x1} y1={y1} x2={x2} y2={y2} className="dsc-knob-tick" data-lit={flag(tickAngle <= angle + 0.01)} />;
          })}
          <circle cx={center} cy={center} r={disc / 2 - 0.5} className="dsc-knob-disc" />
          <circle cx={dotX} cy={dotY} r={size === "small" ? 2.5 : 3} className="dsc-knob-dot" />
        </svg>
      </div>
      {!hideValue && <span className="dsc-knob-reading">{reading}</span>}
      {label !== undefined && (
        <span id={labelId} className="dsc-knob-label">
          {label}
        </span>
      )}
    </div>
  );
}

// ─── Slider ─────────────────────────────────────────────────────────────

export type SliderMark = { value: number; label: ReactNode };

export type SliderProps = RangeProps &
  ReadingProps &
  Omit<ComponentPropsWithoutRef<"div">, "defaultValue" | "onChange" | "children"> & {
    /** Ticks on the ruler. 0 hides the ruler. */
    ticks?: number;
    /** Every how many ticks one is major. Defaults to 5. */
    majorEvery?: number;
    /** Numbers under chosen ticks. */
    marks?: SliderMark[];
    /** Fill from the middle, for ranges around zero. */
    centered?: boolean;
  };

/** A fader on a ruler: a hairline track filled in ink up to an accent pointer. */
export function Slider({ value, defaultValue, onValueChange, min = 0, max = 100, step = 1, disabled, label, format, hideValue, ticks = 21, majorEvery = 5, marks = [], centered, className, ...props }: SliderProps) {
  const range = useRange({ value, defaultValue, onValueChange, min, max, step, disabled });
  const track = useRef<HTMLDivElement>(null);
  const [dragging, setDragging] = useState(false);
  const labelId = useId();
  const reading = format ? format(range.current) : String(range.current);
  const origin = centered ? 0.5 : 0;
  const position = (to: number) => `${to * 100}%`;
  const fromPointer = (clientX: number) => {
    const rect = track.current!.getBoundingClientRect();
    range.set(min + clamp((clientX - rect.left) / rect.width, 0, 1) * (max - min));
  };
  return (
    <div className={cx("dsc-slider", className)} data-disabled={flag(disabled)} data-dragging={flag(dragging)}>
      {(label !== undefined || !hideValue) && (
        <div className="dsc-instrument-header">
          <span id={labelId}>{label}</span>
          {!hideValue && <span className="dsc-instrument-reading">{reading}</span>}
        </div>
      )}
      <div
        {...props}
        ref={track}
        className="dsc-slider-track"
        role="slider"
        tabIndex={disabled ? -1 : 0}
        aria-labelledby={label !== undefined ? labelId : undefined}
        aria-valuemin={min}
        aria-valuemax={max}
        aria-valuenow={range.current}
        aria-valuetext={reading}
        aria-disabled={disabled || undefined}
        onKeyDown={range.onKeyDown}
        onPointerDown={(event) => {
          if (disabled || event.button !== 0) return;
          event.currentTarget.setPointerCapture(event.pointerId);
          setDragging(true);
          fromPointer(event.clientX);
        }}
        onPointerMove={(event) => dragging && fromPointer(event.clientX)}
        onPointerUp={() => setDragging(false)}
        onPointerCancel={() => setDragging(false)}
        onDoubleClick={() => !disabled && defaultValue !== undefined && range.set(defaultValue)}
      >
        <span className="dsc-slider-rail" />
        <span
          className="dsc-slider-fill"
          style={{ left: position(Math.min(origin, range.fraction)), width: position(Math.abs(range.fraction - origin)) }}
        />
        <span className="dsc-slider-pointer" style={{ left: position(range.fraction) }} />
      </div>
      {ticks > 1 && (
        <div className="dsc-slider-ruler" aria-hidden="true">
          {Array.from({ length: ticks }, (_, index) => {
            const at = index / (ticks - 1);
            const major = index % majorEvery === 0 || index === ticks - 1;
            return <span key={index} className="dsc-slider-tick" data-major={flag(major)} data-lit={flag(at <= range.fraction + 1e-6)} style={{ left: position(at) }} />;
          })}
          {marks.map((mark) => (
            <span key={mark.value} className="dsc-slider-mark" style={{ left: position((mark.value - min) / (max - min)) }}>
              {mark.label}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}

// ─── Slide switch ───────────────────────────────────────────────────────

export type SlideSwitchOption = { value: string; label: ReactNode };

export type SlideSwitchProps = {
  label?: ReactNode;
  /** Two to four positions. */
  options: SlideSwitchOption[];
  value?: string;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
  orientation?: "vertical" | "horizontal";
  disabled?: boolean;
  className?: string;
};

/** A hardware switch with two to four labelled positions. */
export function SlideSwitch({ label, options, value, defaultValue, onValueChange, orientation = "vertical", disabled, className }: SlideSwitchProps) {
  const [inner, setInner] = useState(defaultValue ?? options[0]?.value);
  const current = value ?? inner;
  const index = Math.max(0, options.findIndex((option) => option.value === current));
  const refs = useRef<Array<HTMLButtonElement | null>>([]);
  const labelId = useId();
  const pick = (next: number) => {
    const option = options[clamp(next, 0, options.length - 1)];
    if (value === undefined) setInner(option.value);
    if (option.value !== current) onValueChange?.(option.value);
    refs.current[options.indexOf(option)]?.focus();
  };
  const onKeyDown = (event: KeyboardEvent) => {
    const forward = orientation === "vertical" ? ["ArrowDown", "ArrowRight"] : ["ArrowRight", "ArrowDown"];
    const back = orientation === "vertical" ? ["ArrowUp", "ArrowLeft"] : ["ArrowLeft", "ArrowUp"];
    if (forward.includes(event.key)) pick(index + 1);
    else if (back.includes(event.key)) pick(index - 1);
    else return;
    event.preventDefault();
  };
  return (
    <div className={cx("dsc-slide-switch", className)} data-orientation={orientation} data-disabled={flag(disabled)}>
      {label !== undefined && (
        <span id={labelId} className="dsc-slide-switch-label">
          {label}
        </span>
      )}
      <div
        className="dsc-slide-switch-body"
        role="radiogroup"
        aria-labelledby={label !== undefined ? labelId : undefined}
        aria-orientation={orientation}
        onKeyDown={onKeyDown}
        style={{ ["--dsc-stops" as string]: options.length, ["--dsc-index" as string]: index }}
      >
        <span className="dsc-slide-switch-track" aria-hidden="true">
          <span className="dsc-slide-switch-thumb" />
        </span>
        {options.map((option, position) => (
          <button
            key={option.value}
            ref={(element) => {
              refs.current[position] = element;
            }}
            type="button"
            role="radio"
            aria-checked={position === index}
            tabIndex={position === index ? 0 : -1}
            disabled={disabled}
            className="dsc-slide-switch-stop"
            onClick={() => pick(position)}
          >
            <span className="dsc-slide-switch-dash" aria-hidden="true" />
            {option.label}
          </button>
        ))}
      </div>
    </div>
  );
}

// ─── Readout ────────────────────────────────────────────────────────────

export type ReadoutProps = Omit<ComponentPropsWithoutRef<"div">, "children"> & {
  label: ReactNode;
  value: ReactNode;
  unit?: ReactNode;
  /** In faint, for a value that is off or not in use. */
  dim?: boolean;
  /** An accent dot after the label, for the value being set now. */
  live?: boolean;
  /** Makes the readout a button, to open what changes it. */
  onPress?: () => void;
  selected?: boolean;
};

/** One setting read at a distance: a mono label over a large value. */
export function Readout({ label, value, unit, dim, live, onPress, selected, className, ...props }: ReadoutProps) {
  const content = (
    <>
      <span className="dsc-readout-label">
        {label}
        {live && <span className="dsc-readout-live" aria-label="(live)" />}
      </span>
      <span className="dsc-readout-value">
        {value}
        {unit !== undefined && <span className="dsc-readout-unit">{unit}</span>}
      </span>
    </>
  );
  const shared = { className: cx("dsc-readout", className), "data-dim": flag(dim), "data-selected": flag(selected) };
  if (onPress) {
    return (
      <button type="button" {...(props as ComponentPropsWithoutRef<"button">)} {...shared} onClick={onPress} aria-pressed={selected}>
        {content}
      </button>
    );
  }
  return (
    <div {...props} {...shared} role="group">
      {content}
    </div>
  );
}

export type ReadoutGridProps = ComponentPropsWithoutRef<"div"> & { columns?: number };

/** Readouts and controls in hairline cells, like an instrument panel. */
export function ReadoutGrid({ columns = 3, className, style, ...props }: ReadoutGridProps) {
  return <div {...props} className={cx("dsc-readout-grid", className)} style={{ ["--dsc-cols" as string]: columns, ...style }} />;
}
