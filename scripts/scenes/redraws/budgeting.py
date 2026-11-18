from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import panel, printed_stroke, ruled_amounts

DESCRIPTION = "An open budget ledger shows a large allocation pie chart beside three aligned expense rows."


def draw(s):
    left = lambda x, z: (x, -.34 * z + x * .28, z)
    right = lambda x, z: (x, -.34 * z - x * .16, z)
    panel(s, [(-42, 2), (0, 0), (0, 54), (-42, 58)], left, 5)
    panel(s, [(0, 0), (42, 3), (42, 58), (0, 54)], right, 5)
    printed_stroke(s, left, [(-36, 50), (-11, 47)], DETAIL)
    center = (-22, 26)
    main = oval(*center, 13, 13, 26, 301, 35)
    printed_stroke(s, left, [*main, center, main[0]], BOLD)
    offset_center = (-19.4, 24)
    wedge = oval(*offset_center, 13, 13, -59, 26, 12)
    printed_stroke(s, left, [*wedge, offset_center, wedge[0]], EDGE)
    ruled_amounts(s, right, ((39, 13), (30, 9), (21, 12)), 7, 35, width=7)
    printed_stroke(s, right, [(7, 14), (35, 14)], EDGE)
