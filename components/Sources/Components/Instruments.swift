import SwiftUI

// MARK: - Shared

private func clamped(_ value: Double, _ range: ClosedRange<Double>) -> Double {
    min(range.upperBound, max(range.lowerBound, value))
}

private func snapped(_ value: Double, _ range: ClosedRange<Double>, step: Double) -> Double {
    guard step > 0 else { return clamped(value, range) }
    return clamped((((value - range.lowerBound) / step).rounded() * step) + range.lowerBound, range)
}

private func fraction(_ value: Double, _ range: ClosedRange<Double>) -> Double {
    range.upperBound == range.lowerBound ? 0 : (clamped(value, range) - range.lowerBound) / (range.upperBound - range.lowerBound)
}

/// The mono label and reading above a meter or slider.
struct DSInstrumentHeader<Reading: View>: View {
    let label: String?
    let reading: Reading
    @Environment(\.dsDensity) private var density

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            if let label { DSText(label, variant: .label) }
            Spacer(minLength: DSSpace.s4)
            reading
        }
    }
}

extension DSInstrumentHeader where Reading == DSInstrumentReading {
    init(label: String?, reading: String?) {
        self.label = label
        self.reading = DSInstrumentReading(text: reading)
    }
}

/// The value of an instrument in mono, upper case and tabular.
struct DSInstrumentReading: View {
    let text: String?
    @Environment(\.dsDensity) private var density

    var body: some View {
        if let text {
            let size = DSTextVariant.label.size(density)
            Text(text).font(DSFont.of(.label, density)).tracking(size * 0.02).monospacedDigit().foregroundColor(DSColor.ink)
        }
    }
}

// MARK: - Meter

/// Thin vertical bars, or dots.
public enum DSMeterVariant: String, CaseIterable, Sendable { case bars, dots }

/// A level read at a glance: segments that light up to the value.
public struct DSMeter: View {
    let value: Double
    let label: String?
    let segments: Int
    let variant: DSMeterVariant
    let tone: DSTone
    let orientation: DSOrientation
    let format: ((Double) -> String)?

    /// `value` goes from 0 to 1. The reading defaults to a percentage. Vertical meters stand
    /// beside a fader and fill from the bottom.
    public init(value: Double, label: String? = nil, segments: Int = 24, variant: DSMeterVariant = .bars, tone: DSTone = .accent, orientation: DSOrientation = .horizontal, format: ((Double) -> String)? = nil) {
        self.orientation = orientation
        self.value = min(1, max(0, value))
        self.label = label
        self.segments = max(1, segments)
        self.variant = variant
        self.tone = tone == .neutral ? .accent : tone
        self.format = format
    }

    private var reading: String { format?(value) ?? "\(Int((value * 100).rounded()))%" }

