from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_marker, rule, sparkle, speech_bubble

DESCRIPTION = "An agent conversation bubble shows a progress arrow descending past three task rows."


def draw(s):
    def p(x, z):
        return x*.73, -x*.27, z

    speech_bubble(s, p, 100, 87, depth=9)
    sparkle(s, p, 20, 67, 8, EDGE)
    rule(s, p, 34, 67, 40, EDGE)
    for z, length in ((48, 47), (33, 39), (18, 43)):
        chart_marker(s, p, 35, z, 2.4, DETAIL)
        rule(s, p, 45, z, length - 5)
    arrow(s, [p(17, 50), p(17, 15)], BOLD, head=5)
