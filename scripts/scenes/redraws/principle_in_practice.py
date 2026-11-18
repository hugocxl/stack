from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import clinic_clipboard

DESCRIPTION = "A procedure clipboard singles out the completed instruction with a check badge."


def draw(s):
    sheet = clinic_clipboard(s)
    sheet.rows(12, 24, (34,), ink=EDGE)
    for row, width in ((40, 30), (58, 26), (76, 31)):
        sheet.frame(12, row - 4, 8, 8, 1, EDGE)
        sheet.rows(26, row - 2, (width, width - 8), step=5, ink=DETAIL)
    sheet.frame(8, 51, 54, 15, 2, EDGE)
    badge(s, "check", *sheet.at(66, 58), 14)
