from scenes.redraws._kit import badge
from scenes.redraws.request_cancelled import request_ticket

DESCRIPTION = "A request ticket with a perforated stub carries a circular retry arrow."


def draw(s):
    ticket = request_ticket(s)
    badge(s, "refresh", *ticket.point(87, 46), 16)
