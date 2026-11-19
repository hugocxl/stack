from geometry import DETAIL, EDGE
from scenes.redraws._w1 import profile_card, screen_point

DESCRIPTION = "A sharpened pencil rests diagonally across the portrait corner of a profile card."


def draw(s):
    profile_card(s, -34, 0, 0)
    anchor = (-29, 2, 36)

    def pencil(u, v, depth=0):
        x, y, z = screen_point(*anchor, .51 * u - .86 * v, .86 * u + .51 * v)
        return (x, y - depth, z)

    outline = [(-15, 0), (-8, -3.3), (17, -3.3), (17, 3.3), (-8, 3.3)]
    s.face([pencil(u, 3.3, d) for u, d in ((-8, 0), (17, 0), (17, 1.9), (-8, 1.9))], EDGE)
    s.face([pencil(17, v, d) for v, d in ((-3.3, 0), (3.3, 0), (3.3, 1.9), (-3.3, 1.9))], EDGE)
    s.face([pencil(u, v) for u, v in outline], EDGE)
    for u in (-8, 12):
        s.line([pencil(u, -3.3), pencil(u, 3.3)], EDGE)
    s.line([pencil(-8, .3), pencil(12, .3)], DETAIL)
    s.line([pencil(-12, -1.4), pencil(-12, 1.4)], DETAIL)
