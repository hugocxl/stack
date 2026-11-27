from geometry import EDGE, oval
from scenes.redraws._sf import plate, right_face

DESCRIPTION = "An adjustable dumbbell holds plates of three sizes on each side of its grip."

PLATES = ((14, 6), (11, 5), (8, 4))


def draw(s):
    s.tube([(-60, 0, 14), (60, 0, 14)], 2.6, EDGE)
    # Left plates first (farther from the viewer), largest nearest the grip.
    xs, x = [], -26
    for r, w in PLATES:
        xs.append((x, r, w))
        x -= w
    for x, r, w in reversed(xs):
        plate(s, right_face(x, 0, 14), oval(0, 0, r, r, count=48)[:-1], w, (-1, 0, 0))
    x = 26
    for r, w in PLATES:
        x += w
        plate(s, right_face(x, 0, 14), oval(0, 0, r, r, count=48)[:-1], w, (-1, 0, 0))
