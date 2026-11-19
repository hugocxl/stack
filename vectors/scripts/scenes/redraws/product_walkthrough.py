from geometry import EDGE
from scenes.redraws._w4 import attached_panel, dashboard_chart, product_window

DESCRIPTION = "A large cursor touches the highlighted control above the chart in a desktop product window."


def draw(s):
    screen = product_window(s)
    dashboard_chart(screen, 35, 11, 34, 31)
    screen.frame(75, 35, 22, 13, 6, EDGE)
    screen.rows(81, 41.5, (10,), ink=EDGE)
    pointer = attached_panel(screen)
    pointer.slab([(89, 39), (107, 26), (99, 24), (104, 15),
                  (99, 13), (94, 22), (88, 17)], 3)
