import SwiftUI

/// One option of a radio group, select or segmented control. Its words can be a plain string,
/// a localized key or any Text.
public struct DSOption<Value: Hashable>: Identifiable {
    public let value: Value
    public let title: Text
    public let description: Text?
    public let icon: (any IconResource)?
    public var id: Value { value }

    public init(_ value: Value, label: Text, description: Text? = nil, icon: (any IconResource)? = nil) {
        self.value = value
        self.title = label
        self.description = description
        self.icon = icon
    }

    public init(_ value: Value, label: LocalizedStringKey, description: LocalizedStringKey? = nil, icon: (any IconResource)? = nil) {
        self.init(value, label: Text(label), description: description.map { Text($0) }, icon: icon)
    }

    @_disfavoredOverload
    public init(_ value: Value, label: String, description: String? = nil, icon: (any IconResource)? = nil) {
        self.init(value, label: Text(verbatim: label), description: description.map { Text(verbatim: $0) }, icon: icon)
    }
}

/// Where a field shows its label. `hidden` keeps it for assistive technology only, for a field
/// whose label is already on screen, such as in a property row or a toolbar.
public enum DSLabelPlacement: String, CaseIterable, Sendable { case top, hidden }

/// The help or error line under a field.
struct DSFieldHelp: View {
    let help: String?
    let error: String?
    @Environment(\.dsDensity) private var density

    var body: some View {
        if let error {
            HStack(alignment: .firstTextBaseline, spacing: DSSpace.s2) {
                Circle().fill(DSColor.error).frame(width: density.metrics.dot, height: density.metrics.dot).accessibilityHidden(true)
                DSText(error, variant: .small, tone: .ink)
            }
            .accessibilityElement(children: .combine)
        } else if let help {
            DSText(help, variant: .small, tone: .muted)
        }
    }
}

/// A field's well: inset, its edge darkening on focus and turning to the error role when invalid.
struct DSFieldWell: ViewModifier {
    let focused: Bool
    let invalid: Bool
    var multiline = false
    @Environment(\.dsDensity) private var density

    func body(content: Content) -> some View {
        let shape = RoundedRectangle(cornerRadius: DSRadius.control)
        let control = density.metrics.control
        content
            .padding(.horizontal, density.metrics.unit)
            // One line is exactly the control height; a multiline field grows from it.
            .frame(minHeight: control, maxHeight: multiline ? nil : control)
            .dsInset(shape)
            .overlay {
                if invalid || focused {
                    shape.strokeBorder(invalid ? DSColor.error : DSColor.ruleStrong, lineWidth: 1)
                }
            }
    }
}

/// A hairline under a field that darkens on focus and turns red on error.
struct DSFieldLine: View {
    let focused: Bool
    let invalid: Bool

    var body: some View {
        Rectangle()
            .fill(invalid ? DSColor.error : (focused ? DSColor.ruleStrong : DSColor.rule))
            .frame(height: 1)
    }
}

/// Lets people type a value, on a hairline, with its label above and help or an error below.
public struct DSTextField<Action: View>: View {
    let label: Text
    @Binding var text: String
    let placeholder: String?
    let help: String?
    let error: String?
    let multiline: Bool
    let labelPlacement: DSLabelPlacement
    let icon: (any IconResource)?
    let action: Action
    @FocusState private var focused: Bool
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsStaticRendering) private var staticRendering
    @Environment(\.dsDensity) private var density

    public init(_ label: LocalizedStringKey, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil, @ViewBuilder action: () -> Action) {
        self.init(Text(label), text: text, placeholder: placeholder, help: help, error: error, multiline: multiline, labelPlacement: labelPlacement, icon: icon, action: action)
    }

    @_disfavoredOverload
    public init(_ label: String, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil, @ViewBuilder action: () -> Action) {
        self.init(Text(verbatim: label), text: text, placeholder: placeholder, help: help, error: error, multiline: multiline, labelPlacement: labelPlacement, icon: icon, action: action)
    }

    public init(_ label: Text, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil, @ViewBuilder action: () -> Action) {
        self.label = label
        self._text = text
        self.placeholder = placeholder
        self.help = help
        self.error = error
        self.multiline = multiline
        self.labelPlacement = labelPlacement
        self.icon = icon
        self.action = action()
    }

    public var body: some View {
        let metrics = density.metrics
        VStack(alignment: .leading, spacing: metrics.labelGap) {
            if labelPlacement == .top {
                DSText(label, variant: density == .regular ? .reading : .small, tone: density == .regular ? nil : .muted)
                    .accessibilityHidden(true)
            }
            HStack(spacing: DSSpace.s2) {
                if let icon { DSIconImage(icon: icon).foregroundColor(DSColor.muted) }
                field
                    .font(DSFont.of(.reading, density))
                    .foregroundColor(DSColor.ink)
                    .focused($focused)
                    .accessibilityLabel(label)
                    .accessibilityHint(Text(error ?? help ?? ""))
                action
            }
            .modifier(DSFieldWell(focused: focused, invalid: error != nil, multiline: multiline))
            DSFieldHelp(help: help, error: error)
        }
        .opacity(isEnabled ? 1 : 0.4)
    }

    @ViewBuilder private var field: some View {
        let prompt = placeholder.map { Text($0).foregroundColor(DSColor.faint) }
        if staticRendering {
            (text.isEmpty ? (prompt ?? Text("")) : Text(text))
                .frame(maxWidth: .infinity, alignment: .leading)
        } else if multiline, #available(iOS 16, macOS 13, tvOS 16, watchOS 9, *) {
            TextField("", text: $text, prompt: prompt, axis: .vertical)
                .lineLimit(density == .regular ? 3...10 : 2...12)
                .textFieldStyle(.plain)
                .padding(.vertical, density.metrics.row + DSSpace.s1)
        } else {
            TextField("", text: $text, prompt: prompt)
                .textFieldStyle(.plain)
        }
    }
}

