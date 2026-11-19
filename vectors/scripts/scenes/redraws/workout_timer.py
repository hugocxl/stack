from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w4 import dumbbell_mark, front_surface, upright

DESCRIPTION = "A mechanical stopwatch shows a dumbbell on its dial beneath a sweeping timer hand."


def draw(s):
    angle = -30
    upright(s, rounded(-5, 66, 10, 12, 2), -2, 5, angle=angle)
    upright(s, rounded(-10, 76, 20, 7, 2), 1, 6, angle=angle)
    upright(s, [(19, 62), (24, 69), (30, 65), (25, 58)], 0, 6, angle=angle)
    upright(s, oval(0, 35, 32, 32)[:-1], 3, 10, angle=angle)
    dial = front_surface(s, angle=angle, y=3)
    dial.oval(0, 35, 26, 26)
    for x, z, dx, dz in ((0, 58, 0, -5), (-23, 35, 4, 0), (23, 35, -4, 0), (0, 13, 0, 4)):
        dial.line([(x, z), (x + dx, z + dz)], DETAIL)
    dial.line([(0, 36), (9, 51)], EDGE)
    dial.oval(0, 36, 1.6, 1.6, EDGE)
    dumbbell_mark(dial, 0, 25, 12, BOLD)
