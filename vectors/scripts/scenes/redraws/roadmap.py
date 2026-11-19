from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A winding timeline passes through three round milestones and ends at a planted destination flag."


def draw(s):
    s.line([(8, 68, 0), (46, 68, 0), (53, 66, 0), (58, 61, 0),
            (60, 54, 0), (60, 28, 0), (62, 21, 0), (68, 16, 0),
            (76, 14, 0), (91, 14, 0)], EDGE)
    for x, y in ((8, 68), (38, 68), (60, 36)):
        s.disk(x, y, 0, 7.5, 7.5, 3.6, EDGE)
    s.box(86, 9, 0, 10, 10, 3, 1.5, DETAIL)
    s.tube([(91, 14, 3), (91, 14, 74)], 1.5, EDGE)
    s.face([(91, 14, 73), (121, 14, 73), (113, 14, 61),
            (121, 14, 49), (91, 14, 49)], BOLD)
