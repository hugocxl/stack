import Testing
@testable import Icons

@Test func iconNamesAreUniqueAndRoundTrip() {
    let icons = Icon.allCases
    #expect(!icons.isEmpty)
    #expect(Set(icons.map(\.rawValue)).count == icons.count)
    for icon in icons {
        #expect(Icon(rawValue: icon.rawValue) == icon)
    }
    #expect(Icon(rawValue: "not-an-icon") == nil)
}

@Test func swiftUIImagesCanBeCreated() {
    for icon in Icon.allCases {
        _ = icon.image
    }
}

#if canImport(AppKit)
@Test func appKitImagesLoadFromTheResourceBundle() {
    for icon in Icon.allCases {
        #expect(icon.nsImage != nil, "Missing image: \(icon.rawValue)")
        #expect(icon.nsImage?.isTemplate == true)
    }
}
#endif

@Test func everyStyleLoadsItsOwnVectorResources() {
    #expect(SolidIcon.allCases.count == StrokeIcon.allCases.count)
    #expect(SolidIcon(rawValue: "github") == nil)
    for icon in SolidIcon.allCases {
        #expect(Icon(rawValue: icon.rawValue) != nil)
        #expect(StrokeIcon(rawValue: icon.rawValue) != nil)
        _ = icon.image
        #if canImport(AppKit)
        #expect(icon.nsImage != nil, "Missing solid image: \(icon.rawValue)")
        #expect(icon.nsImage?.isTemplate == true)
        #expect(icon.nsImage?.size.width ?? 0 > 0)
        #endif
    }
    for icon in StrokeIcon.allCases {
        _ = icon.image
        #if canImport(AppKit)
        #expect(icon.nsImage != nil, "Missing stroke image: \(icon.rawValue)")
        #expect(icon.nsImage?.isTemplate == true)
        #endif
    }
}

#if canImport(AppKit)
import AppKit
import SwiftUI

@Test func assignedTintsResolveForBothAppearances() throws {
    let folder = try #require(Icon.folder.defaultColor)
    #expect(folder == SolidIcon.folder.defaultColor)
    #expect(folder == StrokeIcon.folder.defaultColor)
    #expect(Icon.react.defaultColor != nil)
    #expect(Icon.search.defaultColor == nil)
    let color = NSColor(folder)
    for (appearance, expected) in [(NSAppearance.Name.aqua, [160, 128, 5]), (.darkAqua, [206, 171, 60])] {
        let theme = try #require(NSAppearance(named: appearance))
        var resolved: NSColor?
        theme.performAsCurrentDrawingAppearance {
            resolved = color.usingColorSpace(.sRGB)
        }
        let rgb = try #require(resolved)
        #expect([rgb.redComponent, rgb.greenComponent, rgb.blueComponent].map { Int(($0 * 255).rounded()) } == expected)
    }
}
#endif
