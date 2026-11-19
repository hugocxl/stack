from geometry import EDGE, oval
from scenes.redraws._w4 import filter_key, nav_funnel

DESCRIPTION = "A map-pin pictogram clips to the upper rim of a filter funnel."


def pin(face, u, v):
    face.outline([(u, v - 11), *oval(u, v + 3, 8, 8, -36, 216, count=32)], EDGE)
    face.oval(u, v + 3, 3, 3, EDGE)


def draw(s):
    nav_funnel(s)
    filter_key(s, pin)
