from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "A blister pack of six capsules carries a pause badge."


def draw(s):
    foil = paper(s, 93, pitch=.76, run=.64, angle=-23, depth=4)
    foil.slab(rounded(0, 0, 60, 93, 8), 4)
    raised = Surface(s, lambda u, v: (*foil.at(u, v)[:2], foil.at(u, v)[2] + 4))
    for v in (10, 37, 64):
        for u in (11, 36):
            raised.slab(rounded(u, v, 13, 19, 6), 4)
            raised.line([(u + 1, v + 9.5), (u + 12, v + 9.5)], DETAIL)
    badge(s, "pause", *foil.at(65, 27), 15)
