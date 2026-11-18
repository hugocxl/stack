from geometry import EDGE, oval
from scenes.redraws._w1 import solar_cells, turbine

DESCRIPTION = "A wind turbine and a solar panel stand in the two sectors of a divided energy mix chart."


def slab(s, x, y, start, end, visible_start, visible_end, *, cut_start=False):
    center = (x, y)
    outline = [center, *oval(x, y, 42, 32, start, end, 48)]
    side = oval(x, y, 42, 32, visible_start, visible_end, 30)
    if cut_start:
        s.face([(*center, 0), (*outline[1], 0), (*outline[1], 7), (*center, 7)], EDGE)
    s.face([(*p, 0) for p in side] + [(*p, 7) for p in reversed(side)], EDGE)
    s.face([(*p, 7) for p in outline], EDGE)


def draw(s):
    slab(s, -2, -4, 194, 415, 323, 415)
    slab(s, 2, 5, 55, 194, 55, 142, cut_start=True)
    turbine(s, 12, -13, 7, 26)
    for x in (-17, -1):
        s.tube([(x, 16, 8), (x, 16, 16), (x, 24, 8)], 1.2)
    solar_cells(s, lambda u, v: (-22 + 27 * u, 12 + 16 * v, 22 - 13 * v), columns=3)
