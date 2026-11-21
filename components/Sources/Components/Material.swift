import SwiftUI

// The material of the system: a quiet chassis, caps people touch that sit a hair above it, and
// wells that hold values, a shade below. It is drawn with hairlines and one soft shadow, never
// with sheen or gradients. Values mirror "Elevation & Depth" in DESIGN.md.

/// The material colors, as light and dark pairs.
public enum DSMaterialTokens {
    /// A raised cap: buttons, knobs, fader caps, switch knobs, the picked segment.
    public static let plate = DSColorToken(light: 0xFCFCFBFF, dark: 0x1F1F1FFF)
    /// An inset well: fields, grooves, tracks, meters, checkboxes.
    public static let well = DSColorToken(light: 0xEFEFEEFF, dark: 0x171717FF)
}

extension DSColor {
    public static var plate: Color { DSMaterialTokens.plate.color }
    public static var well: Color { DSMaterialTokens.well.color }
}

/// The light and shadow values for one appearance.
struct DSLighting {
    let dark: Bool

    init(_ scheme: ColorScheme) { dark = scheme == .dark }

    var ambient: Color { .black.opacity(dark ? 0.35 : 0.06) }
    var lift: Color { .black.opacity(dark ? 0.45 : 0.1) }
}

/// A cap: plate fill (or `fill`), a hairline and one soft shadow. Pressed, it sinks into a well.
struct DSRaised<S: InsettableShape>: ViewModifier {
    let shape: S
    let fill: Color?
    let pressed: Bool
    @Environment(\.colorScheme) private var scheme


    func body(content: Content) -> some View {
        let light = DSLighting(scheme)
        content.background {
            if pressed {
                DSWell(shape: shape, fill: fill ?? DSColor.well)
            } else {
                shape.fill(fill ?? DSColor.plate)
                    .overlay(shape.strokeBorder(DSColor.rule, lineWidth: 1))
                    .shadow(color: light.ambient, radius: 3, x: 0, y: 1)
            }
        }
    }
}

/// A well: a shade below the chassis, with a hairline. No inner shadow.
struct DSWell<S: InsettableShape>: View {
    let shape: S
    let fill: Color

    var body: some View {
        shape.fill(fill).overlay(shape.strokeBorder(DSColor.rule, lineWidth: 1))
    }
}

struct DSInset<S: InsettableShape>: ViewModifier {
    let shape: S
    let fill: Color?

    func body(content: Content) -> some View {
        content.background { DSWell(shape: shape, fill: fill ?? DSColor.well) }
    }
}

/// The lift under a dialog or a menu: canvas, a hairline and a long soft shadow.
struct DSLift<S: InsettableShape>: ViewModifier {
    let shape: S
    @Environment(\.colorScheme) private var scheme

    func body(content: Content) -> some View {
        let light = DSLighting(scheme)
        content
            .background(shape.fill(DSColor.canvas).shadow(color: light.lift, radius: 24, x: 0, y: 12))
            .overlay(shape.strokeBorder(DSColor.rule, lineWidth: 1))
    }
}

extension View {
    /// Draw this view on a raised cap of `shape`. `pressed` sinks it into a well.
    public func dsRaised<S: InsettableShape>(_ shape: S, fill: Color? = nil, pressed: Bool = false) -> some View {
        modifier(DSRaised(shape: shape, fill: fill, pressed: pressed))
    }

    /// Draw this view in an inset well of `shape`.
    public func dsInset<S: InsettableShape>(_ shape: S, fill: Color? = nil) -> some View {
        modifier(DSInset(shape: shape, fill: fill))
    }

    /// Lift this view above the screen, as a dialog or a menu.
    public func dsLift<S: InsettableShape>(_ shape: S) -> some View {
        modifier(DSLift(shape: shape))
    }
}
