from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "A battery has a segmented capacity gauge printed across its broad side."


def draw(s):
    s.box(-40, -19, 0, 76, 23, 43, 4)
    s.box(34, -13, 13, 10, 12, 18, 2)
    for index in range(5):
        x = -32 + index * 12
        bezel(s, x, 4, 10, 9, 23, EDGE if index < 3 else DETAIL, 1.4)
        if index < 3:
            s.line([(x + 4.5, 4, 14), (x + 4.5, 4, 29)], BOLD)
