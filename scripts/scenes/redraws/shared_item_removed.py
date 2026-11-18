from scenes.redraws._kit import badge
from scenes.redraws.replace_file_failed import file_page
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A folded document has an outward-arrow sharing tab with an X badge at its outer corner."


def draw(s):
    tab = Surface(s, (0, -2, 0), lean=.29)
    tab.plate([(44, 30), (85, 30), (89, 34), (89, 52), (85, 56), (44, 56)], 3)
    tab.arrow([(60, 38), (60, 41), (63, 44), (76, 44)], head=6)
    page = file_page(s)
    for z, width in ((45, 24), (34, 34), (24, 26)):
        page.line([(11, z), (11 + width, z)])
    badge(s, "x", *tab.point(91, 56), 11)
