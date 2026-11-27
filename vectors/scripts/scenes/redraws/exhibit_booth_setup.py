from geometry import DETAIL
from scenes.redraws._sf import left_face, plate, squircle

DESCRIPTION = "A trade-show booth has a back wall, a side panel, a header sign and a counter."


def draw(s):
    back = left_face(-50, -40, 0)
    plate(s, back, [(0, 0), (100, 0), (100, 80), (0, 80)], 4, (0, -1, 0))
    s.line([back(u, v) for u, v in squircle(56, 34, 4)] + [back(*squircle(56, 34, 4)[0])], DETAIL) if False else None
    frame = [back(22 + u, 34 + v) for u, v in squircle(56, 30, 4)]
    s.line(frame + frame[:1], DETAIL)
    s.box(-54, -40, 0, 4, 44, 80, 1)
    head = left_face(-50, -36, 84)
    plate(s, head, squircle(100, 14, 4), 6, (0, -1, 0))
    s.box(-20, 4, 0, 48, 22, 32, 3)
    s.box(-23, 1, 32, 54, 28, 4, 2)