extension DSTextField where Action == EmptyView {
    public init(_ label: LocalizedStringKey, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil) {
        self.init(Text(label), text: text, placeholder: placeholder, help: help, error: error, multiline: multiline, labelPlacement: labelPlacement, icon: icon) { EmptyView() }
    }

    @_disfavoredOverload
    public init(_ label: String, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil) {
        self.init(Text(verbatim: label), text: text, placeholder: placeholder, help: help, error: error, multiline: multiline, labelPlacement: labelPlacement, icon: icon) { EmptyView() }
    }

    public init(_ label: Text, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, labelPlacement: DSLabelPlacement = .top, icon: (any IconResource)? = nil) {
        self.init(label, text: text, placeholder: placeholder, help: help, error: error, multiline: multiline, labelPlacement: labelPlacement, icon: icon) { EmptyView() }
    }
}

/// The text field recipe as a TextFieldStyle, for any SwiftUI TextField or SecureField whose
/// label is already on screen: reading type on a hairline that darkens on focus.
public struct DSTextFieldStyle: TextFieldStyle {
    public init() {}

    public func _body(configuration: TextField<Self._Label>) -> some View {
        configuration.textFieldStyle(.plain).modifier(DSFieldChrome())
    }
}

/// Reading type on a hairline that darkens on focus.
struct DSFieldChrome: ViewModifier {
    @FocusState private var focused: Bool
    @Environment(\.dsDensity) private var density

    nonisolated init() {}

    func body(content: Content) -> some View {
        content
            .font(DSFont.of(.reading, density))
            .foregroundColor(DSColor.ink)
            .focused($focused)
            .modifier(DSFieldWell(focused: focused, invalid: false))
    }
}

extension TextFieldStyle where Self == DSTextFieldStyle {
    /// The design-system field: `.textFieldStyle(.ds)`.
    public static var ds: DSTextFieldStyle { DSTextFieldStyle() }
}

/// The checkbox recipe as a ToggleStyle.
public struct DSCheckboxToggleStyle: ToggleStyle {
    let description: String?
    public init(description: String? = nil) { self.description = description }

    public func makeBody(configuration: Configuration) -> some View {
        Box(configuration: configuration, description: description)
    }

    private struct Box: View {
        let configuration: Configuration
        let description: String?
        @Environment(\.dsDensity) private var density

        var body: some View {
            let side: CGFloat = density == .regular ? 20 : 14
            let radius = density == .regular ? DSRadius.control : DSSpace.s1
            DSChoiceRow(isOn: configuration.$isOn, description: description, trailing: false) {
                ZStack {
                    // Off, a well; on, a raised ink cap.
                    if configuration.isOn {
                        Color.clear.dsRaised(RoundedRectangle(cornerRadius: radius), fill: DSColor.ink)
                    } else {
                        Color.clear.dsInset(RoundedRectangle(cornerRadius: radius))
                    }
                    if configuration.isOn {
                        DSIconImage(icon: StrokeIcon.check, size: side - 6).foregroundColor(DSColor.canvas)
                    }
                }
                .frame(width: side, height: side)
            } label: {
                configuration.label
            }
        }
    }
}

