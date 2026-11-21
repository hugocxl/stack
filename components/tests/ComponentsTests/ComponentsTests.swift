import Foundation
import SwiftUI
import XCTest
@testable import Components

final class ComponentsTests: XCTestCase {
    private var recipesDirectory: URL {
        URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("../../recipes").standardized
    }

    func testFontsRegister() throws {
        XCTAssertTrue(DSFonts.register())
        for name in ["Geist-Light", "Geist-Regular", "Geist-Medium", "GeistMono-Regular"] {
            #if canImport(UIKit)
            XCTAssertNotNil(UIFont(name: name, size: 17), name)
            #elseif canImport(AppKit)
            XCTAssertNotNil(NSFont(name: name, size: 17), name)
            #endif
        }
    }

    func testTokensDecode() {
        XCTAssertEqual(DSColorTokens.canvas.light, 0xF5F5F4FF)
        XCTAssertEqual(DSColorTokens.ink.dark, 0xEDEDEDFF)
        XCTAssertEqual(DSSpace.s5, 20)
        XCTAssertEqual(DSRadius.control, 6)
        XCTAssertEqual(DSLayout.target, 44)
    }

    /// Compact keeps every ratio and role and only steps sizes down.
    func testCompactDensityScalesTypeAndTargets() {
        XCTAssertEqual(DSTextVariant.reading.size(.regular), 17)
        XCTAssertEqual(DSTextVariant.reading.size(.compact), 13)
        XCTAssertEqual(DSTextVariant.title.size(.compact), 17)
        XCTAssertEqual(DSTextVariant.label.size(.compact), 13, "one size: labels read at the reading size")
        XCTAssertEqual(DSTextVariant.small.size(.compact), DSTextVariant.reading.size(.compact))
        XCTAssertEqual(DSTextVariant.reading.size, DSTextVariant.reading.size(.regular))
        XCTAssertEqual(DSDensity.regular.metrics.target, DSLayout.target)
        XCTAssertEqual(DSDensity.compact.metrics.target, 28)
        for variant in DSTextVariant.allCases {
            XCTAssertLessThanOrEqual(variant.size(.compact), variant.size(.regular), variant.rawValue)
            XCTAssertLessThanOrEqual(variant.size(.compact), DSTextVariant.title.size(.compact), "nothing is larger than the title")
        }
        XCTAssertEqual(DSTextVariant.label.tracking(.compact), 13 * 0.1, accuracy: 0.0001)
        let sizes = Set(DSTextVariant.allCases.filter { $0 != .title }.map { $0.size(.compact) })
        XCTAssertEqual(sizes.count, 1, "every style but the title is the reading size")
    }

    /// Spacing in compact comes from the token scale, never free numbers.
    /// One spacing unit lays out everything: padding, gaps and the space between sections.
    func testEveryLayoutSpacingIsTheUnit() {
        let steps: Set<CGFloat> = [DSSpace.s1, DSSpace.s2, DSSpace.s3, DSSpace.s4, DSSpace.s5, DSSpace.s6, DSSpace.s7]
        for density in DSDensity.allCases {
            let m = density.metrics
            XCTAssertTrue(steps.contains(m.unit), "\(m.unit) at \(density) is not a spacing token")
            for value in [m.gap, m.inset, m.labelGap, m.stack, m.section] {
                XCTAssertEqual(value, m.unit, "a layout spacing at \(density) is not the unit")
            }
            // Rows meet on a hairline; they never add space between them.
            XCTAssertEqual(m.row, 0)
        }
        XCTAssertEqual(DSDensity.compact.metrics.unit, 12)
        XCTAssertEqual(DSDensity.regular.metrics.unit, 16)
    }

    func testOptionsAcceptLocalizedAndVerbatimLabels() {
        let localized = DSOption("a", label: "Day")
        let verbatim = DSOption("b", label: String("Week"))
        XCTAssertEqual([localized.id, verbatim.id], ["a", "b"])
    }

    func testSoundsAreOffUnlessTheAppTurnsThemOn() {
        XCTAssertFalse(EnvironmentValues().dsSounds)
        XCTAssertEqual(EnvironmentValues().dsDensity, .regular)
    }

    /// Every single-line control is exactly the control height at both densities, so a row of
    /// mixed controls lines up.
    @MainActor
    func testEveryControlIsTheControlHeight() throws {
        #if os(macOS)
        func height(_ view: some View, _ density: DSDensity) -> CGFloat {
            let host = NSHostingController(rootView: view.dsTheme().dsDensity(density).environment(\.dsStaticRendering, true))
            return host.sizeThatFits(in: CGSize(width: 320, height: 400)).height
        }
        let controls: [(String, AnyView)] = [
            ("button", AnyView(DSButton("Export") {})),
            ("secondary button", AnyView(DSButton("Cancel", variant: .secondary) {})),
            ("icon button", AnyView(DSIconButton(StrokeIcon.close, label: "Close") {})),
            ("select", AnyView(DSSelect("Rate", selection: .constant(1), options: [DSOption(1, label: "48 kHz")], labelPlacement: .hidden))),
            ("text field", AnyView(DSTextField("Name", text: .constant("Sunrise"), labelPlacement: .hidden))),
            ("search field", AnyView(DSSearchField("Search", text: .constant("")))),
            ("segmented control", AnyView(DSSegmentedControl("Mode", selection: .constant(0), options: [DSOption(0, label: "A"), DSOption(1, label: "B")]))),
            ("slider", AnyView(DSSlider(value: .constant(40), ticks: 0))),
            ("switch", AnyView(DSSwitch("Sounds", isOn: .constant(true)))),
            ("checkbox", AnyView(DSCheckbox("Loop", isOn: .constant(false)))),
            ("menu", AnyView(DSMenu("Sort") { Button("Name") {} })),
        ]
        for density in DSDensity.allCases {
            for (name, view) in controls {
                XCTAssertEqual(height(view, density), density.metrics.control, accuracy: 0.5, "\(name) at \(density)")
            }
        }
        #endif
    }

    /// Every recipe with a Swift implementation has a specimen in the gallery, in the same set.
    func testGalleryCoversEverySwiftRecipe() throws {
        let files = try FileManager.default.contentsOfDirectory(at: recipesDirectory, includingPropertiesForKeys: nil)
            .filter { $0.pathExtension == "json" }
        var swiftRecipes: Set<String> = []
        for file in files {
            let json = try JSONSerialization.jsonObject(with: Data(contentsOf: file)) as! [String: Any]
            let platforms = json["platforms"] as! [String: Any]
            if platforms["swift"] is String { swiftRecipes.insert(json["name"] as! String) }
        }
        XCTAssertFalse(swiftRecipes.isEmpty)
        XCTAssertEqual(Set(DSGallery.recipes), swiftRecipes)
    }

    @MainActor
    func testSpecimensRender() throws {
        guard #available(macOS 13, iOS 16, *) else { throw XCTSkip("ImageRenderer needs macOS 13 or iOS 16") }
        for recipe in DSGallery.recipes {
            let renderer = ImageRenderer(content: DSGallery.specimen(recipe))
            XCTAssertNotNil(renderer.cgImage, recipe)
        }
    }
}
