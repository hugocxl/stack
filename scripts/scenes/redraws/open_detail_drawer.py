from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import attached_panel, desktop_display

DESCRIPTION = "A right-hand detail drawer slides out beside a selected profile row on a desktop display."


def draw(s):
    screen = desktop_display(s, width=123, height=82, angle=-32)
    screen.rows(11, 67, (33,), ink=EDGE)
    screen.line([(6, 60), (117, 60)], EDGE)
    for v, width in ((52, 26), (37, 30), (22, 22)):
        screen.frame(12, v - 5, 7, 8, 1, EDGE)
        screen.rows(24, v - 1, (width,), ink=EDGE)
    screen.frame(8, 29, 60, 15, 2, BOLD)

    drawer = attached_panel(screen, 3)
    drawer.slab(rounded(62, 12, 51, 43, 3), 3)
    drawer.line([(67, 29), (67, 37)], EDGE)
    drawer.frame(75, 33, 12, 13, 2, EDGE)
    drawer.rows(92, 43, (14,), ink=EDGE)
    drawer.rows(92, 37, (10,))
    drawer.line([(75, 28), (105, 28)])
    drawer.rows(75, 21, (24,), ink=EDGE)
