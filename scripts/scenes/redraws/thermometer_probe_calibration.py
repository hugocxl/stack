from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import panel, printed_stroke, rect

DESCRIPTION = "A digital probe thermometer stands with its stem immersed to the marked water level in a calibration bath."


def draw(s):
    s.box(0, 0, 0, 51, 43, 17, 4)
    s.face([(0, 1, 17), (51, 1, 17), (51, 1, 26), (0, 1, 26)], DETAIL)
    # The probe stops at the visible water surface, just below the bath rim.
    s.ellipse(25, 20, 21, 10, 8, DETAIL)
    s.ellipse(25, 20, 21, 6.5, 5.2, DETAIL)
    s.face([(51, 0, 16), (51, 43, 16), (51, 43, 26), (51, 0, 26)])
    s.face([(0, 43, 16), (51, 43, 16), (51, 43, 26), (0, 43, 26)])
    s.face([(x, y, 26) for x, y in rounded(0, 0, 51, 43, 3)],
           openings=[[(x, y, 26) for x, y in rounded(3, 3, 45, 37, 3)]])
    s.tube([(25, 20, 21), (25, 20, 45)], 1.65)
    s.line([(22.6, 20, 25), (27.4, 20, 25)], EDGE)
    mark = lambda x, z: (x, 43, z)
    printed_stroke(s, mark, [(9, 19), (18, 19)], BOLD)
    printed_stroke(s, mark, [(9, 14), (14, 14)], DETAIL)
    printed_stroke(s, mark, [(9, 9), (14, 9)], DETAIL)
    face = lambda x, z: (x, 21 - .24 * (z - 43), z)
    panel(s, rounded(14, 43, 22, 31, 4), face, 4)
    rect(s, face, 17.5, 59, 15, 9, 1.4, EDGE)
    printed_stroke(s, face, [(21, 63.5), (29, 63.5)], DETAIL)
    printed_stroke(s, face, oval(25, 52.5, 2.3, 2.3), DETAIL)
