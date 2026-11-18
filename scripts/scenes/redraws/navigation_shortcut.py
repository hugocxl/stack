from geometry import BOLD, EDGE
from scenes.redraws._w4 import folder_emblem, nav_path, standing_card

DESCRIPTION = "A bent arrow bypasses the intermediate levels of a nested menu and lands on its deepest folder."


def draw(s):
    face = standing_card(s, 96, 82, angle=-31, lean=.16, depth=8)
    face.line([(15, 56), (15, 42), (24, 42)])
    face.line([(29, 36), (29, 25), (38, 25)])
    for u, v, width in ((10, 57, 22), (24, 39, 20), (38, 22, 20)):
        folder_emblem(face, u, v, 12, 11)
        face.rows(u + 17, v + 5, (width,), ink=EDGE)
    nav_path(face, [(54, 63), (86, 63), (86, 27), (77, 27)], BOLD, head=7)
