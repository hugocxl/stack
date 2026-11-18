from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import folded_sheet, rule, upright_face

DESCRIPTION = "A check badge overlaps the heading of a proposal tucked into a presentation folder."


def draw(s):
    def point(x, z):
        return .81*x, -.19*x - .40*z, .88*z

    # The folder back and pocket hold the proposal at its bottom edge.
    upright_face(s, point, rounded(0, 0, 110, 67, 5), 7)

    def sheet(x, z):
        a, b, c = point(x + 13, z + 9)
        return a + 1, b + 3, c + 1

    folded_sheet(s, sheet, 84, 91, fold=14, depth=3)
    rule(s, sheet, 10, 74, 37, EDGE)
    rule(s, sheet, 10, 59, 57, DETAIL)
    rule(s, sheet, 10, 49, 49, DETAIL)

    def pocket(x, z):
        a, b, c = point(x, z)
        return a + 3, b + 8, c

    s.face([pocket(x, z) for x, z in ((0, 0), (110, 0), (110, 33),
                                     (70, 33), (63, 26), (43, 26), (36, 33), (0, 33))], EDGE)
    rule(s, pocket, 13, 10, 84, DETAIL)
    badge(s, "check", *sheet(83, 80), 15)
