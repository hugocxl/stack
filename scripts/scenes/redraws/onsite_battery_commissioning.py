from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph

DESCRIPTION = "Two battery modules with exposed terminal posts carry a commissioning check badge."


def draw(s):
    for x in (-34, 2):
        s.box(x, -17, 0, 32, 34, 31, 3)
        s.box(x - 1, -18, 29, 34, 36, 5, 2)
        for offset in (8, 24):
            s.disk(x + offset, -4, 34, 4.1, 4.1, 6)
            s.ellipse(x + offset, -4, 40, 2.3, 2.3, DETAIL)
        glyph(s, "bolt", x + 16, 17, 15, 7, EDGE)
    badge(s, "check", 36, 17, 17, 13)
