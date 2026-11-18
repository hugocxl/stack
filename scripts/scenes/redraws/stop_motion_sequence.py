from geometry import EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "A continuous three-frame film strip shows a ball advancing at discrete positions."


def draw(s):
    strip = paper(s, 57, pitch=.93, run=.32, angle=-31, depth=5)
    strip.slab(rounded(0, 0, 152, 57, 3), 5)
    for x in range(6, 146, 12):
        for v in (4, 49):
            strip.frame(x, v, 5, 4, 1)
    for left, u, v in ((4, 16, 35), (54, 75, 23), (104, 137, 35)):
        strip.frame(left, 12, 44, 33, 2, EDGE)
        strip.oval(u, v, 7.5, 7.5, EDGE)
