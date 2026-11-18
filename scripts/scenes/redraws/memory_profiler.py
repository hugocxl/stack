from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "A memory profiler panel shows a stepped allocation trace beneath a fixed capacity line."


def draw(s):
    s.box(-13, -16, 0, 26, 24, 4, 3)
    s.box(-5, -11, 4, 10, 9, 13, 1.5)
    s.box(-39, -10, 12, 78, 10, 58, 4)
    bezel(s, -33, 0, 17, 66, 48, EDGE, 2)

    for z in (22, 31, 40, 49):
        s.line([(-26, 0, z), (-22, 0, z)], EDGE)
    s.line([(-22, 0, 49), (-22, 0, 22), (27, 0, 22)], DETAIL)
    s.line([(-22, 0, 49), (27, 0, 49)], EDGE, dashed=True)
    steps = [(-21, 27), (-13, 27), (-13, 32), (-6, 32), (-6, 41),
             (5, 41), (5, 34), (13, 34), (13, 44), (27, 44)]
    s.line([(x, 0, z) for x, z in steps], BOLD)

    bezel(s, -27, 0, 55, 30, 8, EDGE, 1)
    for x in (-23, -17, -11, -5):
        s.line([(x, 0, 53), (x, 0, 55)], EDGE)
    for x in (-23, -11):
        bezel(s, x, 0, 57, 7, 4, DETAIL, .8)
