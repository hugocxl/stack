from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import left_face, smooth

DESCRIPTION = "A dashed route on the ground leads to a clock tower landmark."


def draw(s):
    route = smooth([(-52, 46), (-36, 40), (-22, 26), (-6, 22), (6, 16)], 8)
    s.line([(x, y, 0) for x, y in route], DETAIL, dashed=True)
    s.box(0, -14, 0, 28, 28, 6, 2)
    s.box(4, -10, 6, 20, 20, 64, 1)
    apex = (14, 0, 98)
    for face in ([(4, 10, 70), (24, 10, 70), apex], [(24, -10, 70), (24, 10, 70), apex]):
        s.face(face, EDGE)
    clock = left_face(4, 10, 0)
    s.line([clock(10 + a, 54 + b) for a, b in oval(0, 0, 6.5, 6.5, count=32)], EDGE)
    s.line([clock(10, 58), clock(10, 54), clock(13, 52)], DETAIL)
    for z in (20, 34):
        s.line([clock(7, z), clock(7, z + 8)], DETAIL)
        s.line([clock(13, z), clock(13, z + 8)], DETAIL)
