from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two fading position outlines trail a moving tile marked with a slash badge."


def draw(s):
    outline = rounded(0, 0, 44, 44, 7)
    rise, back = (-.22, .98), (0, -.98, -.22)
    for x, ink in ((0, DETAIL), (15, EDGE)):
        ghost = Surface(s, (x, 0, 2), rise=rise, back=back)
        ghost.stroke(outline, ink, closed=True, dashed=True)
    tile = Surface(s, (30, 0, 2), rise=rise, back=back)
    tile.plate(outline, 7)
    badge(s, "slash", *tile.point(39, 37, -2), 14)
