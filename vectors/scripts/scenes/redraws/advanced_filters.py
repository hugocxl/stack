from geometry import BOLD
from scenes.redraws._w4 import Surface, nav_funnel

DESCRIPTION = "Three slider tracks with offset handles sit inside the mouth of a filter funnel."


def draw(s):
    nav_funnel(s)
    face = Surface(s, lambda u, v: ((u + v)*.7071, (v - u)*.7071, 56))
    for v, knob in ((-14, 7), (-1, -8), (12, 1)):
        face.line([(-18, v), (knob - 3.5, v)], BOLD)
        face.line([(knob + 3.5, v), (18, v)], BOLD)
        face.frame(knob - 3.5, v - 3.5, 7, 7, 1.5, BOLD)
