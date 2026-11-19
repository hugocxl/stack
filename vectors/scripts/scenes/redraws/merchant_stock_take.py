from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import clipboard

DESCRIPTION = "A stock-count clipboard shows three product rows with tally marks and a separate total line."


def draw(s):
    clipboard(s)
    for z in (16, 26, 36):
        s.line([(-20, 0, z), (20, 0, z)], DETAIL)

    s.line([(a, 0, b) for a, b in [(-19, 29), (-19, 33), (-14, 33), (-14, 29), (-19, 29)]], EDGE)
    s.line([(a, 0, b) for a, b in oval(-16.5, 21, 2.7, 2.7, count=24)], EDGE)
    s.line([(a, 0, b) for a, b in [(-19, 40), (-16.5, 44), (-14, 40), (-19, 40)]], EDGE)

    for z, count in ((18, 2), (28, 3), (38, 4)):
        for i in range(count):
            x = -7 + 4 * i
            s.line([(x, 0, z), (x, 0, z + 5)], EDGE)
    s.line([(-9, 0, 39), (7, 0, 42)], EDGE)
    for z in (8, 11):
        s.line([(2, 0, z), (20, 0, z)], EDGE)
