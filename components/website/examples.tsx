// Live examples for every recipe: the React specimen, its code, and the Swift code that
// draws the same thing (the Swift captures come from DSGallery in Sources/Components).
import { useEffect, useState, type ReactNode } from "react";
import {
  Button,
  ButtonGroup,
  Checkbox,
  CodeBlock,
  Dialog,
  Divider,
  Figure,
  FigureGrid,
  Footer,
  IconButton,
  Knob,
  Link,
  List,
  Masthead,
  Meta,
  Meter,
  Muted,
  Notice,
  Progress,
  RadioGroup,
  Readout,
  ReadoutGrid,
  Section,
  SegmentedControl,
  Select,
  SlideSwitch,
  Slider,
  Statement,
  Status,
  Switch,
  Table,
  Text,
  TextField,
  ThemeToggle,
  Title,
} from "@hugocxl/components/react";
import { ArrowLeftIcon } from "@hugocxl/icons/react/arrow-left";
import { ArrowRightIcon } from "@hugocxl/icons/react/arrow-right";
import { BookOpenIcon } from "@hugocxl/icons/react/book-open";
import { CloseIcon } from "@hugocxl/icons/react/close";
import { CodeIcon } from "@hugocxl/icons/react/code";
import { EllipsisIcon } from "@hugocxl/icons/react/ellipsis";
import { PencilIcon } from "@hugocxl/icons/react/pencil";
import { PhoneIcon } from "@hugocxl/icons/react/phone";
import { SendIcon } from "@hugocxl/icons/react/send";
import { FastPerformanceVector } from "@hugocxl/vectors/react/fast-performance";
import { HandoffVector } from "@hugocxl/vectors/react/handoff";
import { HowItWorksVector } from "@hugocxl/vectors/react/how-it-works";
import { ModularDesignVector } from "@hugocxl/vectors/react/modular-design";

export type Example = {
  title: string;
  /** Stretch the specimen to the stage's width. */
  fill?: boolean;
  render: () => ReactNode;
  react: string;
};

/** card: what the component's card on the home grid shows, when not its first example. */
export type RecipeExamples = { examples: Example[]; swift?: string; card?: () => ReactNode };

