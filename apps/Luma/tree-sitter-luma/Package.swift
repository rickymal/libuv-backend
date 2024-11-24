// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "TreeSitterLuma",
    products: [
        .library(name: "TreeSitterLuma", targets: ["TreeSitterLuma"]),
    ],
    dependencies: [
        .package(url: "https://github.com/ChimeHQ/SwiftTreeSitter", from: "0.8.0"),
    ],
    targets: [
        .target(
            name: "TreeSitterLuma",
            dependencies: [],
            path: ".",
            sources: [
                "src/parser.c",
                // NOTE: if your language has an external scanner, add it here.
            ],
            resources: [
                .copy("queries")
            ],
            publicHeadersPath: "bindings/swift",
            cSettings: [.headerSearchPath("src")]
        ),
        .testTarget(
            name: "TreeSitterLumaTests",
            dependencies: [
                "SwiftTreeSitter",
                "TreeSitterLuma",
            ],
            path: "bindings/swift/TreeSitterLumaTests"
        )
    ],
    cLanguageStandard: .c11
)
