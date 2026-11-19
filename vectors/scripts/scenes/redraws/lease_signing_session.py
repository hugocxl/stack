from geometry import DETAIL, EDGE
from scenes.redraws._w2 import folded_sheet, rule
from scenes.redraws.homebuyer_closing_packet import house_emblem, signature

DESCRIPTION = "A pen touches the signature line of a landscape lease sheet headed by a house outline."


def draw(s):
    def point(x, z):
        return .80*x + .12*z, -.20*x - .65*z, .64*z

    folded_sheet(s, point, 103, 68, fold=11, depth=4)
    house_emblem(s, point, 24, 50, 13)
    for z, width in ((55, 40), (45, 29), (32, 67)):
        rule(s, point, 44 if z > 40 else 12, z, width)
    signature(s, point, 12, 13, 59)
    tip = point(51, 19)
    shoulder = (tip[0] + 6, tip[1] - 8, tip[2] + 12)
    cap = (tip[0] + 29, tip[1] - 31, tip[2] + 47)
    s.tube([shoulder, cap], 3.0, EDGE)
    s.tube([tip, shoulder], 1.25, EDGE)
    s.line([(cap[0] - 7, cap[1] + 2, cap[2] - 1),
            (cap[0] - 13, cap[1] + 7, cap[2] - 10)], DETAIL)