    public var body: some View {
        let lit = Int((value * Double(segments)).rounded())
        Group {
            if orientation == .vertical {
                // Upright, lit from the bottom.
                VStack(spacing: 0) {
                    ForEach((0..<segments).reversed(), id: \.self) { index in
                        segment(lit: index < lit, vertical: true)
                        if index > 0 { Spacer(minLength: 1) }
                    }
                }
                .frame(width: variant == .bars ? 6 : 6)
                .padding(.vertical, DSSpace.s1)
                .padding(.horizontal, 3)
                .dsInset(RoundedRectangle(cornerRadius: DSSpace.s1))
            } else {
                VStack(alignment: .leading, spacing: DSSpace.s3) {
                    if label != nil { DSInstrumentHeader(label: label, reading: reading) }
                    // LED segments in an inset strip; lit ones glow faintly.
                    HStack(spacing: 0) {
                        ForEach(0..<segments, id: \.self) { index in
                            if index > 0 { Spacer(minLength: 1) }
                            segment(lit: index < lit)
                        }
                    }
                    .frame(height: variant == .bars ? 16 : 8)
                    .padding(.horizontal, DSSpace.s2)
                    .padding(.vertical, DSSpace.s1)
                    .dsInset(RoundedRectangle(cornerRadius: DSSpace.s1))
                }
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Level"))
        .accessibilityValue(Text(reading))
    }

    @ViewBuilder private func segment(lit: Bool, vertical: Bool = false) -> some View {
        let color = lit ? tone.color : DSColor.rule
        switch variant {
        case .bars where vertical: RoundedRectangle(cornerRadius: 1).fill(color).frame(height: 2)
        case .bars: RoundedRectangle(cornerRadius: 1).fill(color).frame(width: 2)
        case .dots: Circle().fill(color).frame(width: 6, height: 6)
        }
    }
}

// MARK: - Knob

/// Small, medium or large across the disc: 48, 64 or 88pt, or 32, 44 or 60pt at compact density.
public enum DSKnobSize: String, CaseIterable, Sendable {
    case small, medium, large

    var disc: CGFloat { disc(.regular) }

    func disc(_ density: DSDensity) -> CGFloat {
        switch (self, density) {
        case (.small, .regular): return 48
        case (.medium, .regular): return 64
        case (.large, .regular): return 88
        case (.small, .compact): return 32
        case (.medium, .compact): return 44
        case (.large, .compact): return 60
        }
    }

    var ticks: Int {
        switch self {
        case .small: return 21
        case .medium: return 29
        case .large: return 37
        }
    }
}

/// How a knob shows its value around the disc.
public enum DSKnobStyle: String, CaseIterable, Sendable {
    /// A ring of ticks that fills in ink up to the value, with an accent dot on the disc.
    case ticks
    /// A segmented accent arc that sweeps to the value, like a lit ring, with an ink pointer.
    case arc
}

/// The ring and disc of a knob, drawn for one value.
struct DSKnobFace: View {
    let fraction: Double
    let size: DSKnobSize
    let style: DSKnobStyle
    let centered: Bool
    let active: Bool
    @Environment(\.dsDensity) private var density

    var body: some View {
        let disc = size.disc(density)
        let gap: CGFloat = density == .regular ? 14 : 10
        let box = disc + gap * 2
        let angle = -135 + fraction * 270
        ZStack {
            switch style {
            case .ticks:
                ForEach(0..<size.ticks, id: \.self) { index in
                    let tickAngle = -135 + Double(index) / Double(size.ticks - 1) * 270
                    let major = index % 4 == 0 || index == size.ticks - 1
                    let origin = centered ? 0.0 : -135
                    let lit = tickAngle >= min(origin, angle) - 0.01 && tickAngle <= max(origin, angle) + 0.01
                    Capsule()
                        .fill(lit ? DSColor.ink : DSColor.rule)
                        .frame(width: 1.25, height: major ? gap / 2 : gap / 3.5)
                        .offset(y: -(disc / 2 + gap / 2.8 + (major ? gap / 4 : gap / 7)))
                        .rotationEffect(.degrees(tickAngle))
                }
            case .arc:
                let ring = disc + gap
                let width: CGFloat = density == .regular ? 2 : 1.5
                // A hairline track, drawn over in ink up to the value.
                Circle().trim(from: 0, to: 0.75)
                    .stroke(DSColor.rule, style: StrokeStyle(lineWidth: width, lineCap: .round))
                    .rotationEffect(.degrees(135))
                    .frame(width: ring, height: ring)
                let start = centered ? 0.375 : 0
                let end = fraction * 0.75
                Circle().trim(from: min(start, end), to: max(start, end))
                    .stroke(DSColor.ink, style: StrokeStyle(lineWidth: width, lineCap: .round))
                    .rotationEffect(.degrees(135))
                    .frame(width: ring, height: ring)
            }
            // A raised cap with a faint inner ring.
            Color.clear
                .frame(width: disc, height: disc)
                .dsRaised(Circle(), pressed: false)
            Circle().strokeBorder(DSColor.rule, lineWidth: 1)
                .frame(width: disc * 0.72, height: disc * 0.72)
                .opacity(active ? 1 : 0.7)
            if style == .ticks {
                Circle().fill(DSColor.ink)
                    .frame(width: disc < 40 ? 4 : 6, height: disc < 40 ? 4 : 6)
                    .offset(y: -(disc / 2 - disc * 0.17))
                    .rotationEffect(.degrees(angle))
            } else {
                Circle().fill(DSColor.ink)
                    .frame(width: disc < 40 ? 4 : 5, height: disc < 40 ? 4 : 5)
                    .offset(y: -(disc / 2 - disc * 0.17))
                    .rotationEffect(.degrees(angle))
            }
        }
        .frame(width: box, height: box)
    }
}

/// A dial that sets a value by dragging up or right. Double-click it to reset; double-click
/// the reading to type a value.
public struct DSKnob: View {
    let label: Text?
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double
    let size: DSKnobSize
    let style: DSKnobStyle
    let centered: Bool
    let defaultValue: Double?
    let editable: Bool
    let format: ((Double) -> String)?
    let parse: ((String) -> Double?)?
    let onEditingChanged: (Bool) -> Void
    @State private var dragStart: Double?
    @State private var typing = false
    @State private var input = ""
    @FocusState private var inputFocused: Bool
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsSounds) private var sounds
    @Environment(\.dsInGrid) private var inGrid
    @Environment(\.dsDensity) private var density

    /// - Parameters:
    ///   - style: ticks, or an accent arc like a lit ring.
    ///   - centered: the value grows both ways from twelve o'clock, for values around zero.
    public init(
        _ label: LocalizedStringKey? = nil, value: Binding<Double>, in range: ClosedRange<Double> = 0...100,
        step: Double = 1, size: DSKnobSize = .medium, style: DSKnobStyle = .ticks, centered: Bool = false,
        defaultValue: Double? = nil, editable: Bool = false, format: ((Double) -> String)? = nil,
        parse: ((String) -> Double?)? = nil, onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) {
        self.init(
            label: label.map { Text($0) }, value: value, in: range, step: step, size: size, style: style,
            centered: centered, defaultValue: defaultValue, editable: editable, format: format, parse: parse,
            onEditingChanged: onEditingChanged)
    }

    @_disfavoredOverload
    public init(
        _ label: String?, value: Binding<Double>, in range: ClosedRange<Double> = 0...100,
        step: Double = 1, size: DSKnobSize = .medium, style: DSKnobStyle = .ticks, centered: Bool = false,
        defaultValue: Double? = nil, editable: Bool = false, format: ((Double) -> String)? = nil,
        parse: ((String) -> Double?)? = nil, onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) {
        self.init(
            label: label.map { Text(verbatim: $0) }, value: value, in: range, step: step, size: size, style: style,
            centered: centered, defaultValue: defaultValue, editable: editable, format: format, parse: parse,
            onEditingChanged: onEditingChanged)
    }

    public init(
        label: Text?, value: Binding<Double>, in range: ClosedRange<Double> = 0...100,
        step: Double = 1, size: DSKnobSize = .medium, style: DSKnobStyle = .ticks, centered: Bool = false,
        defaultValue: Double? = nil, editable: Bool = false, format: ((Double) -> String)? = nil,
        parse: ((String) -> Double?)? = nil, onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) {
        self.label = label
        self._value = value
        self.range = range
        self.step = step
        self.size = size
        self.style = style
        self.centered = centered
        self.defaultValue = defaultValue
        self.editable = editable
        self.format = format
        self.parse = parse
        self.onEditingChanged = onEditingChanged
    }

    private var reading: String { format?(value) ?? (step >= 1 ? "\(Int(value.rounded()))" : String(format: "%.1f", value)) }

    private func set(_ next: Double) {
        let new = snapped(next, range, step: step)
        let ticks = Double(size.ticks - 1)
        if sounds, (fraction(new, range) * ticks).rounded() != (fraction(value, range) * ticks).rounded() { DSSounds.shared.play(.tick) }
        value = new
    }

    private func finishTyping() {
        guard typing else { return }
        typing = false
        let cleaned = input.trimmingCharacters(in: .whitespaces)
        if let parsed = parse?(cleaned) ?? Double(cleaned.replacingOccurrences(of: ",", with: ".")) {
            value = snapped(parsed, range, step: step)
        }
        onEditingChanged(false)
    }

    public var body: some View {
        Group {
            if inGrid {
                // In a grid the knob is a cell: its name top-left, the dial centred one unit
                // below, and its reading under the dial.
                VStack(alignment: .leading, spacing: density.metrics.unit) {
                    if let label {
                        DSText(label, variant: .label).lineLimit(2).fixedSize(horizontal: false, vertical: true)
                    }
                    VStack(spacing: density == .regular ? DSSpace.s1 : 0) {
                        face
                        readingView
                    }
                    .frame(maxWidth: .infinity)
                }
            } else {
                VStack(spacing: density == .regular ? DSSpace.s1 : 0) {
                    face
                    readingView.padding(.top, density == .regular ? -DSSpace.s2 : -DSSpace.s1)
                    // A long name wraps to a second line rather than shrinking: one size everywhere.
                    if let label {
                        DSText(label, variant: .label).lineLimit(2).multilineTextAlignment(.center)
                    }
                }
            }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(label ?? Text("Knob"))
        .accessibilityValue(Text(reading))
        .accessibilityAdjustableAction { direction in
            onEditingChanged(true)
            switch direction {
            case .increment: set(value + step)
            case .decrement: set(value - step)
            @unknown default: break
            }
            onEditingChanged(false)
        }
    }

    private var face: some View {
            DSKnobFace(fraction: fraction(value, range), size: size, style: style, centered: centered, active: dragStart != nil)
                .contentShape(Circle())
                .gesture(
                    DragGesture(minimumDistance: 1)
                        .onChanged { drag in
                            let start = dragStart ?? value
                            if dragStart == nil {
                                dragStart = start
                                onEditingChanged(true)
                            }
                            let travel = Double(drag.translation.width - drag.translation.height)
                            set(start + travel * (range.upperBound - range.lowerBound) / 200)
                        }
                        .onEnded { _ in
                            dragStart = nil
                            onEditingChanged(false)
                        }
                )
                .onTapGesture(count: 2) {
                    if let defaultValue {
                        onEditingChanged(true)
                        set(defaultValue)
                        onEditingChanged(false)
                    }
                }
    }

    @ViewBuilder private var readingView: some View {
        let font = density == .regular ? DSFont.mono : DSFont.of(.mono, .compact)
        if typing {
            TextField("", text: $input)
                .textFieldStyle(.plain)
                .font(font)
                .monospacedDigit()
                .multilineTextAlignment(.center)
                .frame(width: size.disc(density) + 16)
                .focused($inputFocused)
                .onSubmit { finishTyping() }
                .dsOnChange(of: inputFocused) { focused in if !focused { finishTyping() } }
                .overlay(alignment: .bottom) { DSFieldLine(focused: true, invalid: false) }
        } else {
            Text(reading).font(font).monospacedDigit().foregroundColor(DSColor.ink)
                .lineLimit(1)
                .contentShape(Rectangle())
                .onTapGesture(count: 2) {
                    guard editable else { return }
                    input = step >= 1 ? "\(Int(value.rounded()))" : value.formatted(.number.grouping(.never).precision(.fractionLength(0...4)))
                    onEditingChanged(true)
                    typing = true
                    inputFocused = true
                }
        }
    }
}

// MARK: - Slider

/// A fader on a ruler: a hairline track filled in ink up to an accent pointer.
public struct DSSlider: View {
    let label: String?
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double
    let ticks: Int
    let majorEvery: Int
    let centered: Bool
    let defaultValue: Double?
    let editable: Bool
    let format: ((Double) -> String)?
    let parse: ((String) -> Double?)?
    let onEditingChanged: (Bool) -> Void
    @State private var dragging = false
    @State private var typing = false
    @State private var input = ""
    @FocusState private var inputFocused: Bool
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    /// - Parameters:
    ///   - step: 0 for a continuous value.
    ///   - defaultValue: double-clicking the track or the label puts the value back.
    ///   - editable: double-clicking the reading lets people type an exact value, read back with
    ///     `parse` (a plain number by default).
    ///   - onEditingChanged: true when a drag or typed edit starts, false when it ends, so the
    ///     app can group the whole gesture into one undo step.
    public init(
        _ label: String? = nil,
        value: Binding<Double>,
        in range: ClosedRange<Double> = 0...100,
        step: Double = 1,
        ticks: Int = 21,
        majorEvery: Int = 5,
        centered: Bool = false,
        defaultValue: Double? = nil,
        editable: Bool = false,
        format: ((Double) -> String)? = nil,
        parse: ((String) -> Double?)? = nil,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) {
        self.label = label
        self._value = value
        self.range = range
        self.step = step
        self.ticks = ticks
        self.majorEvery = max(1, majorEvery)
        self.centered = centered
        self.defaultValue = defaultValue
        self.editable = editable
        self.format = format
        self.parse = parse
        self.onEditingChanged = onEditingChanged
    }

    private var reading: String { format?(value) ?? (step >= 1 ? "\(Int(value.rounded()))" : String(format: "%.2f", value)) }

    private func commit(_ next: Double) {
        let new = snapped(next, range, step: step)
        if sounds, ticks > 1, tickIndex(new) != tickIndex(value) { DSSounds.shared.play(.tick) }
        value = new
    }

    private func tickIndex(_ v: Double) -> Int { Int((fraction(v, range) * Double(ticks - 1)).rounded()) }

    private func reset() {
        guard let defaultValue else { return }
        onEditingChanged(true)
        value = snapped(defaultValue, range, step: step)
        onEditingChanged(false)
    }

    private func finishTyping() {
        guard typing else { return }
        typing = false
        let cleaned = input.trimmingCharacters(in: .whitespaces)
        if let parsed = parse?(cleaned) ?? Double(cleaned.replacingOccurrences(of: ",", with: ".")) {
            value = snapped(parsed, range, step: step)
        }
        onEditingChanged(false)
    }

    public var body: some View {
        let at = fraction(value, range)
        let origin = centered ? 0.5 : 0
        let metrics = density.metrics
        let compact = density == .compact
        Group {
            if label == nil {
                // Without a label (as in a property row), the reading sits after the track.
                HStack(spacing: metrics.gap) {
                    VStack(spacing: 0) {
                        track(at: at, origin: origin, compact: compact)
                        tickRuler(compact: compact)
                    }
                    readingView.frame(minWidth: compact ? 44 : 64, alignment: .trailing)
                }
            } else {
                VStack(alignment: .leading, spacing: 0) {
                    DSInstrumentHeader(label: label, reading: readingView)
                        .contentShape(Rectangle())
                        .onTapGesture(count: 2) { reset() }
                    track(at: at, origin: origin, compact: compact)
                    tickRuler(compact: compact)
                }
            }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.12), value: dragging)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Slider"))
        .accessibilityValue(Text(reading))
        .accessibilityAdjustableAction { direction in
            let increment = step > 0 ? step : (range.upperBound - range.lowerBound) / 100
            onEditingChanged(true)
            switch direction {
            case .increment: value = snapped(value + increment, range, step: step)
            case .decrement: value = snapped(value - increment, range, step: step)
            @unknown default: break
            }
            onEditingChanged(false)
        }
    }

    private func track(at: Double, origin: Double, compact: Bool) -> some View {
        GeometryReader { proxy in
            let width = proxy.size.width
            let line: CGFloat = 2
            let thumb: CGFloat = compact ? 12 : 16
            ZStack(alignment: .leading) {
                // A hairline track drawn over in ink up to a small round thumb.
                Capsule().fill(DSColor.rule).frame(height: line)
                Capsule().fill(DSColor.ink)
                    .frame(width: max(0, width * abs(at - origin)), height: line)
                    .offset(x: width * min(at, origin))
                Color.clear
                    .frame(width: thumb, height: thumb)
                    .dsRaised(Circle(), pressed: dragging)
                    .offset(x: min(max(width * at - thumb / 2, -thumb / 2), width - thumb / 2))
            }
            .frame(maxHeight: .infinity)
            .contentShape(Rectangle())
            .modifier(DSSliderGestures(
                dragging: $dragging,
                position: { point in range.lowerBound + min(1, max(0, Double(point.x / max(width, 1)))) * (range.upperBound - range.lowerBound) },
                commit: commit, reset: reset, onEditingChanged: onEditingChanged))
        }
        .frame(height: density.metrics.control)
    }

    @ViewBuilder private func tickRuler(compact: Bool) -> some View {
        if ticks > 1 {
            GeometryReader { proxy in
                ForEach(0..<ticks, id: \.self) { index in
                    let position = Double(index) / Double(ticks - 1)
                    let major = index % majorEvery == 0 || index == ticks - 1
                    Rectangle()
                        .fill(major ? DSColor.ink.opacity(0.4) : DSColor.rule)
                        .frame(width: 1, height: major ? (compact ? 5 : 9) : (compact ? 3 : 5))
                        .offset(x: proxy.size.width * position - 0.5)
                }
            }
            .frame(height: compact ? 6 : 12)
            .padding(.top, -DSSpace.s2)
        }
    }

    @ViewBuilder private var readingView: some View {
        if typing {
            TextField("", text: $input)
                .textFieldStyle(.plain)
                .font(DSFont.of(.label, density))
                .monospacedDigit()
                .multilineTextAlignment(.trailing)
                .frame(maxWidth: 96)
                .focused($inputFocused)
                .onSubmit { finishTyping() }
                .dsOnChange(of: inputFocused) { focused in if !focused { finishTyping() } }
                #if os(macOS)
                .onExitCommand {
                    typing = false
                    onEditingChanged(false)
                }
                #endif
                .overlay(alignment: .bottom) { DSFieldLine(focused: true, invalid: false) }
        } else {
            DSInstrumentReading(text: reading)
                .contentShape(Rectangle())
                .onTapGesture(count: 2) {
                    guard editable else { return }
                    input = step >= 1 ? "\(Int(value.rounded()))" : value.formatted(.number.grouping(.never).precision(.fractionLength(0...4)))
                    onEditingChanged(true)
                    typing = true
                    inputFocused = true
                }
                .help(editable ? Text("Double-click to type a value") : Text(""))
        }
    }
}

/// One gesture, one edit: a drag, a click that jumps to a position, or a double-click that
/// resets. A double-click never jumps first, so it leaves a single undo step.
struct DSSliderGestures: ViewModifier {
    @Binding var dragging: Bool
    /// The value at a point in the control.
    let position: (CGPoint) -> Double
    let commit: (Double) -> Void
    let reset: () -> Void
    let onEditingChanged: (Bool) -> Void

