@_exported import Icons
@_exported import Vectors
import CoreText
import Foundation
import SwiftUI
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

// MARK: - Colors

extension DSColorToken {
    /// The role as a SwiftUI color that follows the light or dark appearance.
    public var color: Color {
        #if os(watchOS)
        return Color(rgba: dark)
        #elseif canImport(UIKit)
        let light = UIColor(rgba: light), dark = UIColor(rgba: dark)
        return Color(UIColor { $0.userInterfaceStyle == .dark ? dark : light })
        #elseif canImport(AppKit)
        let light = NSColor(rgba: light), dark = NSColor(rgba: dark)
        return Color(NSColor(name: nil) { appearance in
            appearance.bestMatch(from: [.darkAqua, .aqua]) == .darkAqua ? dark : light
        })
        #endif
    }

    /// The value for one appearance.
    public func color(for scheme: ColorScheme) -> Color {
        Color(rgba: scheme == .dark ? dark : light)
    }
}

private func channels(_ rgba: UInt32) -> (Double, Double, Double, Double) {
    (Double((rgba >> 24) & 0xFF) / 255, Double((rgba >> 16) & 0xFF) / 255, Double((rgba >> 8) & 0xFF) / 255, Double(rgba & 0xFF) / 255)
}

extension Color {
    init(rgba: UInt32) {
        let (r, g, b, a) = channels(rgba)
        self.init(.sRGB, red: r, green: g, blue: b, opacity: a)
    }
}

#if canImport(UIKit)
extension UIColor {
    convenience init(rgba: UInt32) {
        let (r, g, b, a) = channels(rgba)
        self.init(red: r, green: g, blue: b, alpha: a)
    }
}
#elseif canImport(AppKit)
extension NSColor {
    convenience init(rgba: UInt32) {
        let (r, g, b, a) = channels(rgba)
        self.init(srgbRed: r, green: g, blue: b, alpha: a)
    }
}
#endif

/// The design system's color roles. Use only these; never a raw color.
public enum DSColor {
    public static var canvas: Color { DSColorTokens.canvas.color }
    public static var ink: Color { DSColorTokens.ink.color }
    public static var muted: Color { DSColorTokens.muted.color }
    public static var faint: Color { DSColorTokens.faint.color }
    public static var rule: Color { DSColorTokens.rule.color }
    public static var surface: Color { DSColorTokens.surface.color }
    public static var accent: Color { DSColorTokens.accent.color }
    public static var accentText: Color { DSColorTokens.accentText.color }
    public static var success: Color { DSColorTokens.success.color }
    public static var warning: Color { DSColorTokens.warning.color }
    public static var error: Color { DSColorTokens.error.color }
    public static var info: Color { DSColorTokens.info.color }
    public static var neutral: Color { DSColorTokens.neutral.color }
    /// Ink at 40%, for hairlines that darken on hover and focus.
    public static var ruleStrong: Color { DSColorTokens.ink.color.opacity(0.4) }
}

// MARK: - Fonts

/// Geist Sans and Geist Mono, registered from the package's resources on first use.
public enum DSFonts {
    private static let registration: Bool = {
        var registered = true
        for name in ["Geist-Variable", "GeistMono-Variable"] {
            guard let url = Bundle.module.url(forResource: name, withExtension: "woff2", subdirectory: "Fonts")
                ?? Bundle.module.url(forResource: name, withExtension: "woff2") else {
                registered = false
                continue
            }
            var error: Unmanaged<CFError>?
            if !CTFontManagerRegisterFontsForURL(url as CFURL, .process, &error) {
                // Already registered by an earlier call or by the app is fine.
                let code = error.map { CFErrorGetCode($0.takeRetainedValue()) } ?? 0
                if code != CTFontManagerError.alreadyRegistered.rawValue { registered = false }
            }
        }
        return registered
    }()

    /// Registers the faces. Safe to call more than once; `dsTheme()` calls it for you.
    @discardableResult
    public static func register() -> Bool { registration }
}

