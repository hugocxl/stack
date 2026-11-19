from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import clipboard, cloche_mark, printed_stroke

DESCRIPTION = "A recipe clipboard presents preparation, cooking, and serving in three ordered pictogram rows."


def draw(s):
    face = clipboard(s, 59, 79)
    for level, count in ((56, 1), (37, 2), (18, 3)):
        for i in range(count):
            dot = oval(9.5 + 4.2*i, level, 1.25, 1.25, count=14)
            printed_stroke(s, face, dot, BOLD)
    for z in (27, 46, 65):
        s.line([face(8, z), face(50, z)], DETAIL)
    printed_stroke(s, face, [(24, 53), (27, 51), (38, 51), (38, 55),
                             (46, 55), (46, 58), (37, 58), (37, 55),
                             (28, 54), (24, 53)], EDGE)
    printed_stroke(s, face, [(27, 41), (28, 34), (30, 32), (42, 32),
                             (44, 34), (45, 41), (27, 41)], EDGE)
    printed_stroke(s, face, [(24, 41), (48, 41)], EDGE)
    printed_stroke(s, face, [(32, 42), (33, 44), (38, 44), (39, 42)], EDGE)
    cloche_mark(s, face, 35, 16, .78)
