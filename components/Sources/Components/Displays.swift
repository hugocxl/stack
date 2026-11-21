import SwiftUI

// Displays: what an instrument shows, as opposed to what you touch. A screen is an always-dark
// LCD whose type and marks are lit in the accent; a data table is a light well of mono rows.

/// The colors of a screen. It stays dark in both themes, like hardware.
public enum DSScreenTokens {
    /// The glass of the screen.
    public static let glass = DSColorToken(light: 0x0C0C0BFF, dark: 0x080808FF)
    /// Unlit segments and dim type: the accent barely glowing.
    public static let unlit = DSColorToken(light: 0xFE936926, dark: 0xFE936922)
}

extension DSColor {
    public static var screen: Color { DSScreenTokens.glass.color }
    public static var unlit: Color { DSScreenTokens.unlit.color }
}

/// Lit type: the accent with a faint glow.
struct DSLit: ViewModifier {
    let lit: Bool

    func body(content: Content) -> some View {
        content
            .foregroundColor(lit ? DSColor.accent : Color.white.opacity(0.42))
    }
}

extension View {
    /// Light this view's type or marks as on a screen.
    public func dsLit(_ lit: Bool = true) -> some View { modifier(DSLit(lit: lit)) }
}

/// An LCD screen: dark glass in a well, content lit in the accent. Use it for live readouts,
/// levels and status, never for forms.
public struct DSScreen<Content: View>: View {
    let content: Content
    @Environment(\.dsDensity) private var density

    public init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: density.metrics.unit) { content }
            .padding(density.metrics.unit)
            .frame(maxWidth: .infinity, alignment: .topLeading)
            .dsInset(RoundedRectangle(cornerRadius: DSRadius.control), fill: DSColor.screen)
            .environment(\.colorScheme, .dark)
    }
}

/// The mode tabs along the top of a screen: the picked one lit, the rest dim, over a dim rule.
public struct DSScreenTabs<Value: Hashable>: View {
    let label: Text
    @Binding var selection: Value
    let options: [DSOption<Value>]
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    public init(_ label: LocalizedStringKey, selection: Binding<Value>, options: [DSOption<Value>]) {
        self.label = Text(label)
        self._selection = selection
        self.options = options
    }

    public var body: some View {
        HStack(spacing: DSSpace.s4) {
            ForEach(options) { option in
                let picked = option.value == selection
                Button {
                    if sounds && !picked { DSSounds.shared.play(.blip) }
                    selection = option.value
                } label: {
                    option.title
                        .font(DSFont.of(.label, density))
                        .tracking(DSTextVariant.label.tracking(density))
                        .textCase(.uppercase)
                        .dsLit(picked)
                        .frame(height: density.metrics.control)
                        .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityAddTraits(picked ? [.isButton, .isSelected] : .isButton)
            }
            Spacer(minLength: 0)
        }
        .overlay(alignment: .bottom) {
            Rectangle().fill(DSColor.unlit).frame(height: 1)
        }
        .accessibilityElement(children: .contain)
        .accessibilityLabel(label)
    }
}

/// One live value on a screen: a dim mono label over a lit mono figure.
public struct DSScreenReadout: View {
    let label: Text
    let value: String
    let unit: String?
    @Environment(\.dsDensity) private var density

    public init(_ label: LocalizedStringKey, value: String, unit: String? = nil) {
        self.label = Text(label)
        self.value = value
        self.unit = unit
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s1) {
            label.font(DSFont.of(.label, density)).tracking(DSTextVariant.label.tracking(density))
                .textCase(.uppercase).dsLit(false)
            HStack(alignment: .firstTextBaseline, spacing: 2) {
                Text(value)
                    .font(.custom("GeistMono-Regular", size: DSTextVariant.title.size(density), relativeTo: .title2))
                    .monospacedDigit()
                    .lineLimit(1)
                    .minimumScaleFactor(0.6)
                if let unit {
                    Text(unit).font(DSFont.of(.label, density))
                }
            }
            .dsLit()
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .accessibilityElement(children: .combine)
    }
}

/// Levels over time as columns of LED segments, lit up to each value.
public struct DSScreenBars: View {
    let values: [Double]
    let segments: Int
    let height: CGFloat?
    @Environment(\.dsDensity) private var density

