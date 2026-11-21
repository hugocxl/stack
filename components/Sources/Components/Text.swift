import SwiftUI

/// The tone of a piece of text.
public enum DSTextTone: String, CaseIterable, Sendable {
    case ink, muted, accent

    var color: Color {
        switch self {
        case .ink: return DSColor.ink
        case .muted: return DSColor.muted
        case .accent: return DSColor.accentText
        }
    }
}

/// Copy in one of the system's type styles.
public struct DSText: View {
    let content: Text
    let variant: DSTextVariant
    let tone: DSTextTone?
    @Environment(\.dsDensity) private var density

    @_disfavoredOverload
    public init(_ string: String, variant: DSTextVariant = .reading, tone: DSTextTone? = nil) {
        self.content = Text(verbatim: variant == .label ? string.uppercased() : string)
        self.variant = variant
        self.tone = tone
    }

    /// Localized copy.
    public init(_ key: LocalizedStringKey, variant: DSTextVariant = .reading, tone: DSTextTone? = nil) {
        self.content = Text(key)
        self.variant = variant
        self.tone = tone
    }

    public init(_ text: Text, variant: DSTextVariant = .reading, tone: DSTextTone? = nil) {
        self.content = text
        self.variant = variant
        self.tone = tone
    }

    public var body: some View {
        content
            .font(variant.font(density))
            .tracking(variant.tracking(density))
            .lineSpacing(variant.lineSpacing(density))
            .foregroundColor((tone ?? (variant == .label ? .muted : .ink)).color)
            .textCase(variant == .label ? .uppercase : nil)
            .fixedSize(horizontal: false, vertical: true)
    }
}

extension Text {
    /// Style a Text in place, keeping it a Text so it can be concatenated.
    public func ds(_ variant: DSTextVariant, tone: DSTextTone? = nil, density: DSDensity = .regular) -> Text {
        self.font(variant.font(density))
            .tracking(variant.tracking(density))
            .foregroundColor((tone ?? (variant == .label ? .muted : .ink)).color)
    }
}
