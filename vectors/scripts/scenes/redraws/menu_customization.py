from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import cloche_mark, panel, printed_stroke, rect

DESCRIPTION = "A single dish card lists three toppings, with a check on the middle option."


def draw(s):
    face = lambda x, z: (x, 8 - .48 * z, z)
    panel(s, rounded(0, 0, 68, 48, 3.7), face, 5)
    cloche_mark(s, face, 16, 30, 1)
    printed_stroke(s, face, [(7, 22), (25, 22)], DETAIL)
    printed_stroke(s, face, [(7, 16), (20, 16)], DETAIL)
    printed_stroke(s, face, [(31, 8), (31, 40)], DETAIL)
    toppings = (
        [(34, 35), (35, 38), (38, 39), (41, 38), (42, 35), (39, 35),
         (39, 32), (37, 32), (37, 35), (34, 35)],
        [(38, 28), (38, 26), (35, 26), (34, 23), (35, 20), (40, 20),
         (42, 23), (41, 26), (38, 26)],
        oval(38, 12, 3.6, 2.8, count=24),
    )
    for (z, w), topping in zip(((36, 8), (24, 8), (12, 6)), toppings):
        printed_stroke(s, face, topping, EDGE)
        printed_stroke(s, face, [(45, z), (45 + w, z)], DETAIL)
        if z != 24:
            rect(s, face, 56, z - 3.3, 7, 6.6, 1, EDGE)
    badge(s, "check", *face(59.5, 24), 5.2)
