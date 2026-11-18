from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w1 import browser_header, laptop, portrait_mark

DESCRIPTION = "A laptop browser displays a signed-in profile with a clock badge on the screen corner."


def draw(s):
    y = laptop(s, -38, 0, w=76, h=58, depth=33)
    browser_header(s, -34, y, 52, 68)
    portrait_mark(s, -11, y, 28, 12)
    s.line([(6, y, 32), (24, y, 32)], DETAIL)
    s.line([(6, y, 23), (19, y, 23)], DETAIL)
    badge(s, "clock", 38, y, 59, 12)
