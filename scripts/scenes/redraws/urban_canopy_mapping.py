from geometry import DETAIL
from scenes.redraws._w1 import tree_crown
from scenes.systems_shapes import bezel

DESCRIPTION = "Three tree crowns mark a planted corridor on a standing street map sign."


def draw(s):
    for x in (-28, 28):
        s.box(x - 3, -5, 0, 6, 9, 34, 1)
    s.box(-45, -6, 21, 90, 12, 59, 3)
    bezel(s, -41, 6, 25, 82, 51, DETAIL)
    for z in (36, 62):
        s.line([(-38, 6, z), (38, 6, z)], DETAIL)
    for x in (-25, 20):
        s.line([(x, 6, 28), (x, 6, 72)], DETAIL)
    s.line([(-38, 6, 49), (20, 6, 49)], DETAIL)
    s.line([(32, 6, 36), (32, 6, 61)], DETAIL)
    for x, z, size in ((-23, 50, 9), (0, 53, 12), (24, 48, 10)):
        tree_crown(s, x, 6, z, size, outline=True)
