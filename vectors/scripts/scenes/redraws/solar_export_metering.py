from geometry import EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import meter_reader

DESCRIPTION = "A right-pointing export arrow fills the window of an electrical meter with a sun emblem."


def draw(s):
    meter_reader(s)
    glyph(s, "arrow", 0, 17, 44.5, 16)
    s.line([(-5, 17, 58), (-3.5, 17, 61), (0, 17, 62.3),
            (3.5, 17, 61), (5, 17, 58)], EDGE)
    for a, b in (((-7, 59), (-9, 61)), ((-4, 63), (-5.5, 65)),
                 ((0, 64), (0, 66)), ((4, 63), (5.5, 65)), ((7, 59), (9, 61))):
        s.line([(a[0], 17, a[1]), (b[0], 17, b[1])], EDGE)
