from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import chart_line, laptop, rule

DESCRIPTION = "A code editor shows an arrow from uneven source lines to neatly aligned code blocks."


def draw(s):
    point = laptop(s, 126, 79)
    for x in (13, 75):
        chart_line(s, point, [(x + 6, 66), (x, 62), (x + 6, 58)], EDGE)
        chart_line(s, point, [(x + 12, 66), (x + 18, 62), (x + 12, 58)], EDGE)
    for row, x, width in ((50, 17, 22), (42, 25, 21), (34, 15, 27), (26, 31, 12)):
        rule(s, point, x, row, width, EDGE)
    for row, x, width in ((50, 79, 33), (42, 86, 20), (34, 86, 24), (26, 79, 33)):
        rule(s, point, x, row, width, EDGE)
    chart_line(s, point, [(80, 46), (80, 30)], DETAIL)
    glyph(s, "arrow", 59, 0, 42, 12)
