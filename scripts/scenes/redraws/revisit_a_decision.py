from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, printed_glyph, rule, upright_face

DESCRIPTION = "A circular history arrow overlaps the corner of a square decision note with a checked box."


def draw(s):
    def point(x, z):
        return .72*x, -.28*x - .22*z, .9*z

    upright_face(s, point, rounded(0, 0, 84, 84, 2), 5)
    closed_outline(s, point, [(14, 34), (37, 34), (37, 57), (14, 57)], EDGE)
    printed_glyph(s, point, "check", 26, 46, 11, EDGE)
    rule(s, point, 47, 51, 22, EDGE)
    rule(s, point, 47, 40, 17, DETAIL)
    rule(s, point, 14, 21, 53, DETAIL)
    badge(s, "refresh", *point(83, 82), 16)
