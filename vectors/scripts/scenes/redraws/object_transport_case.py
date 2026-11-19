from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.museum_cabinet_label import faceted_sculpture

DESCRIPTION = "An open transport case holds a faceted sculpture in a foam recess cut to its shape."


def draw(s):
    lid = Surface(s, (0, 0, 15), rise=(-.22, .98), back=(0, -.98, -.22))
    lid.plate(rounded(0, 0, 75, 45, 5), 5)
    lid.rect(5, 5, 65, 35, 3)
    s.box(0, 0, 0, 75, 60, 15, 5)
    s.tube([(28, 60, 8), (28, 69, 8), (47, 69, 8), (47, 60, 8)], 2.1)

    foam = Surface(s, (0, 60, 15), rise=(-1, 0))
    foam.rect(5, 5, 65, 50, 3, EDGE)
    recess = [(15, 9), (56, 9), (58, 34), (34, 53), (15, 34)]
    foam.stroke(recess, EDGE, closed=True)
    foam.stroke([(16, 11), (55, 11), (57, 33)], DETAIL)
    faceted_sculpture(s, lambda u, v, n: (35 + u, 42 - .84 * v, 13 + .60 * n))
    for x in (15, 53):
        s.face([(x, 60.2, 14), (x + 7, 60.2, 14), (x + 7, 60.2, 8), (x, 60.2, 8)], EDGE)
