import SwiftUI

/// One option of a radio group, select or segmented control.
public struct DSOption<Value: Hashable>: Identifiable {
    public let value: Value
    public let label: String
    public let description: String?
    public let icon: (any IconResource)?
    public var id: Value { value }

    public init(_ value: Value, label: String, description: String? = nil, icon: (any IconResource)? = nil) {
        self.value = value
        self.label = label
        self.description = description
        self.icon = icon
    }
}

/// The help or error line under a field.
struct DSFieldHelp: View {
    let help: String?
    let error: String?

    var body: some View {
        if let error {
            HStack(alignment: .firstTextBaseline, spacing: DSSpace.s2) {
                Circle().fill(DSColor.error).frame(width: 8, height: 8).accessibilityHidden(true)
                DSText(error, variant: .small, tone: .ink)
            }
            .accessibilityElement(children: .combine)
        } else if let help {
            DSText(help, variant: .small, tone: .muted)
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
    let label: String
    @Binding var text: String
    let placeholder: String?
    let help: String?
    let error: String?
    let multiline: Bool
    let action: Action
    @FocusState private var focused: Bool
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsStaticRendering) private var staticRendering

    public init(_ label: String, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false, @ViewBuilder action: () -> Action) {
        self.label = label
        self._text = text
        self.placeholder = placeholder
        self.help = help
        self.error = error
        self.multiline = multiline
        self.action = action()
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s3) {
            DSText(label, variant: .reading)
                .accessibilityHidden(true)
            HStack(spacing: DSSpace.s2) {
                field
                    .font(DSFont.reading)
                    .foregroundColor(DSColor.ink)
                    .focused($focused)
                    .accessibilityLabel(Text(label))
                    .accessibilityHint(Text(error ?? help ?? ""))
                action
            }
            .frame(minHeight: DSLayout.target)
            .overlay(alignment: .bottom) { DSFieldLine(focused: focused, invalid: error != nil) }
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
                .lineLimit(3...10)
                .textFieldStyle(.plain)
                .padding(.vertical, DSSpace.s3)
        } else {
            TextField("", text: $text, prompt: prompt)
                .textFieldStyle(.plain)
        }
    }
}

extension DSTextField where Action == EmptyView {
    public init(_ label: String, text: Binding<String>, placeholder: String? = nil, help: String? = nil, error: String? = nil, multiline: Bool = false) {
        self.init(label, text: text, placeholder: placeholder, help: help, error: error, multiline: multiline) { EmptyView() }
    }
}

/// The checkbox recipe as a ToggleStyle.
public struct DSCheckboxToggleStyle: ToggleStyle {
    let description: String?
    public init(description: String? = nil) { self.description = description }

    public func makeBody(configuration: Configuration) -> some View {
        DSChoiceRow(isOn: configuration.$isOn, description: description, trailing: false) {
            ZStack {
                RoundedRectangle(cornerRadius: DSRadius.control)
                    .fill(configuration.isOn ? DSColor.ink : .clear)
                RoundedRectangle(cornerRadius: DSRadius.control)
                    .strokeBorder(configuration.isOn ? DSColor.ink : DSColor.ruleStrong, lineWidth: 1)
                if configuration.isOn {
                    DSIconImage(icon: StrokeIcon.check, size: 14).foregroundColor(DSColor.canvas)
                }
            }
            .frame(width: 20, height: 20)
        } label: {
            configuration.label
        }
    }
}

/// The switch recipe as a ToggleStyle.
public struct DSSwitchToggleStyle: ToggleStyle {
    let description: String?
    public init(description: String? = nil) { self.description = description }

    public func makeBody(configuration: Configuration) -> some View {
        DSChoiceRow(isOn: configuration.$isOn, description: description, trailing: true) {
            ZStack(alignment: configuration.isOn ? .trailing : .leading) {
                Capsule().fill(configuration.isOn ? DSColor.ink : DSColor.surface)
                Capsule().strokeBorder(configuration.isOn ? DSColor.ink : DSColor.rule, lineWidth: 1)
                Circle()
                    .fill(configuration.isOn ? DSColor.canvas : DSColor.muted)
                    .frame(width: 18, height: 18)
                    .padding(3)
            }
            .frame(width: 40, height: 24)
            .animation(.easeOut(duration: 0.12), value: configuration.isOn)
        } label: {
            configuration.label
        }
    }
}

/// A row with a control and its label, where the whole row is the target.
struct DSChoiceRow<Control: View, Label: View>: View {
    @Binding var isOn: Bool
    let description: String?
    let trailing: Bool
    let control: Control
    let label: Label
    @Environment(\.isEnabled) private var isEnabled

    init(isOn: Binding<Bool>, description: String?, trailing: Bool, @ViewBuilder control: () -> Control, @ViewBuilder label: () -> Label) {
        self._isOn = isOn
        self.description = description
        self.trailing = trailing
        self.control = control()
        self.label = label()
    }

