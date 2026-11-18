from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "Three overlapping page proofs repeat a ready-made layout with a heading, an image slot, and text rows."


def draw(s):
    for x, y, z in ((-22, -9, 13), (-11, -4, 6), (0, 0, 0)):
        face = Surface(s, (x, y, z), rise=(-.35, .94), back=(0, -.94, -.35))
        face.plate(rounded(0, 0, 70, 84, 3), 4)
        face.rules(8, 74, [32], ink=EDGE)
    photo_art(face, 8, 34, 54, 30)
    face.rules(8, 25, [49, 43, 47], gap=8, ink=EDGE)
