from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import left_face, plate, squircle, turned

DESCRIPTION = "On a standing chart, one observed line splits at today into three dashed projections."


def draw(s):
    w, h = 112, 76
    for x in (14, w - 14):
        s.box(x - 9, -14, 0, 18, 22, 4, 2)
    face = left_face(0, 0, 6)
    plate(s, face, squircle(w, h, 6), 6, (0, -1, 0))
    s.line([face(12, h - 10), face(12, 10), face(w - 10, 10)], DETAIL)
    observed = [(12, 22), (24, 28), (34, 24), (46, 34), (58, 38)]
    s.line([face(u, v) for u, v in observed], BOLD)
    s.line([face(58, 12), face(58, h - 12)], DETAIL, dashed=True)
    for end in (62, 44, 26):
        s.line([face(58, 38), face(98, end)], EDGE, dashed=True)
    for u, v in ((98, 62), (98, 44), (98, 26)):
        s.line([face(u + a, v + b) for a, b in __import__("geometry").oval(0, 0, 2.6, 2.6, count=20)], EDGE)
    s.line([face(58 + a, 38 + b) for a, b in __import__("geometry").oval(0, 0, 3.2, 3.2, count=20)], BOLD)