/// The switch recipe as a ToggleStyle.
public struct DSSwitchToggleStyle: ToggleStyle {
    let description: String?
    public init(description: String? = nil) { self.description = description }

    public func makeBody(configuration: Configuration) -> some View {
        Track(configuration: configuration, description: description)
    }

    private struct Track: View {
        let configuration: Configuration
        let description: String?
        @Environment(\.dsDensity) private var density

        var body: some View {
            let compact = density == .compact
            DSChoiceRow(isOn: configuration.$isOn, description: description, trailing: true) {
                ZStack(alignment: configuration.isOn ? .trailing : .leading) {
                    // An inset track, filled with ink when on, and a raised knob.
                    Color.clear.dsInset(Capsule(), fill: configuration.isOn ? DSColor.ink : nil)
                    Color.clear
                        .frame(width: compact ? 12 : 18, height: compact ? 12 : 18)
                        .dsRaised(Circle())
                        .padding(compact ? 2 : 3)
                }
                .frame(width: compact ? 28 : 40, height: compact ? 16 : 24)
                .animation(.easeOut(duration: 0.12), value: configuration.isOn)
            } label: {
                configuration.label
            }
        }
    }
}

extension ToggleStyle where Self == DSSwitchToggleStyle {
    /// The design-system switch: `.toggleStyle(.dsSwitch)`.
    public static var dsSwitch: DSSwitchToggleStyle { DSSwitchToggleStyle() }
}

extension ToggleStyle where Self == DSCheckboxToggleStyle {
    /// The design-system checkbox: `.toggleStyle(.dsCheckbox)`.
    public static var dsCheckbox: DSCheckboxToggleStyle { DSCheckboxToggleStyle() }
}

/// A row with a control and its label, where the whole row is the target.
struct DSChoiceRow<Control: View, Label: View>: View {
    @Binding var isOn: Bool
    let description: String?
    let trailing: Bool
    let control: Control
    let label: Label
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    init(isOn: Binding<Bool>, description: String?, trailing: Bool, @ViewBuilder control: () -> Control, @ViewBuilder label: () -> Label) {
        self._isOn = isOn
        self.description = description
        self.trailing = trailing
        self.control = control()
        self.label = label()
    }

    var body: some View {
        let metrics = density.metrics
        Button {
            isOn.toggle()
            if sounds { DSSounds.shared.play(isOn ? .latchDown : .latchUp) }
        } label: {
            HStack(alignment: description == nil ? .center : .top, spacing: trailing ? metrics.stack : metrics.gap) {
                if !trailing { control.padding(.top, description == nil ? 0 : 1) }
                VStack(alignment: .leading, spacing: DSSpace.s1) {
                    label.font(DSFont.of(.reading, density)).foregroundColor(DSColor.ink)
                    if let description { DSText(description, variant: .small, tone: .muted) }
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                if trailing { control }
            }
            .padding(.vertical, description == nil ? 0 : metrics.row)
            .frame(minHeight: metrics.control)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .opacity(isEnabled ? 1 : 0.4)
        .accessibilityElement(children: .combine)
        .accessibilityValue(Text(isOn ? "On" : "Off"))
    }
}

/// Turns one option on or off when the choice is applied later, as in a form.
public struct DSCheckbox: View {
    let label: Text
    @Binding var isOn: Bool
    let description: String?

    public init(_ label: LocalizedStringKey, isOn: Binding<Bool>, description: String? = nil) {
        self.init(Text(label), isOn: isOn, description: description)
    }

    @_disfavoredOverload
    public init(_ label: String, isOn: Binding<Bool>, description: String? = nil) {
        self.init(Text(verbatim: label), isOn: isOn, description: description)
    }

    public init(_ label: Text, isOn: Binding<Bool>, description: String? = nil) {
        self.label = label
        self._isOn = isOn
        self.description = description
    }

    public var body: some View {
        Toggle(isOn: $isOn) { label }.toggleStyle(DSCheckboxToggleStyle(description: description))
    }
}

/// Turns a setting on or off immediately.
public struct DSSwitch: View {
    let label: Text
    @Binding var isOn: Bool
    let description: String?

    public init(_ label: LocalizedStringKey, isOn: Binding<Bool>, description: String? = nil) {
        self.init(Text(label), isOn: isOn, description: description)
    }

    @_disfavoredOverload
    public init(_ label: String, isOn: Binding<Bool>, description: String? = nil) {
        self.init(Text(verbatim: label), isOn: isOn, description: description)
    }

    public init(_ label: Text, isOn: Binding<Bool>, description: String? = nil) {
        self.label = label
        self._isOn = isOn
        self.description = description
    }

    public var body: some View {
        Toggle(isOn: $isOn) { label }.toggleStyle(DSSwitchToggleStyle(description: description))
    }
}

/// Picks exactly one option from two to six that are all worth reading.
public struct DSRadioGroup<Value: Hashable>: View {
    let label: Text
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let labelPlacement: DSLabelPlacement
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    public init(_ label: LocalizedStringKey, selection: Binding<Value>, options: [DSOption<Value>], labelPlacement: DSLabelPlacement = .top) {
        self.init(Text(label), selection: selection, options: options, labelPlacement: labelPlacement)
    }

    @_disfavoredOverload
    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>], labelPlacement: DSLabelPlacement = .top) {
        self.init(Text(verbatim: label), selection: selection, options: options, labelPlacement: labelPlacement)
    }

