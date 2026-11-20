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
struct DSInstrumentHeader: View {
    let label: String?
    let reading: String?

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            if let label { DSText(label, variant: .label) }
            Spacer(minLength: DSSpace.s4)
            if let reading {
                Text(reading.uppercased()).font(DSFont.label).tracking(13 * 0.02).monospacedDigit().foregroundColor(DSColor.ink)
            }
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
    let format: ((Double) -> String)?

    /// `value` goes from 0 to 1. The reading defaults to a percentage.
    public init(value: Double, label: String? = nil, segments: Int = 24, variant: DSMeterVariant = .bars, tone: DSTone = .accent, format: ((Double) -> String)? = nil) {
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
        VStack(alignment: .leading, spacing: DSSpace.s3) {
            if label != nil { DSInstrumentHeader(label: label, reading: reading) }
            HStack(spacing: 0) {
                ForEach(0..<segments, id: \.self) { index in
                    if index > 0 { Spacer(minLength: 1) }
                    segment(lit: index < lit)
                }
            }
            .frame(height: variant == .bars ? 16 : 8)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Level"))
        .accessibilityValue(Text(reading))
    }

    @ViewBuilder private func segment(lit: Bool) -> some View {
        let color = lit ? tone.color : DSColor.rule
        switch variant {
        case .bars: RoundedRectangle(cornerRadius: 1).fill(color).frame(width: 2)
        case .dots: Circle().fill(color).frame(width: 6, height: 6)
        }
    }
}

// MARK: - Knob

/// 48, 64 or 88pt across the disc.
public enum DSKnobSize: String, CaseIterable, Sendable {
    case small, medium, large

