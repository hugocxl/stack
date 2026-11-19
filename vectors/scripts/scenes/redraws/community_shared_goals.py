from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Three tabbed member passes sit inside a thick progress ring with one unfinished segment."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.36, 1), back=(0, -1, -.36))
    outer = oval(0, 0, 48, 48, 70, 390, 72)
    inner = oval(0, 0, 39, 39, 390, 70, 72)
    face.plate(outer + inner, 8)
    face.stroke(oval(0, 0, 43.5, 43.5, 30, 70, 12), EDGE, dashed=True)

    for x, v, width, height in ((-26, -10, 20, 26), (6, -10, 20, 26), (-12, -17, 24, 33)):
        face.plate(rounded(x, v, width, height, 3), 2)
        face.rules(x + width * .33, v + height - 6, [width * .34], ink=BOLD)
        face.rules(x + width * .25, v + 10, [width * .50])
