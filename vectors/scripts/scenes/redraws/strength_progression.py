from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._sf import plate, right_face

DESCRIPTION = "A dumbbell loaded with two plates a side carries an up badge for progression."

PLATES = ((16, 7), (12, 6))


def draw(s):
    s.tube([(-56, 0, 16), (56, 0, 16)], 2.8, EDGE)
    xs, x = [], -24
    for r, w in PLATES:
        xs.append((x, r, w))
        x -= w
    for x, r, w in reversed(xs):
        plate(s, right_face(x, 0, 16), oval(0, 0, r, r, count=48)[:-1], w, (-1, 0, 0))
    x = 24
    for r, w in PLATES:
        x += w
        plate(s, right_face(x, 0, 16), oval(0, 0, r, r, count=48)[:-1], w, (-1, 0, 0))
    badge(s, "up", 30, 0, 62, 13)
