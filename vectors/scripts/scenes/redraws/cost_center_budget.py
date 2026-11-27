from geometry import DETAIL, EDGE
from scenes.redraws._sf import coin_stack

DESCRIPTION = "An office tower stands beside a short stack of coins set aside for it."


def draw(s):
    s.box(-30, -20, 0, 40, 36, 82, 2)
    for z in range(14, 76, 12):
        for x in (-22, -12, -2):
            s.line([(x, 16, z), (x + 5, 16, z)], DETAIL)
        for y in (-12, -2, 8):
            s.line([(10, y, z), (10, y - 5, z)], DETAIL)
    coin_stack(s, 36, 26, 0, 16, 6)
