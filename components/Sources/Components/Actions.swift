import SwiftUI

/// How much an action stands out.
public enum DSButtonVariant: String, CaseIterable, Sendable {
    case primary, secondary, ghost
}

/// The button recipe as a ButtonStyle, for any SwiftUI Button.
public struct DSButtonStyle: ButtonStyle {
    public var variant: DSButtonVariant
    public var fullWidth: Bool
    public var destructive: Bool

    /// `destructive` marks an action that removes or discards: its words turn to the error role
    /// and the hairline stays, so the fill never carries the meaning alone.
    public init(_ variant: DSButtonVariant = .primary, fullWidth: Bool = false, destructive: Bool = false) {
        self.variant = variant
        self.fullWidth = fullWidth
        self.destructive = destructive
    }

    public func makeBody(configuration: Configuration) -> some View {
        StyledButton(configuration: configuration, variant: variant, fullWidth: fullWidth, destructive: destructive || configuration.role == .destructive)
    }

    private struct StyledButton: View {
        let configuration: Configuration
        let variant: DSButtonVariant
        let fullWidth: Bool
        let destructive: Bool
        @Environment(\.isEnabled) private var isEnabled
        @Environment(\.dsDensity) private var density
        @State private var hovered = false

        var body: some View {
            let metrics = density.metrics
            configuration.label
                .font(DSFont.of(.control, density))
                .lineLimit(1)
                .foregroundColor(foreground)
                .padding(.horizontal, variant == .ghost ? density.metrics.unit : metrics.inset)
                .frame(height: metrics.control)
                .frame(maxWidth: fullWidth ? .infinity : nil)
                .background(background)
                .contentShape(RoundedRectangle(cornerRadius: DSRadius.control))
                .opacity(isEnabled ? 1 : 0.4)
                .animation(.easeOut(duration: 0.08), value: configuration.isPressed)
                .onHover { hovered = $0 }
                .dsPressSounds(configuration.isPressed, primary: variant == .primary)
        }

        private var effectiveVariant: DSButtonVariant { destructive && variant == .primary ? .secondary : variant }

        private var foreground: Color {
            if destructive { return DSColor.error }
            return effectiveVariant == .primary ? DSColor.canvas : DSColor.ink
        }

        /// Primary and secondary are raised caps that sink when pressed; ghost is flat until
        /// pressed, then sinks into a well.
        @ViewBuilder private var background: some View {
            let shape = RoundedRectangle(cornerRadius: DSRadius.control)
            switch effectiveVariant {
            case .primary:
                Color.clear.dsRaised(shape, fill: DSColor.ink, pressed: configuration.isPressed)
            case .secondary:
                Color.clear.dsRaised(shape, pressed: configuration.isPressed)
            case .ghost:
                if configuration.isPressed {
                    Color.clear.dsInset(shape)
                } else {
                    shape.fill(hovered && isEnabled ? DSColor.surface : .clear)
                }
            }
        }
    }
}

extension ButtonStyle where Self == DSButtonStyle {
    /// The design-system button: `.buttonStyle(.ds(.secondary))`.
    public static func ds(_ variant: DSButtonVariant = .primary, fullWidth: Bool = false, destructive: Bool = false) -> DSButtonStyle {
        DSButtonStyle(variant, fullWidth: fullWidth, destructive: destructive)
    }
}

/// Starts an action. One primary button per screen.
public struct DSButton: View {
    let title: Text
    let icon: (any IconResource)?
    let variant: DSButtonVariant
    let fullWidth: Bool
    let destructive: Bool
    let action: () -> Void
    @Environment(\.dsDensity) private var density

    public init(_ title: LocalizedStringKey, icon: (any IconResource)? = nil, variant: DSButtonVariant = .primary, fullWidth: Bool = false, destructive: Bool = false, action: @escaping () -> Void) {
        self.init(Text(title), icon: icon, variant: variant, fullWidth: fullWidth, destructive: destructive, action: action)
    }

    @_disfavoredOverload
    public init(_ title: String, icon: (any IconResource)? = nil, variant: DSButtonVariant = .primary, fullWidth: Bool = false, destructive: Bool = false, action: @escaping () -> Void) {
        self.init(Text(verbatim: title), icon: icon, variant: variant, fullWidth: fullWidth, destructive: destructive, action: action)
    }

