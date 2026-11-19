from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import upright

DESCRIPTION = "A published article card shows a landscape preview with an X badge over its upper corner."


def draw(s):
    upright(s, rounded(0, 0, 90, 68, 4), 0, 4)

    preview = [(x, 0, z) for x, z in rounded(8, 24, 74, 36, 2)]
    s.line([*preview, preview[0]], DETAIL)
    s.line([(8, 0, 31), (28, 0, 49), (45, 0, 32), (57, 0, 42), (82, 0, 28)], EDGE)
    s.line([(x, 0, z) for x, z in oval(48, 51, 4.5, 4.5)], EDGE)
    s.line([(9, 0, 16), (57, 0, 16)], EDGE)
    s.line([(9, 0, 8), (42, 0, 8)], DETAIL)

    badge(s, "x", 87, 4, 65, 16)
