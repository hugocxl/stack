from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A thick upward arrow points to a short top boundary bar."


def draw(s):
    symbol = front_surface(s, angle=-20, z=9)
    symbol.slab(rounded(0, 74, 70, 9, 3), 6, EDGE)
    symbol.slab([(27, 0), (43, 0), (43, 36), (60, 36),
                 (35, 62), (10, 36), (27, 36)], 6, BOLD)
