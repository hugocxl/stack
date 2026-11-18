from scenes.redraws._kit import warning
from scenes.redraws._w4 import service_ticket

DESCRIPTION = "A warning triangle marks the foremost ticket in a staggered stack of support tickets."


def draw(s):
    service_ticket(s, offset=-20)
    service_ticket(s, offset=-10)
    ticket = service_ticket(s)
    warning(s, *ticket.at(96, 22), size=37)
