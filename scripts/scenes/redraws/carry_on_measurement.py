from geometry import EDGE
from scenes.redraws._w5 import luggage

DESCRIPTION = "An upright carry-on fits inside an open airline sizing frame with ruler marks on its front post."


def draw(s):
    s.box(-8, -5, -4, 63, 35, 4, 2)
    for x, width in ((-8, 6), (51, 4)):
        s.box(x, -5, 0, width, 4, 74, .7)
    s.box(-8, -5, 70, 63, 4, 4, .7)
    luggage(s)
    # The open face exposes the case and lets it slide straight into the frame.
    for x, width in ((-8, 6), (51, 4)):
        s.box(x, 26, 0, width, 4, 74, .7)
        s.box(x, -1, 70, width, 27, 4, .7)
    for z in range(9, 69, 7):
        width = 4.7 if (z - 9) % 14 == 0 else 3
        s.line([(-7.2, 30, z), (-7.2 + width, 30, z)], EDGE)
