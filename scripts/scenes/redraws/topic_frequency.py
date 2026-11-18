from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A small receipt printer feeds out a tally with three topic rows and unequal bars."


def draw(s):
    s.box(0, 0, 0, 106, 45, 24, 5)
    s.line([(9, 23, 24), (97, 23, 24)], DETAIL)
    s.line([(9, 30, 24), (97, 30, 24)], EDGE)
    s.ellipse(94, 37, 24, 2.5, 2.5, DETAIL)

    def p(x, z):
        return x, 27 - .23*z, 24 + z

    edge = [(13, 0), (13, 64), (20, 68), (26, 64), (32, 68), (38, 64),
            (44, 68), (50, 64), (56, 68), (62, 64), (68, 68), (74, 64),
            (80, 68), (86, 64), (86, 0)]
    s.face([p(x, z) for x, z in edge], EDGE)
    for z, length in ((50, 44), (32, 22), (14, 32)):
        bubble = [(21, z + 4), (31, z + 4), (31, z - 3), (25, z - 3),
                  (22, z - 6), (22, z - 3), (21, z - 3), (21, z + 4)]
        s.line([p(x, v) for x, v in bubble], EDGE)
        s.face([p(36, z - 3), p(36 + length, z - 3), p(36 + length, z + 4),
                p(36, z + 4)], BOLD if length == 44 else EDGE)
