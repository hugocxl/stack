from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, filmstrip

DESCRIPTION = "A single chapter flag marks the boundary between two segments of a video timeline."


def draw(s):
    p = filmstrip(s)
    for x, z in ((30, 35), (83, 35)):
        closed_outline(s, p, [(x - 5, z - 7), (x - 5, z + 7), (x + 7, z)], DETAIL)
    chart_line(s, p, [(58, 13), (58, 92)], EDGE)
    s.face([p(x, z) for x, z in [(58, 93), (88, 93), (81, 85), (88, 77), (58, 77)]], BOLD)
    closed_outline(s, p, rounded(52, 8, 12, 5, 1), EDGE)
