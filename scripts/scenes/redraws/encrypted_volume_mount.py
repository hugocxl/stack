from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel, rectangle

DESCRIPTION = "A disk drive slides into a thick mounting bay with a lock badge attached to the drive."


def draw(s):
    s.box(-36, -34, 0, 72, 41, 37, 3)
    bezel(s, -30, 7, 7, 60, 23, EDGE, 2)
    s.box(-26, 6, 9, 52, 33, 15, 3)
    s.ellipse(-7, 24, 24, 9, 9, EDGE)
    s.ellipse(-7, 24, 24, 2.4, 2.4, DETAIL)
    s.line([(-4, 26, 24), (2, 32, 24), (10, 32, 24)], DETAIL)
    rectangle(s, -20, 35, 24, 8, 2, DETAIL, .8)
    s.line([(-20, 39, 16), (-11, 39, 16)], DETAIL)
    badge(s, "lock", 24, 22, 28, 12)
