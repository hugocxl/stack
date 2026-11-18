from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import photo_print

DESCRIPTION = "A landscape print with mountains and a sun carries a check badge on its border."


def draw(s):
    face = photo_print(s, width=70, height=51)
    s.line([face(x, z) for x, z in ((5, 15), (21, 32), (35, 17), (47, 28), (65, 14))], EDGE)
    s.line([face(x, z) for x, z in oval(51, 36, 4.4, 4.4, count=32)], EDGE)
    badge(s, "check", *face(68, 9), 12.2)
