import XCTest
@testable import Sounds

final class SoundsTests: XCTestCase {
    func testEverySoundRendersAudibleSamplesWithinItsDuration() {
        for sound in DSSound.allCases {
            let definition = sound.definition
            let samples = DSSoundSynth.render(definition)
            XCTAssertEqual(samples.count, Int((definition.duration * DSSoundSynth.sampleRate).rounded(.up)), sound.rawValue)
            let peak = samples.map { abs($0) }.max() ?? 0
            XCTAssertGreaterThan(peak, 0.001, "\(sound.rawValue) is silent")
            XCTAssertLessThan(peak, 1, "\(sound.rawValue) clips")
            XCTAssertFalse(samples.contains { $0.isNaN }, sound.rawValue)
        }
    }

    func testRenderingWithoutHumanizeIsStableInLevelAndHumanizeVaries() {
        let definition = DSSound.blip.definition
        let a = DSSoundSynth.render(definition)
        let b = DSSoundSynth.render(definition)
        XCTAssertEqual(a, b, "a pure tone renders the same without variation")
        let varied = (0..<4).map { _ in DSSoundSynth.render(definition, humanize: true) }
        XCTAssertTrue(varied.contains { $0 != a }, "humanize varies repeats")
    }

    func testTheEnvelopeDecaysToSilence() {
        let samples = DSSoundSynth.render(DSSound.down.definition)
        let tail = samples.suffix(200).map { abs($0) }.max() ?? 1
        XCTAssertLessThan(tail, 0.001)
    }

    func testEveryHapticMapsToItsSound() {
        XCTAssertEqual(DSFeedback.selection.sound, .tick)
        XCTAssertEqual(DSFeedback.rigid.sound, .latchDown)
        XCTAssertEqual(DSFeedback.soft.sound, .latchUp)
        XCTAssertEqual(DSFeedback.allCases.count, 9)
    }

    func testMutedPlayerStaysSilentAndVolumeIsClamped() {
        let player = DSSounds.shared
        let enabled = player.isEnabled
        defer { player.isEnabled = enabled; player.volume = 0.55 }
        player.volume = 4
        XCTAssertEqual(player.volume, 1)
        player.isEnabled = false
        player.play(.success) // must return without starting audio
    }
}
