// swift-tools-version: 6.0
import PackageDescription
let package = Package(
    name: "hugocxlStack",
    platforms: [.macOS(.v12), .iOS(.v15), .tvOS(.v15), .watchOS(.v8)],
    products: [
        .library(name: "Icons", targets: ["Icons"]),
        .library(name: "Vectors", targets: ["Vectors"]),
        .library(name: "Components", targets: ["Components"])
    ],
    targets: [
        .target(name: "Icons", path: "icons/Sources/Icons", resources: [.process("Resources")]),
        .testTarget(name: "IconsTests", dependencies: ["Icons"], path: "icons/tests/IconsTests"),
        .target(name: "Vectors", path: "vectors/Sources/Vectors", resources: [.process("Resources")]),
        .testTarget(name: "VectorsTests", dependencies: ["Vectors"], path: "vectors/tests/VectorsTests"),
        .target(name: "Components", dependencies: ["Icons", "Vectors"], path: "components/Sources/Components", resources: [.copy("Resources/Fonts")]),
        .testTarget(name: "ComponentsTests", dependencies: ["Components"], path: "components/tests/ComponentsTests")
    ]
)
