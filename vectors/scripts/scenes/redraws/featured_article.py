from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "An article cover with a masthead, feature image, and two columns carries a star badge at its upper corner."


def draw(s):
    cover = paper(s, 100, pitch=.78, run=.51, angle=-15, depth=7)
    cover.slab(rounded(0, 0, 77, 100, 3), 7)
    cover.rows(10, 15, (42,), ink=BOLD)
    cover.rows(10, 23, (30,), ink=EDGE)
    landscape(cover, 10, 32, 57, 32)
    cover.rows(10, 74, (24, 20, 23, 18), step=6)
    cover.rows(41, 74, (25, 21, 25, 15), step=6)
    badge(s, "star", *cover.at(76, 14), 17)
