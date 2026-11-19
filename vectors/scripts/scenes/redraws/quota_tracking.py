from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.systems_shapes import bezel

DESCRIPTION = "A standing quota gauge shows a partially filled bar and a tall capacity mark at its end."


def draw(s):
    s.solid(rounded(-44, -30, 88, 30, 3), 0, 39,
            top=rounded(-44, -15, 88, 15, 3))
    bezel(s, -36, 0, 7, 72, 25, DETAIL, 2)
    bezel(s, -30, 0, 15, 60, 10, EDGE, 1.3)
    for x in range(-26, 6, 5):
        s.line([(x, 0, 17), (x + 2, 0, 23)], EDGE)
    s.line([(7, 0, 15), (7, 0, 25)], EDGE)
    s.line([(30, 0, 10), (30, 0, 29)], BOLD)
    for x in (-30, -15, 0, 15):
        s.line([(x, 0, 11), (x, 0, 12.5)], DETAIL)
