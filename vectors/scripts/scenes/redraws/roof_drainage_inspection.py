from geometry import DETAIL, EDGE
from scenes.redraws._w2 import face_magnifier

DESCRIPTION = "A magnifier frames the elbow where a roof gutter joins the downspout."


def draw(s):
    s.box(-36, -13, 0, 72, 25, 44, 1)
    s.face([(36, -15, 44), (36, 14, 44), (36, -13, 68)])
    s.face([(-39, -13, 68), (39, -13, 68), (39, 16, 43), (-39, 16, 43)])
    for y in (-4, 6):
        z = 68 - (y + 13)*25/29
        s.line([(-39, y, z), (39, y, z)], DETAIL)
    for z in (14, 29):
        s.line([(-36, 12.1, z), (36, 12.1, z)], DETAIL)
    s.tube([(23, 21, 41), (23, 21, 31), (23, 17, 25),
            (23, 17, 6), (23, 23, 0), (23, 30, 0)], 3.5, EDGE)
    profile = [(15, 43), (17, 39), (23, 39), (26, 42), (26, 46)]
    for a, b in zip(profile, profile[1:]):
        s.face([(-39, *a), (39, *a), (39, *b), (-39, *b)], EDGE)
    s.line([(-39, 16, 45), (39, 16, 45)], DETAIL)
    s.face([(39, y, z) for y, z in profile], EDGE)

    def glass(u, v):
        return 29 + .65*u, 25 - .35*u, 42 + v

    face_magnifier(s, glass, 0, 0, 14, direction=(.92, -.39))
