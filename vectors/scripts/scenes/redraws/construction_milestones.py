from geometry import DETAIL, EDGE
from scenes.redraws._sf import house

DESCRIPTION = "A dashed timeline runs from a poured slab through a timber frame to a finished house."


def draw(s):
    s.line([(-100, 30, 0), (100, 30, 0)], DETAIL, dashed=True)
    s.box(-100, -10, 0, 44, 34, 5, 1)
    s.box(-24, -10, 0, 44, 34, 5, 1)
    for x in (-22, -2, 18):
        for y in (-8, 22):
            s.tube([(x, y, 5), (x, y, 30)], 1.1, EDGE)
    for y in (-8, 22):
        s.tube([(-22, y, 30), (18, y, 30)], 1.1, EDGE)
        s.tube([(-22, y, 30), (-2, y, 48), (18, y, 30)], 1.1, EDGE) if False else None
    for x in (-22, 18):
        s.tube([(x, -8, 30), (x, 7, 46), (x, 22, 30)], 1.1, EDGE)
    s.tube([(-22, 7, 46), (18, 7, 46)], 1.1, EDGE)
    house(s, 52, -10, 0, 44, 34, 26, 18)
