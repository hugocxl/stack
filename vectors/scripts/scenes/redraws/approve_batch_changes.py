from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule, upright_face

DESCRIPTION = "Three aligned change sheets form a packet, with a large check badge over the front sheet's changed rows."


def draw(s):
    def front(x, z):
        return .56*x, -.44*x - .67*z, .72*z

    for offset in (14, 7, 0):
        def sheet(x, z):
            a, b, c = front(x, z)
            return a + offset*.3, b - offset, c + offset*.42

        upright_face(s, sheet, rounded(0, 0, 89, 79, 4), 4)
    rule(s, front, 13, 63, 40, EDGE)
    for z, length in ((46, 39), (31, 31), (16, 41)):
        closed_outline(s, front, rounded(13, z - 4, 8, 8, 1.2), DETAIL)
        rule(s, front, 26, z, length, DETAIL)
    badge(s, "check", *front(83, 37), 21)
