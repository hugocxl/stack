from geometry import DETAIL
from scenes.redraws._w5 import harvest_crate

DESCRIPTION = "A produce crate crosses the raised threshold of an open walk-in cooler."


def draw(s):
    s.box(0, 0, 0, 62, 34, 4, 1.5)
    s.box(0, 0, 4, 62, 5, 62, 2)
    s.box(0, 4, 4, 8, 24, 62, 1)
    s.box(54, 4, 4, 8, 24, 62, 1)
    s.box(0, 4, 58, 62, 24, 8, 1.5)
    s.line([(9, 27, 4), (53, 27, 4)], DETAIL)
    s.line([(51, 28, 6), (51, 28, 55), (10, 28, 55)], DETAIL)
    # The insulated door swings out around the left jamb.
    def door(u, z, thickness=0):
        return (7 - .48*u + thickness, 28 + u, z)

    s.face([door(0, 5), door(0, 58), door(37, 58), door(37, 5)])
    s.face([door(37, 5), door(37, 58), door(37, 58, 4.5), door(37, 5, 4.5)])
    s.face([door(0, 58), door(37, 58), door(37, 58, 4.5), door(0, 58, 4.5)])
    s.line([door(4, 9), door(33, 9), door(33, 54), door(4, 54), door(4, 9)], DETAIL)
    s.tube([door(30, 25), door(30, 25, 4), door(30, 38, 4), door(30, 38)], 1.25)
    harvest_crate(s, 15, 18, 4, scale=.63)
