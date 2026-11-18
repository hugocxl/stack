from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import paper, wrench_mark

DESCRIPTION = "A notched repair ticket bears a wrench emblem above a partially completed segmented progress strip."


def draw(s):
    ticket = paper(s, 80, pitch=.78, run=.56, angle=9, depth=5)
    ticket.slab([(0, 0), (94, 0), (94, 24), (87, 29), (87, 35), (94, 40),
                 (94, 80), (0, 80), (0, 40), (7, 35), (7, 29), (0, 24)], 5)
    wrench_mark(ticket, 29, 28, .69)
    ticket.rows(54, 25, (26,), ink=EDGE)
    ticket.rows(54, 34, (19,))
    ticket.frame(12, 53, 70, 14, 3, EDGE)
    for x in (29.5, 47, 64.5):
        ticket.line([(x, 53), (x, 67)], DETAIL)
    for x in (15, 32.5):
        ticket.rows(x, 60, (11.5,), ink=BOLD)
