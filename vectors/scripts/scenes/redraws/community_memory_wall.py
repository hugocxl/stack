from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A gallery story board mounts a framed photograph directly above its caption."


def draw(s):
    board = Surface(s, (0, 0, 0), rise=(-.39, .92), back=(0, -.92, -.39))
    board.plate(rounded(0, 0, 79, 84, 3), 11)
    board.rect(5, 5, 69, 74, 2)
    photo = Surface(s, (0, 2.7, .7), rise=board.rise, back=board.back)
    photo.plate(rounded(12, 35, 55, 38, 2), 2.5)
    photo_art(photo, 16, 39, 47, 30)
    board.rect(17, 11, 45, 16, 1.5, EDGE)
    board.rules(22, 22, [31, 22], gap=6)
