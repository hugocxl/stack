from scenes.redraws._kit import badge
from scenes.redraws._w4 import service_ticket

DESCRIPTION = "A workshop admission ticket bears a wrench emblem and a plus badge on its tear-off stub."


def draw(s):
    ticket = service_ticket(s, workshop=True)
    badge(s, "plus", *ticket.at(100, 35), 15)
