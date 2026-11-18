from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, printed_stroke, rect

DESCRIPTION = "A countertop kitchen monitor displays two hanging order tickets with itemized lines."


def draw(s):
    s.box(21, -25, 0, 36, 25, 4, 4)
    s.box(33, -21, 4, 13, 14, 14, 2)
    face = lambda x, z: (x, 5 - .23 * x - .20 * (z - 15), z)
    panel(s, rounded(0, 15, 80, 49, 4.3), face, 7)
    rect(s, face, 4, 21, 72, 38, 2, EDGE)
    for x, widths in ((11, (11, 14, 9)), (44, (14, 8, 13))):
        ticket = [(x, 23), (x + 4, 25), (x + 9, 23), (x + 14, 25),
                  (x + 19, 23), (x + 24, 25), (x + 27, 23),
                  (x + 27, 55), (x, 55), (x, 23)]
        printed_stroke(s, face, ticket, EDGE)
        printed_stroke(s, face, [(x + 4, 49), (x + 18, 49)], EDGE)
        for z, w in zip((43, 37, 31), widths):
            printed_stroke(s, face, [(x + 4, z), (x + 4 + w, z)], DETAIL)
            printed_stroke(s, face, [(x + 21, z), (x + 23, z)], DETAIL)
