from geometry import DETAIL, EDGE
from scenes.redraws._w1 import hard_drive, upright_profile
from scenes.systems_shapes import bezel

DESCRIPTION = "Three staggered snapshot tabs stand in a slot on a backup drive."


def draw(s):
    hard_drive(s)
    for offset, y, z in ((0, -18, 21), (7, -12, 18), (14, -6, 15)):
        x = -16 + offset
        outline = [(x, z), (x, z + 23), (x + 5, z + 28), (x + 14, z + 28),
                   (x + 19, z + 23), (x + 37, z + 23), (x + 37, z)]
        upright_profile(s, outline, y, 3)
    s.box(-6, -8, 15, 43, 10, 4, 1)
    bezel(s, 4, -6, 23, 24, 10, DETAIL, 1.5)
    s.line([(7, -6, 27), (12, -6, 27), (15, -6, 30), (20, -6, 26), (25, -6, 26)], EDGE)
