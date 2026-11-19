from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import browser_page, rule

DESCRIPTION = "A single browser shows a forward arrow joining three successive page nodes."


def draw(s):
    p = browser_page(s, 135, 73, depth=15)
    arrow(s, [p(12, 23), p(119, 23)], BOLD, head=8)
    for index, x in enumerate((19, 53, 87)):
        s.face([p(x, 29), p(x + 21, 29), p(x + 21, 52), p(x, 52)], EDGE)
        s.line([p(x + 10, 29), p(x + 10, 23)], EDGE)
        rule(s, p, x + 4, 46, 13)
        rule(s, p, x + 4, 40, (8, 6, 10)[index], DETAIL)
