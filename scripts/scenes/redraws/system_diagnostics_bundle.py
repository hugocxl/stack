from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import pulse
from scenes.systems_shapes import bezel

DESCRIPTION = "A zipper closes a boxed diagnostics bundle with a pulse trace across its front."


def draw(s):
    s.box(-37, -25, 0, 74, 50, 45, 4)
    for x in (-25, -16):
        s.line([(x, -24, 45), (x, 24, 45), (x, 25, 16)], EDGE)
    for y in range(-21, 24, 5):
        s.line([(-25, y, 45), (-16, y + 2, 45)], DETAIL)
    for z in (23, 29, 35, 41):
        s.line([(-25, 25, z), (-16, 25, z + 2)], DETAIL)
    bezel(s, -24, 25, 11, 7, 12, EDGE, 2)
    s.line([(x - 10, 25, 22 + z) for x, z in pulse(42, 12)], BOLD)
