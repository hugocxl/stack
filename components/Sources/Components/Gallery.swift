import SwiftUI

/// A specimen of every component, by recipe name. Use it in Xcode previews to check the
/// components on a device; the website's Swift captures are rendered from it.
public enum DSGallery {
    /// The recipes that have a Swift implementation, in the website's order.
    public static let recipes: [String] = [
        "theme", "text",
        "button", "icon-button", "link",
        "text-field", "checkbox", "switch", "radio-group", "select", "segmented-control",
        "status", "notice", "dialog", "progress",
        "title", "statement", "meta", "section", "divider", "code-block", "list", "figure", "figure-grid",
        "page",
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
        case "button":
            HStack(spacing: DSSpace.s3) {
                DSButton("Get started", icon: StrokeIcon.arrowRight) {}
                DSButton("Read the docs", variant: .secondary) {}
            }
            HStack(spacing: DSSpace.s3) {
                DSButton("Edit", icon: StrokeIcon.pencil, variant: .ghost) {}
                DSButton("Disabled") {}.disabled(true)
            }
        case "icon-button":
            HStack(spacing: DSSpace.s3) {
                DSIconButton(StrokeIcon.arrowLeft, label: "Previous") {}
                DSIconButton(StrokeIcon.arrowRight, label: "Next") {}
                DSIconButton(StrokeIcon.close, label: "Close", variant: .ghost) {}
                DSIconButton(StrokeIcon.ellipsis, label: "More", variant: .ghost) {}
            }
        case "link":
            DSLink("Read the documentation", destination: URL(string: "https://hugocxl.github.io/stack/")!)
            DSLink("Changelog", destination: URL(string: "https://hugocxl.github.io/stack/")!, icon: StrokeIcon.bookOpen, variant: .standalone)
            DSLink("GitHub", destination: URL(string: "https://github.com/hugocxl/stack")!, variant: .standalone, external: true)
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
            DSSegmentedControl("Platform", selection: .constant("swift"), options: [
                DSOption("react", label: "React", icon: StrokeIcon.code),
                DSOption("swift", label: "Swift", icon: StrokeIcon.phone),
            ])
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
