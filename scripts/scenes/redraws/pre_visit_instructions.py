from geometry import EDGE
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "An appointment instructions clipboard has a calendar heading above three checked instructions."


def draw(s):
    page = clinic_clipboard(s)
    page.frame(12, 24, 22, 18, 2, EDGE)
    page.line([(12, 30), (34, 30)], EDGE)
    for u in (17, 29):
        page.line([(u, 22), (u, 27)], EDGE)
    page.rows(40, 31, (17, 13), step=6)
    for v, n in ((53, 33), (66, 27), (79, 32)):
        printed_glyph(page, "check", 18, v, 7, EDGE, down=True)
        page.rows(28, v, (n,), ink=EDGE)
