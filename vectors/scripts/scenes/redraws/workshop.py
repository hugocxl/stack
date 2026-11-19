from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A screwdriver turns a screw in a piece of wood clamped to a four-legged workbench."


def draw(s):
    for x, y in ((9, 7), (87, 7), (9, 53), (87, 53)):
        s.box(x, y, 0, 8, 8, 43, 1)
    s.box(7, 6, 12, 88, 8, 7, 1)
    s.box(0, 0, 42, 105, 69, 8, 2)
    s.box(9, 9, 50, 70, 27, 8, 2)
    s.box(49, 34, 50, 21, 17, 11, 2)
    s.box(50, 57, 44, 19, 12, 15, 2)
    s.tube([(60, 66, 51), (60, 80, 51)], 2.1)
    s.tube([(52, 80, 49), (68, 80, 54)], 1.6)
    s.disk(36, 22, 58, 6, 6, 3)
    s.tube([(36, 22, 60), (36, 22, 84)], 1.9)
    s.disk(36, 22, 82, 5, 5, 6)
    s.box(29, 15, 87, 14, 14, 34, 6)
    handle = Surface(s, (0, 29, 0))
    handle.stroke([(35, 96), (35, 114)], EDGE)
