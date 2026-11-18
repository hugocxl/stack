from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, paper, stethoscope_mark

DESCRIPTION = "A standing therapy progress record shows a stethoscope above a rising path ending in a check badge."


def draw(s):
    page = paper(s, 76, angle=-22, pitch=.87, run=.49, depth=5)
    rear = Surface(s, lambda u, v: (page.at(u, 0)[0], page.at(u, 0)[1] - .46*v,
                                   page.at(u, 0)[2]*(1 - v/76)))
    rear.slab(rounded(0, 0, 99, 76, 2), 3)
    page.slab(rounded(0, 0, 99, 76, 4), 5)
    stethoscope_mark(Surface(s, lambda u, v: page.at(u, -v)), 22, -15, .73)
    page.rows(42, 13, (38, 27), step=6)
    page.line([(10, 29), (90, 29)], DETAIL)
    page.line([(13, 37), (13, 66), (90, 66)], DETAIL)
    page.line([(21, 59), (41, 51), (59, 54), (78, 46)], EDGE)
    for u, v in ((21, 59), (41, 51), (59, 54)):
        page.oval(u, v, 2.6, 2.6, EDGE)
    badge(s, "check", *page.at(82, 44), 11.5)
