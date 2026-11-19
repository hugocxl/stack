from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import open_guide, rect

DESCRIPTION = "An open neighborhood guide shows a street map on one page and three short place entries on the facing page."


def draw(s):
    left, right = open_guide(s)
    for point, a, b in ((left, 0, 40), (right, 40, 80)):
        s.line([point(a + 2, 2), point(b - 2, 2)], DETAIL)
    for street in ([(5, 15), (16, 15), (34, 19)], [(5, 31), (18, 30), (35, 35)],
                   [(12, 7), (12, 19), (17, 31), (17, 41)],
                   [(26, 7), (27, 18), (25, 30), (26, 42)]):
        s.line([left(x, z) for x, z in street], EDGE)
    s.line([left(x, z) for x, z in oval(23, 24, 3.4, 3.4, count=24)], BOLD)
    s.line([right(46, 40), right(71, 40)], BOLD)
    for z, length in ((11, 13), (22, 17), (33, 15)):
        rect(s, right, 47, z - 2, 4, 4, 1, DETAIL)
        s.line([right(56, z), right(56 + length, z)], EDGE)
