from geometry import DETAIL, EDGE, oval
from scenes.redraws._w3 import Surface

DESCRIPTION = "A festival entrance arch carries a swallowtail welcome banner above a string of pennants."


def draw(s):
    front = Surface(s, (0, 0, 0))
    inner = oval(47, 47, 34, 29, 0, 180, 28)
    outer = oval(47, 47, 47, 43, 180, 0, 32)
    outline = [(0, 0), *outer, (94, 0), (81, 0), *inner, (13, 0)]
    front.plate(outline, 16)
    for x in (0, 81):
        s.box(x - 3, -18, 0, 19, 21, 6, 1)
    front.stroke([(13, 49), (30, 40), (48, 36), (64, 40), (81, 49)], EDGE)
    for a, b, u, v in ((20, 45, 30, 40), (34, 39, 45, 37),
                       (50, 37, 61, 39), (65, 41, 75, 46)):
        front.stroke([(a, b), ((a + u) / 2, min(b, v) - 10), (u, v)], EDGE)

    banner = Surface(s, (0, 4, 0))
    banner.plate([(8, 65), (31, 67), (63, 67), (86, 65), (81, 74),
                  (86, 84), (63, 86), (31, 86), (8, 84), (13, 74)], 2)
    banner.stroke([(25, 67), (25, 85)], DETAIL)
    banner.stroke([(69, 67), (69, 85)], DETAIL)
    banner.rules(33, 77, [28], ink=EDGE)
