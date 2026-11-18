from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import front_surface, printed_glyph

DESCRIPTION = "A release-note sheet has three bold version headings and individual change lines arranged along a timeline."


def draw(s):
    page = front_surface(s, angle=-22, z=5, lean=.52)
    page.slab([(0, 4), (4, 0), (63, 0), (67, 4), (67, 74),
               (50, 90), (4, 90), (0, 86)], 5)
    page.line([(50, 90), (50, 74), (67, 74)], EDGE)
    for v, width in ((69, 29), (48, 24), (27, 31)):
        page.oval(13, v, 3.1, 3.1, EDGE)
        page.rows(24, v, (width,), ink=BOLD)
        page.rows(24, v - 7, (width + 6,), ink=DETAIL)
    for hi, lo in ((66, 51), (45, 30), (24, 12)):
        page.line([(13, hi), (13, lo)], DETAIL)
    printed_glyph(page, "down", 13, 11, 5, EDGE)
