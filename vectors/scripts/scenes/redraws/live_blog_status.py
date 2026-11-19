from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A blog page shows two timestamped posts and a live dot between broadcast arcs in its heading."


def draw(s):
    page = paper(s, 89, pitch=.59, angle=-18, depth=4)
    page.slab(rounded(0, 0, 89, 89, 3), 4)
    page.rows(10, 17, (33,), ink=BOLD)
    page.rows(10, 30, (69,), ink=EDGE)
    for v, widths in ((43, (41, 48, 32)), (67, (40, 48, 30))):
        page.oval(15, v, 5, 5, EDGE)
        page.line([(15, v - 2.8), (15, v), (17.3, v + 1.2)], EDGE)
        page.rows(25, v, widths, step=6)
    for radius in (12, 17):
        for start, end in ((-41, 41), (139, 221)):
            page.line(oval(66, 16, radius, radius, start, end, 20), EDGE)
    badge(s, "dot", *page.at(66, 16), 7.7)
