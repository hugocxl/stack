from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_brackets

DESCRIPTION = "Three code packages sit on parallel release rails, with a check badge marking the nearest channel."


def draw(s):
    for x, y in ((19, -34), (0, 0), (-19, 34)):
        for rail in (y - 9, y + 9):
            s.box(-42, rail - 1, 0, 84, 2, 2, .6)
        for end in (-42, 39):
            s.box(end, y - 12, 0, 3, 24, 2, .6, DETAIL)

        s.box(x - 14, y - 11, 2, 28, 22, 28, 1.4, EDGE)
        code_brackets(s, lambda u, v: (x + u, y + 11, 15 + v), 11)

    badge(s, "check", -30, 47, 30, 9)
