from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import browser_window

DESCRIPTION = "A double-ended horizontal arrow spans an expanded browser column between two dashed original margins."


def draw(s):
    page = browser_window(s, 127, 76)
    page.rect(8, 7, 111, 47, 2, EDGE)
    for x in (33, 94):
        page.stroke([(x, 12), (x, 49)], DETAIL, dashed=True)
    for x in (15, 112):
        page.stroke([(x, 22), (x, 38)], EDGE)
    p = page.point
    arrow(s, [p(17, 30), p(108, 30)], BOLD, head=10)
    arrow(s, [p(60, 30), p(17, 30)], BOLD, head=10)
