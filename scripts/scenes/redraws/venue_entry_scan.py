from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface, ticket_outline

DESCRIPTION = "A freestanding barcode reader projects a scan line across an admission ticket held under its hood."


def draw(s):
    s.box(13, 0, 0, 60, 53, 9, 4)
    s.box(21, 2, 8, 44, 16, 62, 3)
    s.box(14, 0, 68, 59, 39, 22, 5)
    head = Surface(s, (13, 39, 68))
    head.rect(10, 5, 40, 12, 4, EDGE)
    head.rules(22, 11, [14], ink=EDGE)

    ticket = Surface(s, (0, 73, 15), rise=(-.50, .86), back=(0, -.86, -.50))
    ticket.plate([(x * .82, v * .77) for x, v in ticket_outline()], 2.5)
    ticket.stroke([(60.7, 5), (60.7, 32)], EDGE, dashed=True)
    ticket.rules(10, 27, [35, 25], gap=8)
    for x in (66, 70, 75, 79):
        ticket.stroke([(x, 9), (x, 29)], EDGE)
    ticket.stroke([(4, 18), (79, 18)], BOLD)
    s.line([head.point(22, 5), ticket.point(5, 18)], dashed=True)
    s.line([head.point(36, 5), ticket.point(79, 18)], dashed=True)
