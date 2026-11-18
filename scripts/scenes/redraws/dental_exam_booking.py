from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import molar, upright

DESCRIPTION = "A ring-bound appointment calendar shows a molar emblem inside the selected date square."


def draw(s):
    for x in (19, 73):
        s.tube([(x, -7, 72), (x, -7, 82), (x, -3, 87), (x, 2, 84)], 2.3, EDGE)

    upright(s, rounded(0, 0, 92, 77, 4), 0, 5)
    for x in (19, 73):
        s.tube([(x, 2, 84), (x, 4, 80), (x, 4, 72)], 2.3, EDGE)

    for z in (6, 32, 58):
        s.line([(7, 0, z), (85, 0, z)], DETAIL)
    for x in (7, 33, 59, 85):
        s.line([(x, 0, 6), (x, 0, 58)], DETAIL)
    s.face([(33, 0, 32), (59, 0, 32), (59, 0, 58), (33, 0, 58)], EDGE)
    tooth = [(x, 0, z) for x, z in molar(46, 45, .226)]
    s.line([*tooth, tooth[0]], BOLD)
