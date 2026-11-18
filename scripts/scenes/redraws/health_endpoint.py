from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import code_brackets, pulse
from scenes.systems_shapes import bezel

DESCRIPTION = "A standing API response panel pairs a code symbol with a prominent pulse trace."


def draw(s):
    s.box(-39, -26, 0, 78, 26, 7, 3)
    s.box(-37, -9, 7, 74, 9, 56, 3)
    bezel(s, -32, 0, 12, 64, 46, EDGE, 2)
    s.line([(-32, 0, 42), (32, 0, 42)], EDGE)
    code_brackets(s, lambda u, v: (-21 + u, 0, 50 + v), 7, EDGE)
    s.line([(-8, 0, 50), (17, 0, 50)], DETAIL)
    s.line([(x - 25, 0, z + 26) for x, z in pulse(50, 12)], BOLD)
