import Testing
@testable import Vectors

@Test func vectorNamesAreUniqueAndRoundTrip() {
    let vectors = Vector.allCases
    #expect(vectors.count == 2000)
    #expect(Set(vectors.map(\.rawValue)).count == vectors.count)
    for vector in vectors {
        #expect(Vector(rawValue: vector.rawValue) == vector)
    }
    #expect(Vector.modularDesign.rawValue == "modular-design")
    #expect(Vector(rawValue: "not-a-vector") == nil)
}

@Test func swiftUIImagesCanBeCreated() {
    for vector in Vector.allCases {
        _ = vector.image
    }
}

#if canImport(AppKit)
@Test func appKitImagesLoadAsFourByThreeTemplates() {
    for vector in Vector.allCases {
        let image = vector.nsImage
        #expect(image != nil, "Missing image: \(vector.rawValue)")
        #expect(image?.isTemplate == true)
        if let size = image?.size {
            #expect(abs(size.width * 3 - size.height * 4) < 1, "Unexpected aspect: \(vector.rawValue)")
        }
    }
}
#endif
