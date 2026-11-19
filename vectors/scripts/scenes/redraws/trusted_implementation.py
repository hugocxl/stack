from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "A clipboard lists three implementation milestones and carries a check badge at the final row."


def draw(s):
    page = clinic_clipboard(s)
    for v, width in ((33, 32), (51, 24), (69, 21)):
        page.frame(13, v - 4, 8, 8, 1, EDGE)
        page.rows(28, v, (width,), ink=EDGE)
        if v != 69:
            printed_glyph(page, "check", 17, v, 4.5, down=True)
    badge(s, "check", *page.at(66, 72), 12.5)
