from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A disk drive has a full capacity bar with calibration ticks and an exclamation badge."


def draw(s):
    s.box(0, 0, 0, 86, 54, 24, 4)
    s.ellipse(37, 28, 24, 23, 20, EDGE)
    s.disk(37, 28, 24, 5, 5, 2, EDGE)
    s.line([(53, 39, 24), (67, 44, 24), (70, 37, 24)], EDGE)
    front = Surface(s, (0, 54, 0))
    front.frame(9, 5, 67, 13, 2, EDGE)
    front.line([(12, 13), (73, 13)], BOLD)
    for x in (12, 24, 36, 49, 61, 73):
        front.line([(x, 6), (x, 10)], EDGE)
    badge(s, "exclaim", 87, 7, 24, 14)
