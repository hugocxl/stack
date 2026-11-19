from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.museum_collection_loan import ring_sculpture

DESCRIPTION = "An angled gallery label shows a ring sculpture thumbnail above three lines of curatorial notes."


def draw(s):
    s.face([(8, -19, 0), (65, -19, 0), (65, 11, 43), (8, 11, 43)])
    label = Surface(s, (0, 51, 2), rise=(-.72, .69), back=(0, -.69, -.72))
    label.plate(rounded(0, 0, 73, 70, 3), 6)
    label.rect(17, 30, 39, 32, 2)
    ring_sculpture(label, 36.5, 45, 25)
    label.rules(13, 24, [38], ink=EDGE)
    label.rules(13, 16, [47, 31], gap=7)
