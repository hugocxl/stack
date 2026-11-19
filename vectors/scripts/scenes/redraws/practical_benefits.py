from geometry import EDGE
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "A clipboard shows three large checkmarks alongside short benefit lines."


def draw(s):
    sheet = clinic_clipboard(s)
    for row, width in ((31, 32), (53, 27), (75, 34)):
        printed_glyph(sheet, "check", 19, row, 10, EDGE, down=True)
        sheet.rows(30, row - 1, (width,), ink=EDGE)
