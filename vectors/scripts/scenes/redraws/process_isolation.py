from geometry import EDGE, GUIDE
from scenes.redraws._w1 import firmware_chip

DESCRIPTION = "A pin-legged processor sits entirely inside the edges of a transparent cubic sandbox."


def draw(s):
    low, high, roof = -40, 40, 67
    back = (low, low)
    left = (low, high)
    right = (high, low)
    front = (high, high)

    s.line([(*left, 0), (*back, 0), (*right, 0)], GUIDE, dashed=True)
    s.line([(*back, 0), (*back, roof)], GUIDE, dashed=True)
    firmware_chip(s)
    for corner in (left, right):
        s.line([(*corner, 0), (*corner, roof)], EDGE)
    s.line([(*left, 0), (*front, 0), (*right, 0)], EDGE)
    s.line([(*back, roof), (*left, roof), (*front, roof),
            (*right, roof), (*back, roof)], EDGE)
