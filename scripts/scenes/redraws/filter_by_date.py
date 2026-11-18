from geometry import EDGE
from scenes.redraws._w4 import filter_key, nav_funnel

DESCRIPTION = "A calendar with two binding loops and a date grid clips to the upper rim of a filter funnel."


def calendar(face, u, v):
    face.frame(u - 9, v - 9, 18, 17, 2, EDGE)
    face.line([(u - 9, v + 2), (u + 9, v + 2)], EDGE)
    for x in (u - 5, u + 5):
        face.line([(x, v + 6), (x, v + 11)], EDGE)
    for y in (v - 5, v - 1):
        for x in (u - 5, u, u + 5):
            face.rows(x - 1, y, (2,), ink=EDGE)


def draw(s):
    nav_funnel(s)
    filter_key(s, calendar)
