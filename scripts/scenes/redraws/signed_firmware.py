from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_brackets
from scenes.systems_shapes import rectangle

DESCRIPTION = "A pin-legged firmware chip has a code symbol on top and a check badge overlapping one corner."


def draw(s):
    for x in (-22, -11, 0, 11, 22):
        for y, direction in ((-20, -1), (20, 1)):
            s.tube([(x, y, 8), (x, y + direction * 6, 6),
                    (x, y + direction * 9, 1)], 1.8, EDGE)
    s.box(-30, -22, 3, 60, 44, 12, 4)
    rectangle(s, -23, -16, 15, 46, 32, DETAIL, 2)
    code_brackets(s, lambda u, v: (u, -v, 15), 15)
    badge(s, "check", 30, -15, 15, 12)
