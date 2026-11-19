from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "A sheet of bubble wrap curves up inside an open shipping carton."


def draw(s):
    carton = (-35, 35, -25, 25, 26)
    open_carton_back(s, *carton)
    # The sheet rests on the packing floor and turns up against the rear wall.
    sections = [(19, 3), (5, 11), (-5, 23), (-11, 37), (-13, 53)]
    s.face([(-28, y, z) for y, z in sections] +
           [(27, y, z) for y, z in reversed(sections)], EDGE)

    for row, ((front, low), (back, high)) in enumerate(zip(sections, sections[1:])):
        def point(x, t, height):
            return x, front + (back - front) * t, low + (high - low) * t + height

        centers = (-21, -10, 1, 12, 23) if row % 2 == 0 else (-16, -5, 6, 17)
        for x in centers:
            s.line([point(a, t, 0) for a, t in oval(x, .50, 3.6, .28, count=24)], EDGE)
            s.line([point(a, t, 1.1) for a, t in oval(x - .4, .48, 2.05, .15, 55, 150, count=10)], DETAIL)
    open_carton_front(s, *carton)
