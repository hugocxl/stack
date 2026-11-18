from math import pi, sin

from geometry import BOLD, DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A vented air-quality monitor on a pedestal shows a leaf beside its analog gauge."


def draw(s):
    s.disk(0, 0, 0, 22, 17, 5)
    s.tube([(0, 0, 5), (0, 0, 35)], 3.5)
    s.box(-33, -11, 29, 66, 23, 40, 4)
    y = 12
    bezel(s, -29, y, 34, 58, 30, DETAIL, 2)
    def leaf_edge(t, curve):
        bend = curve * sin(pi * t) ** .8
        return (-25 + 19 * t - .72 * bend, y, 41 + 18 * t + .72 * bend)

    leaf = [leaf_edge(i / 20, 6.5) for i in range(21)]
    leaf += [leaf_edge(i / 20, -6) for i in range(19, -1, -1)]
    s.line(leaf, EDGE)
    s.line([(-27, y, 38), (-20, y, 47), (-13, y, 53)], EDGE)
    s.line([(x, y, z) for x, z in oval(12, 45, 12.5, 12, 12, 168, 28)], EDGE)
    for x, z in ((4, 51), (9, 54), (15, 54), (20, 51)):
        s.line([(x, y, z), (x + (12 - x) * .23, y, z + (45 - z) * .23)], DETAIL)
    s.line([(12, y, 42), (18, y, 50)], BOLD)
    for z in (39, 46, 53, 60):
        s.line([(33, -5, z), (33, 6, z)], EDGE)