    public init(_ label: Text, selection: Binding<Value>, options: [DSOption<Value>], labelPlacement: DSLabelPlacement = .top) {
        self.label = label
        self._selection = selection
        self.options = options
        self.labelPlacement = labelPlacement
    }

    public var body: some View {
        let metrics = density.metrics
        let side: CGFloat = density == .regular ? 20 : 14
        VStack(alignment: .leading, spacing: 0) {
            if labelPlacement == .top {
                DSText(label, variant: density == .regular ? .reading : .small, tone: density == .regular ? nil : .muted)
                    .padding(.bottom, DSSpace.s2).accessibilityAddTraits(.isHeader)
            }
            ForEach(options) { option in
                let selected = option.value == selection
                Button {
                    if sounds && !selected { DSSounds.shared.play(.tick) }
                    selection = option.value
                } label: {
                    HStack(alignment: option.description == nil ? .center : .top, spacing: metrics.gap) {
                        ZStack {
                            Color.clear.dsInset(Circle())
                            if selected {
                                Color.clear.frame(width: side / 2, height: side / 2)
                                    .dsRaised(Circle(), fill: DSColor.ink)
                            }
                        }
                        .frame(width: side, height: side)
                            .padding(.top, option.description == nil ? 0 : 1)
                        VStack(alignment: .leading, spacing: DSSpace.s1) {
                            DSText(option.title)
                            if let description = option.description { DSText(description, variant: .small, tone: .muted) }
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                    }
                    .padding(.vertical, option.description == nil ? 0 : metrics.row)
                    .frame(minHeight: metrics.control)
                    .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityElement(children: .combine)
                .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
            }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(label)
    }
}

/// Picks one option from a long list, with the platform's own menu.
public struct DSSelect<Value: Hashable>: View {
    let label: Text
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let help: String?
    let labelPlacement: DSLabelPlacement
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsStaticRendering) private var staticRendering
    @Environment(\.dsDensity) private var density

    public init(_ label: LocalizedStringKey, selection: Binding<Value>, options: [DSOption<Value>], help: String? = nil, labelPlacement: DSLabelPlacement = .top) {
        self.init(Text(label), selection: selection, options: options, help: help, labelPlacement: labelPlacement)
    }

    @_disfavoredOverload
    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>], help: String? = nil, labelPlacement: DSLabelPlacement = .top) {
        self.init(Text(verbatim: label), selection: selection, options: options, help: help, labelPlacement: labelPlacement)
    }

    public init(_ label: Text, selection: Binding<Value>, options: [DSOption<Value>], help: String? = nil, labelPlacement: DSLabelPlacement = .top) {
        self.label = label
        self._selection = selection
        self.options = options
        self.help = help
        self.labelPlacement = labelPlacement
    }

    public var body: some View {
        let metrics = density.metrics
        VStack(alignment: .leading, spacing: metrics.labelGap) {
            if labelPlacement == .top {
                DSText(label, variant: density == .regular ? .reading : .small, tone: density == .regular ? nil : .muted)
                    .accessibilityHidden(true)
            }
            menu
                .padding(.horizontal, density.metrics.unit)
                .frame(height: metrics.control)
                .dsRaised(RoundedRectangle(cornerRadius: DSRadius.control))
                .accessibilityLabel(label)
            DSFieldHelp(help: help, error: nil)
        }
        .opacity(isEnabled ? 1 : 0.4)
    }

