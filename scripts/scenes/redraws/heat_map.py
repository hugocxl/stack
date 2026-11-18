from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import board

DESCRIPTION = "A flat grid uses denser hatching in neighboring cells around one central hotspot."


def draw(s):
    p = board(s, 114, 100, run=.55, rise=.63, depth=7)
    cell = 17
    pattern = (
        (0, 0, 1, 1, 0, 0),
        (0, 1, 2, 3, 1, 0),
        (0, 1, 3, 5, 2, 1),
        (0, 1, 2, 3, 1, 0),
        (0, 0, 1, 1, 0, 0),
    )
    for i in range(7):
        x = 6 + i*cell
        s.line([p(x, 8), p(x, 93)], EDGE if i in (0, 6) else DETAIL)
    for j in range(6):
        z = 8 + j*cell
        s.line([p(6, z), p(108, z)], EDGE if j in (0, 5) else DETAIL)
    for j, row in enumerate(pattern):
        for i, density in enumerate(row):
            for k in range(density):
                offset = (k - (density - 1)/2)*2.3
                long = 4.8 - abs(offset)*.32
                x, z = 14.5 + i*cell, 16.5 + j*cell
                s.line([p(x - long + offset, z - long - offset),
                        p(x + long + offset, z + long - offset)],
                       BOLD if density == 5 else EDGE)
