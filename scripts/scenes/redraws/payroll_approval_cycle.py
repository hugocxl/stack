from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, panel, printed_stroke, ruled_amounts

DESCRIPTION = "A continuous-feed payroll register aligns three wage rows beneath a currency heading and carries a check badge."


def draw(s):
    face = lambda x, z: (x, -.8 * z, z)
    panel(s, [(0, 0), (83, 0), (83, 47), (0, 47)], face, 3.8)
    for x in (4.5, 78.5):
        for z in (8, 18, 28, 38):
            s.line([face(a, b) for a, b in oval(x, z, 1.65, 1.65, count=18)], DETAIL)
    for x in (10, 73):
        printed_stroke(s, face, [(x, 0), (x, 47)], DETAIL)
    currency_mark(s, face, 62, 36, 6.2)
    printed_stroke(s, face, [(16, 37), (42, 37)], EDGE)
    printed_stroke(s, face, [(15, 28.5), (68, 28.5)], EDGE)
    ruled_amounts(s, face, ((22, 19), (14.5, 23), (7, 16)), 16, 68, width=13)
    for z, length in ((22, 7), (14.5, 9), (7, 7)):
        printed_stroke(s, face, [(43, z), (43 + length, z)], DETAIL)
    badge(s, "check", *face(82, 36), 12)
