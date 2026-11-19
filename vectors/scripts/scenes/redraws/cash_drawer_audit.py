from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import coin_stack, rect

DESCRIPTION = "A magnifying glass frames the coins and notes in the open drawer of a cash register."


def draw(s):
    s.box(0, 0, 0, 68, 37, 29, 4)
    for x in (14, 26, 38, 50):
        rect(s, lambda u, v: (u, v, 29), x, 15, 7, 5, 1.2, DETAIL)
    s.box(4, 34, 3, 60, 32, 5, 2)
    s.box(5, 37, 7, 3, 26, 7, 1)
    coin_stack(s, 20, 51, 8, 7, 3)
    for x in (35, 50):
        s.box(x, 39, 8, 11, 23, 2, 1.4)
        s.ellipse(x + 5.5, 50, 10, 2.3, 4.2, DETAIL)
    s.box(31, 37, 8, 2, 27, 6, .7)
    s.box(47, 37, 8, 1.8, 27, 6, .7)
    s.box(61, 37, 7, 3, 28, 8, 1)
    s.box(4, 64, 3, 60, 5, 12, 2)
    rect(s, lambda x, z: (x, 69, z), 24, 7, 20, 4, 1.2, DETAIL)

    lens = lambda x, y: (x, y, 22 - .30 * (y - 50))
    outer = oval(34, 53, 21, 18, count=54)
    inner = oval(34, 53, 17.4, 14.4, count=54)
    s.tube([lens(50, 62), (66, 69, 16), (75, 73, 14)], 3.2)
    s.face([lens(x, y) for x, y in outer], EDGE,
           openings=[[lens(x, y) for x, y in inner]])
