from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import board, chart_line

DESCRIPTION = "A laptop dashboard shows a rising trend and a compact pulse tile beside a live-status badge."


def draw(s):
    point = board(s, 123, 79, run=.11, depth=4, base=2)
    s.line([point(6, 66), point(117, 66)], DETAIL)
    s.line([point(12, 72), point(36, 72)], EDGE)
    s.line([point(12, 55), point(12, 14), point(68, 14)], DETAIL)
    chart_line(s, point, [(17, 22), (27, 29), (37, 25), (48, 40), (55, 36), (67, 53)])
    tile = [(76, 22), (112, 22), (112, 54), (76, 54), (76, 22)]
    s.line([point(x, v) for x, v in tile], EDGE)
    chart_line(s, point, [(81, 35), (86, 35), (90, 40), (93, 31), (97, 46),
                          (101, 35), (107, 35)])
    s.box(0, 0, 0, 123, 55, 5, 4)
    s.line([(x, y, 5) for x, y in rounded(10, 9, 103, 22, 3)], DETAIL)
    for y in (17, 23):
        s.line([(17, y, 5), (106, y, 5)], DETAIL)
    s.line([(x, y, 5) for x, y in rounded(45, 37, 33, 12, 3)], DETAIL)
    x, y, z = point(116, 70)
    badge(s, "dot", x + 7, y, z + 3, 9)
