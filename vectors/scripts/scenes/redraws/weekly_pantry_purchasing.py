from geometry import DETAIL, EDGE
from scenes.redraws._w5 import clipboard, printed_stroke, rect

DESCRIPTION = "A pantry shopping checklist has a jar in the header above three purchase rows."


def jar_mark(s, face, x, z, scale=1):
    for outline in (
        [(-5, 5), (-5, 3), (-7, 1), (-7, -7), (-5, -9), (5, -9),
         (7, -7), (7, 1), (5, 3), (5, 5)],
        [(-6, 5), (-6, 8), (6, 8), (6, 5), (-6, 5)],
        [(-3, -5), (3, -5), (3, 0), (-3, 0), (-3, -5)],
    ):
        printed_stroke(s, face, [(x + u * scale, z + v * scale) for u, v in outline], EDGE)


def draw(s):
    face = clipboard(s, 50, 69)
    jar_mark(s, face, 13, 47, .65)
    printed_stroke(s, face, [(22, 49), (39, 49)], EDGE)
    printed_stroke(s, face, [(22, 44), (33, 44)], DETAIL)
    printed_stroke(s, face, [(8, 38), (41, 38)], DETAIL)
    for z, end in ((30, 40), (20, 35), (10, 37)):
        rect(s, face, 9, z - 2.2, 5, 4.4, .6, EDGE)
        printed_stroke(s, face, [(20, z), (end, z)], EDGE)
