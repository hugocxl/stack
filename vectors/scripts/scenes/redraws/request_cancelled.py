from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A perforated request ticket carries an X badge on its detachable stub."


def request_ticket(s):
    face = Surface(s, (36, 0, 1), lean=.40, side=True)
    left = oval(0, 25, 7, 7, 90, -90, 16)
    right = oval(92, 25, 7, 7, -90, -270, 16)
    face.plate([(0, 0), (92, 0), *right, (92, 50), (0, 50), *left], 4)
    face.line([(68, 3), (68, 47)], EDGE, dashed=True)
    face.frame(12, 29, 39, 7)
    face.line([(13, 20), (51, 20)])
    face.line([(13, 13), (42, 13)])
    return face


def draw(s):
    ticket = request_ticket(s)
    badge(s, "x", *ticket.point(87, 46), 13)
