from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, printed_glyph

DESCRIPTION = "An admission ticket with notched ends and a perforated stub carries a clock badge."


def draw(s):
    ticket = front_surface(s, angle=-23, z=5, lean=.45)
    ticket.slab([(0, 6), (6, 0), (66, 0), (70, 5), (74, 0), (96, 0), (102, 6),
                 (102, 17), (96, 20), (94, 24), (96, 28), (102, 31), (102, 42),
                 (96, 48), (74, 48), (70, 43), (66, 48), (6, 48), (0, 42),
                 (0, 31), (6, 28), (8, 24), (6, 20), (0, 17)], 5)
    ticket.line([(70, 8), (70, 40)], EDGE, dashed=True)
    printed_glyph(ticket, "star", 24, 24, 15, EDGE)
    ticket.rows(41, 29, (17, 12), step=-9)
    ticket.rows(81, 28, (10, 10), step=-8)
    badge(s, "clock", *ticket.at(98, 44), 14)
