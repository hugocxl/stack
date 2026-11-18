from geometry import EDGE
from scenes.redraws._w4 import nav_window

DESCRIPTION = "A browser keeps its address bar above a dashed outline of the missing page."


def draw(s):
    face = nav_window(s, height=81, angle=-20)
    face.rows(39, 73, (36,), ink=EDGE)
    face.line([(19, 12), (91, 12), (91, 54), (19, 54), (19, 12)], EDGE, dashed=True)
