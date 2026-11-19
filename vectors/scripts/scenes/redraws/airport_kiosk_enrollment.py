from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import plane_mark, rect

DESCRIPTION = "A standing airport kiosk has a passport scanner shelf, an airplane on its touchscreen and a plus badge."


def draw(s):
    s.box(0, 0, 0, 44, 33, 5, 3)
    s.box(3, 1, 4, 38, 23, 64, 3)
    s.box(1, 2, 46, 42, 25, 29, 4)
    screen = lambda x, z: (x, 27, z)
    rect(s, screen, 6, 50, 32, 20, 2)
    plane_mark(s, screen, 22, 60, .52)

    s.box(3, 24, 33, 38, 13, 5, 2)
    s.face([(12, 27, 38), (31, 27, 38), (31, 36, 38), (12, 36, 38)], EDGE)
    s.line([(16, 30, 38), (27, 30, 38)], EDGE)
    rect(s, lambda x, z: (x, 24, z), 11, 12, 22, 12, 1.8)
    badge(s, "plus", 44, 23, 75, 10.5)
