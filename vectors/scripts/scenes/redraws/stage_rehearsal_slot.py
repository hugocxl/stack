from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A curtained theater stage carries a clock badge on its proscenium."


def draw(s):
    s.box(0, 0, 0, 91, 54, 8, 3)
    portal = Surface(s, (0, 33, 8))
    curtain = Surface(s, (0, 30, 8))
    s.face([curtain.point(x, v) for x, v in [(9, 46), (82, 46), (82, 38),
            (69, 35), (46, 33), (22, 35), (9, 38)]])
    for hinge, sign in ((10, 1), (81, -1)):
        outline = [(0, 44), (23, 44), (21, 34), (16, 27), (10, 22),
                   (12, 12), (18, 0), (0, 0)]
        s.face([curtain.point(hinge + sign * x, v) for x, v in outline])
        curtain.stroke([(hinge + sign * x, v) for x, v in ((8, 43), (8, 33),
                        (6, 22), (8, 8), (10, 2))])
        curtain.stroke([(hinge + sign, 21), (hinge + sign * 10, 22)], EDGE)
    portal.plate([(0, 0), (10, 0), (10, 44), (81, 44), (81, 0), (91, 0),
                  (91, 59), (0, 59)], 14)
    portal.stroke([(11, 51), (80, 51)])
    badge(s, "clock", 90, 34, 65, 15)
