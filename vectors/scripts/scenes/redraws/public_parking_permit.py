from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.systems_shapes import bezel

DESCRIPTION = "A windshield parking permit hangs by its hook and carries a large parking P."


def draw(s):
    outline = rounded(-19, 0, 38, 59, 4)
    opening = oval(0, 50, 5, 5, count=36)[:-1]
    s.tube([(0, -4, 49), (0, -4, 66), (0, 4, 72), (0, 12, 67)], 2.1)
    for y in (-2.7, 1.5):
        s.face([(x, y, z) for x, z in outline], EDGE,
               openings=[[(x, y, z) for x, z in opening]])
    bezel(s, -14, 1.5, 7, 28, 32, EDGE, 3.2)
    s.line([(-5, 1.5, 13), (-5, 1.5, 33), (2, 1.5, 33),
            (6, 1.5, 31), (7, 1.5, 27), (5, 1.5, 24), (-5, 1.5, 24)], BOLD)
    s.line([(-8, 1.5, 4), (8, 1.5, 4)], DETAIL)
