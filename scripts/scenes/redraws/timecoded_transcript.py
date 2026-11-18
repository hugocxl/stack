from geometry import EDGE, oval, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import chart_line, rule, upright_face

DESCRIPTION = "A transcript binder has a clock above a timestamp column aligned with four lines of dialogue."


def draw(s):
    def point(x, z):
        return x, 0, z

    upright_face(s, point, rounded(0, 0, 88, 94, 5), 13)
    chart_line(s, point, [(6, 4), (6, 90)])
    chart_line(s, point, [(34, 12), (34, 83)], EDGE)
    chart_line(s, point, oval(22, 80, 7, 7, count=30), EDGE)
    glyph(s, "clock", 22, 0, 80, 6, EDGE)
    rule(s, point, 43, 79, 27, EDGE)
    for z, length in ((64, 32), (48, 27), (32, 34), (16, 25)):
        for x in (13, 24):
            rule(s, point, x, z, 6, EDGE)
        for offset in (-1.3, 1.3):
            rule(s, point, 21, z + offset, .8, EDGE)
        rule(s, point, 43, z, length, EDGE)
        rule(s, point, 43, z - 6, length*.71)
