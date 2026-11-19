from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w3 import browser_window

DESCRIPTION = "A browser window previews light and dark themes with a sun and crescent beneath a check badge."


def draw(s):
    face = browser_window(s, 73, 53)
    face.stroke([(36.5, 0), (36.5, 38)], DETAIL)
    face.oval(18.5, 20, 5, 5, EDGE)
    for a in range(0, 360, 45):
        u, v = cos(radians(a)), sin(radians(a))
        face.stroke([(18.5 + u*7.4, 20 + v*7.4), (18.5 + u*10.2, 20 + v*10.2)], EDGE)
    for stroke in _strokes("moon", 13.7):
        face.stroke([(54 + u, 20 + v) for u, v in stroke], EDGE)
    badge(s, "check", *face.point(70, 47), 12.6)
