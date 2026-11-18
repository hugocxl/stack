from scenes.redraws._kit import badge
from scenes.redraws._w1 import tunnel_link

DESCRIPTION = "An x badge overlaps the midpoint of a flanged network tunnel."


def draw(s):
    tunnel_link(s)
    badge(s, "x", 0, -1, 25, 13)
