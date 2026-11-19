from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A recessed interface slot contains a dashed placeholder with a sun and mountain outline."


def draw(s):
    slot = Surface(s, (0, 0, 0), rise=(-.43, .9), back=(0, -.9, -.43),
                   across=(.98, -.2))
    outline = rounded(0, 0, 98, 67, 7)
    opening = rounded(10, 9, 78, 49, 5)
    slot.plate(outline, 9)
    s.layers.pop()
    s.face([slot.point(*p, 5) for p in opening], EDGE)
    s.face([slot.point(*p) for p in outline], EDGE,
           openings=[[slot.point(*p) for p in opening]])
    slot.stroke([(20, 17), (78, 17), (78, 49), (20, 49), (20, 17)],
                EDGE, dashed=True)
    slot.stroke([(27, 23), (39, 36), (48, 28), (58, 39), (72, 23)], EDGE)
    slot.oval(69, 39, 3, 3, EDGE)
