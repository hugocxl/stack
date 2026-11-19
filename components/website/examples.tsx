// Live examples for every recipe: the React specimen, its code, and the Swift code that
// draws the same thing (the Swift captures come from DSGallery in Sources/Components).
import { useState, type ReactNode } from "react";
import {
  Button,
  ButtonGroup,
  Checkbox,
  CodeBlock,
  Dialog,
  Divider,
  Figure,
  FigureGrid,
  IconButton,
  Link,
  List,
  Meta,
  Muted,
  Notice,
  Progress,
  RadioGroup,
  Section,
  SegmentedControl,
  Select,
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

export type RecipeExamples = { examples: Example[]; swift?: string };

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

export const examples: Record<string, RecipeExamples> = {
  theme: {
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
        render: () => <Text tone="muted">The masthead at the top of this page.</Text>,
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
        render: () => <Text tone="muted">The footer at the end of this page.</Text>,
        react: code`
          <Footer
            links={[{ label: "Docs", href: "/docs" }, { label: "Changelog", href: "/changelog" }]}
            secondary={[{ label: "npm", href: "…" }, { label: "GitHub", href: "…" }]} />
        `,
      },
    ],
  },
};
