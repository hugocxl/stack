from geometry import BOLD, EDGE, rounded
from scenes.redraws._w1 import chain_links
from scenes.redraws._w3 import Surface, component_art

DESCRIPTION = "A thick component tile carries a pair of closed, interlocking chain links at its upper-right corner."


def draw(s):
    tile = Surface(s, (0, 0, 0), rise=(-.48, .88), back=(0, -.88, -.48),
                   across=(.96, -.28))
    tile.plate(rounded(0, 0, 72, 65, 8), 9)
    component_art(tile, 34, 29, 38, 34, BOLD)

    # A solid clasp behind the hardware keeps the tile out of the link openings.
    clasp = Surface(s, tile.point(70, 59, -4))
    place = clasp.viewer_axes(0, 0)
    clasp.plate([place(x, z) for x, z in rounded(-22, -13, 44, 26, 9)], 3, EDGE)
    chain_links(s, *clasp.point(0, 0, -1), scale=.49)
