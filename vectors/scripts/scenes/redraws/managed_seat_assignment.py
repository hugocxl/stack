from geometry import BOLD, EDGE
from scenes.redraws._w1 import portrait_mark, upright_profile

DESCRIPTION = "A workspace model shows four chairs around a shared desk and an employee token on the selected chair."


def chair(s, x, y, *, front=False):
    back = y + 6 if front else y - 7
    s.disk(x, y, 0, 6.5, 5.5, 2)
    s.tube([(x, y, 2), (x, y, 7)], 1.2)
    s.box(x - 7, y - 6, 7, 14, 12, 3, 2)
    s.box(x - 7, back, 8, 14, 3, 12, 1.4)


def draw(s):
    s.box(-31, -34, -3, 62, 65, 3, 2)
    for x in (-15, 15):
        chair(s, x, -24)
    for x in (-22, 20):
        s.box(x, -8, 0, 3, 6, 12, 1)
    s.box(-27, -13, 12, 54, 23, 3, 2)
    for x in (-15, 15):
        chair(s, x, 20, front=True)
    upright_profile(s, [(11, 6), (11, 26), (33, 26), (33, 6)], 30, 3, BOLD)
    portrait_mark(s, 22, 30, 16, 7.7, EDGE)
