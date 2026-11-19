from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface
from scenes.redraws._w5 import clipboard

DESCRIPTION = "An intake clipboard shows a knee-joint diagram above two form rows."


def draw(s):
    point = clipboard(s, 64, 85)
    page = Surface(s, point)
    page.frame(10, 34, 44, 37, 2)
    page.outline([(25, 67), (33, 67), (33, 61), (37, 55), (36, 51),
                  (32, 49), (28, 52), (24, 52), (22, 55), (25, 60)], EDGE)
    page.outline([(24, 47), (29, 48), (33, 46), (33, 43), (27, 38),
                  (20, 38), (22, 42), (21, 45)], EDGE)
    page.oval(39, 48, 2.8, 4.1, EDGE)
    page.line([(43, 48), (48, 48)], DETAIL)
    for v in (12, 22):
        page.frame(12, v, 5, 5, .8)
        page.rows(23, v + 2.5, (25,), ink=EDGE)
