from geometry import BOLD, EDGE
from scenes.redraws._w4 import bezier_path, nav_path, nav_phone

DESCRIPTION = "A curved back arrow loops from the bottom of a navigation history list to an earlier visited row."


def draw(s):
    face = nav_phone(s, width=77, height=94, angle=-15)
    face.line([(15, 28), (15, 66)])
    for v, width in ((66, 24), (47, 19), (28, 23)):
        face.oval(15, v, 2.5, 2.5, EDGE)
        face.rows(24, v, (width,), ink=EDGE)
        face.rows(24, v - 6, (width*.67,))
    nav_path(face, bezier_path((49, 24), ((76, 21), (78, 68), (50, 66))), BOLD, head=8)
