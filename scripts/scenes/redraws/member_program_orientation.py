from geometry import EDGE
from scenes.redraws._w3 import book
from scenes.redraws.introduction_buddy import avatar

DESCRIPTION = "A bound orientation booklet shows three profile pictograms above a short list of three steps."


def draw(s):
    face = book(s, w=72, h=77, depth=10)
    for x, v, size in ((29, 55, 13), (55, 55, 13), (42, 53, 17)):
        avatar(face, x, v, size)
    for v, length in ((35, 33), (25, 27), (15, 31)):
        face.oval(21, v, 1.8, 1.8, EDGE)
        face.rules(28, v, [length])
