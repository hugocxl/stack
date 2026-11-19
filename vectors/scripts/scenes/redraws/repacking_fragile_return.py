from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "An open shipping carton holds a stemmed glass upright in a fitted packing insert."


def draw(s):
    carton = (-32, 32, -25, 25, 27)
    open_carton_back(s, *carton)
    s.face([(-29, -22, 22), (29, -22, 22), (29, 22, 22), (-29, 22, 22)], EDGE,
           openings=([(x, y, 22) for x, y in oval(0, 0, 15, 15)[:-1]],))
    s.disk(0, 0, 22, 11, 11, 3)
    s.disk(0, 0, 25, 2.5, 2.5, 15)
    s.solid(oval(0, 0, 4, 4)[:-1], 39, 21, top=oval(0, 0, 14, 14)[:-1], crease=False)
    s.ring(0, 0, 60, 14, 14, 1.5, 1.25)
    s.ellipse(0, 0, 61.5, 11, 11, DETAIL, 15, 180)
    open_carton_front(s, *carton)