    public init(values: [Double], segments: Int = 12, height: CGFloat? = nil) {
        self.values = values.map { min(1, max(0, $0)) }
        self.segments = max(2, segments)
        self.height = height
    }

    public var body: some View {
        HStack(alignment: .bottom, spacing: density == .regular ? 4 : 3) {
            ForEach(Array(values.enumerated()), id: \.offset) { _, value in
                let lit = Int((value * Double(segments)).rounded())
                VStack(spacing: 2) {
                    ForEach((0..<segments).reversed(), id: \.self) { index in
                        Rectangle()
                            .fill(index < lit ? DSColor.accent : DSColor.unlit)
                    }
                }
            }
        }
        .frame(height: height ?? (density == .regular ? 96 : 64))
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text("Levels"))
        .accessibilityValue(Text(values.map { "\(Int(($0 * 100).rounded()))%" }.joined(separator: ", ")))
    }
}

// MARK: - Data table

/// Rows people scan in a light well: a mono header over a dashed rule, mono cells, and the
/// active row lit in the accent between two dashes, like a cursor on a hardware list.
public struct DSDataTable: View {
    let columns: [Text]
    let rows: [[String]]
    let active: Int?
    let onSelect: ((Int) -> Void)?
    @Environment(\.dsDensity) private var density

    /// - Parameters:
    ///   - active: the row the instrument is on (playing, rendering, focused). Its words light.
    public init(columns: [LocalizedStringKey], rows: [[String]], active: Int? = nil, onSelect: ((Int) -> Void)? = nil) {
        self.columns = columns.map { Text($0) }
        self.rows = rows
        self.active = active
        self.onSelect = onSelect
    }

    public var body: some View {
        let metrics = density.metrics
        let mark: CGFloat = density == .regular ? 20 : 14
        VStack(alignment: .leading, spacing: 0) {
            HStack(spacing: DSSpace.s3) {
                ForEach(Array(columns.enumerated()), id: \.offset) { index, column in
                    column.font(DSFont.of(.label, density)).tracking(DSTextVariant.label.tracking(density))
                        .textCase(.uppercase).foregroundColor(DSColor.muted)
                        .frame(maxWidth: .infinity, alignment: index == columns.count - 1 && columns.count > 2 ? .trailing : .leading)
                }
            }
            .padding(.horizontal, mark + DSSpace.s1)
            .frame(height: metrics.control)
            .overlay(alignment: .bottom) {
                Rectangle().stroke(DSColor.ruleStrong, style: StrokeStyle(lineWidth: 1, dash: [2, 2])).frame(height: 1)
            }
            ForEach(Array(rows.enumerated()), id: \.offset) { index, row in
                let isActive = index == active
                let line = HStack(spacing: DSSpace.s3) {
                    ForEach(Array(row.enumerated()), id: \.offset) { cell, value in
                        Text(value).font(DSFont.of(.mono, density)).lineLimit(1)
                            .frame(maxWidth: .infinity, alignment: cell == row.count - 1 && row.count > 2 ? .trailing : .leading)
                    }
                }
                .foregroundColor(isActive ? DSColor.accentText : DSColor.ink)
                .padding(.horizontal, mark + DSSpace.s1)
                .frame(height: metrics.control)
                .overlay(alignment: .leading) { if isActive { Rectangle().fill(DSColor.accent).frame(width: mark - 4, height: 2) } }
                .overlay(alignment: .trailing) { if isActive { Rectangle().fill(DSColor.accent).frame(width: mark - 4, height: 2) } }
                .contentShape(Rectangle())
                .accessibilityElement(children: .combine)
                .accessibilityAddTraits(isActive ? .isSelected : [])
                if let onSelect {
                    Button { onSelect(index) } label: { line }.buttonStyle(.plain)
                } else {
                    line
                }
            }
        }
        .padding(.vertical, DSSpace.s1)
        .dsInset(RoundedRectangle(cornerRadius: DSRadius.control))
    }
}

