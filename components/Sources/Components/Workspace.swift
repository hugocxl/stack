import SwiftUI

// Components for product interfaces: tools people work in, made of panes on one canvas. They
// follow the same rules as pages: flat, hairlines instead of boxes, mono labels, ink as the only
// emphasis. Set `.dsDensity(.compact)` at the root of a desktop tool.

// MARK: - Pane

/// A pane's name: an optional muted icon, the mono label and an optional subtitle.
public struct DSPaneTitle: View {
    let title: Text
    let icon: (any IconResource)?
    let subtitle: String?

    public init(_ title: Text, icon: (any IconResource)? = nil, subtitle: String? = nil) {
        self.title = title
        self.icon = icon
        self.subtitle = subtitle
    }

    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, subtitle: String? = nil) {
        self.init(Text(title), icon: icon, subtitle: subtitle)
    }

    public var body: some View {
        HStack(spacing: DSSpace.s2) {
            if let icon { DSIconImage(icon: icon).foregroundColor(DSColor.muted) }
            DSText(title, variant: .label)
                .lineLimit(1)
                .accessibilityAddTraits(.isHeader)
            if let subtitle { DSText(subtitle, variant: .label, tone: .ink).lineLimit(1) }
        }
    }
}

/// The bar on top of a pane: its title and trailing tools, over a hairline. The title is a view,
/// so a workspace can make it the handle people drag the pane by.
public struct DSPaneHeader<Title: View, Accessories: View>: View {
    let title: Title
    let accessories: Accessories
    @Environment(\.dsDensity) private var density

    public init(@ViewBuilder title: () -> Title, @ViewBuilder accessories: () -> Accessories) {
        self.title = title()
        self.accessories = accessories()
    }

    public var body: some View {
        let metrics = density.metrics
        HStack(spacing: metrics.gap) {
            title
                .frame(minWidth: metrics.control, maxWidth: .infinity, alignment: .leading)
            // Tools scroll instead of clipping when the pane gets narrow.
            if #available(iOS 16, macOS 13, tvOS 16, watchOS 9, *) {
                ViewThatFits(in: .horizontal) {
                    HStack(spacing: DSSpace.s1) { accessories }.fixedSize(horizontal: true, vertical: false)
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: DSSpace.s1) { accessories }
                    }
                }
            } else {
                HStack(spacing: DSSpace.s1) { accessories }
            }
        }
        .padding(.horizontal, density.metrics.unit)
        .frame(height: metrics.bar)
        .overlay(alignment: .bottom) { DSDivider() }
    }
}

extension DSPaneHeader where Title == DSPaneTitle {
    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder accessories: () -> Accessories) {
        self.init(Text(title), icon: icon, subtitle: subtitle, accessories: accessories)
    }

    @_disfavoredOverload
    public init(_ title: String, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder accessories: () -> Accessories) {
        self.init(Text(verbatim: title), icon: icon, subtitle: subtitle, accessories: accessories)
    }

    public init(_ title: Text, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder accessories: () -> Accessories) {
        self.init(title: { DSPaneTitle(title, icon: icon, subtitle: subtitle) }, accessories: accessories)
    }
}

extension DSPaneHeader where Title == DSPaneTitle, Accessories == EmptyView {
    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, subtitle: String? = nil) {
        self.init(Text(title), icon: icon, subtitle: subtitle) { EmptyView() }
    }
}

/// One cell of a workspace: a header and its content on the canvas. Panes have no corners, no
/// fill of their own and no shadow; the workspace divides them with one hairline.
public struct DSPane<Accessories: View, Content: View>: View {
    let title: Text
    let icon: (any IconResource)?
    let subtitle: String?
    let accessories: Accessories
    let content: Content

    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.init(Text(title), icon: icon, subtitle: subtitle, accessories: accessories, content: content)
    }

    public init(_ title: Text, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.title = title
        self.icon = icon
        self.subtitle = subtitle
        self.accessories = accessories()
        self.content = content()
    }

    public var body: some View {
        VStack(spacing: 0) {
            DSPaneHeader(title, icon: icon, subtitle: subtitle) { accessories }
            content.frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
        }
        .background(DSColor.canvas)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(title)
    }
}

