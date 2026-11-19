from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import laptop, prompt

DESCRIPTION = "A database query appears on a laptop terminal with a clock badge at the screen corner."


def draw(s):
    y = laptop(s, -36, -10)
    prompt(s, -24, y, 33, 5)
    s.line([(-23, y, 18), (8, y, 18)], DETAIL)
    s.line([(-23, y, 13), (-3, y, 13)], DETAIL)
    x, z = 15, 29
    s.line([(a, y, b) for a, b in oval(x, z, 8, 3.5, count=32)], EDGE)
    for level in (z - 5, z - 10):
        s.line([(a, y, b) for a, b in oval(x, level, 8, 3.5, 180, 360, 18)], EDGE)
    for side in (x - 8, x + 8):
        s.line([(side, y, z), (side, y, z - 10)], EDGE)
    badge(s, "clock", 37, -10, 50, 13)
