from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, wheelchair

DESCRIPTION = "A ramp leads through an open venue doorway with a wheelchair-access sign mounted beside it."


def draw(s):
    entrance = Surface(s, (0, 0, 0))
    entrance.plate([(0, 0), (0, 91), (108, 91), (108, 0), (71, 0),
                    (71, 77), (12, 77), (12, 0)], 14)
    s.box(9, -12, 0, 65, 12, 5, 1)
    s.face([(74, 0, 0), (74, 26, 0), (74, 0, 5)], EDGE)
    s.face([(9, 0, 5), (74, 0, 5), (74, 26, 0), (9, 26, 0)], EDGE)
    s.face([(14, -5, 5), (30, 33, 5), (30, 33, 70), (14, -5, 76)])
    s.line([(27, 28, 40), (27, 28, 47)], EDGE)
    s.line([entrance.point(77, 83), entrance.point(101, 83)], DETAIL)
    sign = Surface(s, (73, 1, 30))
    sign.plate(rounded(0, 0, 32, 37, 3), 2)
    wheelchair(sign, 16, 18, 23)
