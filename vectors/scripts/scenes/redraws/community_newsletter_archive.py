from geometry import EDGE, rounded
from scenes.editorial_objects import archive
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A folded newsletter with a masthead and story columns protrudes from a slotted archive box."


def draw(s):
    archive(s)
    lid = Surface(s, (0, 47, 31), rise=(-1, 0), back=(0, 0, -1))
    lid.rect(4, 13, 46, 7, 2, EDGE)

    paper = Surface(s, (6, 30, 31), rise=(-.30, 1), back=(0, -1, -.30))
    paper.plate(rounded(0, 0, 42, 46, 2), 3)
    paper.rules(5, 38, [32], ink=EDGE)
    paper.rules(5, 33, [32])
    photo_art(paper, 5, 13, 14, 15)
    paper.rules(23, 26, [14, 12, 14, 10], gap=4)
    paper.rules(5, 8, [30])
