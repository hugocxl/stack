from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, audio_description_art

DESCRIPTION = "A film-frame tile pairs an eye with radiating sound waves."


def draw(s):
    tile = Surface(s, (0, 0, 0), rise=(-.41, .91), back=(0, -.91, -.41))
    tile.plate(rounded(0, 0, 107, 69, 6), 10)
    tile.rect(17, 8, 74, 53, 4, EDGE)
    for x in (5, 96):
        for v in (15, 31, 47):
            tile.rect(x, v, 6, 8, 1, EDGE)
    audio_description_art(tile, 50, 34, 33, BOLD)
