from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import left_face, plate, squircle

DESCRIPTION = "A thick envelope stands upright and carries a refresh badge at its upper corner."


def envelope(s, x=-40, y=0, z=0, w=80, h=52):
    face = left_face(x, y, z)
    plate(s, face, squircle(w, h, 4), 6, (0, -1, 0))
    s.line([face(2, h - 3), face(w/2, h*.38), face(w - 2, h - 3)], EDGE)
    s.line([face(3, 3), face(w*.36, h*.5)], DETAIL)
    s.line([face(w - 3, 3), face(w*.64, h*.5)], DETAIL)
    return face


def draw(s):
    envelope(s)
    badge(s, "refresh", 40, 0, 50, 12)
