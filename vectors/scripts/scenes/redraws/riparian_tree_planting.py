from geometry import DETAIL, EDGE
from scenes.redraws._sf import tree

DESCRIPTION = "A young tree stands on a raised riverbank just above gentle water lines."


def draw(s):
    s.solid([(-60, -40), (60, -40), (60, 6), (-60, 6)], 0, 22)
    s.face([(-60, 6, 0), (60, 6, 0), (60, 30, 0), (-60, 30, 0)], DETAIL)
    for y in (14, 22):
        s.line([(x, y + 2*__import__("math").sin(x/6), 0) for x in range(-54, 56, 3)], DETAIL)
    tree(s, 0, -14, 22, 60, 22)
