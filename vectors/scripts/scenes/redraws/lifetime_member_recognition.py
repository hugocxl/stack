from math import pi, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import coin
from scenes.redraws._w3 import Surface

DESCRIPTION = "A ribbon medallion carries a large embossed infinity emblem."


def ribbon_medal(s):
    """A heavy hanging medallion with a folded neck ribbon."""
    ribbon = Surface(s, (0, -3, 0))
    ribbon.plate([(-28, 72), (-14, 78), (10, 38), (1, 30), (-10, 41)], 3)
    ribbon.plate([(12, 79), (28, 74), (12, 46), (3, 32), (-8, 36)], 3)
    ribbon.stroke([(18, 73), (2, 42)], DETAIL)
    ribbon.oval(0, 35, 7, 8, EDGE)
    coin(s, 0, 0, 0, 32, depth=5)
    s.line([(x, .01, z) for x, z in oval(0, 0, 26, 26)], DETAIL)
    return Surface(s, (0, .02, 0))


def draw(s):
    face = ribbon_medal(s)
    place = face.viewer_axes(0, 0)
    angles = [i * pi / 30 for i in range(61)]
    face.stroke([place(17 * sin(a), 8 * sin(2 * a)) for a in angles], BOLD)
