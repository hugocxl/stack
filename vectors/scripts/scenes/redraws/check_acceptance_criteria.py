from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A large check badge marks the final row of a three-item acceptance checklist."


def draw(s):
    def point(x, z):
        return .61*x, -.39*x - .43*z, .84*z

    upright_face(s, point, rounded(0, 0, 79, 110, 4), 8)
    rule(s, point, 12, 94, 39, EDGE)
    rule(s, point, 12, 86, 53, DETAIL)
    for z, length in ((68, 34), (46, 27), (20, 30)):
        closed_outline(s, point, rounded(12, z - 6, 12, 12, 1.5), EDGE)
        rule(s, point, 31, z, length, EDGE)
    for z in (68, 46):
        printed_glyph(s, point, "check", 18, z, 5.5, EDGE)
    badge(s, "check", *point(17, 20), 14)
