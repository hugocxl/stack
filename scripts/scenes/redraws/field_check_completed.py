from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule, upright_face

DESCRIPTION = "A check badge attaches to the metal clip of a site-inspection clipboard with a simple floor plan."


def draw(s):
    def point(x, z):
        return .88*x, -.12*x - .49*z, .82*z

    upright_face(s, point, rounded(0, 0, 82, 96, 5), 7)
    closed_outline(s, point, rounded(6, 7, 70, 81, 2), DETAIL)

    def clip(x, z):
        a, b, c = point(x, z)
        return a + 1, b + 3, c + 2

    upright_face(s, clip, rounded(23, 80, 36, 18, 3), 4)
    rule(s, clip, 29, 90, 22, EDGE)
    closed_outline(s, point, [(16, 37), (63, 37), (63, 73), (16, 73)], EDGE)
    s.line([point(35, 73), point(35, 57), point(47, 57)], EDGE)
    s.line([point(35, 47), point(35, 37)], EDGE)
    s.line([point(55, 57), point(63, 57)], EDGE)
    rule(s, point, 16, 25, 42, DETAIL)
    rule(s, point, 16, 17, 32, DETAIL)
    badge(s, "check", *clip(60, 97), 15)
