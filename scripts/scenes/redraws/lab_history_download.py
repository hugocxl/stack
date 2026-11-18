from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws.lab_results import lab_report

DESCRIPTION = "A bound lab report lists past specimens beside date marks and carries a download badge."


def draw(s):
    page = lab_report(s)
    page.line([(15, 42), (71, 42)], EDGE)
    for v in (47, 59, 71):
        page.frame(17, v, 10, 7, 1, EDGE)
        page.line([(19, v + 2), (25, v + 2)], DETAIL)
        page.rows(33, v + 4, (32,), ink=EDGE)
        page.rows(15, v + 10, (55,))
    badge(s, "down", *page.at(84, 22), 17)
