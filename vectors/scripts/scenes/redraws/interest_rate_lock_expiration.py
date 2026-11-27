from geometry import BOLD, oval
from scenes.redraws._kit import badge
from scenes.redraws._sf import padlock

DESCRIPTION = "A padlock printed with a percent sign carries a clock badge at its lower right."


def draw(s):
    body = padlock(s, -30, 0, 0, w=60, h=48, depth=16, keyhole=False)
    s.line([body(22, 14), body(38, 34)], BOLD)
    for u, v in ((22, 30), (38, 18)):
        s.line([body(u + a, v + b) for a, b in oval(0, 0, 3.6, 3.6, count=24)], BOLD)
    badge(s, "clock", 30, 0, 4, 14)
