from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A closed archive box has a label holder on its front and a check badge above the right end of the lid."


def draw(s):
    s.box(0, 0, 0, 67, 43, 30, 3)
    s.box(-2, -2, 27, 71, 47, 8, 3)

    bezel(s, 21, 43, 9, 25, 11, EDGE, 2)
    s.line([(26, 43, 14.5), (41, 43, 14.5)], DETAIL)
    # The carrying slot is set into the end wall.
    handle = [(67, y, z) for y, z in ((15, 16), (26, 16), (28, 18),
                                    (27, 21), (14, 21), (13, 18))]
    s.line(handle + handle[:1], EDGE)

    badge(s, "check", 69, 38, 53, 13)