extension DSPane where Accessories == EmptyView {
    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, subtitle: String? = nil, @ViewBuilder content: () -> Content) {
        self.init(title, icon: icon, subtitle: subtitle, accessories: { EmptyView() }, content: content)
    }
}

// MARK: - Toolbar

/// The row of tools above a workspace: leading, centered and trailing groups over a hairline.
public struct DSToolbar<Leading: View, Center: View, Trailing: View>: View {
    let leading: Leading
    let center: Center
    let trailing: Trailing
    @Environment(\.dsDensity) private var density

    public init(@ViewBuilder leading: () -> Leading, @ViewBuilder center: () -> Center, @ViewBuilder trailing: () -> Trailing) {
        self.leading = leading()
        self.center = center()
        self.trailing = trailing()
    }

    public var body: some View {
        let metrics = density.metrics
        ZStack {
            HStack(spacing: DSSpace.s1) {
                leading
                Spacer(minLength: metrics.gap)
                trailing
            }
            HStack(spacing: DSSpace.s1) { center }
        }
        .padding(.horizontal, density.metrics.unit)
        .frame(height: metrics.bar + (density == .regular ? 0 : DSSpace.s2))
        .overlay(alignment: .bottom) { DSDivider() }
        .accessibilityElement(children: .contain)
    }
}

/// A hairline between groups of tools in a toolbar or pane header.
public struct DSToolbarDivider: View {
    @Environment(\.dsDensity) private var density
    public init() {}

    public var body: some View {
        Rectangle().fill(DSColor.rule).frame(width: 1, height: density.metrics.control / 2)
            .padding(.horizontal, DSSpace.s1)
            .accessibilityHidden(true)
    }
}

// MARK: - Disclosure

/// A group people open and close: a chevron and a heading over its content, between hairlines.
public struct DSDisclosure<Accessories: View, Content: View>: View {
    let title: Text
    @Binding var isExpanded: Bool
    let accessories: Accessories
    let content: Content
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    public init(_ title: LocalizedStringKey, isExpanded: Binding<Bool>, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.init(Text(title), isExpanded: isExpanded, accessories: accessories, content: content)
    }

    @_disfavoredOverload
    public init(_ title: String, isExpanded: Binding<Bool>, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.init(Text(verbatim: title), isExpanded: isExpanded, accessories: accessories, content: content)
    }

    public init(_ title: Text, isExpanded: Binding<Bool>, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.title = title
        self._isExpanded = isExpanded
        self.accessories = accessories()
        self.content = content()
    }

    public var body: some View {
        let metrics = density.metrics
        VStack(alignment: .leading, spacing: 0) {
            HStack(spacing: DSSpace.s2) {
                Button {
                    isExpanded.toggle()
                    if sounds { DSSounds.shared.play(.tick) }
                } label: {
                    HStack(spacing: DSSpace.s2) {
                        DSIconImage(icon: StrokeIcon.chevronRight, size: metrics.icon - 2)
                            .foregroundColor(DSColor.muted)
                            .rotationEffect(.degrees(isExpanded ? 90 : 0))
                        DSText(title, variant: density == .regular ? .heading : .label, tone: density == .regular ? .muted : nil)
                            .lineLimit(1)
                        Spacer(minLength: 0)
                    }
                    .frame(height: metrics.control)
                    .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityAddTraits(.isHeader)
                .accessibilityValue(Text(isExpanded ? "Expanded" : "Collapsed"))
                accessories
            }
            if isExpanded {
                VStack(alignment: .leading, spacing: metrics.stack) { content }
                    .padding(.bottom, metrics.stack)
                    .transition(.opacity)
            }
        }
        .animation(.easeOut(duration: 0.16), value: isExpanded)
    }
}

extension DSDisclosure where Accessories == EmptyView {
    public init(_ title: LocalizedStringKey, isExpanded: Binding<Bool>, @ViewBuilder content: () -> Content) {
        self.init(title, isExpanded: isExpanded, accessories: { EmptyView() }, content: content)
    }
}

#if os(iOS) || os(macOS) || os(visionOS)
/// The disclosure recipe as a DisclosureGroupStyle, for any SwiftUI DisclosureGroup.
@available(iOS 16, macOS 13, *)
public struct DSDisclosureGroupStyle: DisclosureGroupStyle {
    public init() {}

