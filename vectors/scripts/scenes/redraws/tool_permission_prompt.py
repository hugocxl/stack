from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import browser_page, closed_outline, rule

DESCRIPTION = "A browser permission dialog shows two action buttons with a lock badge beside them."


def draw(s):
    point = browser_page(s, 104, 76, depth=12)
    closed_outline(s, point, rounded(13, 13, 78, 41, 3), EDGE)
    rule(s, point, 21, 44, 37, EDGE)
    rule(s, point, 21, 35, 53)
    for x in (34, 62):
        closed_outline(s, point, rounded(x, 18, 21, 9, 2), EDGE)
    badge(s, "lock", 101, 2, 27, 12)
