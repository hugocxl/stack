from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A notched queue ticket has a perforated stub and an attached clock badge."


def draw(s):
    ticket = front_surface(s, angle=-22, z=6, lean=.66)
    outline = [(0, 8), (5, 4), (10, 7), (15, 4), (20, 7), (25, 4),
               (30, 7), (35, 4), (40, 7), (45, 4), (50, 8), (50, 26),
               (46, 29), (46, 35), (50, 38), (50, 77), (46, 81), (4, 81),
               (0, 77), (0, 38), (4, 35), (4, 29), (0, 26)]
    ticket.slab(outline, 6)
    ticket.line([(7, 32), (43, 32)], EDGE, dashed=True)
    ticket.frame(9, 46, 32, 22, 2, EDGE)
    ticket.rows(15, 60, (20,), ink=EDGE)
    ticket.rows(16, 52, (14,))
    ticket.rows(11, 19, (20,))
    badge(s, "clock", *ticket.at(46, 77), 13)