    public func makeBody(configuration: Configuration) -> some View {
        DSDisclosureGroupBody(configuration: configuration)
    }
}

@available(iOS 16, macOS 13, *)
private struct DSDisclosureGroupBody: View {
    let configuration: DisclosureGroupStyleConfiguration
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    var body: some View {
        let metrics = density.metrics
        VStack(alignment: .leading, spacing: 0) {
            Button {
                configuration.isExpanded.toggle()
                if sounds { DSSounds.shared.play(.tick) }
            } label: {
                HStack(spacing: DSSpace.s2) {
                    DSIconImage(icon: StrokeIcon.chevronRight, size: metrics.icon - 2)
                        .foregroundColor(DSColor.muted)
                        .rotationEffect(.degrees(configuration.isExpanded ? 90 : 0))
                    configuration.label
                        .font(DSFont.of(.reading, density))
                        .foregroundColor(DSColor.ink)
                    Spacer(minLength: 0)
                }
                .frame(height: metrics.control)
                .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            .accessibilityValue(Text(configuration.isExpanded ? "Expanded" : "Collapsed"))
            if configuration.isExpanded {
                VStack(alignment: .leading, spacing: metrics.stack) { configuration.content }
                    .padding(.leading, metrics.icon + DSSpace.s2)
                    .padding(.bottom, metrics.row)
            }
        }
    }
}

@available(iOS 16, macOS 13, *)
extension DisclosureGroupStyle where Self == DSDisclosureGroupStyle {
    /// The design-system disclosure: `.disclosureGroupStyle(.ds)`.
    public static var ds: DSDisclosureGroupStyle { DSDisclosureGroupStyle() }
}
#endif

// MARK: - Property row

private struct DSPropertyLabelWidthKey: EnvironmentKey {
    static let defaultValue: CGFloat? = nil
}

extension EnvironmentValues {
    /// The width of property labels in a group, so their controls line up.
    public var dsPropertyLabelWidth: CGFloat? {
        get { self[DSPropertyLabelWidthKey.self] }
        set { self[DSPropertyLabelWidthKey.self] = newValue }
    }
}

/// A setting in an inspector: a small muted label beside its control, on one line.
public struct DSPropertyRow<Content: View>: View {
    let label: Text
    let content: Content
    @Environment(\.dsDensity) private var density
    @Environment(\.dsPropertyLabelWidth) private var labelWidth

    public init(_ label: LocalizedStringKey, @ViewBuilder content: () -> Content) {
        self.init(Text(label), content: content)
    }

    @_disfavoredOverload
    public init(_ label: String, @ViewBuilder content: () -> Content) {
        self.init(Text(verbatim: label), content: content)
    }

    public init(_ label: Text, @ViewBuilder content: () -> Content) {
        self.label = label
        self.content = content()
    }

    @Environment(\.dsInGrid) private var inGrid

    public var body: some View {
        let metrics = density.metrics
        if inGrid {
            // In a grid the row is a cell: its label top-left, the control one unit below.
            VStack(alignment: .leading, spacing: metrics.unit) {
                DSText(label, variant: .label).lineLimit(1).accessibilityHidden(true)
                content.frame(maxWidth: .infinity, alignment: .leading).accessibilityLabel(label)
            }
            .accessibilityElement(children: .contain)
        } else {
            row(metrics)
        }
    }

