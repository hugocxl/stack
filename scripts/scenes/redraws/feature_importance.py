from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w2 import level_face

DESCRIPTION = "Three labeled horizontal contribution bars descend in rank from longest to shortest."


def draw(s):
    s.line([level_face(22, 12), level_face(22, 83)], EDGE)
    for index, (z, length) in enumerate(((66, 99), (42, 68), (18, 37))):
        bar = rounded(25, z, length, 12, 2)
        s.face([level_face(x, v, -5) for x, v in bar], DETAIL)
        s.face([level_face(x, v) for x, v in bar], BOLD if index == 0 else EDGE)
    for mark in (
        oval(11, 72, 4.5, 4.5, count=28),
        ((6, 43), (16, 43), (11, 52), (6, 43)),
        ((7, 20), (15, 20), (15, 28), (7, 28), (7, 20)),
    ):
        s.line([level_face(x, z) for x, z in mark], EDGE)