    private var current: some View {
        let picked = options.first { $0.value == selection }
        return HStack(spacing: DSSpace.s2) {
            if let icon = picked?.icon { DSIconImage(icon: icon) }
            DSText(picked?.title ?? Text(verbatim: "")).lineLimit(1).fixedSize(horizontal: true, vertical: false)
            Spacer(minLength: DSSpace.s1)
            DSIconImage(icon: StrokeIcon.chevronDown).foregroundColor(DSColor.muted)
        }
        .contentShape(Rectangle())
    }

    @ViewBuilder private var menu: some View {
        #if os(iOS) || os(macOS) || os(visionOS)
        if staticRendering {
            current
        } else {
            Menu {
                Picker(selection: $selection) {
                    ForEach(options) { option in option.title.tag(option.value) }
                } label: { label }
                .pickerStyle(.inline)
                .labelsHidden()
            } label: {
                current.frame(maxWidth: .infinity, alignment: .leading)
            }
            .dsMenuTrigger()
        }
        #else
        Picker(selection: $selection) {
            ForEach(options) { option in option.title.tag(option.value) }
        } label: { label }
        #endif
    }
}

/// What marks the picked segment besides its raised cap.
public enum DSSegmentIndicator: String, CaseIterable, Sendable {
    case none
    /// An LED under each position, lit under the picked one, as on a hardware selector.
    case leds
}

/// Switches between two to five views or modes, in a hairline pill.
public struct DSSegmentedControl<Value: Hashable>: View {
    let label: Text
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let iconOnly: Bool
    let fullWidth: Bool
    let indicator: DSSegmentIndicator
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds
    @Environment(\.isEnabled) private var isEnabled

    /// `iconOnly` shows each option's icon alone, with its label as tooltip and accessible
    /// name: for tab bars of familiar icons. `fullWidth` shares the width evenly.
    public init(_ label: LocalizedStringKey, selection: Binding<Value>, options: [DSOption<Value>], iconOnly: Bool = false, fullWidth: Bool = false, indicator: DSSegmentIndicator = .none) {
        self.init(Text(label), selection: selection, options: options, iconOnly: iconOnly, fullWidth: fullWidth, indicator: indicator)
    }

    @_disfavoredOverload
    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>], iconOnly: Bool = false, fullWidth: Bool = false, indicator: DSSegmentIndicator = .none) {
        self.init(Text(verbatim: label), selection: selection, options: options, iconOnly: iconOnly, fullWidth: fullWidth, indicator: indicator)
    }

    public init(_ label: Text, selection: Binding<Value>, options: [DSOption<Value>], iconOnly: Bool = false, fullWidth: Bool = false, indicator: DSSegmentIndicator = .none) {
        self.label = label
        self._selection = selection
        self.options = options
        self.iconOnly = iconOnly
        self.fullWidth = fullWidth
        self.indicator = indicator
    }

    public var body: some View {
        let metrics = density.metrics
        // Segments fill the track: with its 2pt inset, the control is exactly the control height.
        let inner = metrics.control - 4
        HStack(spacing: 0) {
            ForEach(options) { option in
                let selected = option.value == selection
                Button {
                    if sounds && !selected { DSSounds.shared.play(.tick) }
                    selection = option.value
                } label: {
                    HStack(spacing: DSSpace.s2) {
                        if let icon = option.icon { DSIconImage(icon: icon) }
                        if !iconOnly || option.icon == nil {
                            option.title.font(DSFont.of(.control, density)).lineLimit(1)
                                .fixedSize(horizontal: !fullWidth, vertical: false)
                        }
                    }
                    .foregroundColor(selected ? DSColor.ink : DSColor.muted)
                    .padding(.horizontal, iconOnly ? 0 : density.metrics.unit)
                    .frame(minWidth: iconOnly ? inner : metrics.control)
                    .frame(height: inner)
                    .frame(maxWidth: fullWidth ? .infinity : nil)
                    .background { if selected { Color.clear.dsRaised(Capsule()) } }
                    .contentShape(Capsule())
                }
                .buttonStyle(.plain)
                .overlay(alignment: .bottom) {
                    // An LED under each position; the picked one is lit.
                    if indicator == .leds {
                        Circle()
                            .fill(selected ? DSColor.accent : DSColor.rule)
                            .frame(width: 5, height: 5)
                            .offset(y: 2 + DSSpace.s2 + 2.5)
                    }
                }
                .help(option.title)
                .accessibilityLabel(option.title)
                .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
            }
        }
        .padding(2)
        .dsInset(Capsule())
        .padding(.bottom, indicator == .leds ? DSSpace.s3 : 0)
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.12), value: selection)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(label)
    }
}