    private func row(_ metrics: DSMetrics) -> some View {
        HStack(spacing: metrics.gap) {
            DSText(label, variant: .small, tone: .muted)
                .lineLimit(1)
                .frame(width: labelWidth ?? (density == .regular ? 140 : 88), alignment: .leading)
                .accessibilityHidden(true)
            content
                .frame(maxWidth: .infinity, alignment: .leading)
                .accessibilityLabel(label)
        }
        .frame(minHeight: metrics.control)
        .accessibilityElement(children: .contain)
    }
}

/// The property row recipe as a LabeledContentStyle, for any SwiftUI LabeledContent.
@available(iOS 16, macOS 13, tvOS 16, watchOS 9, *)
public struct DSLabeledContentStyle: LabeledContentStyle {
    public init() {}

    public func makeBody(configuration: Configuration) -> some View {
        DSLabeledContentBody(configuration: configuration)
    }
}

@available(iOS 16, macOS 13, tvOS 16, watchOS 9, *)
private struct DSLabeledContentBody: View {
    let configuration: LabeledContentStyleConfiguration
    @Environment(\.dsDensity) private var density
    @Environment(\.dsPropertyLabelWidth) private var labelWidth

    var body: some View {
        let metrics = density.metrics
        HStack(spacing: metrics.gap) {
            configuration.label
                .font(DSFont.of(.small, density))
                .foregroundColor(DSColor.muted)
                .lineLimit(1)
                .frame(width: labelWidth ?? (density == .regular ? 140 : 88), alignment: .leading)
            configuration.content
                .font(DSFont.of(.reading, density))
                .foregroundColor(DSColor.ink)
                .frame(maxWidth: .infinity, alignment: .leading)
        }
        .frame(minHeight: metrics.control)
    }
}

@available(iOS 16, macOS 13, tvOS 16, watchOS 9, *)
extension LabeledContentStyle where Self == DSLabeledContentStyle {
    /// The design-system property row: `.labeledContentStyle(.ds)`.
    public static var ds: DSLabeledContentStyle { DSLabeledContentStyle() }
}

// MARK: - Selectable row

/// A row people pick in a sidebar, a browser or a menu-like list: the surface under the pointer
/// and under the selection. Selection never uses the accent.
public struct DSRowStyle: ViewModifier {
    let isSelected: Bool
    @State private var hovered = false
    @Environment(\.dsDensity) private var density

    public init(isSelected: Bool = false) { self.isSelected = isSelected }

    public func body(content: Content) -> some View {
        content
            .padding(.horizontal, density.metrics.unit)
            .frame(minHeight: density.metrics.control)
            .background(
                RoundedRectangle(cornerRadius: DSRadius.control)
                    .fill(isSelected ? DSColor.surface : (hovered ? DSColor.surface.opacity(0.6) : .clear))
            )
            .contentShape(RoundedRectangle(cornerRadius: DSRadius.control))
            .onHover { hovered = $0 }
            .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}

extension View {
    /// Style a view as a selectable row.
    public func dsRow(selected: Bool = false) -> some View { modifier(DSRowStyle(isSelected: selected)) }
}

// MARK: - Menu

/// How a menu's trigger looks.
public enum DSMenuTrigger: Sendable {
    /// An icon alone, as an icon button, with its label as tooltip.
    case icon(any IconResource)
    /// Words with a chevron, as a ghost button.
    case text
}

/// Opens a list of actions with the platform's own menu, from an icon or a ghost button.
public struct DSMenu<Content: View>: View {
    let label: String
    let trigger: DSMenuTrigger
    let content: Content
    @Environment(\.dsDensity) private var density
    @Environment(\.dsStaticRendering) private var staticRendering

    public init(_ label: String, trigger: DSMenuTrigger = .text, @ViewBuilder content: () -> Content) {
        self.label = label
        self.trigger = trigger
        self.content = content()
    }

    public var body: some View {
        #if os(iOS) || os(macOS) || os(visionOS)
        if staticRendering {
            triggerView
        } else {
            menu
        }
        #else
        triggerView
        #endif
    }

    #if os(iOS) || os(macOS) || os(visionOS)
    private var menu: some View {
        Menu { content } label: { triggerView }
            .dsMenuTrigger()
            .fixedSize()
            .accessibilityLabel(Text(label))
            .help(Text(label))
    }
    #endif

