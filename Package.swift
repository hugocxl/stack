// swift-tools-version: 6.0
import PackageDescription
let package = Package(
    name: "Icons",
    platforms: [.macOS(.v12), .iOS(.v15), .tvOS(.v15), .watchOS(.v8)],
    products: [.library(name: "Icons", targets: ["Icons"])],
    targets: [
        .target(name: "Icons", resources: [.process("Resources")]),
        .testTarget(name: "IconsTests", dependencies: ["Icons"], path: "tests/IconsTests")
    ]
)
