from geometry import EDGE
from scenes.redraws._w4 import filter_key, nav_funnel

DESCRIPTION = "A portrait-format identification credential with a lanyard slot clips to the rim of a filter funnel."


def credential(face, u, v):
    face.frame(u - 9, v - 12, 18, 24, 2.5, EDGE)
    face.frame(u - 4, v + 6, 8, 3, 1.5, EDGE)
    face.line([(u - 5, v + 1), (u + 5, v + 1)], EDGE)
    face.rows(u - 5, v - 3, (10, 7), step=-4)


def draw(s):
    nav_funnel(s)
    filter_key(s, credential)
