from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import browser_page, chart_marker, outline, section

DESCRIPTION = "A tall browser page has a ticked scroll-depth ruler with one drop-off marker."


def draw(s):
    p = browser_page(s, 72, 112, depth=15)
    outline(s, 10, 0, 57, 33, 24, 2, EDGE)
    s.line([p(14, 62), p(23, 73), p(29, 67), p(34, 72), p(40, 63)], DETAIL)
    section(s, p, 10, 90, (34,))
    section(s, p, 10, 47, (33, 27, 30))
    section(s, p, 10, 19, (33, 27))
    s.line([p(56, 85), p(56, 14)], EDGE)
    for z in (19, 31, 43, 55, 67, 79):
        s.line([p(56, z), p(62, z)], DETAIL)
    chart_marker(s, p, 56, 42, 5.5, BOLD)
