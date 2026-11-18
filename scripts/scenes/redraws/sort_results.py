from geometry import BOLD, EDGE
from scenes.redraws._w4 import nav_path, standing_card

DESCRIPTION = "Four bars increase in length down a results panel beside a downward sort arrow."


def draw(s):
    face = standing_card(s, 88, 81, angle=-16, lean=.41, depth=8)
    for v, width in ((60, 15), (46, 24), (32, 34), (18, 44)):
        face.frame(30, v, width, 5, 2.5, EDGE)
    nav_path(face, [(16, 64), (16, 18)], BOLD, head=10)
