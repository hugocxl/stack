from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import book, component_art

DESCRIPTION = "An inward arrow meets the cover of a bound design library embossed with four component diamonds."


def draw(s):
    cover = book(s, 71, 83, 14)
    cover.rect(15, 14, 44, 55, 3, EDGE)
    for x, v in ((27, 29), (47, 29), (27, 53), (47, 53)):
        component_art(cover, x, v, 14, 16, EDGE)
    badge(s, "down", *cover.point(59, 85, -7), 13)
