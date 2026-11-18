from geometry import DETAIL
from scenes.redraws._w1 import branch, browser_header, laptop

DESCRIPTION = "A laptop browser shows a preview thumbnail beside a large Git branch diagram."


def draw(s):
    y = laptop(s, -35, 0, w=70, h=53, depth=36)
    browser_header(s, -30, y, 47, 60)
    s.line([(-25, y, 31), (-9, y, 31), (-9, y, 14),
            (-25, y, 14), (-25, y, 31)], DETAIL)
    s.line([(-25, y, 19), (-20, y, 23), (-17, y, 20),
            (-14, y, 25), (-9, y, 18)], DETAIL)
    branch(s, 6, y, 24, 12)
