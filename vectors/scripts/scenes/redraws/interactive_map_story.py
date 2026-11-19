from geometry import EDGE, GUIDE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import Surface

DESCRIPTION = "A single route runs through three successive waypoints across an accordion-folded map."


def draw(s):
    def at(u, v):
        ridge = (0, 14, 3, 15)
        panel = min(int(u // 37), 2)
        height = ridge[panel] + (ridge[panel + 1] - ridge[panel]) * (u / 37 - panel)
        return u, v * .88, height + (67 - v)*.22

    page = Surface(s, at)
    for left in (0, 37, 74):
        right = left + 37
        page.slab([(left, 0), (right, 0), (right, 67), (left, 67)], 2)
    page.line([(7, 15), (17, 13), (25, 19), (36, 17)], GUIDE)
    page.line([(41, 54), (49, 48), (59, 51), (68, 58)], GUIDE)
    page.line([(80, 13), (89, 19), (96, 17), (105, 20)], GUIDE)
    page.line([(8, 45), (19, 35), (29, 41), (34, 33), (37, 29), (47, 18), (60, 20),
               (68, 28), (74, 36), (83, 47), (96, 39)], EDGE)
    for u, v in ((19, 35), (47, 18), (83, 47)):
        ring = oval(u, v, 5.4, 5.4)
        s.face([at(x, y) for x, y in ring], EDGE)
    arrow(s, [at(95, 40), at(105, 33)], EDGE, head=4)
