from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "An open-front stock bin sits inside the outlined slot of a four-bay rack."


def stock_bin(s, x, z, y):
    # The sloped sidewalls reveal the bin's open mouth above the front lip.
    s.face([(x, -10, z), (x + 24, -10, z), (x + 24, -10, z + 17), (x, -10, z + 17)], DETAIL)
    s.face([(x, -10, z), (x + 24, -10, z), (x + 24, y, z), (x, y, z)], DETAIL)
    for side in (x, x + 24):
        s.face([(side, -10, z), (side, -10, z + 17), (side, y - 11, z + 17),
                (side, y, z + 7), (side, y, z)], EDGE)
    s.face([(x, y, z), (x + 24, y, z), (x + 24, y, z + 7), (x, y, z + 7)], EDGE)
    s.line([(x + 8, y, z + 3.5), (x + 16, y, z + 3.5)], DETAIL)


def draw(s):
    left, right, back, front, top = -38, 38, -17, 13, 61
    s.face([(left, back, 0), (right, back, 0), (right, back, top), (left, back, top)], DETAIL)
    for z in (4, 33):
        s.face([(left, back, z), (right, back, z), (right, front, z), (left, front, z)], DETAIL)
    for x in (-34, 3):
        s.face([(x, back, 4), (x, front, 4), (x, front, 57), (x, back, 57)], DETAIL)

    for x, z, y in ((-31, 4, 10), (7, 4, 10), (-31, 33, 12)):
        stock_bin(s, x, z, y)

    s.face([(left, back, top), (right, back, top), (right, front, top), (left, front, top)], EDGE)
    s.face([(right, back, 0), (right, front, 0), (right, front, top), (right, back, top)], EDGE)
    openings = []
    for x in (-34, 3):
        for z in (4, 33):
            openings.append([(x, front, z), (x + 31, front, z),
                             (x + 31, front, z + 24), (x, front, z + 24)])
    s.face([(left, front, 0), (right, front, 0), (right, front, top), (left, front, top)],
           EDGE, openings=openings)
    bezel(s, -35.5, front, 31.5, 34, 27, BOLD, 1.5)
