from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A perforated reservation ticket has a bold check badge attached to its tear-off stub."


def draw(s):
    ticket = paper(s, 65, pitch=.74, run=.57, angle=-14, depth=5)
    outline = [(0, 0), (72, 0), (76, 6), (80, 0), (105, 0), (109, 4),
               (109, 24), (101, 29), (101, 36), (109, 41), (109, 61),
               (105, 65), (80, 65), (76, 59), (72, 65), (0, 65), (-4, 61),
               (-4, 41), (4, 36), (4, 29), (-4, 24), (-4, 4)]
    ticket.slab(outline, 5)
    ticket.line([(76, 7), (76, 59)], EDGE, dashed=True)
    ticket.rows(13, 16, (44,), ink=EDGE)
    ticket.rows(13, 28, (33, 44, 22), step=9)
    badge(s, "check", *ticket.at(100, 42), 15)
