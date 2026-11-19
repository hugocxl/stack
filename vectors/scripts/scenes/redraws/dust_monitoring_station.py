from geometry import BOLD, DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A pole-mounted dust monitor has a hooded intake and a particulate level display."


def draw(s):
    s.disk(0, 0, 0, 16, 16, 4)
    s.tube([(0, 0, 4), (0, 0, 51)], 3)
    s.box(-20, -12, 31, 40, 24, 42, 4)
    s.tube([(0, -2, 71), (0, -2, 83)], 2.2)
    s.solid(oval(0, -2, 10, 10)[:-1], 81, 8,
            top=oval(0, -2, 6.5, 6.5)[:-1], crease=False)
    s.disk(0, -2, 88, 7, 7, 3)
    bezel(s, -14, 12, 44, 28, 14, EDGE, 1.5)
    for x, radius, z in ((-8, 1.5, 49), (-4, 2.05, 52), (-8, 1.25, 54)):
        s.line([(a, 12, b) for a, b in oval(x, z, radius, radius, count=20)], BOLD)
    for x, height in ((1, 3), (5, 5.5), (9, 8)):
        s.line([(x, 12, 47), (x, 12, 47 + height)], EDGE)
    for z in (36, 40):
        s.line([(-9, 12, z), (9, 12, z)], DETAIL)
