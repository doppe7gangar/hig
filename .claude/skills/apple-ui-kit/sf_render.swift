// Draws SF Symbols with the Mac's own copy, one PNG per name.
//
//     swift sf_render.swift OUT_DIR house.fill leaf drop.fill ...
//
// sf_icons.py runs this; you shouldn't need to. Each symbol is drawn at
// 64pt and 2x, black on transparent, so a page can use it as a mask and
// colour it with currentColor. Nothing is drawn from memory: a name the
// Mac doesn't know prints "missing" and is skipped.
//
// The symbols stay on your machine, in the design you're making. Apple's
// licence lets you use them in mock-ups of apps for its platforms, not
// pass the images around on their own, so none of them ships in the repo.

import AppKit

let args = Array(CommandLine.arguments.dropFirst())
guard args.count >= 2 else {
    FileHandle.standardError.write("usage: swift sf_render.swift OUT_DIR NAME...\n".data(using: .utf8)!)
    exit(2)
}
let out = URL(fileURLWithPath: args[0], isDirectory: true)
try? FileManager.default.createDirectory(at: out, withIntermediateDirectories: true)
let config = NSImage.SymbolConfiguration(pointSize: 64, weight: .regular)
let scale: CGFloat = 2

for name in args.dropFirst() {
    guard let base = NSImage(systemSymbolName: name, accessibilityDescription: nil),
          let image = base.withSymbolConfiguration(config) else {
        print("missing \(name)")
        continue
    }
    let size = image.size
    guard let rep = NSBitmapImageRep(
        bitmapDataPlanes: nil,
        pixelsWide: Int((size.width * scale).rounded(.up)),
        pixelsHigh: Int((size.height * scale).rounded(.up)),
        bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
        colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0) else {
        print("missing \(name)")
        continue
    }
    rep.size = size
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    image.draw(in: NSRect(origin: .zero, size: size))
    NSGraphicsContext.restoreGraphicsState()
    guard let png = rep.representation(using: .png, properties: [:]) else {
        print("missing \(name)")
        continue
    }
    do {
        try png.write(to: out.appendingPathComponent("\(name).png"))
        print("ok \(name) \(Int(size.width))x\(Int(size.height))")
    } catch {
        print("missing \(name)")
    }
}
