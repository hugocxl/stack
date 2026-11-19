import "@hugocxl/components/styles.css";
import "./site.css";
import { useEffect, useState, type ReactNode } from "react";
import { createRoot } from "react-dom/client";
import {
  Button,
  ButtonGroup,
  Checkbox,
  CodeBlock,
  Footer,
  List,
  Masthead,
  Meta,
  Muted,
  Notice,
  Page,
  Progress,
  Section,
  SegmentedControl,
  Select,
  Statement,
  Status,
  Switch,
  Table,
  Text,
  TextField,
  Title,
} from "@hugocxl/components/react";
import recipes from "@hugocxl/components/recipes.json";
import { ArrowLeftIcon } from "@hugocxl/icons/react/arrow-left";
import { ArrowRightIcon } from "@hugocxl/icons/react/arrow-right";
import { examples } from "./examples.js";

type Recipe = {
  name: string;
  title: string;
  group: string;
  summary: string;
  use: string[];
  anatomy: string[];
  options: { name: string; values: unknown[]; default: unknown; description: string }[];
  states: string[];
  tokens: string[];
  rules: string[];
  accessibility: string[];
  platforms: { react: string | null; swift: string | null };
};

const all = recipes as Recipe[];
const groups: { id: string; title: string; text: string }[] = [
  { id: "foundations", title: "Foundations", text: "The theme and the type every component is set in." },
  { id: "actions", title: "Actions", text: "What people click to do something or go somewhere." },
  { id: "inputs", title: "Inputs", text: "What people type into, pick and switch." },
  { id: "instruments", title: "Instruments", text: "Meters, knobs, faders and readouts for values people tune and watch." },
  { id: "feedback", title: "Feedback", text: "What the interface says back." },
  { id: "content", title: "Content", text: "Headings, text, code, lists and figures." },
  { id: "layout", title: "Layout", text: "The page or screen everything sits in." },
];
const ordered = groups.flatMap((group) => all.filter((recipe) => recipe.group === group.id));
declare const SWIFT_CAPTURES: string[];

