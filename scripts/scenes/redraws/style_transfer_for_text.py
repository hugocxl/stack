from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import chart_line, rule, upright_face

DESCRIPTION = "A comparison card pairs separate upright type strokes with flowing script strokes across a transition arrow."


def draw(s):
    def point(x, z):
        return x, 0, z

    upright_face(s, point, rounded(0, 0, 116, 59, 6), 9)
    for x, height, width in ((9, 17, 8), (21, 22, 9), (34, 14, 8)):
        chart_line(s, point, [(x, 25), (x + 2, 25), (x + 2, 25 + height),
                             (x + width, 25 + height), (x + width, 22 + height)], EDGE)
        rule(s, point, x + 2, 25, width - 2, EDGE)
    glyph(s, "arrow", 57, 0, 34, 11)
    script = [(71, 29), (76, 32), (81, 40), (84, 44), (88, 44), (90, 41),
              (89, 36), (83, 28), (79, 27), (77, 30), (79, 34), (83, 35),
              (88, 29), (91, 29), (98, 37), (101, 38), (103, 36), (101, 30),
              (104, 29), (109, 34)]
    chart_line(s, point, script, EDGE)
    for x, length in ((9, 31), (73, 32)):
        rule(s, point, x, 16, length, DETAIL)
