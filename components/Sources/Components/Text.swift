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

    public init(_ string: String, variant: DSTextVariant = .reading, tone: DSTextTone? = nil) {
        self.content = Text(verbatim: variant == .label ? string.uppercased() : string)
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
            .font(variant.font)
            .tracking(variant.tracking)
            .lineSpacing(variant.lineSpacing)
            .foregroundColor((tone ?? (variant == .label ? .muted : .ink)).color)
            .fixedSize(horizontal: false, vertical: true)
    }
}

extension Text {
    /// Style a Text in place, keeping it a Text so it can be concatenated.
    public func ds(_ variant: DSTextVariant, tone: DSTextTone? = nil) -> Text {
        self.font(variant.font)
            .tracking(variant.tracking)
            .foregroundColor((tone ?? (variant == .label ? .muted : .ink)).color)
    }
}
