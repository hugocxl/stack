from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A freestanding access sign places a route arrow below a wheelchair pictogram with two complete wheels."


def draw(s):
    s.box(14, -22, 0, 48, 34, 5, 6)
    s.box(32, -11, 4, 9, 8, 52, 2)
    sign = Surface(s, (0, 0, 30))
    sign.plate(rounded(0, 0, 74, 68, 6), 7)
    sign.rect(5, 5, 64, 58, 3, EDGE)
    place = sign.viewer_axes(37, 42)
    frame = [(-20, 17), (-14, 17), (-12, 8), (5, 8), (10, -4), (17, -4)]
    sign.stroke([place(x, v) for x, v in frame], BOLD)
    sign.stroke([place(-12, 13), place(-9, 8)], EDGE)
    sign.stroke([place(11, -4), place(11, -9)], EDGE)
    for x, v, r in ((-8, -4, 9), (11, -10, 4)):
        sign.stroke([place(a, b) for a, b in oval(x, v, r, r)], BOLD)
    printed_glyph(sign, "arrow", 37, 16, 16, EDGE)
