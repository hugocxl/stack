from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import board, closed_outline, face_arrow, rule

DESCRIPTION = "An upward arrow runs from an outlined backlog row toward the top of a three-row list."


def draw(s):
    point = board(s, 104, 80, run=.37, rise=.82, depth=9, level=True)
    for z, length in ((62, 43), (42, 32)):
        closed_outline(s, point, rounded(10, z - 7, 63, 14, 3), DETAIL)
        rule(s, point, 18, z, length, EDGE)
    closed_outline(s, point, rounded(10, 12, 63, 16, 3), EDGE)
    rule(s, point, 18, 20, 47, EDGE)
    face_arrow(s, point, [(73, 20), (86, 20), (91, 25), (91, 65)], BOLD, head=9)
