// swift-tools-version: 6.0
import PackageDescription
let package = Package(
    name: "Vectors",
    platforms: [.macOS(.v12), .iOS(.v15), .tvOS(.v15), .watchOS(.v8)],
    products: [.library(name: "Vectors", targets: ["Vectors"])],
    targets: [
        .target(name: "Vectors", resources: [.process("Resources")]),
        .testTarget(name: "VectorsTests", dependencies: ["Vectors"], path: "tests/VectorsTests")
    ]
)
