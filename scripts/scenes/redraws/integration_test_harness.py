from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_brackets
from scenes.systems_shapes import bezel

DESCRIPTION = "A check badge marks a wired test fixture that clamps a code chip between two connector jaws."


def draw(s):
    for x in (-22, 20):
        s.tube([(x, -20, 8), (x, -37, 8), (x + 6, -47, 8)], 2.6)
    s.box(-34, -24, 0, 68, 48, 12, 4)
    s.box(-30, -20, 12, 13, 39, 14, 2)
    s.box(-17, -14, 12, 34, 27, 6, 2)
    code_brackets(s, lambda u, v: (u, -v, 18), 10)
    s.box(17, -20, 12, 13, 39, 14, 2)
    for x in (-24, 24):
        s.line([(x, -12, 26), (x, 10, 26)], DETAIL)
    bezel(s, -12, 24, 3, 24, 6, DETAIL, 1.5)
    badge(s, "check", 33, -9, 35, 13)
