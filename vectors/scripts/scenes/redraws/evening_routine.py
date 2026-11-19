from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import _strokes
from scenes.redraws._w4 import closed_book

DESCRIPTION = "A bedtime checklist notebook has a crescent moon in its header and three ordered checklist rows."


def printed_glyph(face, kind, u, v, radius, ink=EDGE, *, down=False):
    """Place a kit glyph on a surface with its own page coordinates."""
    scale = -1 if down else 1
    for stroke in _strokes(kind, radius):
        face.line([(u + x, v + scale*y) for x, y in stroke], ink)


def draw(s):
    page = closed_book(s, angle=-24, width=79, height=87, depth=10)
    printed_glyph(page, "moon", 25, 19, 12, BOLD, down=True)
    page.rows(42, 17, (23, 16), step=6)
    page.line([(14, 32), (68, 32)], DETAIL)
    for index, widths in enumerate(((39, 25), (33, 22), (41, 17))):
        v = 45 + 14*index
        page.frame(16, v - 4.5, 9, 9, 1.5, EDGE)
        page.rows(31, v - 2, widths, step=5)
        if index < 2:
            printed_glyph(page, "check", 20.5, v, 4.2, down=True)
