from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import capsule, left_face
from scenes.redraws._w1 import portrait_mark

DESCRIPTION = "A profile card shows a display-name field with a blinking text cursor beside its avatar."


def draw(s):
    s.box(-40, -6, 0, 80, 6, 50, 3)
    face = left_face(-40, 0, 0)
    portrait_mark(s, -20, 0, 28, 13)
    field = [face(38 + u, 22 + v) for u, v in capsule(36, 12)]
    s.line(field + field[:1], EDGE)
    s.line([face(44, 28), face(58, 28)], DETAIL)
    s.line([face(62, 24.5), face(62, 31.5)], BOLD)
    s.line([face(8, 8), face(72, 8)], DETAIL)
