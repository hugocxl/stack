from geometry import BOLD, DETAIL, rounded
from scenes.redraws._w4 import Surface, printed_glyph

DESCRIPTION = "A raised keycap presents one bold forward arrow on its top face."


def draw(s):
    s.solid(rounded(-40, -25, 80, 50, 9), 0, 18,
            top=rounded(-34, -20, 68, 40, 8))
    face = Surface(s, lambda u, v: (u, v, 18))
    face.frame(-28, -15, 56, 30, 5, DETAIL)
    printed_glyph(face, "arrow", 0, 0, 21, BOLD)
