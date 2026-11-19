from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, component_art

DESCRIPTION = "One thick component tile carries a publish badge with an upward arrow on its corner."


def draw(s):
    tile = Surface(s, (0, 0, 0), rise=(-.48, .88), back=(0, -.88, -.48), across=(.96, -.28))
    tile.plate(rounded(0, 0, 72, 65, 8), 9)
    component_art(tile, 36, 32, 38, 34, EDGE)
    badge(s, "up", *tile.point(70, 60, -4), 15)
