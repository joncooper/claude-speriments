// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "WakeSleepSounds",
    platforms: [
        .macOS(.v12)
    ],
    targets: [
        .executableTarget(
            name: "WakeSleepSounds",
            path: "Sources/WakeSleepSounds"
        )
    ]
)
