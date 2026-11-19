import SwiftUI

/// How much an action stands out.
public enum DSButtonVariant: String, CaseIterable, Sendable {
    case primary, secondary, ghost
}

/// The button recipe as a ButtonStyle, for any SwiftUI Button.
public struct DSButtonStyle: ButtonStyle {
    public var variant: DSButtonVariant
    public var fullWidth: Bool

    public init(_ variant: DSButtonVariant = .primary, fullWidth: Bool = false) {
        self.variant = variant
        self.fullWidth = fullWidth
    }

    public func makeBody(configuration: Configuration) -> some View {
        StyledButton(configuration: configuration, variant: variant, fullWidth: fullWidth)
    }

    private struct StyledButton: View {
        let configuration: Configuration
        let variant: DSButtonVariant
        let fullWidth: Bool
        @Environment(\.isEnabled) private var isEnabled

        var body: some View {
            configuration.label
                .font(DSFont.control)
                .lineLimit(1)
                .foregroundColor(variant == .primary ? DSColor.canvas : DSColor.ink)
                .padding(.horizontal, variant == .ghost ? DSSpace.s3 : DSSpace.s5)
                .frame(minHeight: DSLayout.target)
                .frame(maxWidth: fullWidth ? .infinity : nil)
                .background(background)
                .overlay(
                    RoundedRectangle(cornerRadius: DSRadius.control)
                        .strokeBorder(variant == .secondary ? (configuration.isPressed ? DSColor.ruleStrong : DSColor.rule) : .clear, lineWidth: 1)
                )
                .contentShape(RoundedRectangle(cornerRadius: DSRadius.control))
                .opacity(isEnabled ? (variant == .primary && configuration.isPressed ? 0.84 : 1) : 0.4)
                .scaleEffect(configuration.isPressed ? 0.96 : 1)
                .animation(.easeOut(duration: 0.12), value: configuration.isPressed)
        }

        @ViewBuilder private var background: some View {
            switch variant {
            case .primary: RoundedRectangle(cornerRadius: DSRadius.control).fill(DSColor.ink)
            case .secondary: Color.clear
            case .ghost: RoundedRectangle(cornerRadius: DSRadius.control).fill(configuration.isPressed ? DSColor.surface : .clear)
            }
        }
    }
}

extension ButtonStyle where Self == DSButtonStyle {
    /// The design-system button: `.buttonStyle(.ds(.secondary))`.
    public static func ds(_ variant: DSButtonVariant = .primary, fullWidth: Bool = false) -> DSButtonStyle {
        DSButtonStyle(variant, fullWidth: fullWidth)
    }
}

/// Starts an action. One primary button per screen.
public struct DSButton: View {
    let title: String
    let icon: (any IconResource)?
    let variant: DSButtonVariant
    let fullWidth: Bool
    let action: () -> Void

    public init(_ title: String, icon: (any IconResource)? = nil, variant: DSButtonVariant = .primary, fullWidth: Bool = false, action: @escaping () -> Void) {
        self.title = title
        self.icon = icon
        self.variant = variant
        self.fullWidth = fullWidth
        self.action = action
    }

    public var body: some View {
        Button(action: action) {
            HStack(spacing: DSSpace.s3) {
                if let icon { DSIconImage(icon: icon) }
                Text(title)
            }
        }
        .buttonStyle(DSButtonStyle(variant, fullWidth: fullWidth))
    }
}

/// outline has a hairline ring; ghost has none.
public enum DSIconButtonVariant: String, CaseIterable, Sendable {
    case outline, ghost
}

/// The icon button recipe as a ButtonStyle.
public struct DSIconButtonStyle: ButtonStyle {
    public var variant: DSIconButtonVariant

    public init(_ variant: DSIconButtonVariant = .outline) { self.variant = variant }

    public func makeBody(configuration: Configuration) -> some View {
        StyledIconButton(configuration: configuration, variant: variant)
    }

    private struct StyledIconButton: View {
        let configuration: Configuration
        let variant: DSIconButtonVariant
        @Environment(\.isEnabled) private var isEnabled

        var body: some View {
            configuration.label
                .foregroundColor(variant == .ghost && !configuration.isPressed ? DSColor.muted : DSColor.ink)
                .frame(width: DSLayout.target, height: DSLayout.target)
                .background(Circle().fill(configuration.isPressed ? DSColor.surface : .clear))
                .overlay(Circle().strokeBorder(variant == .outline ? DSColor.rule : .clear, lineWidth: 1))
                .contentShape(Circle())
                .opacity(isEnabled ? 1 : 0.4)
                .scaleEffect(configuration.isPressed ? 0.96 : 1)
                .animation(.easeOut(duration: 0.12), value: configuration.isPressed)
        }
    }
}

/// An action shown only as an icon, in a 44pt circle.
public struct DSIconButton: View {
    let icon: any IconResource
    let label: String
    let variant: DSIconButtonVariant
    let action: () -> Void

    public init(_ icon: any IconResource, label: String, variant: DSIconButtonVariant = .outline, action: @escaping () -> Void) {
        self.icon = icon
        self.label = label
        self.variant = variant
        self.action = action
    }

    public var body: some View {
        Button(action: action) { DSIconImage(icon: icon) }
            .buttonStyle(DSIconButtonStyle(variant))
            .accessibilityLabel(Text(label))
            .help(Text(label))
    }
}

/// inline sits in running text; standalone has no underline and a 44pt target.
public enum DSLinkVariant: String, CaseIterable, Sendable {
    case inline, standalone
}

/// Takes people somewhere.
public struct DSLink: View {
    let title: String
    let destination: URL
    let icon: (any IconResource)?
    let variant: DSLinkVariant
    let external: Bool

    public init(_ title: String, destination: URL, icon: (any IconResource)? = nil, variant: DSLinkVariant = .inline, external: Bool = false) {
        self.title = title
        self.destination = destination
        self.icon = icon
        self.variant = variant
        self.external = external
    }

    public var body: some View {
        Link(destination: destination) {
            HStack(spacing: DSSpace.s2) {
                if let icon { DSIconImage(icon: icon, size: 14) }
                Text(title)
                    .underline(variant == .inline, color: DSColor.ink.opacity(0.4))
                if external { DSIconImage(icon: StrokeIcon.arrowUpRight, size: 12) }
            }
            .foregroundColor(DSColor.ink)
            .frame(minHeight: variant == .standalone ? DSLayout.target : nil)
            .contentShape(Rectangle())
        }
    }
}