    @ViewBuilder private var triggerView: some View {
        let metrics = density.metrics
        switch trigger {
        case let .icon(icon):
            DSIconImage(icon: icon)
                .foregroundColor(DSColor.muted)
                .frame(width: metrics.control, height: metrics.control)
                .contentShape(Circle())
        case .text:
            HStack(spacing: DSSpace.s1) {
                Text(label).font(DSFont.of(.control, density)).foregroundColor(DSColor.ink)
                DSIconImage(icon: StrokeIcon.chevronDown, size: metrics.icon - 2).foregroundColor(DSColor.muted)
            }
            .padding(.horizontal, DSSpace.s2)
            .frame(height: metrics.control)
            .contentShape(Rectangle())
        }
    }
}

// MARK: - Search field

/// Filters what is on screen as people type: a search icon, the field and a clear button.
public struct DSSearchField: View {
    let label: String
    @Binding var text: String
    let placeholder: String?

    public init(_ label: String = "Search", text: Binding<String>, placeholder: String? = nil) {
        self.label = label
        self._text = text
        self.placeholder = placeholder
    }

    public var body: some View {
        DSTextField(label, text: $text, placeholder: placeholder ?? label, labelPlacement: .hidden, icon: StrokeIcon.search) {
            if !text.isEmpty {
                Button { text = "" } label: { DSIconImage(icon: StrokeIcon.circleX).foregroundColor(DSColor.muted) }
                    .buttonStyle(.plain)
                    .accessibilityLabel(Text("Clear"))
                    .help(Text("Clear"))
            }
        }
    }
}

// MARK: - Empty state

/// What a pane shows when it has nothing yet: a vector, a title, one sentence and the action that
/// fills it.
public struct DSEmptyState<Action: View>: View {
    let vector: (any VectorResource)?
    let title: Text
    let message: Text?
    let action: Action
    @Environment(\.dsDensity) private var density

    public init(_ title: LocalizedStringKey, message: LocalizedStringKey? = nil, vector: (any VectorResource)? = nil, @ViewBuilder action: () -> Action) {
        self.init(Text(title), message: message.map { Text($0) }, vector: vector, action: action)
    }

    public init(_ title: Text, message: Text? = nil, vector: (any VectorResource)? = nil, @ViewBuilder action: () -> Action) {
        self.vector = vector
        self.title = title
        self.message = message
        self.action = action()
    }

    public var body: some View {
        let metrics = density.metrics
        VStack(alignment: .leading, spacing: 0) {
            if let vector {
                vector.image.resizable().scaledToFit()
                    .foregroundColor(DSColor.ink)
                    .frame(maxWidth: density == .regular ? 280 : 200)
                    .padding(.bottom, metrics.stack)
                    .accessibilityHidden(true)
            }
            DSText(title, variant: .heading)
                .accessibilityAddTraits(.isHeader)
            if let message {
                DSText(message, variant: .small, tone: .muted).padding(.top, DSSpace.s2)
            }
            action.padding(.top, metrics.stack)
        }
        .frame(maxWidth: density == .regular ? DSLayout.measure : 320, alignment: .leading)
        .padding(metrics.stack)
        .accessibilityElement(children: .contain)
    }
}

extension DSEmptyState where Action == EmptyView {
    public init(_ title: LocalizedStringKey, message: LocalizedStringKey? = nil, vector: (any VectorResource)? = nil) {
        self.init(title, message: message, vector: vector) { EmptyView() }
    }

    public init(_ title: Text, message: Text? = nil, vector: (any VectorResource)? = nil) {
        self.init(title, message: message, vector: vector) { EmptyView() }
    }
}

// MARK: - Data marks

/// The eleven hues, for marks that name a kind of thing.
public enum DSHue: String, CaseIterable, Sendable {
    case red, orange, yellow, green, teal, sky, blue, violet, purple, pink, brown

    public var token: DSColorToken {
        switch self {
        case .red: return DSColorTokens.red
        case .orange: return DSColorTokens.orange
        case .yellow: return DSColorTokens.yellow
        case .green: return DSColorTokens.green
        case .teal: return DSColorTokens.teal
        case .sky: return DSColorTokens.sky
        case .blue: return DSColorTokens.blue
        case .violet: return DSColorTokens.violet
        case .purple: return DSColorTokens.purple
        case .pink: return DSColorTokens.pink
        case .brown: return DSColorTokens.brown
        }
    }

