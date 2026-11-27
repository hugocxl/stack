from math import sin

from geometry import DETAIL, EDGE
from scenes.redraws._sf import left_face

DESCRIPTION = "A graduated staff gauge stands in calm water, its markings reading the level."


def draw(s):
    for r, ink in ((56, DETAIL), (40, DETAIL)):
        s.ellipse(0, 0, 0, r, r*.7, ink)
    s.box(-5, -3, 0, 10, 3, 92, .8)
    face = left_face(-5, 0, 0)
    for k in range(1, 22):
        v = k*4
        s.line([face(0, v), face(6 if k % 5 else 10, v)], EDGE if k % 5 == 0 else DETAIL)