// MARK: - Drum

/// A drum select, like a hardware roller: the options in a short column, the picked one lit
/// between two marks, the others fading away from it. Drag or scroll to turn it, click a
/// neighbour to pick it, or use the arrow keys.
public struct DSDrum<Value: Hashable>: View {
    let label: Text
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let visible: Int
    @State private var dragStart: Int?
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds
    @Environment(\.isEnabled) private var isEnabled

    /// `visible` is the rows on show, odd: 3 or 5.
    public init(_ label: LocalizedStringKey, selection: Binding<Value>, options: [DSOption<Value>], visible: Int = 5) {
        self.label = Text(label)
        self._selection = selection
        self.options = options
        self.visible = max(3, visible | 1)
    }

    private var index: Int { options.firstIndex { $0.value == selection } ?? 0 }

    private func pick(_ next: Int) {
        let clamped = min(options.count - 1, max(0, next))
        guard clamped != index, options.indices.contains(clamped) else { return }
        if sounds { DSSounds.shared.play(.tick) }
        selection = options[clamped].value
    }

    public var body: some View {
        let row = density == .regular ? DSLayout.target * 0.7 : 20
        let half = visible / 2
        let markWidth: CGFloat = density == .regular ? 24 : 16
        VStack(spacing: 0) {
            ForEach(-half...half, id: \.self) { offset in
                let position = index + offset
                Group {
                    if options.indices.contains(position) {
                        let picked = offset == 0
                        Button { pick(position) } label: {
                            options[position].title
                                .font(picked ? DSFont.of(.mono, density).weight(.regular) : DSFont.of(.mono, density))
                                .foregroundColor(picked ? DSColor.accentText : DSColor.muted)
                                .opacity(picked ? 1 : max(0.25, 1 - Double(abs(offset)) * 0.35))
                                .scaleEffect(picked ? 1 : 1 - CGFloat(abs(offset)) * 0.06)
                                .frame(maxWidth: .infinity)
                                .frame(height: row)
                                .contentShape(Rectangle())
                        }
                        .buttonStyle(.plain)
                    } else {
                        Color.clear.frame(height: row)
                    }
                }
            }
        }
        .overlay {
            HStack {
                Rectangle().fill(DSColor.accent).frame(width: markWidth, height: 1.5)
                Spacer()
                Rectangle().fill(DSColor.accent).frame(width: markWidth, height: 1.5)
            }
            .padding(.horizontal, DSSpace.s2)
            .allowsHitTesting(false)
        }
        .padding(.vertical, DSSpace.s1)
        .dsInset(RoundedRectangle(cornerRadius: DSRadius.media))
        .clipShape(RoundedRectangle(cornerRadius: DSRadius.media))
        .contentShape(Rectangle())
        .gesture(
            DragGesture(minimumDistance: 4)
                .onChanged { drag in
                    let start = dragStart ?? index
                    if dragStart == nil { dragStart = start }
                    pick(start - Int((drag.translation.height / row).rounded()))
                }
                .onEnded { _ in dragStart = nil }
        )
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.12), value: index)
        #if os(macOS)
        .focusable()
        .onMoveCommand { direction in
            if direction == .up { pick(index - 1) }
            if direction == .down { pick(index + 1) }
        }
        #endif
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(label)
        .accessibilityValue(options.indices.contains(index) ? options[index].title : Text(""))
        .accessibilityAdjustableAction { direction in
            switch direction {
            case .increment: pick(index + 1)
            case .decrement: pick(index - 1)
            @unknown default: break
            }
        }
    }
}