    public var color: Color { token.color }
}

/// A data mark: an item in a timeline, a track or a chart that a hue names the kind of. The fill
/// is the hue at 16% on the surface with a 1px hue edge; selected, the edge turns ink and 2px.
/// Its words stay ink, and they always say what the color means.
public struct DSDataMark: ViewModifier {
    let hue: DSHue?
    let isSelected: Bool

    public init(hue: DSHue?, isSelected: Bool = false) {
        self.hue = hue
        self.isSelected = isSelected
    }

    public func body(content: Content) -> some View {
        let tint = hue?.color ?? DSColor.muted
        content
            .background(
                RoundedRectangle(cornerRadius: DSSpace.s1)
                    .fill(DSColor.surface)
                    .overlay(RoundedRectangle(cornerRadius: DSSpace.s1).fill(tint.opacity(0.16)))
            )
            .overlay(
                RoundedRectangle(cornerRadius: DSSpace.s1)
                    .strokeBorder(isSelected ? DSColor.ink : tint.opacity(0.7), lineWidth: isSelected ? 2 : 1)
            )
            .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}

extension View {
    /// Draw this view as a data mark of a hue.
    public func dsDataMark(_ hue: DSHue?, selected: Bool = false) -> some View {
        modifier(DSDataMark(hue: hue, isSelected: selected))
    }
}

// MARK: - Rack

/// A bay of instruments, as on a hardware rack or a plugin: an inset well that holds a group of
/// knobs, faders or meters, with its name on a raised tab across the top edge. With pages, the
/// tab steps through them and dots show where you are.
public struct DSRack<Content: View>: View {
    let title: Text
    let pages: Int
    let page: Binding<Int>?
    let content: Content
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    public init(_ title: LocalizedStringKey, pages: Int = 1, page: Binding<Int>? = nil, @ViewBuilder content: () -> Content) {
        self.init(title: Text(title), pages: pages, page: page, content: content)
    }

    public init(title: Text, pages: Int = 1, page: Binding<Int>? = nil, @ViewBuilder content: () -> Content) {
        self.title = title
        self.pages = max(1, pages)
        self.page = page
        self.content = content()
    }

    private var paged: Bool { pages > 1 && page != nil }

    private func go(_ delta: Int) {
        guard let page else { return }
        let next = min(pages - 1, max(0, page.wrappedValue + delta))
        guard next != page.wrappedValue else { return }
        if sounds { DSSounds.shared.play(.tick) }
        page.wrappedValue = next
    }

    public var body: some View {
        let metrics = density.metrics
        let tab = metrics.control
        VStack(spacing: metrics.stack) {
            content
            if paged, let page {
                HStack(spacing: DSSpace.s2) {
                    ForEach(0..<pages, id: \.self) { index in
                        Circle()
                            .fill(index == page.wrappedValue ? DSColor.ink : .clear)
                            .overlay(Circle().strokeBorder(DSColor.ruleStrong, lineWidth: 1))
                            .frame(width: 6, height: 6)
                    }
                }
                .accessibilityHidden(true)
            }
        }
        .frame(maxWidth: .infinity)
        .padding(.horizontal, metrics.stack)
        .padding(.top, tab / 2 + metrics.stack)
        .padding(.bottom, metrics.stack)
        // A hairline frame; the name sits in a notch cut into its top edge.
        .overlay(RoundedRectangle(cornerRadius: DSRadius.media).strokeBorder(DSColor.rule, lineWidth: 1))
        .overlay(alignment: .top) {
            HStack(spacing: DSSpace.s1) {
                if paged {
                    pageButton(StrokeIcon.chevronLeft, "Previous page", -1)
                }
                DSText(title, variant: .label, tone: .ink).lineLimit(1)
                    .accessibilityAddTraits(.isHeader)
                if paged {
                    pageButton(StrokeIcon.chevronRight, "Next page", 1)
                }
            }
            .padding(.horizontal, DSSpace.s3)
            .frame(height: tab)
            .background(DSColor.canvas)
            .offset(y: -tab / 2)
        }
        .padding(.top, tab / 2)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(title)
        .accessibilityValue(paged ? Text("Page \((page?.wrappedValue ?? 0) + 1) of \(pages)") : Text(""))
    }

