from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A printed checkout receipt emphasizes its percentage tax row immediately above the total."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.53, .85), back=(0, -.85, -.53))
    teeth = [(x, 3 if x % 12 == 0 else 0) for x in range(0, 61, 6)]
    face.plate([*teeth, (60, 87), (0, 87)], 2)
    face.rules(8, 77, [31], ink=EDGE)
    for v, width in ((64, 28), (55, 20), (46, 25)):
        face.rules(8, v, [width])
        face.rules(44, v, [8])
    face.rect(4, 23, 52, 15, 2, EDGE)
    face.stroke([(10, 26), (21, 35)], BOLD)
    face.oval(12, 33, 1.8, 1.8, BOLD)
    face.oval(19, 28, 1.8, 1.8, BOLD)
    face.rules(26, 31, [10], ink=EDGE)
    face.rules(43, 31, [8], ink=BOLD)
    face.rules(8, 14, [17], ink=EDGE)
    face.rules(39, 14, [12, 12], gap=4, ink=BOLD)
