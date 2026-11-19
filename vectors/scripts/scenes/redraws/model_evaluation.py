from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, model_layers, upright_face

DESCRIPTION = "A model score gauge points past its marked pass threshold and carries a check badge beside the score."


def draw(s):
    def p(x, z):
        return .79*x, -.21*x, z

    base = [(0, 0), (105, 0), (105, 21)]
    base += oval(52.5, 21, 52.5, 51, start=0, end=180, count=50)[1:]
    upright_face(s, p, base, 15)
    chart_line(s, p, oval(52.5, 23, 39, 37, start=12, end=170), EDGE)
    chart_line(s, p, oval(52.5, 23, 32, 30, start=12, end=65), EDGE)
    for degrees in (35, 65, 95, 125, 155):
        angle = radians(degrees)
        tick = [(52.5 + r*cos(angle), 23 + r*sin(angle)) for r in (42, 49)]
        chart_line(s, p, tick, EDGE if degrees == 65 else DETAIL)
    chart_line(s, p, [(52.5, 23), (80, 45)], EDGE)
    model_layers(s, p, 52.5, 7, 2)
    badge(s, "check", *p(105, 37), 14)
