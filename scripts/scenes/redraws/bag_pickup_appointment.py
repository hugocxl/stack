from geometry import EDGE, oval
from scenes.redraws._w5 import luggage, panel, rect

DESCRIPTION = "An upright suitcase carries a hanging luggage tag with a calendar on its face."


def draw(s):
    luggage(s)
    s.tube([(30, 10, 67), (38, 13, 64), (47, 21, 56)], .9)
    face = lambda x, z: (x, 23, z)
    outline = [(37, 52), (45, 58), (56, 58), (62, 52),
               (62, 30), (60, 28), (37, 28), (35, 30), (35, 50)]
    panel(s, outline, face, 2.2)
    s.line([face(a, z) for a, z in oval(47, 54, 1.6, 1.6, count=20)], EDGE)
    rect(s, face, 39.5, 33, 18, 16, 1.7)
    s.line([face(40, 43), face(57, 43)], EDGE)
    for x in (44, 53):
        s.line([face(x, 46), face(x, 50)], EDGE)
        s.line([face(x - 1.2, 38), face(x + 1.2, 38)], EDGE)
