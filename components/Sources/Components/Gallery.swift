import SwiftUI

/// A specimen of every component, by recipe name. Use it in Xcode previews to check the
/// components on a device; the website's Swift captures are rendered from it.
public enum DSGallery {
    /// The recipes that have a Swift implementation, in the website's order.
    public static let recipes: [String] = [
        "theme", "text", "density",
        "button", "icon-button", "link", "menu",
        "text-field", "search-field", "checkbox", "switch", "radio-group", "select", "segmented-control", "drum", "property-row",
        "meter", "knob", "slider", "fader", "slide-switch", "readout", "rack",
        "status", "notice", "dialog", "progress", "empty-state", "screen",
        "title", "statement", "meta", "section", "divider", "code-block", "list", "data-table", "spec-list", "row", "disclosure", "data-mark", "figure", "figure-grid",
        "page", "pane", "toolbar", "grid",
    ]

    /// The specimen for one recipe, on the canvas.
    @MainActor @ViewBuilder
    public static func specimen(_ recipe: String) -> some View {
        VStack(alignment: .leading, spacing: DSSpace.s5) {
            content(recipe)
        }
        .padding(DSSpace.s6)
        .frame(width: 440, alignment: .leading)
        .background(DSColor.canvas)
        .dsTheme()
    }

    @MainActor @ViewBuilder
    static func content(_ recipe: String) -> some View {
        switch recipe {
        case "theme":
            HStack(spacing: DSSpace.s3) {
                DSIconButton(StrokeIcon.contrast, label: "Switch theme") {}
                DSText("Light, dark or the system’s.", tone: .muted)
            }
        case "text":
            DSText("Title, the largest text", variant: .title)
            DSText("Reading type carries every screen.")
            DSText("Small supporting text, in muted.", variant: .small, tone: .muted)
            DSText("Label · 5 October 2026", variant: .label)
            DSText("npm install @hugocxl/components", variant: .mono)
        case "density":
            HStack(alignment: .top, spacing: DSSpace.s6) {
                VStack(alignment: .leading, spacing: DSSpace.s3) {
                    DSText("Regular", variant: .label)
                    DSButton("Export") {}
                    DSSwitch("Sounds", isOn: .constant(true))
                }
                VStack(alignment: .leading, spacing: DSSpace.s2) {
                    DSText("Compact", variant: .label)
                    DSButton("Export") {}
                    DSSwitch("Sounds", isOn: .constant(true))
                }
                .dsDensity(.compact)
            }
        case "button":
            HStack(spacing: DSSpace.s3) {
                DSButton("Get started", icon: StrokeIcon.arrowRight) {}
                DSButton("Read the docs", variant: .secondary) {}
            }
            HStack(spacing: DSSpace.s3) {
                DSButton("Edit", icon: StrokeIcon.pencil, variant: .ghost) {}
                DSButton("Disabled") {}.disabled(true)
            }
            HStack(spacing: DSSpace.s3) {
                DSButton("Delete clip", icon: StrokeIcon.trash, variant: .secondary, destructive: true) {}
                DSButton("Export", variant: .primary) {}.dsDensity(.compact)
            }
        case "icon-button":
            HStack(spacing: DSSpace.s3) {
                DSIconButton(StrokeIcon.arrowLeft, label: "Previous") {}
                DSIconButton(StrokeIcon.arrowRight, label: "Next") {}
                DSIconButton(StrokeIcon.close, label: "Close", variant: .ghost) {}
                DSIconButton(StrokeIcon.ellipsis, label: "More", variant: .ghost) {}
            }
            HStack(spacing: DSSpace.s1) {
                DSIconButton(StrokeIcon.layoutPanelLeft, label: "Browser", variant: .ghost, isOn: true) {}
                DSIconButton(StrokeIcon.layoutPanelTop, label: "Viewer", variant: .ghost, isOn: true) {}
                DSIconButton(StrokeIcon.sliders, label: "Inspector", variant: .ghost) {}
            }
            .dsDensity(.compact)
        case "link":
            DSLink("Read the documentation", destination: URL(string: "https://hugocxl.github.io/stack/")!)
            DSLink("Changelog", destination: URL(string: "https://hugocxl.github.io/stack/")!, icon: StrokeIcon.bookOpen, variant: .standalone)
            DSLink("GitHub", destination: URL(string: "https://github.com/hugocxl/stack")!, variant: .standalone, external: true)
        case "menu":
            HStack(spacing: DSSpace.s3) {
                DSMenu("Sort by") {
                    Button("Name") {}
                    Button("Date added") {}
                }
                DSMenu("More", trigger: .icon(StrokeIcon.ellipsis)) {
                    Button("Rename") {}
                    Button("Duplicate") {}
                }
            }
            .dsDensity(.compact)
        case "search-field":
            DSSearchField("Search media", text: .constant(""))
            DSSearchField("Search media", text: .constant("sunrise")).dsDensity(.compact)
        case "property-row":
            VStack(alignment: .leading, spacing: 0) {
                DSPropertyRow("Opacity") {
                    DSSlider(value: .constant(80), in: 0...100, ticks: 0) { "\(Int($0))%" }
                }
                DSPropertyRow("Blend") {
                    DSSelect("Blend", selection: .constant("normal"), options: [DSOption("normal", label: "Normal"), DSOption("screen", label: "Screen")], labelPlacement: .hidden)
                }
                DSPropertyRow("Name") {
                    DSTextField("Name", text: .constant("Sunrise"), labelPlacement: .hidden)
                }
            }
            .dsDensity(.compact)
        case "empty-state":
            DSEmptyState("No media yet", message: "Drop video, audio or images here, or import them from Finder.", vector: Vector.mediaImport) {
                DSButton("Import media", icon: StrokeIcon.plus, variant: .secondary) {}
            }
            .dsDensity(.compact)
        case "row":
            VStack(spacing: DSSpace.s1) {
                HStack { DSText("Sunrise.mov"); Spacer(); DSText("0:12", variant: .label) }.dsRow(selected: true)
                HStack { DSText("Lagoon.mov"); Spacer(); DSText("0:08", variant: .label) }.dsRow()
                HStack { DSText("Theme.wav"); Spacer(); DSText("2:41", variant: .label) }.dsRow()
            }
            .dsDensity(.compact)
        case "disclosure":
            VStack(alignment: .leading, spacing: 0) {
                DSDisclosure("Transform", isExpanded: .constant(true)) {
                    DSSlider("Scale", value: .constant(100), in: 0...400, ticks: 0) { "\(Int($0))%" }
                }
                DSDivider()
                DSDisclosure("Cropping", isExpanded: .constant(false)) { EmptyView() }
                DSDivider()
            }
            .dsDensity(.compact)
        case "data-mark":
            HStack(spacing: 2) {
                DSText("Sunrise", variant: .small).padding(.horizontal, DSSpace.s2).frame(width: 160, height: 32, alignment: .leading).dsDataMark(.pink)
                DSText("Lagoon", variant: .small).padding(.horizontal, DSSpace.s2).frame(width: 110, height: 32, alignment: .leading).dsDataMark(.teal, selected: true)
            }
            DSText("Contrast · Warmth", variant: .small).padding(.horizontal, DSSpace.s2).frame(width: 272, height: 24, alignment: .leading).dsDataMark(.violet)
        case "text-field":
            DSTextField("Email", text: .constant(""), placeholder: "you@example.com", help: "We only write when something ships.")
            DSTextField("Project name", text: .constant("fieldwork!"), error: "Use letters, numbers and dashes only.")
        case "checkbox":
            DSCheckbox("Send me release notes", isOn: .constant(true))
            DSCheckbox("Include pre-releases", isOn: .constant(false), description: "Betas ship every Tuesday.")
        case "switch":
            DSSwitch("Sounds", isOn: .constant(true), description: "Play a sound when a task finishes.")
            DSSwitch("Reduce motion", isOn: .constant(false))
        case "radio-group":
            DSRadioGroup("Plan", selection: .constant("team"), options: [
                DSOption("personal", label: "Personal", description: "For one person and their side projects."),
                DSOption("team", label: "Team", description: "Shared projects and roles."),
            ])
        case "select":
            DSSelect("Region", selection: .constant("eu"), options: [
                DSOption("eu", label: "Europe"),
                DSOption("us", label: "United States"),
                DSOption("ap", label: "Asia Pacific"),
            ], help: "Where your data is stored.")
        case "segmented-control":
            DSSegmentedControl("Period", selection: .constant("week"), options: [
                DSOption("day", label: "Day"),
                DSOption("week", label: "Week"),
                DSOption("month", label: "Month"),
            ])
            DSSegmentedControl("Pattern", selection: .constant(1), options: [
                DSOption(1, label: "1"), DSOption(2, label: "2"), DSOption(3, label: "3"), DSOption(4, label: "4"),
            ], indicator: .leds)
            DSSegmentedControl("Platform", selection: .constant("swift"), options: [
                DSOption("react", label: "React", icon: StrokeIcon.code),
                DSOption("swift", label: "Swift", icon: StrokeIcon.phone),
            ])
        case "meter":
            DSMeter(value: 0.68, label: "CPU")
            DSMeter(value: 0.42, label: "Input", segments: 16, variant: .dots)
            DSMeter(value: 0.91, label: "Storage", tone: .warning) { "\(Int(($0 * 64).rounded())) of 64 GB" }
        case "knob":
            HStack(spacing: DSSpace.s3) {
                DSKnob("Tone", value: .constant(30))
                DSKnob("Drive", value: .constant(72))
                DSKnob("Space", value: .constant(50))
                DSKnob("Mix", value: .constant(18))
            }
            HStack(spacing: DSSpace.s3) {
                DSKnob("Heat", value: .constant(62), style: .arc)
                DSKnob("Ignite", value: .constant(40), size: .large, style: .arc)
                DSKnob("Tint", value: .constant(-30), in: -100...100, style: .arc, centered: true)
            }
        case "slider":
            DSSlider("Volume", value: .constant(64), in: 0...127, ticks: 33, majorEvery: 4)
            DSSlider("Exposure", value: .constant(4.0 / 3), in: -3...3, step: 1.0 / 3, ticks: 19, majorEvery: 3, centered: true) { _ in "+1 ⅓" }
        case "fader":
            HStack(alignment: .bottom, spacing: DSSpace.s6) {
                DSFader("In", value: .constant(72), level: 0.64)
                DSFader("Out", value: .constant(58), level: 0.48)
                DSFader("Mix", value: .constant(40))
                DSFader("Fbk", value: .constant(24))
            }
            .dsDensity(.compact)
        case "rack":
            DSRack("Node 1 FX", pages: 4, page: .constant(0)) {
                HStack(spacing: DSSpace.s2) {
                    DSKnob("Volume", value: .constant(70), size: .small, style: .arc)
                    DSKnob("Pan", value: .constant(-20), in: -100...100, size: .small, style: .arc, centered: true)
                    DSKnob("Drive", value: .constant(35), size: .small, style: .arc)
                    DSKnob("Reverb", value: .constant(55), size: .small, style: .arc)
                }
            }
            .dsDensity(.compact)
        case "slide-switch":
            HStack(alignment: .top, spacing: DSSpace.s7) {
                DSSlideSwitch("Output", selection: .constant("cue"), options: [
                    DSOption("main", label: "Main"), DSOption("cue", label: "Cue"), DSOption("both", label: "Both"),
                ])
                DSSlideSwitch("Quality", selection: .constant("mid"), options: [
                    DSOption("lo", label: "Lo"), DSOption("mid", label: "Mid"), DSOption("hi", label: "Hi"),
                ], orientation: .horizontal)
            }
        case "readout":
            DSReadoutGrid(columns: 3) {
                DSReadout("Lens", value: "24", unit: "mm")
                DSReadout("Mode", value: "Auto", live: true)
                DSReadout("Preset", value: "Off", dim: true)
                DSReadout("Speed", value: "1/125", selected: true) {}
                DSReadout("ISO", value: "250") {}
                DSReadout("WB", value: "5600", unit: "K") {}
            }
        case "status":
            HStack(spacing: DSSpace.s5) {
                DSStatus("Beta")
                DSStatus("Operational", tone: .success)
                DSStatus("Degraded", tone: .warning)
            }
            HStack(spacing: DSSpace.s5) {
                DSStatus("Down", tone: .error, mark: .icon)
                DSStatus("Scheduled", tone: .info, mark: .icon)
                DSStatus("Draft", tone: .neutral)
            }
            DSStatus("All systems operational", tone: .success, mark: .icon, appearance: .text)
        case "notice":
            DSNotice("Your changes are live.", message: "It can take a minute to reach every region.", tone: .success, onDismiss: {})
            DSNotice("The import failed.", message: "Three rows have no email. Fix them and try again.", tone: .error) {
                DSButton("Download the rows", variant: .ghost) {}
            }
        case "dialog":
            DSDialog("Delete this project?", description: "Its pages and history go with it. This cannot be undone.", onClose: {}) {
                DSButton("Cancel", variant: .secondary) {}
                DSButton("Delete project") {}
            }
        case "progress":
            DSProgress(value: 0.64, label: "Uploading 3 files")
            DSProgress(label: "Preparing the export")
        case "title":
            DSTitle("Public testing is beginning", byline: "Fieldwork team")
        case "statement":
            DSStatement("Field notes for teams that ship", accent: "every day.")
        case "meta":
            DSMeta([.status("Beta", .accent), .text("Version 0.4"), .text("5 October 2026")])
        case "section":
            DSSection("What is available") {
                DSText(Text("Testing is limited to the macOS app. ") + Text("Linux and Windows follow once the first wave is stable.").foregroundColor(DSColor.muted))
            }
        case "divider":
            DSText("Above the hairline")
            DSDivider()
            DSText("Below the hairline")
        case "code-block":
            DSCodeBlock("npm install @hugocxl/components\nimport \"@hugocxl/components/styles.css\"", label: "Terminal")
        case "list":
            DSList([
                DSListItem("Components", label: "0.1.0", description: "Buttons, fields and feedback for React and Swift."),
                DSListItem("Notifications", label: "Settings", trailing: "On") {},
                DSListItem("Billing", label: "Settings", trailing: "Team") {},
            ])
        case "figure":
            DSFigure(Vector.howItWorks, caption: "Fig. 01 / How it works", title: "How it works")
        case "figure-grid":
            DSFigureGrid([
                DSFigureGridItem("Purpose-built", vector: Vector.modularDesign, text: "Shaped by teams who ship daily."),
                DSFigureGridItem("Designed for speed", vector: Vector.fastPerformance, text: "Less noise, more momentum."),
            ])
        case "page":
            VStack(alignment: .leading, spacing: 0) {
                DSStatement("Field notes for teams that ship", accent: "every day.")
                DSMeta([.status("Beta", .accent), .text("5 October 2026")])
                DSSection {
                    DSText("A screen is the canvas, a 20pt gutter and the reading column.")
                }
                DSButton("Get started", fullWidth: true) {}.padding(.top, DSSpace.s7)
            }
        case "pane":
            DSPane("Inspector", icon: StrokeIcon.sliders, accessories: {
                DSIconButton(StrokeIcon.refreshCcw, label: "Reset", variant: .ghost) {}
                DSMenu("More", trigger: .icon(StrokeIcon.ellipsis)) { Button("Move to the left") {} }
            }) {
                VStack(alignment: .leading, spacing: 0) {
                    DSPropertyRow("Opacity") { DSSlider(value: .constant(100), in: 0...100, ticks: 0) { "\(Int($0))%" } }
                    DSPropertyRow("Speed") { DSSlider(value: .constant(1), in: 0.25...4, step: 0.25, ticks: 0) { String(format: "%.2f×", $0) } }
                }
                .padding(.horizontal, DSSpace.s3)
            }
            .frame(height: 140)
            .overlay(Rectangle().strokeBorder(DSColor.rule, lineWidth: 1))
            .dsDensity(.compact)
        case "screen":
            DSScreen {
                DSScreenTabs("Mode", selection: .constant(0), options: [DSOption(0, label: "Overview"), DSOption(1, label: "Deploys"), DSOption(2, label: "Logs")])
                HStack(spacing: DSSpace.s4) {
                    DSScreenReadout("Req/s", value: "1,284")
                    DSScreenReadout("Errors", value: "0.21", unit: "%")
                    DSScreenReadout("P95", value: "182", unit: "ms")
                }
                DSScreenBars(values: [0.3, 0.35, 0.55, 0.7, 0.75, 0.62, 0.58, 0.66, 0.5, 0.42, 0.48, 0.6])
            }
            .dsDensity(.compact)
        case "spec-list":
            DSSpecList([
                .init("Format", value: "QuickTime · HEVC"),
                .init("Resolution", value: "3840 × 2160"),
                .init("Duration", value: "00:02:41"),
                .init("Audio", value: "48 kHz · stereo"),
            ])
            .dsDensity(.compact)
        case "data-table":
            DSDataTable(columns: ["Project", "Branch", "Age"], rows: [
                ["checkout-api", "main", "4m"], ["web", "feat/search", "9m"], ["docs", "main", "1h"],
            ], active: 0)
            .dsDensity(.compact)
        case "drum":
            DSDrum("Sample rate", selection: .constant(48), options: [
                DSOption(44, label: "44.1 kHz"), DSOption(47, label: "47.25 kHz"), DSOption(48, label: "48 kHz"),
                DSOption(50, label: "50 kHz"), DSOption(50.4, label: "50.4 kHz"),
            ])
            .frame(width: 180)
            .dsDensity(.compact)
        case "grid":
            DSGrid(columns: 3) {
                DSGridHeader("Dynamics")
                DSKnob("Threshold", value: .constant(-18), in: -40 ... -3, step: 0, style: .arc).dsSpan(1)
                DSKnob("Ratio", value: .constant(2.5), in: 1...8, step: 0, style: .arc).dsSpan(1)
                DSKnob("Attack", value: .constant(10), in: 1...100, style: .arc).dsSpan(1)
                DSPropertyRow("Mode") {
                    DSSegmentedControl("Mode", selection: .constant(1), options: [DSOption(0, label: "Auto"), DSOption(1, label: "Manual")])
                }
                DSSwitch("Clicks", isOn: .constant(true))
            }
            .frame(width: 360)
            .overlay(Rectangle().strokeBorder(DSColor.rule, lineWidth: 1))
            .dsDensity(.compact)
        case "toolbar":
            DSToolbar {
                DSIconButton(StrokeIcon.folder, label: "Media", variant: .ghost, isOn: true) {}
                DSIconButton(StrokeIcon.star, label: "Selects", variant: .ghost) {}
            } center: {
                DSIconButton(StrokeIcon.layoutPanelTop, label: "Viewer", variant: .ghost, isOn: true) {}
                DSIconButton(StrokeIcon.sliders, label: "Inspector", variant: .ghost, isOn: true) {}
                DSToolbarDivider()
                DSIconButton(StrokeIcon.sparkles, label: "Assistant", variant: .ghost) {}
            } trailing: {
                DSButton("Export", icon: StrokeIcon.upload) {}
            }
            .dsDensity(.compact)
        default:
            DSText("No specimen for \(recipe)", tone: .muted)
        }
    }
}

#if DEBUG
struct DSGallery_Previews: PreviewProvider {
    static var previews: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 0) {
                ForEach(DSGallery.recipes, id: \.self) { recipe in
                    DSText(recipe, variant: .label).padding(.horizontal, DSSpace.s6).padding(.top, DSSpace.s6)
                    DSGallery.specimen(recipe)
                }
            }
        }
        .background(DSColor.canvas)
    }
}
#endif
