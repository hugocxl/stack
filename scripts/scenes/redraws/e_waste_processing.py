from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A discarded circuit board sits in a collection bin with a circular-arrow badge on its front wall."


def draw(s):
    s.face([(-34, -22, 27), (34, -22, 27), (29, -17, 0), (-29, -17, 0)], EDGE)
    s.face([(-34, -22, 27), (-34, 20, 27), (-29, 15, 0), (-29, -17, 0)], EDGE)

    s.box(-26, -8, 3, 54, 4, 58, 2)
    bezel(s, -19, -4, 32, 24, 20, EDGE, 1)
    bezel(s, -15, -4, 35, 16, 14, DETAIL, 1)
    for x in (-16, -10, -4, 2):
        s.line([(x, -4, 52), (x, -4, 56)], EDGE)
        s.line([(x, -4, 28), (x, -4, 32)], EDGE)
    for z in (35, 40, 45, 49):
        s.line([(-23, -4, z), (-19, -4, z)], EDGE)
        s.line([(5, -4, z), (9, -4, z)], EDGE)
    s.box(14, -4, 34, 10, 4, 19, 1.1)
    for z in (39, 48):
        s.line([(16, 0, z), (22, 0, z)], DETAIL)
    bezel(s, -16, -4, 17, 30, 8, DETAIL, 1)
    for x in (-13, -8, -3, 2, 7, 12):
        s.line([(x, -4, 19), (x, -4, 23)], DETAIL)

    s.face([(34, -22, 27), (34, 20, 27), (29, 15, 0), (29, -17, 0)], EDGE)
    s.face([(-34, 20, 27), (34, 20, 27), (29, 15, 0), (-29, 15, 0)], EDGE)
    s.line([(-33, 19.6, 22), (33, 19.6, 22), (33, -21, 22)], DETAIL)
    badge(s, "refresh", -1, 22, 15, 12)
