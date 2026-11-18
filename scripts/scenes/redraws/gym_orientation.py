from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import paper

DESCRIPTION = "A sloped gym directory shows a route from the entrance to a dumbbell-marked training room."


def draw(s):
    floor = paper(s, 78, pitch=.70, angle=-12, depth=9)
    floor.slab(rounded(0, 0, 111, 78, 3), 9)
    floor.line([(15, 59), (15, 10), (99, 10), (99, 66), (44, 66)], EDGE)
    floor.line([(15, 31), (37, 31), (37, 10)], DETAIL)
    floor.line([(99, 41), (65, 41), (65, 29)], EDGE)
    floor.line([(65, 19), (65, 10)], EDGE)
    floor.line([(40, 66), (40, 44), (54, 44)], DETAIL)
    floor.line([(23, 65), (33, 65)], EDGE)

    route = [(27, 59), (27, 39), (52, 39), (52, 24), (76, 24)]
    floor.line(route[:-1], EDGE, dashed=True)
    arrow(s, [floor.at(*p) for p in route[-2:]], EDGE, head=5)
    floor.line([(82, 24), (91, 24)], BOLD)
    for u in (79, 91):
        floor.frame(u, 16, 4, 16, 1.5, EDGE)
