from geometry import rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, design_layer, photo_art, selection_handle

DESCRIPTION = "An arrow points out from the selected artwork tile on a tilted design canvas."


def draw(s):
    canvas = design_layer(s)
    tile = Surface(s, canvas.point(21, 18, -3), rise=canvas.rise, back=canvas.back)
    tile.plate(rounded(0, 0, 43, 29, 2), 3)
    photo_art(tile, 4, 4, 35, 21)
    for x, v in ((0, 0), (43, 0), (0, 29)):
        selection_handle(tile, x, v, 5)
    badge(s, "arrow", *tile.point(50, 32, -4), 13)
