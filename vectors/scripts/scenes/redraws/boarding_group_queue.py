from geometry import EDGE
from scenes.redraws._sf import left_face, plate, squircle

DESCRIPTION = "Two upright carry-ons queue in line in front of a gate sign on a post."


def carry_on(s, x, y):
    for dx in (-8, 8):
        s.tube([(x + dx, y, 46), (x + dx, y, 60)], 1.3, EDGE)
    s.tube([(x - 8, y, 60), (x + 8, y, 60)], 1.8, EDGE)
    face = left_face(x - 16, y + 10, 3)
    plate(s, face, squircle(32, 44, 7), 16, (0, -1, 0))
    for dx in (-10, 10):
        s.disk(x + dx, y + 6, 0, 3, 3, 3)


def draw(s):
    s.tube([(-50, -40, 0), (-50, -40, 84)], 2, EDGE)
    sign = left_face(-78, -38, 74)
    plate(s, sign, squircle(56, 26, 5), 4, (0, -1, 0))
    s.line([sign(14, 13), sign(42, 13)], EDGE)
    s.line([sign(34, 19), sign(42, 13), sign(34, 7)], EDGE)
    carry_on(s, 0, -30)
    carry_on(s, 46, -30)
