from scenes.redraws._kit import badge
from scenes.redraws.empty_inbox import inbox_tray

DESCRIPTION = "A large check badge sits in the center of an open task inbox tray."


def draw(s):
    floor = inbox_tray(s)
    x, y, z = floor.point(40, 20)
    badge(s, "check", x, y, z + 15, 21)
