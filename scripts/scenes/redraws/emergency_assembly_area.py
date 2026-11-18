from geometry import EDGE
from scenes.redraws._kit import glyph

DESCRIPTION = "Four inward arrows on a freestanding emergency assembly sign point to a cluster of safety helmets."


def draw(s):
    s.tube([(0, -3, 0), (0, -3, 75)], 2.6)
    s.box(-34, -4, 26, 68, 5, 58, 3)
    for x, z, kind in ((-23, 55, "arrow"), (23, 55, "back"),
                       (0, 75, "down"), (0, 35, "up")):
        glyph(s, kind, x, 1, z, 9)
    for x, z in ((-8, 52), (8, 52), (0, 60)):
        s.line([(x - 5, 1, z), (x - 4, 1, z + 3), (x - 2, 1, z + 4.5),
                (x + 2, 1, z + 4.5), (x + 4, 1, z + 3), (x + 5, 1, z),
                (x - 5, 1, z)], EDGE)
