from geometry import DETAIL, EDGE
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A trigger spray bottle of disinfectant stands upright."


def draw(s):
    turned(s, [(18, 0), (19, 3), (19, 50), (16, 58), (8, 64), (7, 70)], steps=3)
    lip(s, 0, 0, 30, 19, DETAIL, -40, 130)
    lip(s, 0, 0, 14, 19, DETAIL, -40, 130)
    s.box(-8, -10, 70, 16, 34, 12, 4)
    s.box(-3, 22, 74, 6, 8, 5, 2)
    s.tube([(0, 6, 70), (0, 12, 56), (0, 16, 58)], 2.2, EDGE)
