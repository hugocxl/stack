from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A tab-cycle arrow loops around two controls entirely inside an open modal dialog."


def draw(s):
    s.box(25, -24, 0, 52, 30, 5, 4)
    s.box(43, -13, 5, 16, 11, 14, 3)
    monitor = Surface(s, (0, 0, 18))
    monitor.plate(rounded(0, 0, 102, 72, 5), 8)
    monitor.rect(5, 8, 92, 59, 3)
    monitor.rules(10, 61, [26], ink=DETAIL)
    modal = Surface(s, (0, 1, 18))
    modal.plate(rounded(13, 14, 76, 44, 3), 2)
    modal.rules(22, 50, [23], ink=EDGE)
    modal.rect(29, 28, 19, 8, 2, EDGE)
    modal.rules(34, 32, [9])
    modal.rect(55, 28, 19, 8, 2, EDGE)
    modal.rules(60, 32, [9])
    route = [(45, 23), (27, 23), (22, 27), (22, 37), (27, 42), (74, 42),
             (80, 38), (80, 27), (75, 23), (54, 23)]
    arrow(s, [modal.point(x, v) for x, v in route], BOLD, head=4)
