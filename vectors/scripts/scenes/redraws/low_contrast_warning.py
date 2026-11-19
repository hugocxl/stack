from geometry import BOLD, GUIDE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w3 import Surface

DESCRIPTION = "A warning triangle marks a contrast sample with a pale ring beside a darker matching ring."


def draw(s):
    face = Surface(s, (0, 0, 0), across=(.96, -.28))
    face.plate(rounded(0, 0, 91, 57, 4), 8)
    face.stroke([(45.5, 9), (45.5, 48)])
    face.oval(24, 29, 13, 13, BOLD)
    face.oval(66, 29, 13, 13, GUIDE)
    warning(s, *face.point(97, 44, -9), size=32)
