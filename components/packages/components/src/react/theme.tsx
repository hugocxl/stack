import { useCallback, useSyncExternalStore } from "react";
import { ContrastIcon } from "@hugocxl/icons/react/contrast";
import { IconButton, type IconButtonProps } from "./actions.js";

export type Appearance = "light" | "dark";
const STORAGE_KEY = "ds-theme";

/**
 * A script for the document head that applies the saved or system appearance before the
 * first paint. It matches the design system's theme.js, so both share the stored choice.
 */
export const themeScript = `(()=>{try{var s=localStorage.getItem("${STORAGE_KEY}");var m=matchMedia("(prefers-color-scheme: dark)");var a=function(){document.documentElement.dataset.theme=localStorage.getItem("${STORAGE_KEY}")||(m.matches?"dark":"light")};a();m.addEventListener("change",a)}catch(e){}})();`;

function systemAppearance(): Appearance {
  return typeof matchMedia !== "undefined" && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function readAppearance(): Appearance {
  if (typeof document === "undefined") return "light";
  const current = document.documentElement.dataset.theme;
  return current === "dark" || current === "light" ? current : systemAppearance();
}

function subscribe(onChange: () => void): () => void {
  const observer = new MutationObserver(onChange);
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  const media = matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", onChange);
  return () => {
    observer.disconnect();
    media.removeEventListener("change", onChange);
  };
}

/** The current appearance and a setter that remembers the choice. */
export function useTheme(): [Appearance, (appearance: Appearance | "system") => void] {
  const appearance = useSyncExternalStore(subscribe, readAppearance, () => "light" as Appearance);
  const setAppearance = useCallback((next: Appearance | "system") => {
    try {
      if (next === "system") localStorage.removeItem(STORAGE_KEY);
      else localStorage.setItem(STORAGE_KEY, next);
    } catch {
      // Storage can be unavailable; the choice then lasts for this page only.
    }
    document.documentElement.dataset.theme = next === "system" ? systemAppearance() : next;
  }, []);
  return [appearance, setAppearance];
}

export type ThemeToggleProps = Omit<IconButtonProps, "icon" | "label"> & { label?: string };

/** Switches between light and dark. Always the contrast icon. */
export function ThemeToggle({ label = "Switch theme", onClick, ...props }: ThemeToggleProps) {
  const [appearance, setAppearance] = useTheme();
  return (
    <IconButton
      {...props}
      label={label}
      icon={<ContrastIcon />}
      onClick={(event) => {
        onClick?.(event);
        if (!event.defaultPrevented) setAppearance(appearance === "dark" ? "light" : "dark");
      }}
    />
  );
}
