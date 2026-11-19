from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, printed_glyph

DESCRIPTION = "A standing reservation pad has two confirmed rows and a clock badge on the waiting row."


def draw(s):
    face = front_surface(s, angle=-12, z=6, lean=.72)
    s.face([face.at(0, 0), face.at(79, 0), (70, -80, 0), (0, -66, 0)])
    s.face([face.at(79, 0), (70, -80, 0), face.at(79, 87)])
    face.slab(rounded(0, 0, 79, 87, 5), 6)
    face.rows(10, 72, (42,), ink=EDGE)
    face.line([(0, 62), (79, 62)], EDGE)
    for v, width in ((50, 37), (34, 29), (18, 27)):
        face.rows(24, v, (width,), ink=EDGE)
        if v > 18:
            printed_glyph(face, "check", 14, v, 6, EDGE)
        else:
            face.oval(14, v, 3, 3, EDGE)
        face.line([(9, v - 8), (69, v - 8)])
    badge(s, "clock", *face.at(76, 17), 14)