const code = (strings: TemplateStringsArray) => {
  const lines = strings.raw.join("").replace(/^\n/, "").replace(/\s+$/, "").split("\n");
  const indent = Math.min(...lines.filter((line) => line.trim()).map((line) => line.match(/^ */)![0].length));
  return lines.map((line) => line.slice(indent)).join("\n").replace(/\\`/g, "`").replace(/\\\$/g, "$");
};

function Controlled<T>({ initial, children }: { initial: T; children: (value: T, set: (value: T) => void) => ReactNode }) {
  const [value, setValue] = useState(initial);
  return <>{children(value, setValue)}</>;
}

function DialogDemo() {
  const [open, setOpen] = useState(false);
  return (
    <>
      <Button variant="secondary" onClick={() => setOpen(true)}>
        Delete project
      </Button>
      <Dialog
        open={open}
        onClose={() => setOpen(false)}
        title="Delete this project?"
        description="Its pages and history go with it. This cannot be undone."
        actions={
          <>
            <Button variant="secondary" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button onClick={() => setOpen(false)}>Delete project</Button>
          </>
        }
      />
    </>
  );
}

function FormDialogDemo() {
  const [open, setOpen] = useState(false);
  return (
    <>
      <Button icon={<SendIcon />} onClick={() => setOpen(true)}>
        Invite people
      </Button>
      <Dialog
        open={open}
        onClose={() => setOpen(false)}
        title="Invite people"
        description="They get an email with a link that works for seven days."
        actions={
          <>
            <Button variant="secondary" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button onClick={() => setOpen(false)}>Send invites</Button>
          </>
        }
      >
        <TextField label="Emails" placeholder="ana@example.com, li@example.com" />
      </Dialog>
    </>
  );
}

function NoticeDemo() {
  const [visible, setVisible] = useState(true);
  return visible ? (
    <Notice tone="success" title="Your changes are live." onDismiss={() => setVisible(false)}>
      It can take a minute to reach every region.
    </Notice>
  ) : (
    <Button variant="ghost" onClick={() => setVisible(true)}>
      Show the notice again
    </Button>
  );
}

function FigurePagerDemo() {
  const figures = [
    { name: "How it works", vector: <HowItWorksVector /> },
    { name: "Handoff", vector: <HandoffVector /> },
  ];
  const [index, setIndex] = useState(0);
  const step = (by: number) => setIndex((current) => (current + by + figures.length) % figures.length);
  return (
    <Figure wide={false} caption={`Fig. 0${index + 1} / ${figures[index].name}`} pager={{ onPrevious: () => step(-1), onNext: () => step(1) }}>
      {figures[index].vector}
    </Figure>
  );
}

const formatEv = (value: number) => {
  if (Math.abs(value) < 1e-6) return "±0";
  const sign = value > 0 ? "+" : "−";
  const thirds = Math.round(Math.abs(value) * 3);
  const whole = Math.floor(thirds / 3);
  const rest = thirds % 3;
  return `${sign}${whole || rest === 0 ? whole : ""}${rest ? (whole ? " " : "") + (rest === 1 ? "⅓" : "⅔") : ""}`;
};

function LiveMeters() {
  const [level, setLevel] = useState(0.4);
  useEffect(() => {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const timer = setInterval(() => setLevel((current) => Math.min(1, Math.max(0.05, current + (Math.random() - 0.5) * 0.3))), 140);
    return () => clearInterval(timer);
  }, []);
  return (
    <>
      <Meter label="CPU" value={0.68} />
      <Meter label="Input" value={level} variant="dots" segments={16} />
      <Meter label="Storage" value={0.91} tone="warning" format={(v) => `${Math.round(v * 64)} of 64 GB`} />
    </>
  );
}

function CameraPanel() {
  const [active, setActive] = useState("speed");
  const [ev, setEv] = useState(1 + 1 / 3);
  return (
    <div className="site-panel">
      <ReadoutGrid columns={3}>
        <Readout label="Lens" value="24" unit="mm" />
        <Readout label="Mode" value="Auto" live />
        <Readout label="Preset" value="Off" dim />
        <Readout label="Speed" value="1/125" onPress={() => setActive("speed")} selected={active === "speed"} />
        <Readout label="ISO" value={250} onPress={() => setActive("iso")} selected={active === "iso"} />
        <Readout label="WB" value="5600" unit="K" onPress={() => setActive("wb")} selected={active === "wb"} />
      </ReadoutGrid>
      <Slider label="EV" min={-3} max={3} step={1 / 3} value={ev} onValueChange={setEv} centered ticks={19} majorEvery={3} format={formatEv} />
    </div>
  );
}

export const examples: Record<string, RecipeExamples> = {
  theme: {
    card: () => (
      <>
        <ThemeToggle />
        <Text variant="label">Switch the whole page</Text>
      </>
    ),
    examples: [
      {
        title: "Set up once",
        render: () => (
          <div className="site-row">
            <ThemeToggle />
            <Text tone="muted">Switches this whole page between light and dark.</Text>
          </div>
        ),
        react: code`
          // main.tsx
          import "@hugocxl/components/styles.css"; // fonts, tokens and components
          import { ThemeToggle, themeScript } from "@hugocxl/components/react";

          // In the document head, before any CSS, to avoid a flash:
          // <script dangerouslySetInnerHTML={{ __html: themeScript }} />

          <ThemeToggle />
        `,
      },
    ],
    swift: code`
      import Components

      @main
      struct FieldworkApp: App {
          var body: some Scene {
              WindowGroup {
                  ContentView().dsTheme() // registers Geist, sets ink and the reading type
              }
          }
      }
    `,
  },
  text: {
    examples: [
      {
        title: "Type styles",
        render: () => (
          <>
            <Text variant="title" as="p">Title, the largest text</Text>
            <Text>Reading type carries every page. <Muted>Supporting sentences follow in muted.</Muted></Text>
            <Text variant="small" tone="muted">Small supporting text.</Text>
            <Text variant="label">Label · 5 October 2026</Text>
            <Text variant="mono">npm install @hugocxl/components</Text>
          </>
        ),
        react: code`
          <Text variant="title" as="p">Title, the largest text</Text>
          <Text>Reading type carries every page. <Muted>Supporting sentences follow in muted.</Muted></Text>
          <Text variant="small" tone="muted">Small supporting text.</Text>
          <Text variant="label">Label · 5 October 2026</Text>
          <Text variant="mono">npm install @hugocxl/components</Text>
        `,
      },
    ],
    swift: code`
      DSText("Title, the largest text", variant: .title)
      DSText("Reading type carries every screen.")
      DSText("Small supporting text, in muted.", variant: .small, tone: .muted)
      DSText("Label · 5 October 2026", variant: .label)
      DSText("npm install @hugocxl/components", variant: .mono)
    `,
  },
  button: {
    examples: [
      {
        title: "Variants",
        render: () => (
          <div className="site-row">
            <Button icon={<ArrowRightIcon />}>Get started</Button>
            <Button variant="secondary">Read the docs</Button>
            <Button variant="ghost" icon={<PencilIcon />}>Edit</Button>
          </div>
        ),
        react: code`
          <Button icon={<ArrowRightIcon />}>Get started</Button>
          <Button variant="secondary">Read the docs</Button>
          <Button variant="ghost" icon={<PencilIcon />}>Edit</Button>
        `,
      },
      {
        title: "States and links",
        render: () => (
          <div className="site-row">
            <Button disabled>Disabled</Button>
            <Button variant="secondary" href="#/link">A link that looks like a button</Button>
          </div>
        ),
        react: code`
          <Button disabled>Disabled</Button>
          <Button variant="secondary" href="/link">A link that looks like a button</Button>
        `,
      },
      {
        title: "Full width, in a group",
        fill: true,
        render: () => (
          <>
            <Button fullWidth>Create account</Button>
            <ButtonGroup align="end">
              <Button variant="secondary">Cancel</Button>
              <Button>Save changes</Button>
            </ButtonGroup>
          </>
        ),
        react: code`
          <Button fullWidth>Create account</Button>
          <ButtonGroup align="end">
            <Button variant="secondary">Cancel</Button>
            <Button>Save changes</Button>
          </ButtonGroup>
        `,
      },
    ],
    swift: code`
      DSButton("Get started", icon: StrokeIcon.arrowRight) { start() }
      DSButton("Read the docs", variant: .secondary) { openDocs() }
      DSButton("Edit", icon: StrokeIcon.pencil, variant: .ghost) { edit() }
      DSButton("Disabled") {}.disabled(true)

      // Or style any SwiftUI button:
      Button("Save changes", action: save).buttonStyle(.ds(.primary, fullWidth: true))
    `,
  },
  "icon-button": {
    examples: [
      {
        title: "Outline and ghost",
        render: () => (
          <div className="site-row">
            <IconButton label="Previous" icon={<ArrowLeftIcon />} />
            <IconButton label="Next" icon={<ArrowRightIcon />} />
            <IconButton variant="ghost" label="Close" icon={<CloseIcon />} />
            <IconButton variant="ghost" label="More" icon={<EllipsisIcon />} />
          </div>
        ),
        react: code`
          <IconButton label="Previous" icon={<ArrowLeftIcon />} />
          <IconButton label="Next" icon={<ArrowRightIcon />} />
          <IconButton variant="ghost" label="Close" icon={<CloseIcon />} />
          <IconButton variant="ghost" label="More" icon={<EllipsisIcon />} />
        `,
      },
    ],
    swift: code`
      DSIconButton(StrokeIcon.arrowLeft, label: "Previous") { previous() }
      DSIconButton(StrokeIcon.arrowRight, label: "Next") { next() }
      DSIconButton(StrokeIcon.close, label: "Close", variant: .ghost) { dismiss() }
    `,
  },
  link: {
    examples: [
      {
        title: "Inline and standalone",
        render: () => (
          <>
            <Text>
              Read the <Link href="#/">documentation</Link> for setup.
            </Text>
            <div className="site-row">
              <Link variant="standalone" icon={<BookOpenIcon />} href="#/">Changelog</Link>
              <Link variant="standalone" external href="https://github.com/hugocxl/stack">GitHub</Link>
            </div>
          </>
        ),
        react: code`
          <Text>Read the <Link href="/docs">documentation</Link> for setup.</Text>
          <Link variant="standalone" icon={<BookOpenIcon />} href="/changelog">Changelog</Link>
          <Link variant="standalone" external href="https://github.com/hugocxl/stack">GitHub</Link>
        `,
      },
    ],
    swift: code`
      DSLink("Read the documentation", destination: docsURL)
      DSLink("Changelog", destination: changelogURL, icon: StrokeIcon.bookOpen, variant: .standalone)
      DSLink("GitHub", destination: githubURL, variant: .standalone, external: true)
    `,
  },
  "text-field": {
    examples: [
      {
        title: "With help and with an error",
        fill: true,
        render: () => (
          <div className="dsc-stack">
            <TextField label="Email" type="email" placeholder="you@example.com" help="We only write when something ships." />
            <TextField label="Project name" defaultValue="fieldwork!" error="Use letters, numbers and dashes only." />
          </div>
        ),
        react: code`
          <TextField label="Email" type="email" placeholder="you@example.com"
            help="We only write when something ships." />
          <TextField label="Project name" defaultValue="fieldwork!"
            error="Use letters, numbers and dashes only." />
        `,
      },
      {
        title: "With an action, and multiline",
        fill: true,
        render: () => (
          <div className="dsc-stack">
            <TextField
              label="Get the release notes"
              placeholder="you@example.com"
              action={<IconButton variant="ghost" label="Subscribe" icon={<ArrowRightIcon />} />}
            />
            <TextField label="Message" multiline placeholder="What are you building?" />
            <TextField label="Disabled" disabled defaultValue="Read only" />
          </div>
        ),
        react: code`
          <TextField label="Get the release notes" placeholder="you@example.com"
            action={<IconButton variant="ghost" label="Subscribe" icon={<ArrowRightIcon />} />} />
          <TextField label="Message" multiline placeholder="What are you building?" />
          <TextField label="Disabled" disabled defaultValue="Read only" />
        `,
      },
    ],
    swift: code`
      DSTextField("Email", text: $email, placeholder: "you@example.com",
                  help: "We only write when something ships.")
      DSTextField("Project name", text: $name, error: nameError)
      DSTextField("Message", text: $message, multiline: true)
      DSTextField("Get the release notes", text: $email) {
          DSIconButton(StrokeIcon.arrowRight, label: "Subscribe", variant: .ghost) { subscribe() }
      }
    `,
  },
  checkbox: {
    examples: [
      {
        title: "Options in a form",
        render: () => (
          <div>
            <Checkbox label="Send me release notes" defaultChecked />
            <Checkbox label="Include pre-releases" description="Betas ship every Tuesday." />
            <Checkbox label="Disabled" disabled />
          </div>
        ),
        react: code`
          <Checkbox label="Send me release notes" defaultChecked />
          <Checkbox label="Include pre-releases" description="Betas ship every Tuesday." />
          <Checkbox label="Disabled" disabled />
        `,
      },
    ],
    swift: code`
      DSCheckbox("Send me release notes", isOn: $releaseNotes)
      DSCheckbox("Include pre-releases", isOn: $preReleases, description: "Betas ship every Tuesday.")
    `,
  },
  switch: {
    examples: [
      {
        title: "Settings",
        fill: true,
        render: () => (
          <div>
            <Switch label="Sounds" description="Play a sound when a task finishes." defaultChecked />
            <Switch label="Reduce motion" />
          </div>
        ),
        react: code`
          <Switch label="Sounds" description="Play a sound when a task finishes." defaultChecked />
          <Switch label="Reduce motion" />
        `,
      },
    ],
    swift: code`
      DSSwitch("Sounds", isOn: $sounds, description: "Play a sound when a task finishes.")
      DSSwitch("Reduce motion", isOn: $reduceMotion)
    `,
  },
  "radio-group": {
    examples: [
      {
        title: "Pick one",
        render: () => (
          <Controlled initial="team">
            {(value, setValue) => (
              <RadioGroup
                label="Plan"
                value={value}
                onValueChange={setValue}
                options={[
                  { value: "personal", label: "Personal", description: "For one person and their side projects." },
                  { value: "team", label: "Team", description: "Shared projects and roles." },
                  { value: "enterprise", label: "Enterprise", description: "Single sign-on and audit logs.", disabled: true },
                ]}
              />
            )}
          </Controlled>
        ),
        react: code`
          const [plan, setPlan] = useState("team");

          <RadioGroup label="Plan" value={plan} onValueChange={setPlan} options={[
            { value: "personal", label: "Personal", description: "For one person and their side projects." },
            { value: "team", label: "Team", description: "Shared projects and roles." },
            { value: "enterprise", label: "Enterprise", description: "Single sign-on and audit logs.", disabled: true },
          ]} />
        `,
      },
    ],
    swift: code`
      DSRadioGroup("Plan", selection: $plan, options: [
          DSOption("personal", label: "Personal", description: "For one person and their side projects."),
          DSOption("team", label: "Team", description: "Shared projects and roles."),
      ])
    `,
  },
  select: {
    examples: [
      {
        title: "A long list",
        fill: true,
        render: () => (
          <Select
            label="Region"
            defaultValue="eu"
            help="Where your data is stored."
            options={[
              { value: "eu", label: "Europe" },
              { value: "us", label: "United States" },
              { value: "ap", label: "Asia Pacific" },
              { value: "sa", label: "South America" },
            ]}
          />
        ),
        react: code`
          <Select label="Region" defaultValue="eu" help="Where your data is stored." options={[
            { value: "eu", label: "Europe" },
            { value: "us", label: "United States" },
            { value: "ap", label: "Asia Pacific" },
          ]} />
        `,
      },
    ],
    swift: code`
      DSSelect("Region", selection: $region, options: [
          DSOption("eu", label: "Europe"),
          DSOption("us", label: "United States"),
          DSOption("ap", label: "Asia Pacific"),
      ], help: "Where your data is stored.")
    `,
  },
  "segmented-control": {
    examples: [
      {
        title: "Switch the view",
        render: () => (
          <>
            <Controlled initial="week">
              {(value, setValue) => (
                <SegmentedControl
                  label="Period"
                  value={value}
                  onValueChange={setValue}
                  options={[
                    { value: "day", label: "Day" },
                    { value: "week", label: "Week" },
                    { value: "month", label: "Month" },
                  ]}
                />
              )}
            </Controlled>
            <Controlled initial="swift">
              {(value, setValue) => (
                <SegmentedControl
                  label="Platform"
                  value={value}
                  onValueChange={setValue}
                  options={[
                    { value: "react", label: "React", icon: <CodeIcon /> },
                    { value: "swift", label: "Swift", icon: <PhoneIcon /> },
                  ]}
                />
              )}
            </Controlled>
          </>
        ),
        react: code`
          const [period, setPeriod] = useState("week");

          <SegmentedControl label="Period" value={period} onValueChange={setPeriod} options={[
            { value: "day", label: "Day" },
            { value: "week", label: "Week" },
            { value: "month", label: "Month" },
          ]} />
        `,
      },
    ],
    swift: code`
      DSSegmentedControl("Period", selection: $period, options: [
          DSOption("day", label: "Day"),
          DSOption("week", label: "Week"),
          DSOption("month", label: "Month"),
      ])
    `,
  },
  status: {
    examples: [
      {
        title: "Dots and icons",
        render: () => (
          <>
            <div className="site-row">
              <Status>Beta</Status>
              <Status tone="success">Operational</Status>
              <Status tone="warning">Degraded</Status>
            </div>
            <div className="site-row">
              <Status tone="error" mark="icon">Down</Status>
              <Status tone="info" mark="icon">Scheduled</Status>
              <Status tone="neutral">Draft</Status>
            </div>
            <Status tone="success" mark="icon" appearance="text">All systems operational</Status>
          </>
        ),
        react: code`
          <Status>Beta</Status>
          <Status tone="success">Operational</Status>
          <Status tone="warning">Degraded</Status>
          <Status tone="error" mark="icon">Down</Status>
          <Status tone="info" mark="icon">Scheduled</Status>
          <Status tone="neutral">Draft</Status>
          <Status tone="success" mark="icon" appearance="text">All systems operational</Status>
        `,
      },
    ],
    swift: code`
      DSStatus("Beta")
      DSStatus("Operational", tone: .success)
      DSStatus("Down", tone: .error, mark: .icon)
      DSStatus("All systems operational", tone: .success, mark: .icon, appearance: .text)
    `,
  },
  notice: {
    examples: [
      {
        title: "Tones",
        fill: true,
        render: () => (
          <>
            <NoticeDemo />
            <Notice tone="error" title="The import failed." action={<Button variant="ghost">Download the rows</Button>}>
              Three rows have no email. Fix them and try again.
            </Notice>
            <Notice tone="warning" title="Your trial ends in three days." />
            <Notice tone="info" title="Maintenance on Sunday at 02:00 UTC." />
          </>
        ),
        react: code`
          <Notice tone="success" title="Your changes are live." onDismiss={hide}>
            It can take a minute to reach every region.
          </Notice>
          <Notice tone="error" title="The import failed."
            action={<Button variant="ghost">Download the rows</Button>}>
            Three rows have no email. Fix them and try again.
          </Notice>
          <Notice tone="warning" title="Your trial ends in three days." />
        `,
      },
    ],
    swift: code`
      DSNotice("Your changes are live.", message: "It can take a minute to reach every region.",
               tone: .success, onDismiss: { showNotice = false })
      DSNotice("The import failed.", message: "Three rows have no email.", tone: .error) {
          DSButton("Download the rows", variant: .ghost) { download() }
      }
    `,
  },
  dialog: {
    examples: [
      {
        title: "Confirm",
        render: () => <DialogDemo />,
        react: code`
          const [open, setOpen] = useState(false);

          <Dialog open={open} onClose={() => setOpen(false)}
            title="Delete this project?"
            description="Its pages and history go with it. This cannot be undone."
            actions={<>
              <Button variant="secondary" onClick={() => setOpen(false)}>Cancel</Button>
              <Button onClick={remove}>Delete project</Button>
            </>} />
        `,
      },
      {
        title: "A short task",
        render: () => <FormDialogDemo />,
        react: code`
          <Dialog open={open} onClose={close} title="Invite people"
            description="They get an email with a link that works for seven days."
            actions={<>…</>}>
            <TextField label="Emails" placeholder="ana@example.com, li@example.com" />
          </Dialog>
        `,
      },
    ],
    swift: code`
      content
          .dsDialog(isPresented: $confirmDelete,
                    title: "Delete this project?",
                    description: "Its pages and history go with it. This cannot be undone.") {
              DSButton("Cancel", variant: .secondary) { confirmDelete = false }
              DSButton("Delete project") { remove() }
          }
    `,
  },
  progress: {
    examples: [
      {
        title: "Known and unknown length",
        fill: true,
        render: () => (
          <>
            <Progress value={0.64} label="Uploading 3 files" />
            <Progress label="Preparing the export" />
          </>
        ),
        react: code`
          <Progress value={0.64} label="Uploading 3 files" />
          <Progress label="Preparing the export" />
        `,
      },
    ],
    swift: code`
      DSProgress(value: 0.64, label: "Uploading 3 files")
      DSProgress(label: "Preparing the export")
    `,
  },
  meter: {
    examples: [
      {
        title: "Bars and dots",
        fill: true,
        render: () => <LiveMeters />,
        react: code`
          <Meter label="CPU" value={0.68} />
          <Meter label="Input" value={level} variant="dots" segments={16} />
          <Meter label="Storage" value={0.91} tone="warning" format={(v) => \`\${Math.round(v * 64)} of 64 GB\`} />
        `,
      },
    ],
    swift: code`
      DSMeter(value: 0.68, label: "CPU")
      DSMeter(value: level, label: "Input", segments: 16, variant: .dots)
      DSMeter(value: 0.91, label: "Storage", tone: .warning) { "\(Int(($0 * 64).rounded())) of 64 GB" }
    `,
  },
  knob: {
    examples: [
      {
        title: "A bank of knobs",
        render: () => (
          <div className="site-row" style={{ gap: "var(--ds-space-5)" }}>
            <Knob label="Tone" defaultValue={30} />
            <Knob label="Drive" defaultValue={72} />
            <Knob label="Space" defaultValue={50} />
            <Knob label="Mix" defaultValue={18} />
          </div>
        ),
        react: code`
          <Knob label="Tone" defaultValue={30} />
          <Knob label="Drive" defaultValue={72} />
          <Knob label="Space" defaultValue={50} />
          <Knob label="Mix" defaultValue={18} />
        `,
      },
      {
        title: "Sizes and readings",
        render: () => (
          <div className="site-row" style={{ gap: "var(--ds-space-6)", alignItems: "flex-end" }}>
            <Knob size="small" label="Pan" min={-50} max={50} defaultValue={0} format={(v) => (v === 0 ? "C" : v < 0 ? `L${-v}` : `R${v}`)} />
            <Knob label="Gain" min={-24} max={24} step={0.5} defaultValue={0} format={(v) => `${v > 0 ? "+" : ""}${v.toFixed(1)} dB`} />
            <Knob size="large" label="Tempo" min={60} max={200} defaultValue={128} format={(v) => `${v} BPM`} />
          </div>
        ),
        react: code`
          <Knob size="small" label="Pan" min={-50} max={50} defaultValue={0}
            format={(v) => (v === 0 ? "C" : v < 0 ? \`L\${-v}\` : \`R\${v}\`)} />
          <Knob label="Gain" min={-24} max={24} step={0.5} defaultValue={0}
            format={(v) => \`\${v > 0 ? "+" : ""}\${v.toFixed(1)} dB\`} />
          <Knob size="large" label="Tempo" min={60} max={200} defaultValue={128} format={(v) => \`\${v} BPM\`} />
        `,
      },
    ],
    swift: code`
      DSKnob("Tone", value: $tone, defaultValue: 50)
      DSKnob("Gain", value: $gain, in: -24...24, step: 0.5, size: .large) { String(format: "%+.1f dB", $0) }
    `,
  },
  slider: {
    examples: [
      {
        title: "Volume",
        fill: true,
        render: () => <Slider label="Volume" defaultValue={64} max={127} ticks={33} majorEvery={4} />,
        react: code`<Slider label="Volume" defaultValue={64} max={127} ticks={33} majorEvery={4} />`,
      },
      {
        title: "Around zero, with marks",
        fill: true,
        render: () => (
          <Slider
            label="Exposure"
            min={-3}
            max={3}
            step={1 / 3}
            defaultValue={1 + 1 / 3}
            centered
            ticks={19}
            majorEvery={3}
            marks={[-3, -2, -1, 0, 1, 2, 3].map((v) => ({ value: v, label: v > 0 ? `+${v}` : String(v) }))}
            format={formatEv}
          />
        ),
        react: code`
          <Slider label="Exposure" min={-3} max={3} step={1 / 3} defaultValue={4 / 3} centered ticks={19} majorEvery={3}
            marks={[-3, -2, -1, 0, 1, 2, 3].map((v) => ({ value: v, label: v > 0 ? \`+\${v}\` : String(v) }))}
            format={formatEv} />
        `,
      },
    ],
    swift: code`
      DSSlider("Volume", value: $volume, in: 0...127, ticks: 33, majorEvery: 4)
      DSSlider("Exposure", value: $ev, in: -3...3, step: 1.0 / 3, ticks: 19, majorEvery: 3, centered: true, format: formatEV)
    `,
  },
  "slide-switch": {
    examples: [
      {
        title: "Vertical and horizontal",
        render: () => (
          <div className="site-row" style={{ gap: "var(--ds-space-7)", alignItems: "flex-start" }}>
            <SlideSwitch
              label="Output"
              defaultValue="cue"
              options={[
                { value: "main", label: "Main" },
                { value: "cue", label: "Cue" },
                { value: "both", label: "Both" },
              ]}
            />
            <SlideSwitch
              label="Quality"
              orientation="horizontal"
              defaultValue="mid"
              options={[
                { value: "lo", label: "Lo" },
                { value: "mid", label: "Mid" },
                { value: "hi", label: "Hi" },
              ]}
            />
          </div>
        ),
        react: code`
          <SlideSwitch label="Output" defaultValue="cue" options={[
            { value: "main", label: "Main" },
            { value: "cue", label: "Cue" },
            { value: "both", label: "Both" },
          ]} />
          <SlideSwitch label="Quality" orientation="horizontal" defaultValue="mid" options={[
            { value: "lo", label: "Lo" }, { value: "mid", label: "Mid" }, { value: "hi", label: "Hi" },
          ]} />
        `,
      },
    ],
    swift: code`
      DSSlideSwitch("Output", selection: $output, options: [
          DSOption("main", label: "Main"), DSOption("cue", label: "Cue"), DSOption("both", label: "Both"),
      ])
      DSSlideSwitch("Quality", selection: $quality, options: qualities, orientation: .horizontal)
    `,
  },
  readout: {
    examples: [
      {
        title: "An instrument panel",
        fill: true,
        render: () => <CameraPanel />,
        react: code`
          <ReadoutGrid columns={3}>
            <Readout label="Lens" value="24" unit="mm" />
            <Readout label="Mode" value="Auto" live />
            <Readout label="Preset" value="Off" dim />
            <Readout label="Speed" value="1/125" onPress={editSpeed} selected />
            <Readout label="ISO" value={250} onPress={editIso} />
            <Readout label="WB" value="5600" unit="K" onPress={editWhiteBalance} />
          </ReadoutGrid>
        `,
      },
    ],
    swift: code`
      DSReadoutGrid(columns: 3) {
          DSReadout("Lens", value: "24", unit: "mm")
          DSReadout("Mode", value: "Auto", live: true)
          DSReadout("Preset", value: "Off", dim: true)
          DSReadout("Speed", value: "1/125", selected: editing == .speed) { editing = .speed }
          DSReadout("ISO", value: "250", selected: editing == .iso) { editing = .iso }
      }
    `,
  },
  title: {
    examples: [
      {
        title: "With a byline",
        render: () => <Title byline="Fieldwork team">Public testing is beginning</Title>,
        react: code`<Title byline="Fieldwork team">Public testing is beginning</Title>`,
      },
    ],
    swift: code`DSTitle("Public testing is beginning", byline: "Fieldwork team")`,
  },
  statement: {
    examples: [
      {
        title: "With the accent",
        render: () => <Statement accent="every day.">Field notes for teams that ship</Statement>,
        react: code`<Statement accent="every day.">Field notes for teams that ship</Statement>`,
      },
    ],
    swift: code`DSStatement("Field notes for teams that ship", accent: "every day.")`,
  },
  meta: {
    examples: [
      {
        title: "Status, version and date",
        render: () => (
          <Meta
            style={{ marginTop: 0 }}
            items={[<Status key="s">Beta</Status>, "Version 0.4", <time key="d" dateTime="2026-10-05">5 October 2026</time>]}
          />
        ),
        react: code`
          <Meta items={[
            <Status>Beta</Status>,
            "Version 0.4",
            <time dateTime="2026-10-05">5 October 2026</time>,
          ]} />
        `,
      },
    ],
    swift: code`DSMeta([.status("Beta", .accent), .text("Version 0.4"), .text("5 October 2026")])`,
  },
  section: {
    examples: [
      {
        title: "Heading and paragraphs",
        render: () => (
          <Section heading="What is available" style={{ marginTop: 0 }}>
            <p>
              Testing is limited to the macOS app. <Muted>Linux and Windows follow once the first wave is stable.</Muted>
            </p>
            <p>
              Read the <a href="#/">documentation</a> for setup.
            </p>
          </Section>
        ),
        react: code`
          <Section heading="What is available" id="what-is-available">
            <p>Testing is limited to the macOS app. <Muted>Linux and Windows follow once the first wave is stable.</Muted></p>
            <p>Read the <a href="/docs">documentation</a> for setup.</p>
          </Section>
        `,
      },
    ],
    swift: code`
      DSSection("What is available") {
          DSText("Testing is limited to the macOS app.")
      }
    `,
  },
  divider: {
    examples: [
      {
        title: "Between groups",
        fill: true,
        render: () => (
          <div>
            <Text>Above the hairline</Text>
            <Divider />
            <Text>Below the hairline</Text>
          </div>
        ),
        react: code`<Divider />`,
      },
    ],
    swift: code`DSDivider()`,
  },
  "code-block": {
    examples: [
      {
        title: "With a label",
        fill: true,
        render: () => <CodeBlock label="Terminal" code={'npm install @hugocxl/components\nimport "@hugocxl/components/styles.css"'} />,
        react: code`
          <CodeBlock label="Terminal" code={\`npm install @hugocxl/components
          import "@hugocxl/components/styles.css"\`} />
        `,
      },
    ],
    swift: code`DSCodeBlock("npm install @hugocxl/components", label: "Terminal")`,
  },
  list: {
    examples: [
      {
        title: "A changelog",
        fill: true,
        render: () => (
          <List
            items={[
              { label: "0.2.0", title: "Dialogs and notices", description: "Confirm, inform and warn without leaving the page." },
              { label: "0.1.0", title: "The first components", description: "Buttons, fields and status for React and Swift." },
            ]}
          />
        ),
        react: code`
          <List items={[
            { label: "0.2.0", title: "Dialogs and notices", description: "Confirm, inform and warn without leaving the page." },
            { label: "0.1.0", title: "The first components", description: "Buttons, fields and status for React and Swift." },
          ]} />
        `,
      },
      {
        title: "Settings rows",
        fill: true,
        render: () => (
          <List
            density="compact"
            items={[
              { title: "Notifications", trailing: "On", href: "#/list" },
              { title: "Billing", trailing: "Team plan", href: "#/list" },
              { title: "Status", trailing: <Status tone="success">Operational</Status> },
            ]}
          />
        ),
        react: code`
          <List density="compact" items={[
            { title: "Notifications", trailing: "On", href: "/settings/notifications" },
            { title: "Billing", trailing: "Team plan", href: "/settings/billing" },
            { title: "Status", trailing: <Status tone="success">Operational</Status> },
          ]} />
        `,
      },
    ],
    swift: code`
      DSList([
          DSListItem("Dialogs and notices", label: "0.2.0", description: "Confirm, inform and warn."),
          DSListItem("Notifications", trailing: "On") { path.append(.notifications) },
      ])
    `,
  },
  table: {
    examples: [
      {
        title: "Plans",
        fill: true,
        render: () => (
          <Table
            caption="Plans"
            columns={[{ label: "Plan" }, { label: "Projects" }, { label: "Price", align: "end" }]}
            rows={[
              ["Personal", "3", "Free"],
              ["Team", "Unlimited", "€12 / month"],
              ["Enterprise", "Unlimited", "Talk to us"],
            ]}
          />
        ),
        react: code`
          <Table caption="Plans"
            columns={[{ label: "Plan" }, { label: "Projects" }, { label: "Price", align: "end" }]}
            rows={[
              ["Personal", "3", "Free"],
              ["Team", "Unlimited", "€12 / month"],
            ]} />
        `,
      },
    ],
  },
  figure: {
    examples: [
      {
        title: "A vector",
        fill: true,
        render: () => (
          <Figure wide={false} caption="Fig. 01 / How it works">
            <HowItWorksVector />
          </Figure>
        ),
        react: code`
          import { HowItWorksVector } from "@hugocxl/vectors/react/how-it-works";

          <Figure caption="Fig. 01 / How it works"><HowItWorksVector /></Figure>
        `,
      },
      {
        title: "With a pager",
        fill: true,
        render: () => <FigurePagerDemo />,
        react: code`
          <Figure caption={caption} pager={{ onPrevious: previous, onNext: next }}>
            {vector}
          </Figure>
        `,
      },
    ],
    swift: code`DSFigure(Vector.howItWorks, caption: "Fig. 01 / How it works", title: "How it works")`,
  },
  "figure-grid": {
    examples: [
      {
        title: "Three features",
        fill: true,
        render: () => (
          <FigureGrid
            wide={false}
            items={[
              { media: <ModularDesignVector />, title: "Purpose-built", text: "Shaped by teams who ship daily." },
              { media: <HandoffVector />, title: "Shared", text: "From the first draft to the merge." },
              { media: <FastPerformanceVector />, title: "Designed for speed", text: "Less noise, more momentum." },
            ]}
          />
        ),
        react: code`
          <FigureGrid items={[
            { media: <ModularDesignVector />, title: "Purpose-built", text: "Shaped by teams who ship daily." },
            { media: <HandoffVector />, title: "Shared", text: "From the first draft to the merge." },
            { media: <FastPerformanceVector />, title: "Designed for speed", text: "Less noise, more momentum." },
          ]} />
        `,
      },
    ],
    swift: code`
      DSFigureGrid([
          DSFigureGridItem("Purpose-built", vector: Vector.modularDesign, text: "Shaped by teams who ship daily."),
          DSFigureGridItem("Designed for speed", vector: Vector.fastPerformance, text: "Less noise, more momentum."),
      ])
    `,
  },
  page: {
    examples: [
      {
        title: "This website",
        render: () => <Text tone="muted">This page is a Page: masthead, the reading column and the footer.</Text>,
        react: code`
          <Page
            masthead={<Masthead wordmark="Fieldwork" links={[{ label: "Docs", href: "/docs" }]} />}
            footer={<Footer links={[{ label: "Docs", href: "/docs" }]} secondary={[{ label: "GitHub", href: "…" }]} />}
          >
            <Statement accent="every day.">Field notes for teams that ship</Statement>
            <Section>…</Section>
          </Page>
        `,
      },
    ],
    swift: code`
      DSPage {
          DSStatement("Field notes for teams that ship", accent: "every day.")
          DSMeta([.status("Beta", .accent), .text("5 October 2026")])
          DSSection { DSText("…") }
      }
    `,
  },
  masthead: {
    examples: [
      {
        title: "Wordmark, links and the theme toggle",
        fill: true,
        render: () => <Masthead style={{ paddingTop: 0, width: "100%" }} wordmark="Fieldwork" href="#/" links={[{ label: "Changelog", href: "#/" }, { label: "Docs", href: "#/" }]} />,
        react: code`
          <Masthead wordmark="Fieldwork" href="/" links={[
            { label: "Changelog", href: "/changelog" },
            { label: "Docs", href: "/docs" },
          ]} />
        `,
      },
    ],
  },
  footer: {
    examples: [
      {
        title: "Two groups of links",
        fill: true,
        render: () => <Footer style={{ margin: 0, padding: 0, width: "100%" }} links={[{ label: "Docs", href: "#/" }, { label: "Changelog", href: "#/" }]} secondary={[{ label: "npm", href: "#/" }, { label: "GitHub", href: "#/" }]} />,
        react: code`
          <Footer
            links={[{ label: "Docs", href: "/docs" }, { label: "Changelog", href: "/changelog" }]}
            secondary={[{ label: "npm", href: "…" }, { label: "GitHub", href: "…" }]} />
        `,
      },
    ],
  },
  density: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/density-light.png" alt="" loading="lazy" />,
    swift: code`
      ContentView()
          .dsTheme()
          .dsDensity(.compact) // a desktop tool: 13pt reading, 28pt targets
    `,
  },
  pane: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/pane-light.png" alt="" loading="lazy" />,
    swift: code`
      DSPane("Inspector", icon: StrokeIcon.sliders, accessories: {
          DSIconButton(StrokeIcon.refreshCcw, label: "Reset", variant: .ghost) { reset() }
      }) {
          InspectorContent()
      }
    `,
  },
  toolbar: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/toolbar-light.png" alt="" loading="lazy" />,
    swift: code`
      DSToolbar {
          DSIconButton(StrokeIcon.folder, label: "Media", variant: .ghost, isOn: showsMedia) { showsMedia.toggle() }
      } center: {
          DSIconButton(StrokeIcon.sparkles, label: "Assistant", variant: .ghost) { openAssistant() }
      } trailing: {
          DSButton("Export", icon: StrokeIcon.upload) { export() }
      }
    `,
  },
  disclosure: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/disclosure-light.png" alt="" loading="lazy" />,
    swift: code`
      DSDisclosure("Transform", isExpanded: $showsTransform) {
          DSSlider("Scale", value: $scale, in: 0...400, ticks: 0)
      }
    `,
  },
  "property-row": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/property-row-light.png" alt="" loading="lazy" />,
    swift: code`
      DSPropertyRow("Opacity") {
          DSSlider(value: $opacity, in: 0...100, ticks: 0, defaultValue: 100, editable: true,
                   onEditingChanged: { editing in if !editing { commitUndo() } })
      }
    `,
  },
  row: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/row-light.png" alt="" loading="lazy" />,
    swift: code`
      ForEach(items) { item in
          Text(item.name).dsRow(selected: item.id == selection)
              .onTapGesture { selection = item.id }
      }
    `,
  },
  menu: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/menu-light.png" alt="" loading="lazy" />,
    swift: code`
      DSMenu("More", trigger: .icon(StrokeIcon.ellipsis)) {
          Button("Rename") { rename() }
          Button("Duplicate") { duplicate() }
      }
    `,
  },
  "search-field": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/search-field-light.png" alt="" loading="lazy" />,
    swift: code`
      DSSearchField("Search media", text: $query)
    `,
  },
  "empty-state": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/empty-state-light.png" alt="" loading="lazy" />,
    swift: code`
      DSEmptyState("No media yet", message: "Drop video, audio or images here.", vector: Vector.mediaImport) {
          DSButton("Import media", icon: StrokeIcon.plus, variant: .secondary) { importMedia() }
      }
    `,
  },
  "data-mark": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/data-mark-light.png" alt="" loading="lazy" />,
    swift: code`
      Text(clip.name)
          .frame(width: width, height: 32, alignment: .leading)
          .dsDataMark(.pink, selected: isSelected)
    `,
  },
  fader: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/fader-light.png" alt="" loading="lazy" />,
    swift: code`
      DSFader("In", value: $input, level: inputLevel, defaultValue: 70,
              onEditingChanged: { editing in if !editing { commitUndo() } })
    `,
  },
  rack: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/rack-light.png" alt="" loading="lazy" />,
    swift: code`
      DSRack("Node 1 FX", pages: 4, page: $page) {
          HStack {
              DSKnob("Volume", value: $volume, size: .small, style: .arc)
              DSKnob("Pan", value: $pan, in: -100...100, size: .small, style: .arc, centered: true)
          }
      }
    `,
  },
  grid: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/grid-light.png" alt="" loading="lazy" />,
    swift: code`
      DSGrid(columns: 3) {
          DSGridHeader("Dynamics")
          DSKnob("Threshold", value: $threshold, style: .arc).dsSpan(1)
          DSKnob("Ratio", value: $ratio, style: .arc).dsSpan(1)
          DSKnob("Attack", value: $attack, style: .arc).dsSpan(1)
          DSPropertyRow("Mode") { DSSegmentedControl("Mode", selection: $mode, options: modes) }
      }
    `,
  },
  screen: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/screen-light.png" alt="" loading="lazy" />,
    swift: code`
      DSScreen {
          DSScreenTabs("Mode", selection: $mode, options: modes)
          DSScreenReadout("Req/s", value: "1,284")
          DSScreenBars(values: levels)
      }
    `,
  },
  "data-table": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/data-table-light.png" alt="" loading="lazy" />,
    swift: code`
      DSDataTable(columns: ["Project", "Branch", "Age"], rows: rows, active: playing)
    `,
  },
  drum: {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/drum-light.png" alt="" loading="lazy" />,
    swift: code`
      DSDrum("Sample rate", selection: $rate, options: rates)
    `,
  },
  "spec-list": {
    examples: [],
    card: () => <img className="site-swift-card" src="swift/spec-list-light.png" alt="" loading="lazy" />,
    swift: code`
      DSSpecList([
          .init("Format", value: "QuickTime · HEVC"),
          .init("Duration", value: "00:02:41"),
      ])
    `,
  },
};
