from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A squat analog desk clock in a rounded case carries a refresh badge at its upper-right corner."


def draw(s):
    face = Surface(s, (0, 0, 0), across=(.94, -.342), back=(-.342, -.94, 0))
    face.plate(rounded(0, 0, 68, 63, 8), 23)
    face.oval(34, 31.5, 24, 24, EDGE)
    for u, v in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        face.stroke([(34 + u * r, 31.5 + v * r) for r in (16.5, 20.5)], DETAIL)
    printed_glyph(face, "clock", 34, 31.5, 16, BOLD)
    badge(s, "refresh", *face.point(73, 60, 5), 15)
