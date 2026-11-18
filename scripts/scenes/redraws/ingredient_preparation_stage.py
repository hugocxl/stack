from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import smooth_loop

DESCRIPTION = "A chef’s knife rests on a thick chopping board alongside neatly sliced produce."


def draw(s):
    board = rounded(0, 0, 79, 49, 5)
    s.solid(board, 0, 7)
    s.line([(x, y, 7) for x, y in oval(68, 39, 5.5, 3.5)], EDGE)
    blade = [(9, 13), (14, 10), (45, 10), (45, 23),
             (29, 23), (18, 20), (12, 17)]
    s.face([(x, y, 8) for x, y in blade])
    s.line([(13, 15, 8), (26, 19.5, 8), (44, 19.5, 8)], DETAIL)
    s.box(44, 10, 7, 26, 8, 3.5, 2.3)
    for x in (52, 63):
        s.ellipse(x, 14, 10.5, 1, 1, DETAIL)
    # The carrot end and three slices share a center line.
    for x, y, rx in ((48, 33, 4), (39, 33, 3.7), (30, 33, 3.4)):
        s.disk(x, y, 7, rx, 5.3, 2.3)
        s.ellipse(x, y, 9.3, rx*.37, 2, DETAIL)
    tip = smooth_loop([(9, 32), (14, 29), (21, 28), (26, 29),
                       (26, 37), (20, 38), (13, 36)])
    s.face([(x, y, 7.8) for x, y in tip])
