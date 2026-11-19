from geometry import BOLD, EDGE
from scenes.redraws._w4 import nav_path, standing_card

DESCRIPTION = "Two inward arrowheads beside five compact list rows indicate vertical compression."


def draw(s):
    face = standing_card(s, 103, 76, angle=0, lean=.44, depth=8)
    for v, width in ((56, 47), (47, 36), (38, 45), (29, 39), (20, 46)):
        face.oval(13, v, 1.3, 1.3, EDGE)
        face.rows(20, v, (width,), ink=EDGE)
    nav_path(face, [(84, 68), (84, 44)], BOLD, head=8)
    nav_path(face, [(84, 8), (84, 32)], BOLD, head=8)
    face.rows(79, 38, (10,))
