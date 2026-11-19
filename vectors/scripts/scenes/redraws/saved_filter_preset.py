from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import attached_panel, front_surface

DESCRIPTION = "A filter panel with two slider settings carries a folded bookmark ribbon at the upper-right edge."


def bookmark(face, u, top, *, width=15, length=24):
    """Fold a real ribbon over the upper edge of a control."""
    tab = attached_panel(face, 1.7)
    tab.slab([(u, top), (u + width, top), (u + width, top - length),
              (u + width/2, top - length + 5), (u, top - length)], 2, BOLD)
    tab.rows(u + 2.8, top - 4, (width - 5.6,))


def draw(s):
    panel = front_surface(s, angle=-23, z=8, lean=.23)
    panel.slab(rounded(0, 0, 91, 58, 7), 8)
    panel.outline([(11, 44), (34, 44), (26, 32), (26, 22),
                   (20, 19), (20, 32)], EDGE)
    panel.line([(41, 13), (41, 45)])
    knob = attached_panel(panel, 1)
    for x, v, track in ((56, 37, 16), (69, 19, 30)):
        panel.rows(49, v, (track,), ink=EDGE)
        knob.slab(rounded(x - 3, v - 5, 6, 10, 2), 2)
    bookmark(panel, 70, 61)
