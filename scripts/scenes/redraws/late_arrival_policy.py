from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A notched reservation ticket carries a clock badge over its perforated stub."


def draw(s):
    ticket = front_surface(s, angle=-22, z=5, lean=.49)
    ticket.slab([(0, 4), (4, 0), (96, 0), (100, 4), (100, 17),
                 (94, 19), (92, 24), (94, 29), (100, 31), (100, 46),
                 (96, 50), (4, 50), (0, 46), (0, 31), (6, 29),
                 (8, 24), (6, 19), (0, 17)], 5)
    ticket.line([(73, 5), (73, 45)], EDGE, dashed=True)
    ticket.rows(20, 36, (39,), ink=EDGE)
    ticket.rows(20, 24, (30, 35), step=-8)
    badge(s, "clock", *ticket.at(91, 39), 13)
