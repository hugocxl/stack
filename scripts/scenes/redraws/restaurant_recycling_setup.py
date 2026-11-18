from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import printed_stroke, rect

DESCRIPTION = "A two-compartment recycling station pairs a paper slot with a round container opening."


def draw(s):
    s.box(0, 0, 0, 65, 36, 40, 3)
    top = lambda x, y: (x, y, 49 - y * .22)
    s.face([(65, 0, 39), (65, 36, 39), top(65, 36), top(65, 0)])
    s.face([(0, 36, 39), (65, 36, 39), top(65, 36), top(0, 36)])
    s.face([top(x, y) for x, y in rounded(0, 0, 65, 36, 2)])
    rect(s, top, 6, 15, 22, 6, 2, EDGE)
    printed_stroke(s, top, oval(49, 17, 8, 8), EDGE)
    face = lambda x, z: (x, 36, z)
    printed_stroke(s, face, [(32, 3), (32, 41)], DETAIL)
    paper = [(9, 12), (23, 12), (23, 27), (19, 31), (9, 31), (9, 12)]
    printed_stroke(s, face, paper, EDGE)
    printed_stroke(s, face, [(19, 31), (19, 27), (23, 27)], EDGE)
    printed_stroke(s, face, [(12, 22), (20, 22)], DETAIL)
    printed_stroke(s, face, [(12, 17), (20, 17)], DETAIL)
    bottle = [(44, 12), (55, 12), (55, 24), (52, 27), (52, 32),
              (47, 32), (47, 27), (44, 24), (44, 12)]
    printed_stroke(s, face, bottle, EDGE)
    printed_stroke(s, face, [(44, 20), (55, 20)], DETAIL)
