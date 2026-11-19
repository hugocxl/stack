from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import clipboard, printed_stroke, ruled_amounts

DESCRIPTION = "A clipped receivables list shows three invoice rows with amounts and a clock badge."


def draw(s):
    face = clipboard(s, 58, 68)
    for z in (47, 33, 19):
        printed_stroke(s, face, [(10, z - 4), (10, z + 5), (15, z + 5),
                                 (18, z + 2), (18, z - 4), (10, z - 4)], EDGE)
        printed_stroke(s, face, [(8, z - 7), (48, z - 7)], DETAIL)
    ruled_amounts(s, face, ((47, 8), (33, 11), (19, 9)), 21, 48, width=8)
    badge(s, "clock", *face(58, 55), 10.5)
