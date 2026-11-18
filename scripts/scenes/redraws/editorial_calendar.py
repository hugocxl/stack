from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "A standing desk calendar marks a scheduled date with a miniature article page."


def desk_calendar(s):
    """Build the tent stand and its grid, and return a surface for scheduled items."""
    width, height = 106, 82
    page = paper(s, height, pitch=.88, run=.48, angle=-17, depth=4)
    rear = Surface(s, lambda u, v: tuple(a + b*v/height for a, b in
                   zip(page.at(u, 0), (-9, -34, -page.at(u, 0)[2]))))
    rear.slab(rounded(0, 0, width, height, 1), 2)
    page.slab(rounded(0, 0, width, height, 3), 4)
    for x in (20, 86):
        a, b, z = page.at(x, 0)
        s.tube([(a, b - 3, z - 2), (a, b - 4, z + 4), (a, b, z + 6),
                (a, b + 3, z + 4), page.at(x, 6)], 1.5, EDGE)

    page.frame(7, 17, 92, 57, 1, EDGE)
    for u in (30, 53, 76):
        page.line([(u, 17), (u, 74)], DETAIL)
    for v in (36, 55):
        page.line([(7, v), (99, v)], DETAIL)
    return page


def draw(s):
    page = desk_calendar(s)
    for u, v in ((12, 22), (35, 22), (58, 22), (81, 22), (12, 41),
                 (35, 41), (81, 41), (12, 60), (35, 60), (58, 60), (81, 60)):
        page.rows(u, v, (4,), ink=DETAIL)

    page.frame(56, 38, 17, 15, 1, BOLD)
    page.rows(59, 42, (10,), ink=EDGE)
    page.frame(59, 45, 4.2, 5, .6, EDGE)
    page.rows(66, 46, (4, 4), step=3, ink=EDGE)
