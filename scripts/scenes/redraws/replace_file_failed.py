from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A folded file with two opposing transfer arrows carries an X badge at its upper-right edge."

FILE_OUTLINE = [(0, 0), (57, 0), (57, 57), (39, 75), (0, 75)]
FOLD = [(39, 75), (39, 57), (57, 57)]


def file_page(s, origin=(0, 0, 0), *, side=False):
    page = Surface(s, origin, lean=.29, side=side)
    page.plate(FILE_OUTLINE, 4)
    page.line(FOLD, EDGE)
    return page


def draw(s):
    page = file_page(s)
    page.arrow([(12, 41), (43, 41)], EDGE, 8)
    page.arrow([(43, 25), (12, 25)], EDGE, 8)
    badge(s, "x", *page.point(58, 51), 12)
