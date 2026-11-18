from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import rect, smooth_loop

DESCRIPTION = "An open food-scraps bin sits on a weighing base with an analog readout."


def draw(s):
    s.box(0, 0, 0, 58, 54, 6, 3)
    s.solid(rounded(0, 0, 58, 54, 3), 6, 8,
            top=rounded(1, 1, 56, 51, 3), crease=False)
    rim = rounded(3, 1, 51, 34, 6)
    hole = rounded(6, 4, 45, 28, 4)
    s.solid(rounded(7, 5, 43, 24, 5), 14, 30, top=rim, crease=False)
    s.face([(x, y, 44) for x, y in rim],
           openings=[[(x, y, 44) for x, y in hole]])
    # An apple core and a curled peel stick out of the open top.
    core = smooth_loop([(11, 42), (17, 46), (15, 50), (11, 54),
                        (15, 56), (26, 56), (31, 54), (27, 51),
                        (25, 46), (30, 43), (26, 41), (15, 40)])
    s.face([(x, 13, z) for x, z in core])
    s.tube([(21, 13, 56), (21, 13, 59), (24, 13, 61)], .75)
    peel = smooth_loop([(33, 44), (39, 44), (46, 51), (47, 47),
                        (44, 42), (39, 40), (35, 41)])
    s.face([(x, 16, z) for x, z in peel])
    s.line([(36, 16, 42), (40, 16, 42), (44, 16, 46)], DETAIL)
    dial = lambda x, y: (x, y, 14)
    rect(s, dial, 14, 36, 33, 14, 3)
    s.line([dial(x, y) for x, y in oval(30.5, 46, 11, 7, 190, 350, 24)], EDGE)
    for x, y in ((22, 43), (26, 41), (31, 40), (36, 41), (40, 43)):
        s.line([dial(x, y), dial(x + (30.5-x)*.13, y+1.4)], DETAIL)
    s.line([dial(31, 46), dial(36, 42)], BOLD)
