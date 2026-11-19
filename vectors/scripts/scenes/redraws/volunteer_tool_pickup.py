from geometry import DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "A handled tool case projects from the open compartment of a pickup locker."


def draw(s):
    s.box(-30, -20, 0, 60, 36, 6, 1.5)
    s.box(-29, -20, 6, 58, 4, 56, 1, DETAIL)
    s.box(-30, -16, 6, 5, 32, 56, 1)
    s.box(-25, -16, 29, 50, 32, 4, 1)
    s.box(-30, -20, 61, 60, 36, 6, 1.5)
    s.box(25, -16, 6, 5, 32, 55, 1)
    s.box(-25, 15, 7, 50, 3, 21, 1.1)
    s.line([(14, 18, 20), (22, 18, 20)], DETAIL)
    s.face([(-25, 16, 33), (-45, 34, 33), (-45, 34, 61), (-25, 16, 61)], EDGE)
    s.line([(-40, 29.5, 43), (-40, 29.5, 51)], DETAIL)
    s.box(-17, 1, 33, 34, 28, 12, 2.5)
    s.line([(-16, 29, 41), (16, 29, 41), (17, 5, 41)], EDGE)
    s.line([(-6, 23, 45), (-8, 21, 45), (2, 15, 45), (2, 12, 45),
            (6, 10, 45), (5, 13, 45), (7, 15, 45), (10, 14, 45),
            (10, 17, 45), (7, 19, 45), (4, 18, 45), (-6, 23, 45)], DETAIL)
    s.tube([(-8, 29, 37), (-8, 35, 37), (8, 35, 37), (8, 29, 37)], 1.4)
    for x in (-13, 11):
        bezel(s, x, 29, 38.5, 3, 5, DETAIL, .5)
