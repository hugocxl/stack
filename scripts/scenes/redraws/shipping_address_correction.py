from geometry import DETAIL, EDGE
from scenes.redraws._w1 import waybill

DESCRIPTION = "A small pencil points to the address block on a standing shipping label."


def draw(s):
    waybill(s)
    tip = (9, 3, 42)
    a, b, c, d = (14, 3, 52), (20, 3, 46), (40, 3, 67), (34, 3, 73)
    s.face([a, d, (34, .2, 73), (14, .2, 52)], EDGE)
    s.face([tip, b, c, d, a], EDGE)
    s.line([a, b], DETAIL)
    s.line([(10.9, 3, 46), (13.7, 3, 44)], EDGE)
    s.line([(17, 3, 49), (36, 3, 69)], DETAIL)
    s.line([(30, 3, 69), (36.4, 3, 63.3)], EDGE)
