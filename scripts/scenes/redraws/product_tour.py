from geometry import EDGE
from scenes.redraws._w4 import attached_panel, dashboard_chart, product_window

DESCRIPTION = "A desktop product window shows a tour popover pointing to the first sidebar control."


def draw(s):
    screen = product_window(s)
    dashboard_chart(screen, 67, 12, 30, 27)
    screen.frame(8, 38, 16, 10, 3, EDGE)
    panel = attached_panel(screen, 8)
    panel.slab([(25, 50), (61, 50), (64, 47), (64, 23), (61, 20),
                (25, 20), (22, 23), (22, 37), (17, 43), (22, 44), (22, 47)], 4)
    panel.rows(30, 42, (30,), ink=EDGE)
    panel.rows(30, 36, (24,))
    for u, radius in ((33, 2.5), (42, 1.4), (51, 1.4)):
        panel.oval(u, 28, radius, radius, EDGE)
