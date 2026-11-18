from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A punch-clock time card shows stamped rows and a boxed hours tally at its foot."


def draw(s):
    s.box(0, 0, 0, 67, 30, 39, 4)
    front = Surface(s, (0, 30, 0))
    front.rect(8, 6, 51, 21, 3, DETAIL)
    front.oval(33, 16.5, 8.5, 8.5, EDGE)
    printed_glyph(front, "clock", 33, 16.5, 7.5)
    s.line([(9, 11, 39), (58, 11, 39), (58, 18, 39), (9, 18, 39), (9, 11, 39)], EDGE)
    card = Surface(s, (0, 18, 39), rise=(-.16, .98), back=(0, -.98, -.16))
    card.plate(rounded(11, 0, 45, 66, 2), 2)
    card.rules(16, 56, [31], ink=EDGE)
    for v in (45, 37, 29):
        card.rules(16, v, [13])
        card.rules(37, v, [12], ink=EDGE)
    card.rect(16, 6, 34, 16, 2, EDGE)
    for x in (26, 30, 34, 38):
        card.stroke([(x, 10), (x, 18)], EDGE)
    card.stroke([(23, 11), (41, 17)], BOLD)