    func body(content: Content) -> some View {
        if #available(iOS 16, macOS 13, tvOS 16, watchOS 9, *) {
            content
                .gesture(drag(minimumDistance: 2))
                .simultaneousGesture(
                    TapGesture(count: 2).onEnded { reset() }
                        .exclusively(before: SpatialTapGesture().onEnded { tap in
                            onEditingChanged(true)
                            commit(position(tap.location))
                            onEditingChanged(false)
                        }))
        } else {
            content
                .gesture(drag(minimumDistance: 0))
                .simultaneousGesture(TapGesture(count: 2).onEnded { reset() })
        }
    }

    private func drag(minimumDistance: CGFloat) -> some Gesture {
        DragGesture(minimumDistance: minimumDistance)
            .onChanged { drag in
                if !dragging {
                    dragging = true
                    onEditingChanged(true)
                }
                commit(position(drag.location))
            }
            .onEnded { _ in
                dragging = false
                onEditingChanged(false)
            }
    }
}

// MARK: - Fader

/// An upright fader, as on a console: an inset groove filled with ink from the bottom, a raised
/// cap with the accent line, a ruler beside it and an optional level meter.
public struct DSFader: View {
    let label: Text?
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double
    let ticks: Int
    let majorEvery: Int
    let defaultValue: Double?
    let level: Double?
    let height: CGFloat?
    let format: ((Double) -> String)?
    let onEditingChanged: (Bool) -> Void
    @State private var dragging = false
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsDensity) private var density
    @Environment(\.dsSounds) private var sounds

    /// - Parameters:
    ///   - level: a live level from 0 to 1 shown on a meter beside the groove.
    ///   - height: the groove's height; 120pt compact, 180pt regular by default.
    public init(
        _ label: LocalizedStringKey? = nil, value: Binding<Double>, in range: ClosedRange<Double> = 0...100,
        step: Double = 0, ticks: Int = 11, majorEvery: Int = 5, defaultValue: Double? = nil, level: Double? = nil,
        height: CGFloat? = nil, format: ((Double) -> String)? = nil, onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) {
        self.label = label.map { Text($0) }
        self._value = value
        self.range = range
        self.step = step
        self.ticks = ticks
        self.majorEvery = max(1, majorEvery)
        self.defaultValue = defaultValue
        self.level = level
        self.height = height
        self.format = format
        self.onEditingChanged = onEditingChanged
    }

    private var reading: String { format?(value) ?? (step >= 1 ? "\(Int(value.rounded()))" : String(format: "%.2f", value)) }

    private func commit(_ next: Double) {
        let new = snapped(next, range, step: step)
        if sounds, ticks > 1,
           (fraction(new, range) * Double(ticks - 1)).rounded() != (fraction(value, range) * Double(ticks - 1)).rounded() {
            DSSounds.shared.play(.tick)
        }
        value = new
    }

    private func reset() {
        guard let defaultValue else { return }
        onEditingChanged(true)
        value = snapped(defaultValue, range, step: step)
        onEditingChanged(false)
    }

    public var body: some View {
        let compact = density == .compact
        let track = height ?? (compact ? 120 : 180)
        let groove: CGFloat = compact ? 4 : 6
        let cap = CGSize(width: compact ? 22 : 30, height: compact ? 10 : 14)
        let at = fraction(value, range)
        VStack(spacing: DSSpace.s2) {
            Text(reading).font(DSFont.of(.label, density)).monospacedDigit().foregroundColor(DSColor.ink).lineLimit(1)
            HStack(alignment: .center, spacing: DSSpace.s2) {
                if let level {
                    DSMeter(value: level, segments: compact ? 20 : 28, orientation: .vertical)
                        .frame(height: track)
                }
                GeometryReader { proxy in
                    let h = proxy.size.height
                    // A well filled with ink from the bottom: the bar is the value.
                    ZStack(alignment: .bottom) {
                        Color.clear.frame(width: groove).dsInset(Capsule())
                        Capsule().fill(DSColor.ink).frame(width: groove, height: max(groove, h * at))
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .contentShape(Rectangle())
                    .modifier(DSSliderGestures(
                        dragging: $dragging,
                        position: { point in range.lowerBound + min(1, max(0, 1 - point.y / max(h, 1))) * (range.upperBound - range.lowerBound) },
                        commit: commit, reset: reset, onEditingChanged: onEditingChanged))
                }
                .frame(width: cap.width, height: track)
                if ticks > 1 {
                    VStack(spacing: 0) {
                        ForEach(0..<ticks, id: \.self) { index in
                            let major = index % majorEvery == 0 || index == ticks - 1
                            Rectangle().fill(major ? DSColor.ink.opacity(0.4) : DSColor.rule)
                                .frame(width: major ? (compact ? 6 : 9) : (compact ? 3 : 5), height: 1)
                                .frame(maxWidth: .infinity, alignment: .leading)
                            if index < ticks - 1 { Spacer(minLength: 0) }
                        }
                    }
                    .frame(width: compact ? 6 : 9, height: track)
                }
            }
            .padding(.vertical, cap.height / 2)
            if let label { DSText(label, variant: .label).lineLimit(1) }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.12), value: dragging)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(label ?? Text("Fader"))
        .accessibilityValue(Text(reading))
        .accessibilityAdjustableAction { direction in
            let increment = step > 0 ? step : (range.upperBound - range.lowerBound) / 100
            onEditingChanged(true)
            switch direction {
            case .increment: value = snapped(value + increment, range, step: step)
            case .decrement: value = snapped(value - increment, range, step: step)
            @unknown default: break
            }
            onEditingChanged(false)
        }
    }
}

