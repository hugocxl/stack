import AVFoundation
import Foundation

#if canImport(UIKit) && !os(watchOS) && !os(tvOS)
    import UIKit
#elseif canImport(AppKit)
    import AppKit
#endif

// The Swift port of @hugocxl/sounds' Web Audio engine: the same layers, filters and envelopes,
// synthesized natively. Nothing is a file; every play is rendered fresh, with the same small
// variation the web engine adds, so repeats never sound identical.

/// One layer of a sound: a burst of filtered noise or a gliding oscillator.
public enum DSSoundLayer: Sendable, Hashable {
    public enum Filter: String, Sendable { case bandpass, highpass, lowpass }
    public enum Wave: String, Sendable { case sine, triangle, square, sawtooth }

    /// White noise through one biquad filter, rising in 0.8ms and falling over `decay` seconds.
    case noise(at: Double, filter: Filter, frequency: Double, q: Double, level: Double, decay: Double)
    /// An oscillator gliding from `frequency` to `to` over `decay` seconds.
    case tone(
        at: Double, wave: Wave, frequency: Double, to: Double, level: Double, decay: Double,
        attack: Double)

    var start: Double {
        switch self {
        case .noise(let at, _, _, _, _, _), .tone(let at, _, _, _, _, _, _): return at
        }
    }

    var decay: Double {
        switch self {
        case .noise(_, _, _, _, _, let decay), .tone(_, _, _, _, _, let decay, _): return decay
        }
    }
}

/// A sound as data: its group, what it is for and its layers.
public struct DSSoundDefinition: Sendable, Hashable {
    public let group: DSSoundGroup
    public let description: String
    public let layers: [DSSoundLayer]

    public init(group: DSSoundGroup, description: String = "", layers: [DSSoundLayer]) {
        self.group = group
        self.description = description
        self.layers = layers
    }

    /// Length in seconds, tails included.
    public var duration: Double { layers.map { $0.start + $0.decay + 0.02 }.max() ?? 0 }
}

/// Renders sounds to samples, exactly as the web engine schedules them.
public enum DSSoundSynth {
    public static let sampleRate: Double = 48_000

    /// Mono samples for a sound. `humanize` adds the web engine's per-play variation.
    public static func render(_ sound: DSSoundDefinition, gain: Double = 1, humanize: Bool = false)
        -> [Float]
    {
        var generator = SystemRandomNumberGenerator()
        let count = Int((sound.duration * sampleRate).rounded(.up))
        var out = [Float](repeating: 0, count: count)
        func vary(_ amount: Double) -> Double {
            humanize ? 1 + Double.random(in: -amount...amount, using: &generator) : 1
        }
        for layer in sound.layers {
            switch layer {
            case .noise(let at, let filter, let frequency, let q, let level, let decay):
                var biquad = Biquad(filter, frequency: frequency * vary(0.06), q: q, sampleRate: sampleRate)
                let peak = level * vary(0.15)
                write(into: &out, start: at, decay: decay, level: peak, attack: 8e-4) { _ in
                    biquad.process(Double.random(in: -1...1, using: &generator))
                }
            case .tone(let at, let wave, let frequency, let to, let level, let decay, let attack):
                let from = frequency * vary(0.04)
                let end = max(20, to / frequency * from)
                var phase = 0.0
                let peak = level * vary(0.12)
                write(into: &out, start: at, decay: decay, level: peak, attack: attack) { t in
                    let progress = min(1, t / decay)
                    let hz = from * pow(end / from, progress)
                    phase += hz / sampleRate
                    phase -= phase.rounded(.down)
                    return oscillator(wave, phase)
                }
            }
        }
        if gain != 1 { for i in out.indices { out[i] *= Float(gain) } }
        return out
    }

    /// Writes one layer: its signal through the linear attack and exponential decay envelope.
    private static func write(
        into out: inout [Float], start: Double, decay: Double, level: Double, attack: Double,
        signal: (Double) -> Double
    ) {
        let first = Int(start * sampleRate)
        let last = min(out.count, Int(((start + decay + 0.02) * sampleRate).rounded(.up)))
        guard first < last, level > 0 else { return }
        let floor = 1e-4
        for index in first..<last {
            let t = Double(index - first) / sampleRate
            let envelope: Double
            if t < attack {
                envelope = level * t / attack
            } else if t < decay {
                envelope = level * pow(floor / level, (t - attack) / max(decay - attack, 1e-6))
            } else {
                envelope = floor
            }
            out[index] += Float(signal(t) * envelope)
        }
    }

    private static func oscillator(_ wave: DSSoundLayer.Wave, _ phase: Double) -> Double {
        switch wave {
        case .sine: return sin(2 * .pi * phase)
        case .triangle: return 1 - 4 * abs(phase - 0.5)
        case .square: return phase < 0.5 ? 1 : -1
        case .sawtooth: return 2 * phase - 1
        }
    }

    /// The Web Audio biquad (Audio EQ Cookbook), with Web Audio's Q conventions.
    private struct Biquad {
        var b0 = 0.0, b1 = 0.0, b2 = 0.0, a1 = 0.0, a2 = 0.0
        var x1 = 0.0, x2 = 0.0, y1 = 0.0, y2 = 0.0

