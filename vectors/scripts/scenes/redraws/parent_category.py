from scenes.redraws._kit import badge
from scenes.redraws._sf import folder, screen

DESCRIPTION = "A small folder stands in front of its larger parent folder and carries an up badge."


def draw(s):
    at = screen()
    folder(s, lambda u, v: at(u - 58, v - 8), 84, 62)
    child = folder(s, lambda u, v: at(u - 10, v - 46), 64, 46)
    badge(s, "up", *child(64, 4), 12)
