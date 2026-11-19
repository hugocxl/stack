from geometry import EDGE
from scenes.redraws._w4 import dashboard_chart, link_emblem, product_window

DESCRIPTION = "A desktop dashboard with a chart and summary rail has a chain-link symbol in its header."


def draw(s):
    face = product_window(s)
    dashboard_chart(face, 35, 11, 43, 35)
    for v in (13, 32):
        face.frame(83, v, 15, 14, 2, EDGE)
        face.rows(86, v + 7, (9,))
    link_emblem(face, 87, 60, 11)
