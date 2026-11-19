from geometry import EDGE, rounded
from scenes.redraws.page_moved import Surface

DESCRIPTION = "An activity timeline has evenly spaced date ticks above a dashed event lane with no entries."


def draw(s):
    timeline = Surface(s, (0, 15, 2), lean=.63)
    timeline.plate(rounded(0, 0, 125, 49, 5), 6)
    timeline.line([(0, 29), (125, 29)], EDGE)
    for x in (17, 39, 62, 85, 108):
        timeline.line([(x, 29), (x, 36)], EDGE)
        timeline.line([(x - 3, 41), (x + 3, 41)])
        timeline.line([(x, 25), (x, 20)])
    timeline.line([(10, 13), (115, 13)], EDGE, dashed=True)
