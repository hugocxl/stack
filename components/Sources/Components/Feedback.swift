import SwiftUI

/// What a state means. accent is only for the page's own status, such as Beta or New.
public enum DSTone: String, CaseIterable, Sendable {
    case accent, success, warning, error, info, neutral

    public var color: Color {
        switch self {
        case .accent: return DSColor.accent
        case .success: return DSColor.success
        case .warning: return DSColor.warning
        case .error: return DSColor.error
        case .info: return DSColor.info
        case .neutral: return DSColor.neutral
        }
    }

    /// The status icon. accent and neutral use a dot instead.
    public var icon: StrokeIcon? {
        switch self {
        case .success: return .circleCheck
        case .warning: return .triangleAlert
        case .error: return .circleX
        case .info: return .circleInfo
        case .accent, .neutral: return nil
        }
    }
}

/// A dot or the status icon.
public enum DSStatusMark: String, CaseIterable, Sendable { case dot, icon }

/// label is mono uppercase; text follows the surrounding type.
public enum DSStatusAppearance: String, CaseIterable, Sendable { case label, text }

/// Names a state with words and a mark in the state's color.
public struct DSStatus: View {
    let title: String
    let tone: DSTone
    let mark: DSStatusMark
    let appearance: DSStatusAppearance
    @Environment(\.dsDensity) private var density

    public init(_ title: String, tone: DSTone = .accent, mark: DSStatusMark = .dot, appearance: DSStatusAppearance = .label) {
        self.title = title
        self.tone = tone
        self.mark = mark
        self.appearance = appearance
    }

    public var body: some View {
        HStack(spacing: DSSpace.s2) {
            let metrics = density.metrics
            if mark == .icon, let icon = tone.icon {
                DSIconImage(icon: icon, size: appearance == .label ? metrics.icon - 2 : metrics.icon).foregroundColor(tone.color)
            } else {
                Circle().fill(tone.color).frame(width: metrics.dot, height: metrics.dot).accessibilityHidden(true)
            }
            if appearance == .label {
                DSText(title, variant: .label, tone: .muted)
            } else {
                DSText(title)
            }
        }
        .accessibilityElement(children: .combine)
    }
}

/// A short message about the screen or a task, in a hairline frame with a status icon.
public struct DSNotice<Action: View>: View {
    let title: String
    let message: String?
    let tone: DSTone
    let action: Action
    let onDismiss: (() -> Void)?
    @Environment(\.dsDensity) private var density

    public init(_ title: String, message: String? = nil, tone: DSTone = .info, onDismiss: (() -> Void)? = nil, @ViewBuilder action: () -> Action) {
        self.title = title
        self.message = message
        self.tone = tone == .accent ? .info : tone
        self.action = action()
        self.onDismiss = onDismiss
    }

    public var body: some View {
        HStack(alignment: .top, spacing: DSSpace.s3) {
            DSIconImage(icon: tone.icon ?? .circleInfo).foregroundColor(tone.color).padding(.top, 2)
            VStack(alignment: .leading, spacing: DSSpace.s1) {
                Text(title).font(DSTextVariant.small.font(density).weight(.regular)).foregroundColor(DSColor.ink)
                    .fixedSize(horizontal: false, vertical: true)
                if let message { DSText(message, variant: .small, tone: .muted) }
                action.padding(.top, DSSpace.s2).padding(.leading, -DSSpace.s3)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            if let onDismiss {
                DSIconButton(StrokeIcon.close, label: "Dismiss", variant: .ghost, action: onDismiss)
                    .padding(.vertical, -DSSpace.s3)
                    .padding(.trailing, -DSSpace.s4)
            }
        }
        .padding(.vertical, density.metrics.unit)
        .padding(.horizontal, density.metrics.unit)
        .overlay(RoundedRectangle(cornerRadius: DSRadius.control).strokeBorder(DSColor.rule, lineWidth: 1))
        .accessibilityElement(children: .contain)
    }
}

extension DSNotice where Action == EmptyView {
    public init(_ title: String, message: String? = nil, tone: DSTone = .info, onDismiss: (() -> Void)? = nil) {
        self.init(title, message: message, tone: tone, onDismiss: onDismiss) { EmptyView() }
    }
}

/// The dialog panel. Present it with `.dsDialog(isPresented:…)`.
public struct DSDialog<Content: View, Actions: View>: View {
    let title: String
    let description: String?
    let content: Content
    let actions: Actions
    let onClose: () -> Void
    @Environment(\.dsDensity) private var density

