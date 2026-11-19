from geometry import EDGE, rounded
from scenes.redraws._w4 import Surface, printed_glyph

DESCRIPTION = "A visitor sign-in sheet rests on the angled writing surface of a reception desk."


def draw(s):
    s.box(0, 0, 0, 96, 46, 32, 4)
    s.box(-3, -4, 30, 102, 54, 6, 4)
    s.box(0, 0, 36, 96, 9, 12, 2)
    s.box(0, 8, 36, 8, 34, 12, 2)
    s.line([(13, 46, 24), (82, 46, 24)], EDGE)
    s.line([(27, 46, 10), (68, 46, 10)])
    # The tilted surface forms a ledge that supports the sheet.
    s.face([(25, 39, 36), (68, 39, 36), (68, 12, 51), (25, 12, 51)])
    s.face([(68, 39, 36), (68, 12, 51), (68, 12, 36)])
    page = Surface(s, lambda u, v: (u, 40 - v, 37 + .55*v))
    page.slab(rounded(29, 4, 35, 23, 2), 1.4)
    page.rows(34, 21, (21,), ink=EDGE)
    for v in (13, 8):
        page.rows(35, v, (23,))
    printed_glyph(page, "check", 37, 15, 3, EDGE)
