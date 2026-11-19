from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, outline

DESCRIPTION = "A spectrum analyzer displays one tall signal peak above a low, continuous noise floor."


def draw(s):
    s.box(0, -30, 0, 113, 30, 67, 5)
    outline(s, 8, 0, 8, 96, 51, 3, EDGE)

    def p(x, z):
        return x, 0, z

    for z in (22, 34, 46):
        s.line([p(14, z), p(98, z)], DETAIL)
    chart_line(s, p, [(13, 17), (20, 18), (27, 15), (33, 20), (39, 16), (46, 18),
                     (49, 21), (53, 27), (57, 54), (61, 28), (65, 20),
                     (71, 18), (78, 15), (84, 20), (90, 17), (98, 19)], BOLD)
    s.line([(113, -24, 18), (113, -7, 18)], DETAIL)
    s.line([(113, -24, 24), (113, -7, 24)], DETAIL)