// MARK: - Slide switch

/// Vertical reads like hardware; horizontal fits a row.
public enum DSOrientation: String, CaseIterable, Sendable { case vertical, horizontal }

/// A hardware switch with two to four labelled positions.
public struct DSSlideSwitch<Value: Hashable>: View {
    let label: String?
    @Binding var selection: Value
    let options: [DSOption<Value>]
    let orientation: DSOrientation
    @Environment(\.isEnabled) private var isEnabled
    @Environment(\.dsDensity) private var density

    public init(_ label: String? = nil, selection: Binding<Value>, options: [DSOption<Value>], orientation: DSOrientation = .vertical) {
        self.label = label
        self._selection = selection
        self.options = options
        self.orientation = orientation
    }

    private var index: Int { options.firstIndex { $0.value == selection } ?? 0 }

    public var body: some View {
        VStack(alignment: .leading, spacing: DSSpace.s3) {
            if let label { DSText(label, variant: .label, tone: .ink) }
            if orientation == .vertical { vertical } else { horizontal }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.16), value: index)
        .accessibilityElement(children: .contain)
        .accessibilityLabel(Text(label ?? ""))
    }

    private var thumb: some View {
        ZStack {
            Color.clear.dsRaised(RoundedRectangle(cornerRadius: 3))
            Rectangle().fill(DSColor.ink).frame(width: orientation == .vertical ? 12 : 1, height: orientation == .vertical ? 1 : 12)
        }
        .frame(width: orientation == .vertical ? 24 : 14, height: orientation == .vertical ? 14 : 24)
    }

    private func stop(_ option: DSOption<Value>, at position: Int) -> some View {
        let selected = position == index
        return Button { selection = option.value } label: {
            Group {
                if orientation == .vertical {
                    HStack(spacing: DSSpace.s2) { dash(selected); stopLabel(option.title, selected) }
                        .frame(height: pitch, alignment: .leading)
                        .padding(.leading, 24 + DSSpace.s3)
                } else {
                    VStack(spacing: DSSpace.s2) { dash(selected); stopLabel(option.title, selected) }
                        .frame(width: pitch, height: density.metrics.control, alignment: .top)
                }
            }
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .accessibilityElement(children: .combine)
        .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
    }

    /// The stop's mark, in a fixed box so a picked stop's label never moves.
    private func dash(_ selected: Bool) -> some View {
        Rectangle()
            .fill(selected ? DSColor.ink : DSColor.rule)
            .frame(width: orientation == .vertical ? 8 : (selected ? 2 : 1), height: orientation == .vertical ? (selected ? 2 : 1) : (selected ? 8 : 6))
            .frame(width: orientation == .vertical ? 8 : 2, height: orientation == .vertical ? 2 : 8, alignment: .top)
    }

    /// The distance between stops: the control height upright, a wider step lying down.
    private var pitch: CGFloat {
        orientation == .vertical ? density.metrics.control : (density == .regular ? 96 : 76)
    }

    private func stopLabel(_ text: Text, _ selected: Bool) -> some View {
        DSText(text, variant: .label, tone: selected ? .ink : .muted)
            .lineLimit(1)
            .fixedSize(horizontal: true, vertical: false)
    }

    private var vertical: some View {
        return ZStack(alignment: .topLeading) {
            Color.clear.frame(width: 4, height: pitch * CGFloat(options.count - 1) + 4)
                .dsInset(Capsule())
                .offset(x: 10, y: pitch / 2 - 2)
            thumb.offset(x: 0, y: pitch / 2 + pitch * CGFloat(index) - 7)
            VStack(alignment: .leading, spacing: 0) {
                ForEach(Array(options.enumerated()), id: \.element.id) { position, option in stop(option, at: position) }
            }
        }
    }

    private var horizontal: some View {
        return ZStack(alignment: .topLeading) {
            Color.clear.frame(width: pitch * CGFloat(options.count - 1) + 4, height: 4)
                .dsInset(Capsule())
                .offset(x: pitch / 2 - 2, y: 10)
            thumb.offset(x: pitch / 2 + pitch * CGFloat(index) - 7, y: 0)
            HStack(spacing: 0) {
                ForEach(Array(options.enumerated()), id: \.element.id) { position, option in stop(option, at: position) }
            }
            .padding(.top, 24)
        }
    }
}

