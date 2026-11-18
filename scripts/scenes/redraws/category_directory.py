from geometry import EDGE
from scenes.redraws._w4 import folder_emblem, nav_thumbnail, standing_card

DESCRIPTION = "A directory card lists three categories beside a folder, a photo, and a document pictogram."


def draw(s):
    face = standing_card(s, 77, 95, angle=-29, lean=.40, depth=9)
    face.rows(10, 83, (37,), ink=EDGE)
    for v in (63, 40, 17):
        face.rows(33, v + 3, (29,), ink=EDGE)
        face.rows(33, v - 4, (20,))
    for v in (52, 29):
        face.line([(9, v), (68, v)])
    folder_emblem(face, 10, 55, 16, 14)
    nav_thumbnail(face, 10, 32, 16, 15)
    face.outline([(12, 9), (25, 9), (25, 21), (20, 26), (12, 26)], EDGE)
    face.line([(20, 26), (20, 21), (25, 21)], EDGE)