function useRoute() {
  const read = () => window.location.hash.replace(/^#\/?/, "");
  const [route, setRoute] = useState(read);
  useEffect(() => {
    const onChange = () => {
      setRoute(read());
      window.scrollTo(0, 0);
    };
    window.addEventListener("hashchange", onChange);
    return () => window.removeEventListener("hashchange", onChange);
  }, []);
  return route;
}

// Cards that need the room of two columns; the rest fill one.
const wideCards = new Set(["meter", "slider", "readout", "list", "table", "figure", "figure-grid", "code-block", "masthead", "footer", "notice", "progress", "knob"]);

function Card({ recipe, number }: { recipe: Recipe; number: number }) {
  const entry = examples[recipe.name];
  const first = entry?.examples[0];
  const wide = wideCards.has(recipe.name);
  const fill = !entry?.card && first?.fill;
  return (
    <section className="site-card" data-span={wide ? 2 : undefined} aria-labelledby={`card-${recipe.name}`}>
      <a className="site-card-head" href={`#/${recipe.name}`} id={`card-${recipe.name}`}>
        <span className="site-card-number">{String(number).padStart(2, "0")}</span>
        {recipe.title}
      </a>
      <div className="site-card-body" data-fill={fill ? "" : undefined}>
        {entry?.card ? entry.card() : first?.render()}
      </div>
    </section>
  );
}

function Home() {
  return (
    <>
      <Statement accent="every platform.">One recipe per component, built for</Statement>
      <Meta items={[<Status key="s">Preview</Status>, `${all.length} components`, "React · Swift"]} />
      <Section>
        <p>
          Each component starts as a recipe: what it is for, its parts, its options and the rules it keeps. <Muted>React and Swift build the same recipe with the design system's tokens. Open any card for its examples, code and recipe.</Muted>
        </p>
      </Section>
      <div className="site-grid dsc-wide">
        {ordered.map((recipe, index) => (
          <Card key={recipe.name} recipe={recipe} number={index + 1} />
        ))}
      </div>
      <Section heading="Install" id="install">
        <CodeBlock label="React" code={'pnpm add @hugocxl/components\n\nimport "@hugocxl/components/styles.css";\nimport { Button } from "@hugocxl/components/react";'} />
        <CodeBlock label="Swift Package Manager" code={'.package(url: "https://github.com/hugocxl/stack", branch: "main")\n\nimport Components\nContentView().dsTheme()'} />
      </Section>
      <Section heading="See them together" id="examples">
        <p>Screens built only from these components, to judge them as a whole.</p>
        <ButtonGroup>
          <Button href="#/examples" icon={<ArrowRightIcon />}>
            Open the examples
          </Button>
        </ButtonGroup>
      </Section>
    </>
  );
}

const show = (value: unknown) => (value === null || value === undefined ? "—" : String(value));

function ComponentPage({ recipe }: { recipe: Recipe }) {
  const entry = examples[recipe.name];
  const index = ordered.indexOf(recipe);
  const previous = ordered[index - 1];
  const next = ordered[index + 1];
  const captures = ["light", "dark"].map((scheme) => `swift/${recipe.name}-${scheme}.png`).filter((path) => SWIFT_CAPTURES.includes(path));
  return (
    <>
      <Title byline={groups.find((group) => group.id === recipe.group)?.title}>{recipe.title}</Title>
      <Meta
        items={[
          <Status key="r" tone={recipe.platforms.react ? "success" : "neutral"}>
            {recipe.platforms.react ? `React · ${recipe.platforms.react}` : "No React"}
          </Status>,
          <Status key="s" tone={recipe.platforms.swift ? "success" : "neutral"}>
            {recipe.platforms.swift ? `Swift · ${recipe.platforms.swift}` : "No Swift"}
          </Status>,
        ]}
      />
      <Section>
        <p>{recipe.summary}</p>
        {recipe.use.length > 0 && (
          <ul>
            {recipe.use.map((line) => (
              <li key={line}>{line}</li>
            ))}
          </ul>
        )}
      </Section>
      {entry?.examples.map((example) => (
        <Section key={example.title} heading={example.title}>
          <div className="site-stage" data-fill={example.fill ? "" : undefined}>
            {example.render()}
          </div>
          <CodeBlock label="React" code={example.react} />
        </Section>
      ))}
      {recipe.platforms.swift && entry?.swift && (
        <Section heading="Swift" id="swift">
          <p>
            <code>{recipe.platforms.swift}</code> in the <code>Components</code> library. <Muted>Rendered by SwiftUI from the package's gallery.</Muted>
          </p>
          {captures.length > 0 && (
            <div className="site-captures">
              {captures.map((path) => (
                <figure key={path}>
                  <img src={path} alt={`${recipe.title} in SwiftUI, ${path.includes("dark") ? "dark" : "light"}`} loading="lazy" />
                  <figcaption>{path.includes("dark") ? "Dark" : "Light"}</figcaption>
                </figure>
              ))}
            </div>
          )}
          <CodeBlock label="Swift" code={entry.swift} />
        </Section>
      )}
      <Section heading="Recipe" id="recipe">
        <p>
          Every implementation keeps this. <Muted>From <code>recipes/{recipe.name}.json</code>.</Muted>
        </p>
        <List
          items={[
            { label: "Anatomy", title: recipe.anatomy.join(" · ") },
            ...(recipe.states.length ? [{ label: "States", title: recipe.states.join(" · ") }] : []),
            ...recipe.rules.map((rule, i) => ({ label: i === 0 ? "Rules" : "", title: rule })),
            ...recipe.accessibility.map((line, i) => ({ label: i === 0 ? "Access" : "", title: line })),
          ]}
          density="compact"
        />
        {recipe.options.length > 0 && (
          <Table
            caption="Options"
            columns={[{ label: "Option" }, { label: "Values" }, { label: "Default" }]}
            rows={recipe.options.map((option) => [
              <span key="n">
                <code>{option.name}</code>
                <br />
                <Muted>{option.description}</Muted>
              </span>,
              option.values.map(show).join(", "),
              show(option.default),
            ])}
          />
        )}
        <ul className="site-tokens" aria-label="Tokens">
          {recipe.tokens.map((token) => (
            <li key={token}>
              <code>--ds-{token}</code>
            </li>
          ))}
        </ul>
      </Section>
      <nav className="site-pager" aria-label="Components">
        {previous ? (
          <Button variant="secondary" href={`#/${previous.name}`} icon={<ArrowLeftIcon />}>
            {previous.title}
          </Button>
        ) : (
          <span />
        )}
        {next && (
          <Button variant="secondary" href={`#/${next.name}`}>
            {next.title}
            <ArrowRightIcon className="dsc-icon" />
          </Button>
        )}
      </nav>
    </>
  );
}

function SettingsScreen() {
  const [sounds, setSounds] = useState(true);
  const [period, setPeriod] = useState("week");
  const [saved, setSaved] = useState(false);
  return (
    <div className="site-demo-screen">
      <Title byline="Fieldwork">Settings</Title>
      {saved && (
        <Notice tone="success" title="Settings saved." onDismiss={() => setSaved(false)}>
          They apply on every device you use.
        </Notice>
      )}
      <div className="dsc-stack">
        <TextField label="Display name" defaultValue="Ana Ruiz" />
        <TextField label="Email" type="email" defaultValue="ana@" error="Add the rest of the address, such as ana@example.com." />
        <Select
          label="Region"
          defaultValue="eu"
          help="Where your data is stored."
          options={[
            { value: "eu", label: "Europe" },
            { value: "us", label: "United States" },
          ]}
        />
      </div>
      <div>
        <Switch label="Sounds" description="Play a sound when a task finishes." checked={sounds} onCheckedChange={setSounds} />
        <Checkbox label="Send me release notes" defaultChecked />
      </div>
      <div className="site-row">
        <Text variant="label">Digest</Text>
        <SegmentedControl
          label="Digest"
          value={period}
          onValueChange={setPeriod}
          options={[
            { value: "day", label: "Daily" },
            { value: "week", label: "Weekly" },
            { value: "never", label: "Never" },
          ]}
        />
      </div>
      <ButtonGroup align="end">
        <Button variant="secondary">Cancel</Button>
        <Button onClick={() => setSaved(true)}>Save changes</Button>
      </ButtonGroup>
    </div>
  );
}

function StatusScreen() {
  return (
    <div className="site-demo-screen">
      <Title byline="Fieldwork">System status</Title>
      <Status tone="success" mark="icon" appearance="text">
        All systems operational
      </Status>
      <List
        density="compact"
        items={[
          { title: "API", trailing: <Status tone="success">Operational</Status> },
          { title: "Dashboard", trailing: <Status tone="success">Operational</Status> },
          { title: "Webhooks", trailing: <Status tone="warning">Degraded</Status> },
          { title: "Exports", trailing: <Status tone="info">Maintenance</Status> },
        ]}
      />
      <Progress value={0.82} label="Webhook backlog cleared" />
      <Table
        caption="Incidents"
        columns={[{ label: "Date" }, { label: "Incident" }, { label: "Duration", align: "end" }]}
        rows={[
          ["12 Nov", "Slow webhook delivery", "38 min"],
          ["3 Nov", "Exports paused for maintenance", "1 h 10 min"],
        ]}
      />
    </div>
  );
}

function ExamplesPage() {
  return (
    <>
      <Title byline="Built only from the components">Examples</Title>
      <Section>
        <p>
          Two screens a project might need, to judge the components together. <Muted>Switch the theme from the masthead to see both appearances.</Muted>
        </p>
      </Section>
      <Section heading="A settings screen">
        <SettingsScreen />
      </Section>
      <Section heading="A status page">
        <StatusScreen />
      </Section>
    </>
  );
}

function NotFound({ route }: { route: string }) {
  return (
    <>
      <Title byline="Not found">No component called “{route}”</Title>
      <Section>
        <p>
          Go back to <a href="#/">every component</a>.
        </p>
      </Section>
    </>
  );
}

function App() {
  const route = useRoute();
  const recipe = all.find((item) => item.name === route);
  let content: ReactNode;
  if (route === "") content = <Home />;
  else if (route === "examples") content = <ExamplesPage />;
  else if (recipe) content = <ComponentPage recipe={recipe} />;
  else content = <NotFound route={route} />;
  useEffect(() => {
    document.title = recipe ? `${recipe.title} · @hugocxl/components` : route === "examples" ? "Examples · @hugocxl/components" : "@hugocxl/components";
  }, [route, recipe]);
  return (
    <Page
      masthead={
        <Masthead
          wordmark="@hugocxl/components"
          href="#/"
          nav={{
            label: "The @hugocxl stack",
            links: [
              { label: "Stack", href: "../" },
              { label: "Design system", href: "../design-system/" },
              { label: "Components", href: "./", current: true },
              { label: "Icons", href: "../icons/" },
              { label: "Vectors", href: "../vectors/" },
              { label: "Sounds", href: "../sounds/" },
            ],
          }}
          links={[
            { label: "Components", href: "#/", current: route === "" },
            { label: "Examples", href: "#/examples", current: route === "examples" },
            { label: "GitHub", href: "https://github.com/hugocxl/stack/tree/main/components" },
          ]}
        />
      }
      footer={
        <Footer
          links={[
            { label: "@hugocxl/design-system", href: "../design-system/" },
            { label: "@hugocxl/icons", href: "../icons/" },
            { label: "@hugocxl/vectors", href: "../vectors/" },
          ]}
          secondary={[
            { label: "npm", href: "https://www.npmjs.com/package/@hugocxl/components" },
            { label: "GitHub", href: "https://github.com/hugocxl/stack" },
          ]}
        />
      }
    >
      {content}
    </Page>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
