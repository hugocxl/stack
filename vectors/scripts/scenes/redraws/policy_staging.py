from geometry import DETAIL, EDGE
from scenes.redraws._w5 import policy_book

DESCRIPTION = "A standing policy binder has a draft sheet with a dashed perimeter and three unmarked clauses."


def draw(s):
    face = policy_book(s, draft=True)
    for z, length in ((42, 25), (30, 28), (18, 24)):
        s.line([face(16, z), face(18, z)], EDGE)
        s.line([face(22, z), face(22 + length - 5, z)], DETAIL)
        s.line([face(22, z - 4), face(33, z - 4)], DETAIL)
