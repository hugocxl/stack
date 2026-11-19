from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import attached_panel, front_surface

DESCRIPTION = "A diagonal outgoing arrow crosses the upper-right corner of a thick browser window."


def browser(s, width, height, *, angle=-25, lean=.18, depth=6):
    """Draw a browser window with a shared chrome rail and return its surface."""
    window = front_surface(s, z=depth, angle=angle, lean=lean)
    window.slab(rounded(0, 0, width, height, 5), depth)
    window.rows(0, height - 13, (width,), ink=EDGE)
    for x in (9, 16, 23):
        window.oval(x, height - 6.5, 1.2, 1.2, EDGE)
    return window


def draw(s):
    window = browser(s, 78, 62)
    window.rows(12, 34, (32, 25, 28), step=-9)
    pointer = attached_panel(window, 4)
    pointer.slab([(49, 47), (70, 68), (59, 68), (59, 77), (87, 77),
                  (87, 49), (78, 49), (78, 60), (57, 39)], 3, BOLD)
