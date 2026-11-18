from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_marker

DESCRIPTION = "Brackets highlight a bounded interval on a standing ruler, and a check identifies an interior tick."


def draw(s):
    s.box(0, -11, 0, 123, 11, 36, 3)
    p = lambda x, z: (x, 0, z)
    s.line([p(8, 24), p(115, 24)], EDGE)
    for i in range(13):
        x = 8 + i*8.9
        s.line([p(x, 24), p(x, 15 if i % 3 == 0 else 19)], DETAIL)
    s.line([p(34.7, 16), p(34.7, 7), p(88.1, 7), p(88.1, 16)], BOLD)
    s.line([p(61.4, 24), p(61.4, 35)], EDGE)
    chart_marker(s, p, 61.4, 25, 3.2, EDGE)
    badge(s, "check", 61.4, 0, 46, 13)
