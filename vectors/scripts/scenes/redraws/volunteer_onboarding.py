from geometry import EDGE
from scenes.redraws._w3 import desk_calendar, printed_check, printed_glyph

DESCRIPTION = "A ring-bound volunteer checklist has a heart-marked name badge in its header and three checked rows."


def draw(s):
    page = desk_calendar(s, w=80, h=86)
    page.rect(17, 62, 45, 13, 2.5, EDGE)
    printed_glyph(page, "heart", 26, 69, 5.5)
    page.rules(34, 69, [21], ink=EDGE)
    for v, width in ((44, 32), (31, 28), (18, 34)):
        printed_check(page, 18, v, 6.5)
        page.rules(31, v, [width], ink=EDGE)
