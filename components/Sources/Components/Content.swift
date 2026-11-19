import SwiftUI
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

/// The name of the screen in ink, with an optional muted byline.
public struct DSTitle: View {
    let title: String
    let byline: String?

    public init(_ title: String, byline: String? = nil) {
        self.title = title
        self.byline = byline
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            DSText(title, variant: .title).accessibilityAddTraits(.isHeader)
            if let byline { DSText(byline, variant: .title, tone: .muted) }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

/// One sentence at title size that opens a home or welcome screen.
public struct DSStatement: View {
    let sentence: String
    let accent: String?

    public init(_ sentence: String, accent: String? = nil) {
        self.sentence = sentence
        self.accent = accent
    }

    public var body: some View {
        var text = Text(sentence).ds(.title)
        if let accent { text = text + Text(" ") + Text(accent).ds(.title, tone: .accent) }
        return text
            .fixedSize(horizontal: false, vertical: true)
            .frame(maxWidth: .infinity, alignment: .leading)
            .accessibilityAddTraits(.isHeader)
    }
}

/// One to three mono labels under the title: status, version, date.
public struct DSMeta: View {
    /// A status label (with its dot) or plain text.
    public enum Item: Hashable, Sendable {
        case status(String, DSTone)
        case text(String)
    }

    let items: [Item]

    public init(_ items: [Item]) { self.items = items }

    public var body: some View {
        HStack(spacing: DSSpace.s5) {
            ForEach(Array(items.enumerated()), id: \.offset) { _, item in
                switch item {
                case let .status(title, tone): DSStatus(title, tone: tone)
                case let .text(title): DSText(title, variant: .label)
                }
            }
        }
        .padding(.top, DSSpace.s6)
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

/// A muted heading followed by content.
public struct DSSection<Content: View>: View {
    let heading: String?
    let content: Content

    public init(_ heading: String? = nil, @ViewBuilder content: () -> Content) {
        self.heading = heading
        self.content = content()
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s4) {
            if let heading {
                DSText(heading, variant: .heading, tone: .muted).accessibilityAddTraits(.isHeader)
            }
            VStack(alignment: .leading, spacing: DSSpace.s5) { content }
        }
        .padding(.top, DSSpace.s7)
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

/// A 1px hairline between groups.
public struct DSDivider: View {
    public init() {}

    public var body: some View {
        Rectangle().fill(DSColor.rule).frame(height: 1).accessibilityHidden(true)
    }
}

/// Code or commands in mono on the surface, with a copy button.
public struct DSCodeBlock: View {
    let code: String
    let label: String?
    @State private var copied = false
    @Environment(\.dsStaticRendering) private var staticRendering

    public init(_ code: String, label: String? = nil) {
        self.code = code
        self.label = label
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            if let label { DSText(label, variant: .label).padding(.horizontal, DSSpace.s5).padding(.top, DSSpace.s3) }
            if staticRendering {
                codeText
            } else {
                ScrollView(.horizontal, showsIndicators: false) { selectable(codeText) }
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(RoundedRectangle(cornerRadius: DSRadius.control).fill(DSColor.surface))
        .overlay(alignment: .topTrailing) {
            #if os(iOS) || os(macOS) || os(visionOS)
            Button(action: copy) {
                DSText(copied ? "Copied" : "Copy", variant: .label, tone: .ink)
                    .padding(.horizontal, DSSpace.s3)
                    .frame(minWidth: DSLayout.target, minHeight: DSLayout.target)
                    .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            #endif
        }
    }

    private var codeText: some View {
        Text(code).font(DSFont.code).lineSpacing(13 * 0.4).foregroundColor(DSColor.ink)
            .fixedSize(horizontal: true, vertical: true)
            .padding(.vertical, DSSpace.s4)
            .padding(.leading, DSSpace.s5)
            .padding(.trailing, DSSpace.s5 + DSLayout.target)
    }

    @ViewBuilder private func selectable(_ text: some View) -> some View {
        #if os(iOS) || os(macOS) || os(visionOS)
        text.textSelection(.enabled)
        #else
        text
        #endif
    }

    private func copy() {
        #if os(iOS) || os(visionOS)
        UIPasteboard.general.string = code
        #elseif os(macOS)
        NSPasteboard.general.clearContents()
        NSPasteboard.general.setString(code, forType: .string)
        #endif
        copied = true
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.6) { copied = false }
    }
}

/// One row of a list.
public struct DSListItem: Identifiable {
    public let id = UUID()
    public let label: String?
    public let title: String
    public let description: String?
    public let trailing: String?
    public let action: (() -> Void)?

    public init(_ title: String, label: String? = nil, description: String? = nil, trailing: String? = nil, action: (() -> Void)? = nil) {
        self.label = label
        self.title = title
        self.description = description
        self.trailing = trailing
        self.action = action
    }
}

/// Rows between hairlines that people scan.
public struct DSList: View {
    let items: [DSListItem]
    #if os(iOS)
    @Environment(\.horizontalSizeClass) private var sizeClass
    private var stacked: Bool { sizeClass == .compact }
    #else
    private let stacked = false
    #endif

    public init(_ items: [DSListItem]) { self.items = items }

    public var body: some View {
        let labels = items.contains { $0.label != nil }
        VStack(spacing: 0) {
            ForEach(items) { item in
                DSDivider()
                if let action = item.action {
                    Button(action: action) { row(item, labels: labels) }.buttonStyle(.plain)
                } else {
                    row(item, labels: labels)
                }
            }
            DSDivider()
        }
    }

    private func row(_ item: DSListItem, labels: Bool) -> some View {
        HStack(alignment: .top, spacing: DSSpace.s5) {
            if labels && !stacked {
                DSText(item.label ?? "", variant: .label).frame(width: 120, alignment: .leading).padding(.top, 3)
            }
            VStack(alignment: .leading, spacing: DSSpace.s2) {
                if labels && stacked, let label = item.label { DSText(label, variant: .label) }
                DSText(item.title, variant: .heading)
                if let description = item.description { DSText(description, tone: .muted) }
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            if item.trailing != nil || item.action != nil {
                HStack(spacing: DSSpace.s2) {
                    if let trailing = item.trailing { DSText(trailing, tone: .muted) }
                    if item.action != nil { DSIconImage(icon: StrokeIcon.chevronRight).foregroundColor(DSColor.muted) }
                }
            }
        }
        .padding(.vertical, DSSpace.s5)
        .contentShape(Rectangle())
        .accessibilityElement(children: .combine)
    }
}

/// One vector or screenshot on the surface at 3:2, with a Fig. caption.
public struct DSFigure: View {
    let image: Image
    let isVector: Bool
    let caption: String?
    let accessibilityTitle: String

    /// A vector from @hugocxl/vectors, in ink.
    public init(_ vector: any VectorResource, caption: String? = nil, title: String) {
        self.image = vector.image
        self.isVector = true
        self.caption = caption
        self.accessibilityTitle = title
    }

    /// A product screenshot, described for assistive technology.
    public init(image: Image, caption: String? = nil, alt: String) {
        self.image = image
        self.isVector = false
        self.caption = caption
        self.accessibilityTitle = alt
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s3) {
            ZStack {
                DSColor.surface
                if isVector {
                    GeometryReader { proxy in
                        image.resizable().scaledToFit()
                            .foregroundColor(DSColor.ink)
                            .frame(width: proxy.size.width * 0.92, height: proxy.size.height * 0.82)
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                    }
                } else {
                    image.resizable().scaledToFill()
                }
            }
            .aspectRatio(3 / 2, contentMode: .fit)
            .clipShape(RoundedRectangle(cornerRadius: DSRadius.media))
            .accessibilityElement()
            .accessibilityLabel(Text(accessibilityTitle))
            .accessibilityAddTraits(.isImage)
            if let caption { DSText(caption, variant: .label).frame(minHeight: DSLayout.target) }
        }
    }
}

/// One item of a figure grid.
public struct DSFigureGridItem: Identifiable {
    public let id = UUID()
    public let label: String?
    public let vector: any VectorResource
    public let title: String
    public let text: String?

    public init(_ title: String, vector: any VectorResource, label: String? = nil, text: String? = nil) {
        self.title = title
        self.vector = vector
        self.label = label
        self.text = text
    }
}

/// Two to four vectors side by side between hairlines; stacked on compact widths.
public struct DSFigureGrid: View {
    let items: [DSFigureGridItem]
    #if os(iOS)
    @Environment(\.horizontalSizeClass) private var sizeClass
    private var stacked: Bool { sizeClass == .compact }
    #else
    private let stacked = false
    #endif

    public init(_ items: [DSFigureGridItem]) { self.items = items }

    public var body: some View {
        if stacked {
            VStack(alignment: .leading, spacing: 0) {
                ForEach(Array(items.enumerated()), id: \.element.id) { index, item in
                    if index > 0 { DSDivider() }
                    cell(item, index: index).padding(.vertical, DSSpace.s5)
                }
            }
        } else {
            HStack(alignment: .top, spacing: 0) {
                ForEach(Array(items.enumerated()), id: \.element.id) { index, item in
                    if index > 0 { Rectangle().fill(DSColor.rule).frame(width: 1) }
                    cell(item, index: index)
                        .padding(.leading, index == 0 ? 0 : DSSpace.s6)
                        .padding(.trailing, index == items.count - 1 ? 0 : DSSpace.s6)
                }
            }
            .fixedSize(horizontal: false, vertical: true)
        }
    }

    private func cell(_ item: DSFigureGridItem, index: Int) -> some View {
        VStack(alignment: .leading, spacing: 0) {
            DSText(item.label ?? "Fig 0.\(index + 1)", variant: .label)
            item.vector.image.resizable().scaledToFit()
                .foregroundColor(DSColor.ink)
                .padding(.vertical, DSSpace.s5)
                .accessibilityLabel(Text(item.title))
            Spacer(minLength: 0)
            DSText(item.title, variant: .heading)
            if let text = item.text { DSText(text, variant: .small, tone: .muted).padding(.top, DSSpace.s2) }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
