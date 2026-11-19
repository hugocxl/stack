from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import upright_profile
from scenes.systems_shapes import bezel, ring_upright

DESCRIPTION = "Three speech bubbles in a standing queue show one, two, and three dots beside a downward arrow."


def draw(s):
    s.box(-39, -25, 0, 78, 25, 9, 4)
    s.box(-35, -8, 9, 70, 8, 75, 4)
    bezel(s, -30, 0, 14, 60, 65, DETAIL, 2)

    for center, count in ((65, 1), (46, 2), (27, 3)):
        bottom, top = center - 6, center + 6
        outline = [(-19, bottom), (-23, bottom + 3), (-23, top - 3),
                   (-19, top), (7, top), (11, top - 3), (11, bottom + 3),
                   (7, bottom), (-12, bottom), (-18, bottom - 4),
                   (-18, bottom)]
        upright_profile(s, outline, .8, 1, EDGE)
        for index in range(count):
            ring_upright(s, -15 + index * 8, .8, center, 1.8, EDGE)
    arrow(s, [(21, .5, 67), (21, .5, 23)], BOLD, head=8)
