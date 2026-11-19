from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import dashboard_chart, product_window

DESCRIPTION = "A desktop product preview shows a chart and activity rows, with a play badge at the upper corner."


def draw(s):
    screen = product_window(s)
    dashboard_chart(screen, 36, 12, 37, 34)
    for v in (16, 27, 38):
        screen.oval(80, v, 1.15, 1.15, EDGE)
        screen.rows(84, v, (12,))
    badge(s, "play", *screen.at(104, 67), 15)
