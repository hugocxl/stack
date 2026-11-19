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
