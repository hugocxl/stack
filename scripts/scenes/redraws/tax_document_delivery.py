from geometry import DETAIL, EDGE
from scenes.redraws._w5 import bank_mark, currency_mark, panel, printed_stroke, rect, ruled_amounts

DESCRIPTION = "An open mailing envelope holds a tax form with a treasury emblem and a boxed currency field."


def draw(s):
    def point(x, y, z):
        return .91 * x + .41 * y, -.41 * x + .91 * y, z

    back = lambda x, z: point(x, -16, z)

    s.face([back(x, z) for x, z in [(0, 0), (76, 0), (76, 37), (38, 68), (0, 37)]])
    form = lambda x, z: point(x, -z * .28 + 8, z)
    outline = [(11, 7), (64, 7), (64, 73), (11, 73)]
    panel(s, outline, form, 2)
    bank_mark(s, form, 25, 63, .78)
    rect(s, form, 38, 57, 19, 13, 1.2, EDGE)
    currency_mark(s, form, 47, 63, 4.8)
    ruled_amounts(s, form, ((49, 15), (41, 20), (33, 12)), 17, 57, width=11)
    front = lambda x, z: point(x, 9, z)
    s.face([back(76, 0), back(76, 37), front(76, 35), front(76, 0)])
    profile = [(0, 0), (76, 0), (76, 35), (38, 15), (0, 35)]
    s.face([front(x, z) for x, z in profile])
    printed_stroke(s, front, [(2, 2), (21, 24)], DETAIL)
    printed_stroke(s, front, [(74, 2), (55, 24)], DETAIL)
