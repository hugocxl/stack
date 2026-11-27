from geometry import DETAIL, EDGE
from scenes.redraws._sf import smooth

DESCRIPTION = "A dashed path on the ground passes three round milestones and ends at a planted flag."


def draw(s):
    path = smooth([(-60, 40), (-36, 30), (-18, 10), (4, 4), (22, -16), (40, -22)], 8)
    s.line([(x, y, 0) for x, y in path], DETAIL, dashed=True)
    for x, y in ((-60, 40), (-18, 10), (22, -16)):
        s.disk(x, y, 0, 11, 11, 5)
    s.disk(44, -24, 0, 5, 5, 2)
    s.tube([(44, -24, 2), (44, -24, 58)], 1.6, EDGE)
    s.face([(44, -24, 56), (44, -24, 38), (44 + 24*.7, -24 - 24*.7, 47)], EDGE)
