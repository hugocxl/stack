import SwiftUI
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

/// A named vector resource in the Vectors asset catalog.
public protocol VectorResource: Sendable {
    var resourceName: String { get }
}

extension VectorResource {
    /// A template image that inherits the caller's foreground style.
    /// Apply `.resizable()` and `.aspectRatio(contentMode: .fit)` to size it; the artwork is 4:3.
    public var image: Image { Image(resourceName, bundle: .module).renderingMode(.template) }
#if canImport(UIKit)
    /// The catalog image, suitable for tinting in UIKit.
    public var uiImage: UIImage? {
        UIImage(named: resourceName, in: .module, compatibleWith: nil)?.withRenderingMode(.alwaysTemplate)
    }
#elseif canImport(AppKit)
    /// The catalog image, suitable for tinting in AppKit.
    public var nsImage: NSImage? { Bundle.module.image(forResource: NSImage.Name(resourceName)) }
#endif
}
