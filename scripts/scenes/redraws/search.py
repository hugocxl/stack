from geometry import EDGE
from scenes.redraws._w4 import nav_window, raised_lens, search_control

DESCRIPTION = "An open magnifier rests over the search field of a single browser window."


def draw(s):
    face = nav_window(s, height=74)
    face.rows(16, 49, (36,), ink=EDGE)
    search_control(face, 13, 24, 72, 17, query=23, icon=False)
    face.rows(16, 13, (40,))
    raised_lens(face, 75, 32, 20)