// MARK: - Readout

private struct DSReadoutGridKey: EnvironmentKey { static let defaultValue = false }

extension EnvironmentValues {
    var dsInReadoutGrid: Bool {
        get { self[DSReadoutGridKey.self] }
        set { self[DSReadoutGridKey.self] = newValue }
    }
}

/// One setting read at a distance: a mono label over a large value.
public struct DSReadout: View {
    let label: String
    let value: String
    let unit: String?
    let dim: Bool
    let live: Bool
    let selected: Bool
    let action: (() -> Void)?
    @Environment(\.dsInReadoutGrid) private var inGrid
    @Environment(\.dsDensity) private var density

    public init(_ label: String, value: String, unit: String? = nil, dim: Bool = false, live: Bool = false, selected: Bool = false, action: (() -> Void)? = nil) {
        self.label = label
        self.value = value
        self.unit = unit
        self.dim = dim
        self.live = live
        self.selected = selected
        self.action = action
    }

    public var body: some View {
        Group {
            if let action {
                Button(action: action) { content }.buttonStyle(.plain)
            } else {
                content
            }
        }
        .accessibilityElement(children: .combine)
        .accessibilityAddTraits(selected ? .isSelected : [])
    }

    private var content: some View {
        VStack(alignment: .leading, spacing: DSSpace.s1) {
            HStack(spacing: DSSpace.s2) {
                DSText(label, variant: .label)
                if live { Circle().fill(DSColor.accent).frame(width: 6, height: 6).accessibilityLabel(Text("live")) }
            }
            HStack(alignment: .firstTextBaseline, spacing: 3) {
                Text(value)
                    .font(.custom("GeistMono-Regular", size: DSTextVariant.title.size(density), relativeTo: .title2))
                    .tracking(DSTextVariant.title.size(density) * -0.03)
                    .monospacedDigit()
                    .lineLimit(1)
                    .minimumScaleFactor(0.6)
                    .foregroundColor(dim ? DSColor.faint : DSColor.ink)
                if let unit {
                    DSText(unit, variant: .label).alignmentGuide(.firstTextBaseline) { $0[.firstTextBaseline] + 8 }
                }
            }
        }
        .frame(maxWidth: inGrid ? .infinity : nil, alignment: .leading)
        .padding(.vertical, inGrid ? density.metrics.unit : 0)
        .padding(.horizontal, inGrid ? density.metrics.unit : 0)
        .overlay(alignment: .bottom) {
            if inGrid && selected { Rectangle().fill(DSColor.accent).frame(height: 2) }
        }
        .overlay {
            if inGrid {
                GeometryReader { proxy in
                    Path { path in
                        path.move(to: CGPoint(x: proxy.size.width - 0.5, y: 0))
                        path.addLine(to: CGPoint(x: proxy.size.width - 0.5, y: proxy.size.height - 0.5))
                        path.addLine(to: CGPoint(x: 0, y: proxy.size.height - 0.5))
                    }
                    .stroke(DSColor.rule, lineWidth: 1)
                }
                .allowsHitTesting(false)
            }
        }
        .contentShape(Rectangle())
    }
}

/// Readouts in hairline cells, like an instrument panel.
public struct DSReadoutGrid<Content: View>: View {
    let columns: Int
    let content: Content

    public init(columns: Int = 3, @ViewBuilder content: () -> Content) {
        self.columns = max(1, columns)
        self.content = content()
    }

    public var body: some View {
        LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 0), count: columns), spacing: 0) {
            content
        }
        .environment(\.dsInReadoutGrid, true)
        .overlay(alignment: .topLeading) {
            GeometryReader { proxy in
                Path { path in
                    path.move(to: CGPoint(x: 0.5, y: proxy.size.height))
                    path.addLine(to: CGPoint(x: 0.5, y: 0.5))
                    path.addLine(to: CGPoint(x: proxy.size.width, y: 0.5))
                }
                .stroke(DSColor.rule, lineWidth: 1)
            }
            .allowsHitTesting(false)
        }
    }
}
