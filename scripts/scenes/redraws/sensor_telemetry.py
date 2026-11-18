from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A sensor module with a raised sensing window carries a wireless signal badge at its edge."


def draw(s):
    s.box(-34, -24, 0, 68, 48, 17, 8)
    s.solid(rounded(-25, -15, 45, 30, 7), 17, 8,
            top=rounded(-20, -11, 35, 22, 7), crease=False)
    for x in (-12, -5, 2, 9):
        s.line([(x, -8, 25), (x, 8, 25), (x, 11, 25),
                (x, 14, 19)], DETAIL)
    s.line([(25, 0, 17), (25, 4, 17)], BOLD)
    bezel(s, -22, 24, 5, 20, 6, DETAIL, 1.5)
    badge(s, "wifi", 30, -18, 31, 13)
