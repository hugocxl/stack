from geometry import DETAIL, EDGE

DESCRIPTION = "A cutaway excavation exposes continuous footing trenches around a rectangular foundation footprint."


def draw(s):
    s.face([(10, 10, 4), (96, 10, 4), (96, 69, 4), (10, 69, 4)], DETAIL)
    s.face([(10, 10, 4), (96, 10, 4), (96, 10, 20), (10, 10, 20)], EDGE)
    s.face([(10, 10, 4), (10, 69, 4), (10, 69, 20), (10, 10, 20)], EDGE)
    s.box(26, 25, 4, 19, 29, 16, 1)
    s.box(57, 25, 4, 23, 29, 16, 1)
    outer = [(0, 0, 20), (106, 0, 20), (106, 79, 20), (0, 79, 20)]
    cut = [(10, 10, 20), (96, 10, 20), (96, 69, 20), (10, 69, 20)]
    s.face(outer, EDGE, openings=(cut,))
    s.face([(0, 79, 0), (106, 79, 0), (106, 79, 20), (0, 79, 20)])
    s.face([(106, 0, 0), (106, 79, 0), (106, 79, 20), (106, 0, 20)])
    s.line([(7, 79, 8), (25, 79, 10), (49, 79, 6), (77, 79, 9), (97, 79, 8)], DETAIL)
    s.line([(106, 9, 9), (106, 30, 7), (106, 56, 10), (106, 70, 8)], DETAIL)
