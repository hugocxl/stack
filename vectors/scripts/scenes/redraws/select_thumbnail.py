from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A landscape thumbnail with film perforations carries a check badge at its lower-right corner."


def draw(s):
    thumb = paper(s, 68, pitch=.75, run=.50, angle=2, depth=7)
    thumb.slab(rounded(0, 0, 106, 68, 5), 7)
    landscape(thumb, 9, 8, 88, 42)
    thumb.line([(1, 54), (105, 54)], EDGE)
    for u in range(10, 95, 12):
        thumb.frame(u, 59, 6, 4, 1, EDGE)
    badge(s, "check", *thumb.at(105, 58), 17)
