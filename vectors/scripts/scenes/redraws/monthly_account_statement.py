from geometry import DETAIL, EDGE
from scenes.redraws._w5 import currency_mark, hardback, printed_stroke, rect, ruled_amounts

DESCRIPTION = "A bound account statement places a calendar heading above separate opening and closing balances."


def draw(s):
    face = hardback(s, 65, 69, depth=10)
    rect(s, face, 13, 41, 24, 19, 2)
    printed_stroke(s, face, [(13, 54), (37, 54)], EDGE)
    for x in (20, 30):
        printed_stroke(s, face, [(x, 58), (x, 63)], EDGE)
    for z in (45, 49):
        for x in (18, 24, 30):
            printed_stroke(s, face, [(x, z), (x + 2.8, z)])
    printed_stroke(s, face, [(43, 54), (57, 54)], EDGE)
    printed_stroke(s, face, [(43, 48), (54, 48)], DETAIL)
    for z in (34, 19):
        printed_stroke(s, face, [(12, z), (58, z)], DETAIL)
    for z in (26, 11):
        currency_mark(s, face, 17, z, 3.8)
    ruled_amounts(s, face, ((26, 10), (11, 15)), 24, 57, width=11)
