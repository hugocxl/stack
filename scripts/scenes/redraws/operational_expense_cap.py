from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import currency_mark, printed_stroke, rect

DESCRIPTION = "An upright expense gauge shows a dollar mark and a heavy stop above the current spend segments."


def draw(s):
    s.box(0, 0, 0, 14, 49, 70, 4.5)
    face = lambda u, z: (14.05, 49 - u, z)
    rect(s, face, 5.5, 7, 38, 56, 4, DETAIL)
    rect(s, face, 10, 12, 16, 46, 5, EDGE)
    for z in (18, 25, 32, 39):
        rect(s, face, 13.5, z, 9, 4.5, .9, EDGE)
    printed_stroke(s, face, [(8, 49), (28, 49)], BOLD)
    currency_mark(s, face, 34, 32, 6)
