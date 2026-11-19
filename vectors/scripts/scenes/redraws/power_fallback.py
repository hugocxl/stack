from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow, glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A curved return arrow loops around the side of an upright backup battery."


def draw(s):
    s.box(-24, -24, 0, 48, 32, 63, 5)
    s.box(-11, -15, 63, 22, 14, 7, 2)
    bezel(s, -18, 8, 8, 36, 46, DETAIL, 3)
    glyph(s, "bolt", -2, 8, 32, 19, EDGE)
    return_path = [(x, -13, z) for x, z in oval(29, 31, 22, 22, -110, 119, 25)]
    arrow(s, return_path, BOLD, head=9)