    var body: some View {
        Button { isOn.toggle() } label: {
            HStack(alignment: .top, spacing: trailing ? DSSpace.s5 : DSSpace.s3) {
                if !trailing { control.padding(.top, 1) }
                VStack(alignment: .leading, spacing: DSSpace.s1) {
                    label.font(DSFont.reading).foregroundColor(DSColor.ink)
                    if let description { DSText(description, variant: .small, tone: .muted) }
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                if trailing { control }
            }
            .padding(.vertical, DSSpace.s3)
            .frame(minHeight: DSLayout.target)
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
    let label: String
    @Binding var isOn: Bool
    let description: String?

    public init(_ label: String, isOn: Binding<Bool>, description: String? = nil) {
        self.label = label
        self._isOn = isOn
        self.description = description
    }

    public var body: some View {
        Toggle(label, isOn: $isOn).toggleStyle(DSCheckboxToggleStyle(description: description))
    }
}

/// Turns a setting on or off immediately.
public struct DSSwitch: View {
    let label: String
    @Binding var isOn: Bool
    let description: String?

    public init(_ label: String, isOn: Binding<Bool>, description: String? = nil) {
        self.label = label
        self._isOn = isOn
        self.description = description
    }

    public var body: some View {
        Toggle(label, isOn: $isOn).toggleStyle(DSSwitchToggleStyle(description: description))
    }
}

/// Picks exactly one option from two to six that are all worth reading.
public struct DSRadioGroup<Value: Hashable>: View {
    let label: String
    @Binding var selection: Value
    let options: [DSOption<Value>]
    @Environment(\.isEnabled) private var isEnabled

    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>]) {
        self.label = label
        self._selection = selection
        self.options = options
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            DSText(label).padding(.bottom, DSSpace.s2).accessibilityAddTraits(.isHeader)
            ForEach(options) { option in
                let selected = option.value == selection
                Button { selection = option.value } label: {
                    HStack(alignment: .top, spacing: DSSpace.s3) {
                        ZStack {
                            Circle().strokeBorder(selected ? DSColor.ink : DSColor.ruleStrong, lineWidth: selected ? 5 : 1)
                        }
                        .frame(width: 20, height: 20)
                        .padding(.top, 1)
                        VStack(alignment: .leading, spacing: DSSpace.s1) {
                            DSText(option.label)
                            if let description = option.description { DSText(description, variant: .small, tone: .muted) }
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                    }
                    .padding(.vertical, DSSpace.s3)
                    .frame(minHeight: DSLayout.target)
                    .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityElement(children: .combine)
                .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
            }
        }
        .opacity(isEnabled ? 1 : 0.4)
    }
}

/// Picks one option from a long list, with the platform's own menu.
public struct DSSelect<Value: Hashable>: View {
    let label: String
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let help: String?
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsStaticRendering) private var staticRendering

    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>], help: String? = nil) {
        self.label = label
        self._selection = selection
        self.options = options
        self.help = help
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s3) {
            DSText(label).accessibilityHidden(true)
            menu
                .frame(minHeight: DSLayout.target)
                .overlay(alignment: .bottom) { DSFieldLine(focused: false, invalid: false) }
                .accessibilityLabel(Text(label))
            DSFieldHelp(help: help, error: nil)
        }
        .opacity(isEnabled ? 1 : 0.4)
    }

    private var current: some View {
        HStack {
            DSText(options.first { $0.value == selection }?.label ?? "")
            Spacer(minLength: DSSpace.s4)
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
            Picker(label, selection: $selection) {
                ForEach(options) { option in Text(option.label).tag(option.value) }
            }
            .pickerStyle(.inline)
            .labelsHidden()
        } label: {
            current
        }
        .menuStyle(.borderlessButton)
        .menuIndicator(.hidden)
        .buttonStyle(.plain)
        }
        #else
        Picker(label, selection: $selection) {
            ForEach(options) { option in Text(option.label).tag(option.value) }
        }
        #endif
    }
}

/// Switches between two to five views or modes, in a hairline pill.
public struct DSSegmentedControl<Value: Hashable>: View {
    let label: String
    @Binding var selection: Value
    let options: [DSOption<Value>]

    public init(_ label: String, selection: Binding<Value>, options: [DSOption<Value>]) {
        self.label = label
        self._selection = selection
        self.options = options
    }

    public var body: some View {
        HStack(spacing: 0) {
            ForEach(options) { option in
                let selected = option.value == selection
                Button { selection = option.value } label: {
                    HStack(spacing: DSSpace.s2) {
                        if let icon = option.icon { DSIconImage(icon: icon) }
                        Text(option.label).font(DSFont.control).lineLimit(1)
                    }
                    .foregroundColor(selected ? DSColor.ink : DSColor.muted)
                    .padding(.horizontal, DSSpace.s4)
                    .frame(minWidth: DSLayout.target, minHeight: DSLayout.target - 6)
                    .background(Capsule().fill(selected ? DSColor.surface : .clear))
                    .contentShape(Capsule())
                }
                .buttonStyle(.plain)
                .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
            }
        }
        .padding(2)
        .overlay(Capsule().strokeBorder(DSColor.rule, lineWidth: 1))
        .animation(.easeOut(duration: 0.12), value: selection)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(Text(label))
    }
}