    public init(_ title: String, description: String? = nil, onClose: @escaping () -> Void, @ViewBuilder content: () -> Content, @ViewBuilder actions: () -> Actions) {
        self.title = title
        self.description = description
        self.content = content()
        self.actions = actions()
        self.onClose = onClose
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            DSText(title, variant: .heading)
                .padding(.trailing, DSLayout.target)
                .accessibilityAddTraits(.isHeader)
            if let description {
                DSText(description, variant: .small, tone: .muted).padding(.top, DSSpace.s2)
            }
            content.padding(.top, density.metrics.stack)
            HStack(spacing: density.metrics.gap) {
                Spacer(minLength: 0)
                actions
            }
            .padding(.top, density.metrics.unit)
        }
        .padding(density.metrics.unit)
        .frame(maxWidth: 512, alignment: .leading)
        .dsLift(RoundedRectangle(cornerRadius: DSRadius.media))
        .overlay(alignment: .topTrailing) {
            DSIconButton(StrokeIcon.close, label: "Close", variant: .ghost, action: onClose).padding(DSSpace.s3)
        }
        .accessibilityElement(children: .contain)
        .accessibilityAddTraits(.isModal)
    }
}

extension DSDialog where Content == EmptyView {
    public init(_ title: String, description: String? = nil, onClose: @escaping () -> Void, @ViewBuilder actions: () -> Actions) {
        self.init(title, description: description, onClose: onClose, content: { EmptyView() }, actions: actions)
    }
}

struct DSDialogModifier<Panel: View>: ViewModifier {
    @Binding var isPresented: Bool
    let panel: Panel
    @Environment(\.dsSounds) private var sounds

    func body(content: Content) -> some View {
        content.overlay {
            if isPresented {
                ZStack {
                    DSColor.canvas.opacity(0.84)
                        .ignoresSafeArea()
                        .onTapGesture { isPresented = false }
                        .accessibilityHidden(true)
                    panel.padding(DSSpace.s5)
                }
                .transition(.opacity)
                #if !os(watchOS) && !os(tvOS)
                .onExitCommandIfAvailable { isPresented = false }
                #endif
            }
        }
        .animation(.easeOut(duration: 0.12), value: isPresented)
        .dsOnChange(of: isPresented) { shown in
            if shown && sounds { DSSounds.shared.play(.open) }
        }
    }
}

extension View {
    #if !os(watchOS) && !os(tvOS)
    @ViewBuilder func onExitCommandIfAvailable(perform action: @escaping () -> Void) -> some View {
        #if os(macOS)
        self.onExitCommand(perform: action)
        #else
        self
        #endif
    }
    #endif

    /// Present a dialog above a veil of the canvas.
    public func dsDialog<Content: View, Actions: View>(
        isPresented: Binding<Bool>,
        title: String,
        description: String? = nil,
        @ViewBuilder content: () -> Content,
        @ViewBuilder actions: () -> Actions
    ) -> some View {
        modifier(DSDialogModifier(
            isPresented: isPresented,
            panel: DSDialog(title, description: description, onClose: { isPresented.wrappedValue = false }, content: content, actions: actions)
        ))
    }

    /// Present a dialog with only a title, a description and actions.
    public func dsDialog<Actions: View>(
        isPresented: Binding<Bool>,
        title: String,
        description: String? = nil,
        @ViewBuilder actions: () -> Actions
    ) -> some View {
        dsDialog(isPresented: isPresented, title: title, description: description, content: { EmptyView() }, actions: actions)
    }
}

/// Shows how far a task has come, or that it is working, on a hairline track.
public struct DSProgress: View {
    let value: Double?
    let label: String?
    let showValue: Bool
    @State private var phase: CGFloat = 0
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    /// Leave `value` empty when the length is unknown.
    public init(value: Double? = nil, label: String? = nil, showValue: Bool = true) {
        self.value = value.map { min(1, max(0, $0)) }
        self.label = label
        self.showValue = showValue
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s2) {
            if let label {
                HStack {
                    DSText(label, variant: .label)
                    Spacer()
                    if showValue, let value { DSText("\(Int((value * 100).rounded()))%", variant: .label) }
                }
            }
            GeometryReader { proxy in
                ZStack(alignment: .leading) {
                    Color.clear.dsInset(Capsule())
                    if let value {
                        Capsule().fill(DSColor.ink).frame(width: proxy.size.width * value)
                    } else if reduceMotion {
                        Capsule().fill(DSColor.ink.opacity(0.4))
                    } else {
                        Capsule().fill(DSColor.ink)
                            .frame(width: proxy.size.width * 0.3)
                            .offset(x: proxy.size.width * (phase * 1.3 - 0.3))
                    }
                }
                .clipShape(Capsule())
            }
            .frame(height: 4)
        }
        .onAppear {
            guard value == nil, !reduceMotion else { return }
            withAnimation(.easeInOut(duration: 1.4).repeatForever(autoreverses: false)) { phase = 1 }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Progress"))
        .accessibilityValue(Text(value.map { "\(Int(($0 * 100).rounded())) percent" } ?? "In progress"))
    }
}