    public init(_ title: Text, icon: (any IconResource)? = nil, variant: DSButtonVariant = .primary, fullWidth: Bool = false, destructive: Bool = false, action: @escaping () -> Void) {
        self.title = title
        self.icon = icon
        self.variant = variant
        self.fullWidth = fullWidth
        self.destructive = destructive
        self.action = action
    }

    public var body: some View {
        Button(action: action) {
            HStack(spacing: density.metrics.gap) {
                if let icon { DSIconImage(icon: icon) }
                title
            }
        }
        .buttonStyle(DSButtonStyle(variant, fullWidth: fullWidth, destructive: destructive))
    }
}

/// outline has a hairline ring; ghost has none.
public enum DSIconButtonVariant: String, CaseIterable, Sendable {
    case outline, ghost
}

/// The icon button recipe as a ButtonStyle.
public struct DSIconButtonStyle: ButtonStyle {
    public var variant: DSIconButtonVariant
    public var isOn: Bool

    /// `isOn` shows a toggle's on state, or the open view a toolbar button stands for: ink on
    /// the surface. Never the accent.
    public init(_ variant: DSIconButtonVariant = .outline, isOn: Bool = false) {
        self.variant = variant
        self.isOn = isOn
    }

    public func makeBody(configuration: Configuration) -> some View {
        StyledIconButton(configuration: configuration, variant: variant, isOn: isOn)
    }

    private struct StyledIconButton: View {
        let configuration: Configuration
        let variant: DSIconButtonVariant
        let isOn: Bool
        @Environment(\.isEnabled) private var isEnabled
        @Environment(\.dsDensity) private var density
        @State private var hovered = false

        var body: some View {
            let target = density.metrics.control
            let lit = isOn || configuration.isPressed || (hovered && isEnabled)
            configuration.label
                .foregroundColor(variant == .ghost && !lit ? DSColor.muted : DSColor.ink)
                .frame(width: target, height: target)
                .background(cap)
                .contentShape(Circle())
                .opacity(isEnabled ? 1 : 0.4)
                .animation(.easeOut(duration: 0.08), value: configuration.isPressed)
                .animation(.easeOut(duration: 0.12), value: isOn)
                .onHover { hovered = $0 }
                .dsPressSounds(configuration.isPressed)
        }

        /// outline is a round cap; ghost is flat until pressed. On, both stay pressed in.
        @ViewBuilder private var cap: some View {
            let down = isOn || configuration.isPressed
            switch variant {
            case .outline:
                Color.clear.dsRaised(Circle(), pressed: down)
            case .ghost:
                if down {
                    Color.clear.dsInset(Circle())
                } else {
                    Circle().fill(hovered && isEnabled ? DSColor.surface.opacity(0.7) : .clear)
                }
            }
        }
    }
}

/// An action shown only as an icon, in a circle the size of the target.
public struct DSIconButton: View {
    let icon: any IconResource
    let label: String
    let variant: DSIconButtonVariant
    let isOn: Bool
    let action: () -> Void

    public init(_ icon: any IconResource, label: String, variant: DSIconButtonVariant = .outline, isOn: Bool = false, action: @escaping () -> Void) {
        self.icon = icon
        self.label = label
        self.variant = variant
        self.isOn = isOn
        self.action = action
    }

    public var body: some View {
        Button(action: action) { DSIconImage(icon: icon) }
            .buttonStyle(DSIconButtonStyle(variant, isOn: isOn))
            .accessibilityLabel(Text(label))
            .accessibilityAddTraits(isOn ? .isSelected : [])
            .help(Text(label))
    }
}

/// inline sits in running text; standalone has no underline and a full target.
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
    @Environment(\.dsDensity) private var density

    public init(_ title: String, destination: URL, icon: (any IconResource)? = nil, variant: DSLinkVariant = .inline, external: Bool = false) {
        self.title = title
        self.destination = destination
        self.icon = icon
        self.variant = variant
        self.external = external
    }

    public var body: some View {
        let metrics = density.metrics
        Link(destination: destination) {
            HStack(spacing: DSSpace.s2) {
                if let icon { DSIconImage(icon: icon, size: metrics.icon - 2) }
                Text(title)
                    .underline(variant == .inline, color: DSColor.ink.opacity(0.4))
                if external { DSIconImage(icon: StrokeIcon.arrowUpRight, size: metrics.icon - 4) }
            }
            .foregroundColor(DSColor.ink)
            .frame(height: variant == .standalone ? metrics.control : nil)
            .contentShape(Rectangle())
        }
    }
}
