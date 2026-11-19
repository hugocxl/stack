// Server-render every React component and check the markup the recipes ask for.
import assert from "node:assert/strict";
import test from "node:test";
import { createElement as h } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import * as C from "@hugocxl/components/react";

const html = (element) => renderToStaticMarkup(element);

test("button variants, icons and links", () => {
  assert.match(html(h(C.Button, null, "Go")), /<button[^>]*class="dsc-button"[^>]*data-variant="primary"[^>]*type="button"|type="button"[^>]*class="dsc-button"/);
  assert.match(html(h(C.Button, { variant: "ghost" }, "Go")), /data-variant="ghost"/);
  const link = html(h(C.Button, { href: "/docs", target: "_blank" }, "Docs"));
  assert.match(link, /^<a /);
  assert.match(link, /rel="noopener noreferrer"/);
  assert.match(html(h(C.Button, { icon: h("svg", { className: "x" }) }, "Go")), /class="dsc-icon x"/);
});

test("icon buttons always have a label", () => {
  const markup = html(h(C.IconButton, { label: "Close", icon: h("svg") }));
  assert.match(markup, /aria-label="Close"/);
  assert.match(markup, /title="Close"/);
});

test("text fields tie the label, help and error to the input", () => {
  const markup = html(h(C.TextField, { id: "email", label: "Email", error: "Add the rest" }));
  assert.match(markup, /<label class="dsc-field-label" for="email">Email<\/label>/);
  assert.match(markup, /aria-invalid="true"/);
  assert.match(markup, /aria-describedby="email-help"/);
  assert.match(markup, /id="email-help"[^>]*data-status="error"/);
  assert.match(html(h(C.TextField, { label: "Message", multiline: true })), /<textarea/);
});

test("checkbox, switch and radio use native inputs", () => {
  assert.match(html(h(C.Checkbox, { label: "Notes" })), /type="checkbox"/);
  assert.match(html(h(C.Switch, { label: "Sounds" })), /role="switch"/);
  const radios = html(h(C.RadioGroup, { label: "Plan", value: "b", onValueChange() {}, options: [{ value: "a", label: "A" }, { value: "b", label: "B" }] }));
  assert.equal((radios.match(/type="radio"/g) ?? []).length, 2);
  assert.match(radios, /<legend>Plan<\/legend>/);
  assert.match(radios, /checked="" value="b"/);
});

test("segmented control is a radio group with one tab stop", () => {
  const markup = html(h(C.SegmentedControl, { label: "Period", value: "w", onValueChange() {}, options: [{ value: "d", label: "Day" }, { value: "w", label: "Week" }] }));
  assert.match(markup, /role="radiogroup" aria-label="Period"/);
  assert.equal((markup.match(/tabindex="0"/g) ?? []).length, 1);
  assert.match(markup, /aria-checked="true" tabindex="0"[^>]*>Week/);
});

test("status and notice carry their tone and role", () => {
  assert.match(html(h(C.Status, { tone: "success" }, "Live")), /data-tone="success"/);
  assert.match(html(h(C.Notice, { tone: "error", title: "Failed" })), /role="alert"/);
  assert.match(html(h(C.Notice, { tone: "info", title: "Heads up" })), /role="status"/);
});

test("progress exposes its value", () => {
  assert.match(html(h(C.Progress, { value: 0.5, label: "Upload" })), /aria-valuenow="50"/);
  assert.doesNotMatch(html(h(C.Progress, { label: "Working" })), /aria-valuenow/);
});

test("content components", () => {
  assert.match(html(h(C.Title, { byline: "Team" }, "Name")), /<hgroup class="dsc-title"><h1>Name<\/h1><p>Team<\/p><\/hgroup>/);
  assert.match(html(h(C.Statement, { accent: "every day." }, "Ship")), /<span class="dsc-accent">every day.<\/span>/);
  assert.match(html(h(C.Section, { heading: "About" }, "x")), /<section class="dsc-section"><h2>About<\/h2>/);
  const table = html(h(C.Table, { columns: [{ label: "A" }, { label: "B" }], rows: [["r", "1"]] }));
  assert.match(table, /<th scope="row"[^>]*>r<\/th>/);
  const list = html(h(C.List, { items: [{ title: "Billing", href: "/billing" }] }));
  assert.match(list, /<a class="dsc-list-action" href="\/billing">/);
  assert.match(html(h(C.FigureGrid, { items: [{ media: h("svg"), title: "A" }, { media: h("svg"), title: "B" }] })), /--dsc-cols:2/);
});

test("page shell", () => {
  const markup = html(
    h(C.Page, { masthead: h(C.Masthead, { wordmark: "Fieldwork", links: [{ label: "Docs", href: "/docs" }] }), footer: h(C.Footer, { links: [{ label: "Docs", href: "/docs" }] }) }, "content"),
  );
  assert.match(markup, /class="dsc-page" data-layout="plain"/);
  assert.match(markup, /<main><article class="dsc-column dsc-opening">content<\/article><\/main>/);
  assert.match(markup, /aria-label="Switch theme"/);
});