    private func pageButton(_ icon: StrokeIcon, _ label: String, _ delta: Int) -> some View {
        Button { go(delta) } label: {
            DSIconImage(icon: icon, size: density.metrics.icon - 2)
                .foregroundColor(DSColor.muted)
                .frame(width: 20, height: 20)
                .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .accessibilityLabel(Text(label))
        .help(Text(label))
    }
}

// MARK: - Grid

private struct DSInGridKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    /// Whether a view sits in a grid cell, which draws its padding and hairlines.
    public var dsInGrid: Bool {
        get { self[DSInGridKey.self] }
        set { self[DSInGridKey.self] = newValue }
    }
}

/// How many columns a cell takes in its grid.
struct DSSpanKey: LayoutValueKey {
    static let defaultValue: Int? = nil
}

@available(iOS 18, macOS 15, tvOS 18, watchOS 11, visionOS 2, *)
extension ContainerValues {
    @Entry var dsSpan: Int? = nil
}

extension View {
    /// The columns this view takes in a grid. Without it, a cell takes the whole row.
    @ViewBuilder
    public func dsSpan(_ columns: Int) -> some View {
        if #available(iOS 18, macOS 15, tvOS 18, watchOS 11, visionOS 2, *) {
            containerValue(\.dsSpan, columns)
        } else {
            self
        }
    }
}

/// Lays cells out on columns, row by row. The last cell of a row stretches to its end, so every
/// row is whole and the hairlines meet.
@available(iOS 16, macOS 13, tvOS 16, watchOS 9, visionOS 1, *)
struct DSGridLayout: Layout {
    let columns: Int

    private func rows(_ subviews: Subviews) -> [[(index: Int, span: Int)]] {
        var rows: [[(index: Int, span: Int)]] = []
        var row: [(index: Int, span: Int)] = []
        var used = 0
        for (index, subview) in subviews.enumerated() {
            let span = min(columns, max(1, subview[DSSpanKey.self] ?? columns))
            if used + span > columns, !row.isEmpty {
                rows.append(row)
                row = []
                used = 0
            }
            row.append((index, span))
            used += span
        }
        if !row.isEmpty { rows.append(row) }
        // Stretch the last cell of each row to fill it.
        return rows.map { row in
            var row = row
            let used = row.reduce(0) { $0 + $1.span }
            if used < columns, let last = row.indices.last { row[last].span += columns - used }
            return row
        }
    }

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let width = proposal.width ?? 320
        let column = width / CGFloat(columns)
        var height: CGFloat = 0
        for row in rows(subviews) {
            height += row.map { item in
                subviews[item.index].sizeThatFits(ProposedViewSize(width: column * CGFloat(item.span), height: nil)).height
            }.max() ?? 0
        }
        return CGSize(width: width, height: height)
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let column = bounds.width / CGFloat(columns)
        var y = bounds.minY
        for row in rows(subviews) {
            let height = row.map { item in
                subviews[item.index].sizeThatFits(ProposedViewSize(width: column * CGFloat(item.span), height: nil)).height
            }.max() ?? 0
            var x = bounds.minX
            for item in row {
                let width = column * CGFloat(item.span)
                subviews[item.index].place(at: CGPoint(x: x, y: y), proposal: ProposedViewSize(width: width, height: height))
                x += width
            }
            y += height
        }
    }
}

/// The layout of every display: a Cartesian grid. Each child becomes a cell, padded by the unit,
/// with hairlines between rows and columns that meet the edges. A child takes the whole row
/// unless it says otherwise with `.dsSpan(_:)`. Spacing lives inside cells, never between them.
public struct DSGrid<Content: View>: View {
    let columns: Int
    let content: Content