/// One of the system's type styles.
public enum DSTextVariant: String, CaseIterable, Sendable {
    case reading, heading, title, small, label, mono, control

    var postScriptName: String {
        switch self {
        case .reading, .small: return "Geist-Light"
        case .heading, .control: return "Geist-Regular"
        case .title: return "Geist-Medium"
        case .label, .mono: return "GeistMono-Regular"
        }
    }

    /// Point size at the default Dynamic Type size. Reading is 17pt, title 1.4× and small 0.8× of it.
    public var size: CGFloat {
        switch self {
        case .reading, .heading: return 17
        case .title: return 24
        case .small: return 14
        case .label: return 13
        case .mono: return 15
        case .control: return 16
        }
    }

    var textStyle: Font.TextStyle {
        switch self {
        case .reading, .heading: return .body
        case .title: return .title2
        case .small: return .subheadline
        case .label: return .caption
        case .mono: return .callout
        case .control: return .callout
        }
    }

    /// Letter spacing in points.
    public var tracking: CGFloat {
        switch self {
        case .title: return size * -0.02
        case .label: return size * 0.08
        case .mono: return 0
        default: return size * -0.01
        }
    }

    /// Extra space between lines, matching the web line heights.
    public var lineSpacing: CGFloat {
        switch self {
        case .reading, .heading: return size * 0.1
        case .small: return size * 0.2
        case .label: return size * 0.3
        case .mono: return size * 0.2
        default: return 0
        }
    }

    public var font: Font {
        DSFonts.register()
        return Font.custom(postScriptName, size: size, relativeTo: textStyle)
    }
}

/// Fonts by style, for the rare view that sets one directly.
public enum DSFont {
    public static var reading: Font { DSTextVariant.reading.font }
    public static var heading: Font { DSTextVariant.heading.font }
    public static var title: Font { DSTextVariant.title.font }
    public static var small: Font { DSTextVariant.small.font }
    public static var label: Font { DSTextVariant.label.font }
    public static var mono: Font { DSTextVariant.mono.font }
    public static var control: Font { DSTextVariant.control.font }
    /// Code blocks: 13pt mono.
    public static var code: Font {
        DSFonts.register()
        return Font.custom("GeistMono-Regular", size: 13, relativeTo: .footnote)
    }
}

// MARK: - Theme

/// Light, dark, or whatever the system uses.
public enum DSAppearance: String, CaseIterable, Sendable {
    case system, light, dark

    var colorScheme: ColorScheme? {
        switch self {
        case .system: return nil
        case .light: return .light
        case .dark: return .dark
        }
    }
}

/// The root of every app: registers the fonts and sets the reading type, ink and tint.
public struct DSTheme: ViewModifier {
    public var appearance: DSAppearance

    public init(appearance: DSAppearance = .system) {
        self.appearance = appearance
        DSFonts.register()
    }

    public func body(content: Content) -> some View {
        content
            .font(DSFont.reading)
            .foregroundColor(DSColor.ink)
            .tint(DSColor.ink)
            .preferredColorScheme(appearance.colorScheme)
    }
}

extension View {
    /// Apply the design system at the root of an app or a screen.
    public func dsTheme(_ appearance: DSAppearance = .system) -> some View {
        modifier(DSTheme(appearance: appearance))
    }
}

// MARK: - Icons

/// An icon at the system size, in the current foreground color.
struct DSIconImage: View {
    let icon: any IconResource
    var size: CGFloat = 16

    var body: some View {
        icon.image
            .resizable()
            .scaledToFit()
            .frame(width: size, height: size)
            .accessibilityHidden(true)
    }
}

// MARK: - Static rendering

private struct DSStaticRenderingKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    /// Draws platform controls (text fields, menus, scroll views) as plain views, so
    /// ImageRenderer can capture them. Used only for the website's captures.
    var dsStaticRendering: Bool {
        get { self[DSStaticRenderingKey.self] }
        set { self[DSStaticRenderingKey.self] = newValue }
    }
}
