import Foundation
import SwiftUI
import XCTest
@testable import Components

/// Renders every gallery specimen to PNG, light and dark, for the website.
/// Runs only when COMPONENTS_SNAPSHOTS names the output folder (pnpm run snapshots).
final class SnapshotTests: XCTestCase {
    @MainActor
    func testRenderSnapshots() throws {
        guard let output = ProcessInfo.processInfo.environment["COMPONENTS_SNAPSHOTS"] else {
            throw XCTSkip("Set COMPONENTS_SNAPSHOTS to render the website captures")
        }
        guard #available(macOS 13, iOS 16, *) else { throw XCTSkip("ImageRenderer needs macOS 13 or iOS 16") }
        let folder = URL(fileURLWithPath: output)
        try FileManager.default.createDirectory(at: folder, withIntermediateDirectories: true)
        for recipe in DSGallery.recipes {
            for scheme in [ColorScheme.light, .dark] {
                let view = DSGallery.specimen(recipe).environment(\.colorScheme, scheme).environment(\.dsStaticRendering, true)
                let renderer = ImageRenderer(content: view)
                renderer.scale = 2
                #if os(macOS)
                let appearance = NSAppearance(named: scheme == .dark ? .darkAqua : .aqua)!
                var image: CGImage?
                appearance.performAsCurrentDrawingAppearance { image = renderer.cgImage }
                #else
                let image = renderer.cgImage
                #endif
                let cgImage = try XCTUnwrap(image, recipe)
                let url = folder.appendingPathComponent("\(recipe)-\(scheme == .dark ? "dark" : "light").png")
                let destination = try XCTUnwrap(CGImageDestinationCreateWithURL(url as CFURL, "public.png" as CFString, 1, nil))
                CGImageDestinationAddImage(destination, cgImage, nil)
                XCTAssertTrue(CGImageDestinationFinalize(destination), url.path)
            }
        }
    }
}