        init(_ filter: DSSoundLayer.Filter, frequency: Double, q: Double, sampleRate: Double) {
            let w0 = 2 * .pi * min(frequency, sampleRate / 2 - 1) / sampleRate
            let cosw = cos(w0)
            var a0 = 1.0
            switch filter {
            case .bandpass:
                let alpha = sin(w0) / (2 * max(q, 1e-4))
                b0 = alpha
                b1 = 0
                b2 = -alpha
                a0 = 1 + alpha
                a1 = -2 * cosw
                a2 = 1 - alpha
            case .highpass, .lowpass:
                // Web Audio gives low- and highpass Q in decibels.
                let alpha = sin(w0) / (2 * pow(10, q / 20))
                let sign = filter == .highpass ? -1.0 : 1.0
                b1 = filter == .highpass ? -(1 + cosw) : 1 - cosw
                b0 = (1 - sign * cosw) / 2
                b2 = b0
                a0 = 1 + alpha
                a1 = -2 * cosw
                a2 = 1 - alpha
            }
            b0 /= a0
            b1 /= a0
            b2 /= a0
            a1 /= a0
            a2 /= a0
        }

        mutating func process(_ x: Double) -> Double {
            let y = b0 * x + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            return y
        }
    }
}

/// Plays interface sounds. Sound confirms what the hand did: a press, a toggle, a detent, a
/// key, an overlay opening, the result of an action. It never carries information alone, and
/// people can turn it off with `isEnabled`.
public final class DSSounds: @unchecked Sendable {
    public static let shared = DSSounds()

    private let lock = NSLock()
    private var engine: AVAudioEngine?
    private var players: [AVAudioPlayerNode] = []
    private var next = 0
    private var _enabled = true
    private var _volume = 0.55
    private let format = AVAudioFormat(
        standardFormatWithSampleRate: DSSoundSynth.sampleRate, channels: 1)!

    /// Whether sounds play. On by default; offer people a setting.
    public var isEnabled: Bool {
        get { lock.withLock { _enabled } }
        set { lock.withLock { _enabled = newValue } }
    }

    /// Volume of every sound, from 0 to 1. The default is 0.55, as on the web.
    public var volume: Double {
        get { lock.withLock { _volume } }
        set { lock.withLock { _volume = min(1, max(0, newValue)) } }
    }

    /// Play a sound now. Returns at once and never throws.
    public func play(_ sound: DSSound) { play(sound.definition) }

    /// Play your own layers.
    public func play(_ definition: DSSoundDefinition) {
        let (enabled, volume) = lock.withLock { (_enabled, _volume) }
        guard enabled, volume > 0 else { return }
        let samples = DSSoundSynth.render(definition, gain: volume, humanize: true)
        guard !samples.isEmpty,
            let buffer = AVAudioPCMBuffer(
                pcmFormat: format, frameCapacity: AVAudioFrameCount(samples.count)),
            let channel = buffer.floatChannelData?[0]
        else { return }
        buffer.frameLength = AVAudioFrameCount(samples.count)
        samples.withUnsafeBufferPointer { channel.update(from: $0.baseAddress!, count: samples.count) }
        lock.withLock {
            guard let player = player() else { return }
            player.scheduleBuffer(buffer, at: nil, options: .interrupts)
            if !player.isPlaying { player.play() }
        }
    }

    /// Play the sound for a haptic, and tap the trackpad or the device where it can.
    public func haptic(_ kind: DSFeedback) {
        play(kind.sound)
        #if canImport(UIKit) && !os(watchOS) && !os(tvOS) && !os(visionOS)
            DispatchQueue.main.async {
                switch kind {
                case .selection: UISelectionFeedbackGenerator().selectionChanged()
                case .success: UINotificationFeedbackGenerator().notificationOccurred(.success)
                case .warning: UINotificationFeedbackGenerator().notificationOccurred(.warning)
                case .error: UINotificationFeedbackGenerator().notificationOccurred(.error)
                case .light: UIImpactFeedbackGenerator(style: .light).impactOccurred()
                case .medium: UIImpactFeedbackGenerator(style: .medium).impactOccurred()
                case .heavy: UIImpactFeedbackGenerator(style: .heavy).impactOccurred()
                case .rigid: UIImpactFeedbackGenerator(style: .rigid).impactOccurred()
                case .soft: UIImpactFeedbackGenerator(style: .soft).impactOccurred()
                }
            }
        #elseif canImport(AppKit)
            DispatchQueue.main.async {
                let pattern: NSHapticFeedbackManager.FeedbackPattern =
                    kind == .selection
                    ? .alignment : kind == .rigid || kind == .soft ? .levelChange : .generic
                NSHapticFeedbackManager.defaultPerformer.perform(pattern, performanceTime: .now)
            }
        #endif
    }

    /// A round-robin pool of players, so overlapping sounds never cut each other off.
    private func player() -> AVAudioPlayerNode? {
        if engine == nil {
            let engine = AVAudioEngine()
            for _ in 0..<6 {
                let node = AVAudioPlayerNode()
                engine.attach(node)
                engine.connect(node, to: engine.mainMixerNode, format: format)
                players.append(node)
            }
            engine.prepare()
            self.engine = engine
        }
        guard let engine else { return nil }
        if !engine.isRunning {
            do { try engine.start() } catch { return nil }
        }
        defer { next = (next + 1) % players.count }
        return players[next]
    }
}

extension DSSound {
    /// Play this sound with the shared player.
    public func play() { DSSounds.shared.play(self) }
}
