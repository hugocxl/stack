from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning

DESCRIPTION = "A standing incident playbook bears a large alert triangle on its hard cover."


def draw(s):
    s.box(0, -15, 0, 57, 3, 69, 1.7)
    s.box(2, -13, 2, 53, 11, 65, 1)
    s.box(0, -3, 0, 57, 3, 69, 1.7)
    s.box(0, -15, 0, 6, 15, 69, 2)
    s.line([(7, 0, 2), (7, 0, 67)], EDGE)
    s.line([(55, -7, 4), (55, -7, 65)], DETAIL)
    warning(s, 32, .8, 22, 39)
