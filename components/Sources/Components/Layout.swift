import SwiftUI

/// The canvas, gutter and reading column a screen sits in. It scrolls.
public struct DSPage<Content: View>: View {
    let opening: Bool
    let content: Content

    /// `opening` adds the generous top space of a page's start.
    public init(opening: Bool = true, @ViewBuilder content: () -> Content) {
        self.opening = opening
        self.content = content()
    }

    public var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 0) { content }
                .frame(maxWidth: DSLayout.measure, alignment: .leading)
                .padding(.horizontal, DSSpace.s5)
                .padding(.top, opening ? DSSpace.s8 : DSSpace.s6)
                .padding(.bottom, DSSpace.s9)
                .frame(maxWidth: .infinity)
        }
        .background(DSColor.canvas.ignoresSafeArea())
        .dsTheme()
    }
}