    var disc: CGFloat {
        switch self {
        case .small: return 48
        case .medium: return 64
        case .large: return 88
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

/// The ticks and disc of a knob, drawn for one value.
struct DSKnobFace: View {
    let fraction: Double
    let size: DSKnobSize
    let active: Bool

    var body: some View {
        let disc = size.disc
        let box = disc + 28
        let angle = -135 + fraction * 270
        ZStack {
            ForEach(0..<size.ticks, id: \.self) { index in
                let tickAngle = -135 + Double(index) / Double(size.ticks - 1) * 270
                let major = index % 4 == 0 || index == size.ticks - 1
                Capsule()
                    .fill(tickAngle <= angle + 0.01 ? DSColor.ink : DSColor.rule)
                    .frame(width: 1.25, height: major ? 7 : 4)
                    .offset(y: -(disc / 2 + 5 + (major ? 3.5 : 2)))
                    .rotationEffect(.degrees(tickAngle))
            }
            Circle().fill(DSColor.canvas)
                .frame(width: disc, height: disc)
            Circle().strokeBorder(DSColor.ink.opacity(active ? 0.6 : 0.28), lineWidth: 1)
                .frame(width: disc, height: disc)
            Circle().fill(DSColor.accent)
                .frame(width: size == .small ? 5 : 6, height: size == .small ? 5 : 6)
                .offset(y: -(disc / 2 - (size == .small ? 8 : 11)))
                .rotationEffect(.degrees(angle))
        }
        .frame(width: box, height: box)
    }
}

/// A flat dial that sets a value by dragging up or right, with a ring of ticks that fills up to it.
public struct DSKnob: View {
    let label: String?
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double
    let size: DSKnobSize
    let defaultValue: Double?
    let format: ((Double) -> String)?
    @State private var dragStart: Double?
    @Environment(\.isEnabled) private var isEnabled

    public init(_ label: String? = nil, value: Binding<Double>, in range: ClosedRange<Double> = 0...100, step: Double = 1, size: DSKnobSize = .medium, defaultValue: Double? = nil, format: ((Double) -> String)? = nil) {
        self.label = label
        self._value = value
        self.range = range
        self.step = step
        self.size = size
        self.defaultValue = defaultValue
        self.format = format
    }

    private var reading: String { format?(value) ?? (step >= 1 ? "\(Int(value.rounded()))" : String(format: "%.1f", value)) }

    private func set(_ next: Double) { value = snapped(next, range, step: step) }

    public var body: some View {
        VStack(spacing: DSSpace.s1) {
            DSKnobFace(fraction: fraction(value, range), size: size, active: dragStart != nil)
                .contentShape(Circle())
                .gesture(
                    DragGesture(minimumDistance: 0)
                        .onChanged { drag in
                            let start = dragStart ?? value
                            if dragStart == nil { dragStart = start }
                            let travel = Double(drag.translation.width - drag.translation.height)
                            set(start + travel * (range.upperBound - range.lowerBound) / 200)
                        }
                        .onEnded { _ in dragStart = nil }
                )
                .onTapGesture(count: 2) { if let defaultValue { set(defaultValue) } }
            Text(reading).font(DSFont.mono).monospacedDigit().foregroundColor(DSColor.ink).padding(.top, -DSSpace.s2)
            if let label { DSText(label, variant: .label) }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Knob"))
        .accessibilityValue(Text(reading))
        .accessibilityAdjustableAction { direction in
            switch direction {
            case .increment: set(value + step)
            case .decrement: set(value - step)
            @unknown default: break
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
    let format: ((Double) -> String)?
    @State private var dragging = false
    @Environment(\.isEnabled) private var isEnabled

    public init(_ label: String? = nil, value: Binding<Double>, in range: ClosedRange<Double> = 0...100, step: Double = 1, ticks: Int = 21, majorEvery: Int = 5, centered: Bool = false, format: ((Double) -> String)? = nil) {
        self.label = label
        self._value = value
        self.range = range
        self.step = step
        self.ticks = ticks
        self.majorEvery = max(1, majorEvery)
        self.centered = centered
        self.format = format
    }

    private var reading: String { format?(value) ?? (step >= 1 ? "\(Int(value.rounded()))" : String(format: "%.1f", value)) }

    public var body: some View {
        let at = fraction(value, range)
        let origin = centered ? 0.5 : 0
        VStack(alignment: .leading, spacing: 0) {
            DSInstrumentHeader(label: label, reading: reading)
            GeometryReader { proxy in
                let width = proxy.size.width
                ZStack(alignment: .leading) {
                    Capsule().fill(DSColor.rule).frame(height: 2)
                    Capsule().fill(DSColor.ink)
                        .frame(width: width * abs(at - origin), height: 2)
                        .offset(x: width * min(at, origin))
                    RoundedRectangle(cornerRadius: 1).fill(DSColor.accent)
                        .frame(width: 2, height: dragging ? 28 : 24)
                        .offset(x: width * at - 1)
                }
                .frame(maxHeight: .infinity)
                .contentShape(Rectangle())
                .gesture(
                    DragGesture(minimumDistance: 0)
                        .onChanged { drag in
                            dragging = true
                            let next = range.lowerBound + min(1, max(0, Double(drag.location.x / width))) * (range.upperBound - range.lowerBound)
                            value = snapped(next, range, step: step)
                        }
                        .onEnded { _ in dragging = false }
                )
            }
            .frame(height: DSLayout.target)
            if ticks > 1 {
                GeometryReader { proxy in
                    ForEach(0..<ticks, id: \.self) { index in
                        let position = Double(index) / Double(ticks - 1)
                        let major = index % majorEvery == 0 || index == ticks - 1
                        Rectangle()
                            .fill(major ? DSColor.ink.opacity(0.4) : DSColor.rule)
                            .frame(width: 1, height: major ? 9 : 5)
                            .offset(x: proxy.size.width * position - 0.5)
                    }
                }
                .frame(height: 12)
                .padding(.top, -DSSpace.s2)
            }
        }
        .opacity(isEnabled ? 1 : 0.4)
        .animation(.easeOut(duration: 0.12), value: dragging)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(Text(label ?? "Slider"))
        .accessibilityValue(Text(reading))
        .accessibilityAdjustableAction { direction in
            switch direction {
            case .increment: value = snapped(value + step, range, step: step)
            case .decrement: value = snapped(value - step, range, step: step)
            @unknown default: break
            }
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
            RoundedRectangle(cornerRadius: 3).fill(DSColor.canvas)
            RoundedRectangle(cornerRadius: 3).strokeBorder(DSColor.ink, lineWidth: 1)
            Rectangle().fill(DSColor.ink).frame(width: orientation == .vertical ? 12 : 1, height: orientation == .vertical ? 1 : 12)
        }
        .frame(width: orientation == .vertical ? 24 : 14, height: orientation == .vertical ? 14 : 24)
    }

    private func stop(_ option: DSOption<Value>, at position: Int) -> some View {
        let selected = position == index
        return Button { selection = option.value } label: {
            Group {
                if orientation == .vertical {
                    HStack(spacing: DSSpace.s2) { dash(selected); stopLabel(option.label, selected) }
                        .frame(height: DSLayout.target, alignment: .leading)
                        .padding(.leading, 24 + DSSpace.s3)
                } else {
                    VStack(spacing: DSSpace.s2) { dash(selected); stopLabel(option.label, selected) }
                        .frame(width: 72, height: DSLayout.target, alignment: .top)
                }
            }
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .accessibilityElement(children: .combine)
        .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
    }

    private func dash(_ selected: Bool) -> some View {
        Rectangle()
            .fill(selected ? DSColor.accent : DSColor.rule)
            .frame(width: orientation == .vertical ? 8 : (selected ? 2 : 1), height: orientation == .vertical ? (selected ? 2 : 1) : (selected ? 8 : 6))
    }

    private func stopLabel(_ text: String, _ selected: Bool) -> some View {
        DSText(text, variant: .label, tone: selected ? .ink : .muted)
    }

    private var vertical: some View {
        let pitch = DSLayout.target
        return ZStack(alignment: .topLeading) {
            Capsule().fill(DSColor.ink)
                .frame(width: 2, height: pitch * CGFloat(options.count - 1))
                .offset(x: 11, y: pitch / 2)
            thumb.offset(x: 0, y: pitch / 2 + pitch * CGFloat(index) - 7)
            VStack(alignment: .leading, spacing: 0) {
                ForEach(Array(options.enumerated()), id: \.element.id) { position, option in stop(option, at: position) }
            }
        }
    }

    private var horizontal: some View {
        let pitch: CGFloat = 72
        return ZStack(alignment: .topLeading) {
            Capsule().fill(DSColor.ink)
                .frame(width: pitch * CGFloat(options.count - 1), height: 2)
                .offset(x: pitch / 2, y: 11)
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
                    .font(.custom("GeistMono-Regular", size: DSTextVariant.title.size, relativeTo: .title2))
                    .tracking(DSTextVariant.title.size * -0.03)
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
        .padding(.vertical, inGrid ? DSSpace.s4 : 0)
        .padding(.horizontal, inGrid ? DSSpace.s4 : 0)
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
