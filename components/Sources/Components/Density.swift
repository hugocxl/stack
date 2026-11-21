import SwiftUI

/// How tightly a screen is set. `regular` is the page and touch scale: 17pt reading and 44pt
/// targets. `compact` is for desktop tools people work in for hours, such as editors and
/// consoles: 13pt reading, 28pt targets and the same tokens, roles and rules.
public enum DSDensity: String, CaseIterable, Sendable {
    case regular, compact

    /// The sizes every component reads at this density.
    public var metrics: DSMetrics { DSMetrics(density: self) }
}

/// The sizes components derive from the density. Every value is a design-system token or a
/// type size; nothing here is a free number.
public struct DSMetrics: Sendable, Hashable {
    public let density: DSDensity

    /// The one height of every single-line control: buttons, icon buttons, selects, fields,
    /// search fields, menu triggers, segmented controls, slider tracks and the rows of switches,
    /// checkboxes and radios. 44pt, or 28pt on a pointer-driven desktop tool. Controls are exactly
    /// this tall, never taller, so a row of mixed controls lines up.
    public var control: CGFloat { density == .regular ? DSLayout.target : 28 }
    /// The smallest interactive target: the control height.
    public var target: CGFloat { control }
    /// The one spacing unit: every padding, margin and gap in the system. 16pt, or 12pt compact.
    /// Cells pad their content by it, controls sit one unit apart, labels sit one unit above
    /// what they name, and groups are one unit apart. The layout is built on it.
    public var unit: CGFloat { density == .regular ? DSSpace.s4 : DSSpace.s3 }
    /// An icon beside words or alone in a control.
    public var icon: CGFloat { density == .regular ? 16 : 14 }
    /// Space between an icon and its words, and between controls in a group: the unit.
    public var gap: CGFloat { unit }
    /// Horizontal padding inside a button, field or cell: the unit.
    public var inset: CGFloat { unit }
    /// Extra vertical padding of a row: none, since controls already have the control height.
    public var row: CGFloat { 0 }
    /// From a label to what it names: the unit.
    public var labelGap: CGFloat { unit }
    /// Between the controls of a group: the unit.
    public var stack: CGFloat { unit }
    /// Between groups: the unit.
    public var section: CGFloat { unit }
    /// The size of a status dot.
    public var dot: CGFloat { density == .regular ? 8 : 6 }
    /// The height of a pane header and of a toolbar row.
    public var bar: CGFloat { density == .regular ? 56 : 36 }
}

private struct DSDensityKey: EnvironmentKey {
    static let defaultValue: DSDensity = .regular
}

private struct DSSoundsKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    /// The density components set themselves at. Set it once at the root with `.dsDensity(_:)`.
    public var dsDensity: DSDensity {
        get { self[DSDensityKey.self] }
        set { self[DSDensityKey.self] = newValue }
    }

    /// Whether components play @hugocxl/sounds for direct actions. Off unless the app turns it on,
    /// and the app offers people a setting for it.
    public var dsSounds: Bool {
        get { self[DSSoundsKey.self] }
        set { self[DSSoundsKey.self] = newValue }
    }
}

extension View {
    /// Set the density of everything inside.
    public func dsDensity(_ density: DSDensity) -> some View {
        environment(\.dsDensity, density)
    }

    /// Let components play interface sounds (press, latch, detent, overlay).
    public func dsSounds(_ enabled: Bool = true) -> some View {
        environment(\.dsSounds, enabled)
    }
}

/// Plays a sound only when the environment allows it.
struct DSSoundCue {
    let enabled: Bool

    func play(_ sound: DSSound) {
        if enabled { DSSounds.shared.play(sound) }
    }
}

extension EnvironmentValues {
    var dsCue: DSSoundCue { DSSoundCue(enabled: dsSounds) }
}

extension View {
    /// Plays `down` (or `down-primary`) when pressed and `up` when released.
    func dsPressSounds(_ pressed: Bool, primary: Bool = false) -> some View {
        modifier(DSPressSounds(pressed: pressed, primary: primary))
    }
}

private struct DSPressSounds: ViewModifier {
    let pressed: Bool
    let primary: Bool
    @Environment(\.dsSounds) private var sounds

    func body(content: Content) -> some View {
        content.dsOnChange(of: pressed) { down in
            guard sounds else { return }
            DSSounds.shared.play(down ? (primary ? .downPrimary : .down) : .up)
        }
    }
}

extension View {
    /// `onChange` with the new value, on every supported OS version.
    @ViewBuilder
    func dsOnChange<Value: Equatable>(of value: Value, perform action: @escaping (Value) -> Void) -> some View {
        if #available(iOS 17, macOS 14, tvOS 17, watchOS 10, *) {
            onChange(of: value) { _, new in action(new) }
        } else {
            onChange(of: value, perform: action)
        }
    }
}

/// A menu trigger drawn exactly as its label, with no platform bezel. A borderless macOS menu
/// would flatten a custom label to an icon and a title.
struct DSMenuTriggerStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .contentShape(Rectangle())
            .opacity(configuration.isPressed ? 0.7 : 1)
    }
}

extension View {
    @ViewBuilder
    func dsMenuTrigger() -> some View {
        #if os(iOS) || os(macOS) || os(visionOS)
        if #available(iOS 16, macOS 13, *) {
            self.menuStyle(.button).buttonStyle(DSMenuTriggerStyle()).menuIndicator(.hidden)
        } else {
            self.menuStyle(.borderlessButton).menuIndicator(.hidden)
        }
        #else
        self
        #endif
    }
}
