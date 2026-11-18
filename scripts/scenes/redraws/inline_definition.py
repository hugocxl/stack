from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import attached_panel, nav_phone

DESCRIPTION = "A definition popover points to an underlined term in a text passage on a handheld reader."


def draw(s):
    page = nav_phone(s, width=94, height=103, angle=-12)
    page.rows(12, 89, (20,), ink=EDGE)
    page.rows(12, 40, (59, 52, 62), step=-8)
    page.rows(12, 16, (42,))
    page.rows(12, 50, (12,))
    page.rows(30, 50, (19,))
    page.rows(55, 50, (23,))
    page.rows(30, 45, (19,), ink=BOLD)

    popover = attached_panel(page, 3)
    outline = rounded(23, 59, 61, 25, 3)
    outline.extend(((34, 59), (40, 53), (48, 59)))
    popover.slab(outline, 2)
    popover.rows(31, 77, (25,), ink=EDGE)
    popover.rows(31, 70, (42, 36), step=-5.5)
