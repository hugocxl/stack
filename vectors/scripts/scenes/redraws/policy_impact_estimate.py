from geometry import DETAIL, EDGE
from scenes.redraws._w5 import policy_book, rect

DESCRIPTION = "A standing policy binder shows a bar chart for estimated impact and two ruled clauses."


def draw(s):
    face = policy_book(s)
    s.line([face(15, 44), face(15, 21), face(49, 21)], DETAIL)
    for x, height in ((19, 8), (29, 13), (39, 21)):
        rect(s, face, x, 21, 6, height, .6, EDGE)
    for z, x in ((14, 45), (9, 37)):
        s.line([face(15, z), face(x, z)], DETAIL)
