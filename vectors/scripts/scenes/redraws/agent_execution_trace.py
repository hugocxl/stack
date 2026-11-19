from geometry import DETAIL, EDGE, oval
from scenes.redraws._w2 import card, magnifier


DESCRIPTION = "A magnifier singles out one step in a vertical execution trace."


def draw(s):
    card(s, 76, 86)
    rows = (69, 47, 25)
    for upper, lower in zip(rows, rows[1:]):
        s.line([(31, 0, upper - 4), (31, 0, lower + 4)], EDGE)
    for z in rows:
        s.line([(x, 0, h) for x, h in oval(31, z, 4, 4)], EDGE)
    s.line([(49, 0, 76), (55, 0, 69), (49, 0, 62)], EDGE)
    s.line([(59, 0, 62), (66, 0, 62)], EDGE)
    s.line([(49, 0, 47), (66, 0, 47)], DETAIL)
    s.line([(49, 0, 25), (64, 0, 25)], DETAIL)
    magnifier(s, 34, 3, 50, 14, direction=(-.6, -.8))
