from geometry import EDGE
from scenes.redraws._w4 import filter_key, nav_funnel

DESCRIPTION = "A folded-corner file pictogram clips to the upper rim of a filter funnel."


def file_mark(face, u, v):
    face.outline([(u - 8, v - 10), (u + 8, v - 10), (u + 8, v + 3),
                  (u + 2, v + 10), (u - 8, v + 10)], EDGE)
    face.line([(u + 2, v + 10), (u + 2, v + 3), (u + 8, v + 3)], EDGE)
    face.rows(u - 4, v, (7, 8), step=-5)


def draw(s):
    nav_funnel(s)
    filter_key(s, file_mark)
