from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A legal file folder has a raised index tab and a closed lock badge at its lower corner."


def draw(s):
    back = lambda x, z: (x, -8 - z * .22, z)
    front = lambda x, z: (x, -z * .06, z)
    s.face([back(x, z) for x, z in [(0, 0), (67, 0), (67, 51), (32, 51),
            (28, 61), (6, 61), (2, 56), (0, 56)]], EDGE)
    for z, length in ((54, 14), (57, 9)):
        s.line([back(8, z), back(8 + length, z)], DETAIL)
    s.face([(x, -4 - z * .13, z) for x, z in
            ((5, 2), (63, 2), (63, 48), (5, 48))], DETAIL)
    s.face([back(67, 0), back(67, 37), front(67, 37), front(67, 0)], EDGE)
    s.face([front(x, z) for x, z in [(0, 0), (67, 0), (67, 39), (64, 44),
            (40, 44), (35, 40), (0, 40)]], EDGE)
    badge(s, "lock", *front(64, 16), 13)
