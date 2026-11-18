from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line

DESCRIPTION = "A continuous insulation layer crosses the face of a stud in a cutaway wall."


def draw(s):
    s.box(0, -14, 0, 78, 12, 57, 1)
    for x in (2, 36, 70):
        s.box(x, -2, 4, 7, 12, 48, .75)
    for z in (0, 52):
        s.box(0, -2, z, 78, 12, 5, .75)

    def face(x, z):
        return x, 10.1, z

    for x in (11, 45):
        for z in (29, 43):
            chart_line(s, face, [(x, z - 2), (x + 5, z + 2), (x + 10, z + 2),
                                 (x + 16, z - 2), (x + 23, z + 1)], DETAIL)

    s.box(-1, 10, 2, 80, 10, 20, 1, EDGE)

    def insulation(x, z):
        return x, 20.1, z

    chart_line(s, insulation, [(x, 12 + offset) for x, offset in
                               ((4, 0), (12, 4), (21, 4), (30, -4), (39, -4),
                                (48, 4), (57, 4), (66, -4), (73, 0))], EDGE)
    s.line([(79.05, 19, 12), (79.05, 16, 15), (79.05, 13, 9), (79.05, 10, 12)], DETAIL)
