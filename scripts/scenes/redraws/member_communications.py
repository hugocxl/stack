from geometry import BOLD, EDGE
from scenes.redraws._w3 import photo_art, sheet

DESCRIPTION = "A folded association newsletter has a wide masthead, an illustrated lead story and a short second item."


def draw(s):
    face = sheet(s, w=85, h=84, rise=(-.56, .83), depth=5)
    face.rules(8, 71, [57], ink=BOLD)
    face.rules(8, 64, [69], ink=EDGE)
    photo_art(face, 8, 35, 32, 23)
    face.rules(46, 55, [28], ink=EDGE)
    face.rules(46, 47, [28, 22], gap=6)
    face.rules(8, 28, [69])
    face.rules(8, 20, [35], ink=EDGE)
    face.rules(8, 13, [65, 48], gap=6)
