from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A screwdriver engages the exposed mounting screw on a wall-mounted control unit."


def draw(s):
    s.box(0, 0, 0, 79, 6, 73, 4, ink=DETAIL)
    s.box(9, 6, 11, 61, 18, 50, 6)
    front = Surface(s, lambda u, v: (u, 24, v))
    front.frame(15, 16, 49, 40, 4, DETAIL)
    upright(s, oval(43, 36, 13.5, 13.5)[:-1], 28, 5)
    s.line([(u, 28, v) for u, v in oval(43, 36, 9, 9)], DETAIL)
    s.line([(43, 28, 36), (46, 28, 42)], EDGE)
    front.oval(18, 45, 4.6, 4.6, EDGE)
    front.line([(15.5, 45), (20.5, 45)], DETAIL)
    s.tube([(18, 24, 45), (18, 51, 45)], 1.5)
    s.tube([(18, 50, 45), (18, 71, 45)], 5.5)
    for y in (54, 64):
        s.line([(14, y, 47), (21, y, 48)], DETAIL)
