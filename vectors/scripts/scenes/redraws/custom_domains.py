from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import loop, rule, upright

DESCRIPTION = "A browser window shows a dot-separated address above a globe."


def draw(s):
    s.box(0, -3, 0, 115, 3, 68, 1.4)
    rule(s, 0, 115, 41, EDGE)

    # Browser controls and a domain-shaped address, drawn without lettering.
    for x in (9, 16, 23):
        loop(s, oval(x, 54, 1.4, 1.4, count=16)[:-1], DETAIL)
    loop(s, rounded(32, 46, 75, 16, 7), BOLD)
    rule(s, 42, 75, 54, EDGE)
    loop(s, oval(80, 52, 1.5, 1.5, count=16)[:-1], EDGE)
    rule(s, 85, 98, 54, EDGE)

    loop(s, oval(57.5, 21, 14, 14, count=56)[:-1], EDGE)
    loop(s, oval(57.5, 21, 6, 14, count=48)[:-1], EDGE)
    s.line(upright([(43.5, 21), (71.5, 21)]), DETAIL)
