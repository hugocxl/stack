from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "A surface inlet carries water between planted slopes into a sunken rain garden."


def tuft(s, x, y, z, size):
    for spread, depth, rise in ((-.76, -.28, .75), (.10, -.32, 1), (.78, .1, .64)):
        s.line([(x, y, z),
                (x + .3*spread*size, y + .2*depth*size, z + .63*rise*size),
                (x + spread*size, y + depth*size, z + rise*size),
                (x + .75*spread*size + 1.3, y + depth*size + 1.6, z + .49*rise*size),
                (x, y, z)], EDGE)


def draw(s):
    basin = oval(0, 0, 45, 30, 12, 325, 60)
    rim = [(-52, -35), (52, -35), (52, -18),
           *reversed(basin), (52, 6.2), (52, 35), (-52, 35)]
    s.face([(52, -35, 0), (52, 35, 0), (52, 35, 9), (52, 6.2, 9),
            (52, 6.2, 5), (52, -18, 5), (52, -18, 9), (52, -35, 9)], EDGE)
    s.face([(-52, 35, 0), (52, 35, 0), (52, 35, 9), (-52, 35, 9)])
    s.face([(x, y, 9) for x, y in rim])
    s.ellipse(0, 0, 3, 33, 20, DETAIL, start=7, end=331)
    s.line([(52, -18, 5), (40, -16, 5), (27, -10, 3)], EDGE)
    s.line([(52, 6, 5), (40, 3, 5), (29, -1, 3)], EDGE)
    for x, y, z, size in ((-23, -15, 5, 14), (0, -18, 4, 11), (-23, 9, 3, 15),
                          (13, 16, 4, 13)):
        tuft(s, x, y, z, size)
    for x, y in ((-9, 4), (5, 2)):
        s.line([(x - 5, y, 3), (x, y - 1, 3), (x + 6, y, 3)], DETAIL)
    arrow(s, [(47, -7, 5), (36, -7, 5), (27, -6, 3), (17, -5, 3)], EDGE, head=5)