    public init(columns: Int = 1, @ViewBuilder content: () -> Content) {
        self.columns = max(1, columns)
        self.content = content()
    }

    public var body: some View {
        Group {
            if #available(iOS 18, macOS 15, tvOS 18, watchOS 11, visionOS 2, *) {
                DSGridLayout(columns: columns) {
                    ForEach(subviews: content) { subview in
                        subview
                            .modifier(DSCellChrome())
                            .layoutValue(key: DSSpanKey.self, value: subview.containerValues.dsSpan)
                    }
                }
                // The last column's hairline would double the edge of the pane.
                .padding(.trailing, -1)
                .clipped()
            } else {
                VStack(alignment: .leading, spacing: 0) {
                    content.modifier(DSCellChrome())
                }
            }
        }
        .frame(maxWidth: .infinity, alignment: .topLeading)
        .environment(\.dsInGrid, true)
    }
}

/// A cell's padding and hairlines.
struct DSCellChrome: ViewModifier {
    @Environment(\.dsDensity) private var density

    func body(content: Content) -> some View {
        content
            .padding(density.metrics.unit)
            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
            .overlay(alignment: .bottom) { DSDivider() }
            .overlay(alignment: .trailing) { DSDivider(.vertical) }
    }
}

/// The header cell of a section: its title in ink and its tools at the trailing end, the whole
/// width of the grid.
public struct DSGridHeader<Accessories: View>: View {
    let title: Text
    let accessories: Accessories
    @Environment(\.dsDensity) private var density

    public init(_ title: LocalizedStringKey, @ViewBuilder accessories: () -> Accessories) {
        self.init(title: Text(title), accessories: accessories)
    }

    public init(title: Text, @ViewBuilder accessories: () -> Accessories) {
        self.title = title
        self.accessories = accessories()
    }

    public var body: some View {
        HStack(spacing: density.metrics.unit) {
            DSText(title, variant: .label, tone: .ink)
                .lineLimit(1)
                .frame(maxWidth: .infinity, alignment: .leading)
                .accessibilityAddTraits(.isHeader)
            HStack(spacing: 0) { accessories }
        }
        .frame(height: density.metrics.control)
    }
}

extension DSGridHeader where Accessories == EmptyView {
    public init(_ title: LocalizedStringKey) {
        self.init(title: Text(title)) { EmptyView() }
    }
}

/// A cell: an optional mono label top-left, then its content one unit below. In a grid the grid
/// draws its padding and hairlines; on its own it draws them itself.
public struct DSCell<Accessories: View, Content: View>: View {
    let title: Text?
    let accessories: Accessories
    let content: Content
    @Environment(\.dsDensity) private var density
    @Environment(\.dsInGrid) private var inGrid

    public init(_ title: LocalizedStringKey? = nil, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.init(title: title.map { Text($0) }, accessories: accessories, content: content)
    }

    public init(title: Text?, @ViewBuilder accessories: () -> Accessories, @ViewBuilder content: () -> Content) {
        self.title = title
        self.accessories = accessories()
        self.content = content()
    }

    public var body: some View {
        let unit = density.metrics.unit
        let body = VStack(alignment: .leading, spacing: unit) {
            if let title {
                HStack(spacing: unit) {
                    DSText(title, variant: .label)
                        .lineLimit(1)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .accessibilityAddTraits(.isHeader)
                    HStack(spacing: 0) { accessories }
                }
            }
            content
        }
        .frame(maxWidth: .infinity, alignment: .topLeading)
        .accessibilityElement(children: .contain)
        if inGrid {
            body
        } else {
            body.modifier(DSCellChrome())
        }
    }
}

extension DSCell where Accessories == EmptyView {
    public init(_ title: LocalizedStringKey? = nil, @ViewBuilder content: () -> Content) {
        self.init(title: title.map { Text($0) }, accessories: { EmptyView() }, content: content)
    }

    public init(title: Text?, @ViewBuilder content: () -> Content) {
        self.init(title: title, accessories: { EmptyView() }, content: content)
    }
}
