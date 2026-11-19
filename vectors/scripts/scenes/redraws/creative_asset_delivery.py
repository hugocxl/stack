from geometry import rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import Surface, landscape, upright

DESCRIPTION = "A tabbed folder holds a photo print and bears a download arrow on its front."


def draw(s):
    upright(s, [(0, 0), (96, 0), (96, 61), (40, 61), (34, 71), (4, 71), (0, 66)],
            0, 4)
    upright(s, rounded(44, 22, 44, 56, 3), 7, 3)
    print_face = Surface(s, lambda u, v: (u, 7, 73 - v))
    landscape(print_face, 49, 0, 34, 21)
    upright(s, [(0, 0), (96, 0), (96, 47), (92, 52), (4, 52), (0, 47)], 16, 4)
    s.face([(96, 0, 0), (96, 16, 0), (96, 16, 5), (96, 0, 5)])
    glyph(s, "down", 48, 16, 27, 22)
