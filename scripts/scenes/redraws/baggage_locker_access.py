from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import coin
from scenes.systems_shapes import bezel

DESCRIPTION = "A key projects from the lock of a vented luggage locker door."


def draw(s):
    s.box(0, 0, 0, 48, 33, 67, 2.5)
    bezel(s, 4, 33, 4, 40, 59, EDGE, 2)
    for z in (11, 17, 50, 56):
        bezel(s, 12, 33, z, 24, 2.5, DETAIL, 1.25)

    key_x, key_z = 13, 32
    coin(s, key_x, 35, key_z, 5, depth=2)
    bow = [(key_x, y, z) for y, z in oval(56, key_z, 9, 9, -160, 160, 44)]
    hole = [(key_x, y, z) for y, z in oval(56, key_z, 4.8, 4.8)[:-1]]
    s.face([(key_x, 35, bow[0][2]), *bow, (key_x, 35, bow[-1][2])],
           EDGE, openings=[hole])
