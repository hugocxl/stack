from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import desktop_display, printed_glyph

DESCRIPTION = "A heart beside the vertical axis identifies the continuous pulse trace on a desktop monitor."


def draw(s):
    chart = desktop_display(s, width=111, height=66, angle=-24)
    chart.line([(29, 52), (29, 12), (98, 12)], EDGE)
    for v in (24, 36, 48):
        chart.line([(26, v), (29, v)], DETAIL)
    printed_glyph(chart, "heart", 17, 38, 11, EDGE)
    chart.line([(33, 26), (42, 26), (49, 36), (54, 21), (63, 50),
                (70, 34), (77, 34), (82, 40), (88, 30), (98, 38)], BOLD)
