from geometry import EDGE, rounded
from scenes.redraws._w4 import front_surface
from scenes.redraws.collapse_results import disclosure

DESCRIPTION = "A downward disclosure chevron opens a raised section header above two indented child rows."


def draw(s):
    nav = front_surface(s, angle=-29, z=9)
    nav.slab(rounded(9, 0, 65, 58, 5), 6)
    nav.line([(23, 46), (23, 12), (31, 12)], EDGE)
    nav.line([(23, 28), (31, 28)], EDGE)
    nav.rows(36, 28, (25,), ink=EDGE)
    nav.rows(36, 12, (18,), ink=EDGE)
    header = front_surface(s, angle=-29, y=3, z=9)
    header.slab(rounded(0, 42, 83, 24, 5), 8)
    disclosure(header, 15, 54, up=False)
    header.rows(29, 54, (36,), ink=EDGE)
