from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, face_magnifier, printed_glyph, rule, upright_face

DESCRIPTION = "A magnifying glass rests over the checked rows of a clipboard with a broad metal clip."


def draw(s):
    def point(x, z):
        return .92*x, -.08*x - .52*z, .83*z

    upright_face(s, point, rounded(0, 0, 83, 94, 5), 7)
    closed_outline(s, point, rounded(6, 6, 71, 78, 2), DETAIL)

    def clamp(x, z):
        a, b, c = point(x, z)
        return a + 1.5, b + 3, c + 3

    upright_face(s, clamp, rounded(23, 77, 37, 15, 3), 4)
    rule(s, clamp, 32, 86, 19)
    for index, z in enumerate((61, 43, 25)):
        closed_outline(s, point, rounded(17, z - 5, 10, 10, 1), EDGE)
        if index < 2:
            printed_glyph(s, point, "check", 22, z, 5.3, BOLD)
        rule(s, point, 34, z, 29 - index*3, EDGE)
    face_magnifier(s, point, 49, 47, 19, direction=(.92, -.39))
