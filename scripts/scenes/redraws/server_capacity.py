from geometry import DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "Two slotted servers occupy the upper bays of a rack above a visibly empty expansion bay."


def draw(s):
    left, right, back, front = -28, 28, -32, 0
    floor, ceiling = 4, 74
    s.face([(left, back, floor), (right, back, floor),
            (right, back, ceiling), (left, back, ceiling)], DETAIL)
    s.face([(left, back, floor), (left, front, floor),
            (left, front, ceiling), (left, back, ceiling)], DETAIL)

    for x in (-24, 24):
        s.line([(x, back, 15), (x, front, 15)], DETAIL)
    s.box(left, back, 0, 56, 32, 4, 1)
    for height in (30, 50):
        s.box(-24, -7, height, 48, 7, 17, 1.4)
        bezel(s, -18, 0, height + 5, 28, 6, EDGE, 1)
        for x in (15, 20):
            s.line([(x, 0, height + 8), (x + 1, 0, height + 8)], EDGE)

    s.face([(right, back, 0), (right, front, 0),
            (right, front, ceiling), (right, back, ceiling)], EDGE)
    for x in (left, right - 4):
        s.face([(x, front, 0), (x + 4, front, 0),
                (x + 4, front, ceiling), (x, front, ceiling)], EDGE)
    s.box(left, back, 71, 56, 32, 5, 1)
