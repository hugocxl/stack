from scenes.redraws._kit import badge
from scenes.redraws._w4 import service_ticket

DESCRIPTION = "A notched support ticket bears a headset emblem and an upward arrow badge on its tear-off stub."


def draw(s):
    ticket = service_ticket(s)
    badge(s, "up", *ticket.at(100, 35), 16)
