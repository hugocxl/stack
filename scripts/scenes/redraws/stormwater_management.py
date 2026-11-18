from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import cable_sleeve

DESCRIPTION = "A flow arrow enters a curbside grate above the exposed chamber and pipe of a cutaway storm drain."


def draw(s):
    length = 38
    top = 32
    s.box(-length, -23, 0, 76, 45, 5, 1.3)
    s.box(-length, -23, 5, 76, 8, 27, 1.2)
    s.box(-length, -15, 5, 9, 37, 27, 1.2)
    cable_sleeve(s, 9, -15, 17, 14, 8, 2)
    s.box(26, -15, 5, 12, 37, 27, 1.2)
    s.face([(-38, -15, top), (38, -15, top), (38, 22, top), (-38, 22, top)], EDGE,
           openings=[[(-23, -8, top), (23, -8, top), (23, 13, top), (-23, 13, top)]])
    s.box(-38, -24, top, 76, 10, 6, 1.2)
    for x in (-19, -11, -3, 5, 13, 21):
        s.box(x, -8, top - 1, 1.8, 21, 1, .55)
    arrow(s, [(-21, 10, 58), (-14, 10, 54), (-6, 10, 46), (-6, 10, 33)],
          BOLD, head=7)
