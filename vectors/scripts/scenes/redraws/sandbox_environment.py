from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes.redraws._w1 import laptop, prompt

DESCRIPTION = "A developer laptop with a command prompt sits inside a transparent test enclosure."


def draw(s):
    low, high, roof = -46, 46, 79
    back, left = (low, low), (low, high)
    right, front = (high, low), (high, high)

    s.line([(*left, 4), (*back, 4), (*right, 4)], GUIDE, dashed=True)
    s.line([(*back, 4), (*back, roof)], GUIDE, dashed=True)
    s.box(low, low, 0, 92, 92, 4, 1.2, EDGE)
    s.line([(*left, roof), (*front, roof), (*right, roof)], DETAIL)
    laptop(s, -34, -13, w=68, h=44, depth=39)
    prompt(s, -22, -13, 31, 8, BOLD)
    s.line([(8, -13, 23), (25, -13, 23)], DETAIL)

    for corner in (left, right):
        s.line([(*corner, 4), (*corner, roof)], EDGE)
    s.line([(*left, roof), (*back, roof), (*right, roof)], EDGE)
    s.line([(*front, 4), (*front, 19)], GUIDE, dashed=True)
    s.line([(*front, 70), (*front, roof)], GUIDE, dashed=True)
