from geometry import DETAIL, EDGE
from scenes.redraws._w5 import bank_mark, money_coin

DESCRIPTION = "A coin enters the open mouth of a bank-marked deposit envelope."


def draw(s):
    rear = [(0, 0, 0), (74, 0, 0), (74, -11, 40), (0, -11, 40)]
    s.face(rear, EDGE)
    s.face([(0, -11, 40), (74, -11, 40), (39, -27, 61), (35, -27, 61)], EDGE)
    s.face([(74, 0, 0), (74, 4, 0), (74, 4, 35), (74, -11, 40)], EDGE)
    money_coin(s, 34, -1, 34, 17)

    face = lambda x, z: (x, 4, z)
    edge = [(0, 0), (74, 0), (74, 35), (45, 29), (29, 29), (0, 35)]
    s.face([face(x, z) for x, z in edge], EDGE)
    bank_mark(s, face, 37, 13, .84)
    s.line([face(73, 1), face(54, 21)], DETAIL)
    s.line([face(1, 1), face(20, 21)], DETAIL)
