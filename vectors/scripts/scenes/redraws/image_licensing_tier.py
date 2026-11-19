from geometry import EDGE, rounded
from scenes.redraws._kit import coin, glyph
from scenes.redraws._w4 import Surface, landscape, upright

DESCRIPTION = "A landscape thumbnail and a raised star seal appear on a photo license certificate."


def draw(s):
    upright(s, rounded(0, 0, 105, 74, 4), 0, 8, angle=-18)

    def at(u, v):
        return (.9510565*u, -.309017*u, 74 - v)

    certificate = Surface(s, at)
    certificate.frame(6, 6, 93, 62, 2, EDGE)
    landscape(certificate, 12, 14, 44, 32)
    certificate.rows(12, 53, (42, 31), step=7)
    certificate.rows(64, 17, (24, 19), step=6, ink=EDGE)
    x, y, z = at(79, 47)
    y += 2
    s.face([(x - 9, y, z - 4), (x - 12, y, z - 17), (x - 3, y, z - 14),
            (x + 5, y, z - 17), (x + 7, y, z - 4)])
    coin(s, x, y + 2, z, 12, depth=2)
    glyph(s, "star", x, y + 2, z, 10)
