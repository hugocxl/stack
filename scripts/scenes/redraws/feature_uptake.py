from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, laptop, outline, response_curve

DESCRIPTION = "A laptop’s cumulative adoption curve climbs below an enabled feature switch."


def draw(s):
    p = laptop(s, 125, 87)
    s.line([p(15, 76), p(15, 17), p(112, 17)], EDGE)
    curve = [(15 + x*.86, 22 + z*.65) for x, z in response_curve()]
    chart_line(s, p, curve, BOLD)
    outline(s, 85, 0, 72, 23, 10, 5, EDGE)
    chart_marker(s, p, 102, 77, 3.1, DETAIL)
    for x in (38, 61, 84, 107):
        s.line([p(x, 17), p(x, 13)], DETAIL)
