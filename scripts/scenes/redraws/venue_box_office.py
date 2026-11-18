from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface, flat, ticket_outline

DESCRIPTION = "A box-office window has a service shelf and a perforated ticket projecting from its slot."


def draw(s):
    s.box(0, 0, 0, 104, 35, 34, 1)
    front = Surface(s, (0, 35, 0))
    s.face([(104, 0, 33), (104, 35, 33), (104, 35, 99), (104, 0, 99)])
    opening = [front.point(x, v) for x, v in ((10, 44), (93, 44), (93, 89), (10, 89))]
    frame = [front.point(x, v) for x, v in ((0, 32), (104, 32), (104, 98), (0, 98))]
    s.face(frame, openings=[opening])
    front.stroke([(60, 46), (60, 89)], EDGE)
    for x, v in ((22, 62), (72, 67)):
        front.stroke([(x, v), (x + 12, v + 17)], DETAIL)
    s.box(-2, -2, 94, 108, 41, 13, 1)
    s.box(-3, 27, 35, 110, 18, 6, 1)
    front.rect(26, 23, 53, 7, 3, EDGE)

    ticket = flat(s, 28, 60, 26)
    ticket.plate([(x * .47, v * .52) for x, v in ticket_outline()], 2)
    ticket.stroke([(34.8, 3), (34.8, 19)], EDGE, dashed=True)
    ticket.rules(8, 16, [19, 13], gap=6)
