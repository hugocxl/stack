from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A metal hook catches the end of an event line beneath code brackets on a script editor."


def draw(s):
    code = Surface(s, (0, 0, 0), across=(.97, -.24))
    code.plate(rounded(0, 0, 101, 82, 5), 9)
    code.rules(0, 67, [101], ink=EDGE)
    code.oval(9, 74, 1.5, 1.5, EDGE)
    code.oval(16, 74, 1.5, 1.5, EDGE)
    code.stroke([(24, 57), (12, 49), (24, 41)], EDGE)
    code.stroke([(41, 57), (32, 41)], EDGE)
    code.stroke([(48, 57), (60, 49), (48, 41)], EDGE)
    code.rules(13, 28, [53], ink=EDGE)
    code.rules(23, 16, [31])
    code.oval(74, 28, 5, 5, EDGE)

    hook = Surface(s, code.point(81, 9, -8), across=(.707, -.707))
    curve = [(0, 30), (0, 11), *oval(10, 11, 10, 10, 180, 391, 32)]
    s.tube([hook.point(x, v) for x, v in curve], 2.3, BOLD)
