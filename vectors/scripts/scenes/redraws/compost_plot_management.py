from geometry import DETAIL, EDGE

DESCRIPTION = "An open slatted compost bin exposes a coarse mound of leaves and stems."


def draw(s):
    s.box(-28, -23, 0, 56, 46, 34, 2.2)
    s.face([(-30, -23, 34), (30, -23, 34), (30, -40, 61),
            (-30, -40, 61)], EDGE)
    s.face([(30, -23, 34), (30, -40, 61), (30, -42, 61),
            (30, -25, 34)], EDGE)
    for fraction in (.31, .64):
        y, z = -23 - 17*fraction, 34 + 27*fraction
        s.line([(-27, y, z), (27, y, z)], DETAIL)
    for x in (-28, 25):
        s.box(x, -23, 31, 3, 46, 5, 1)
    compost = [(-24, 15, 34), (-25, 3, 36), (-20, -7, 41),
               (-12, -8, 39), (-5, -12, 44), (4, -10, 42), (11, -13, 44),
               (20, -7, 40), (25, 5, 35), (24, 18, 34)]
    s.face(compost, EDGE)
    for x, y, z, width in ((-16, -3, 39, 10), (-8, 13, 36, 9),
                            (7, -4, 41, 11), (13, 11, 36, 8)):
        s.face([(x - width / 2, y + 2, z), (x - width / 3, y - 2, z + 2.4),
                (x + width / 2, y - 2, z + 2.7), (x + width / 3, y + 1, z + .4)], EDGE)
    s.line([(-10, -6, 41), (-14, -9, 45), (-20, -9, 48)], EDGE)
    s.line([(-14, -9, 45), (-14, -13, 46)], DETAIL)
    for z in (9, 17, 25):
        s.line([(-27, 23, z), (27, 23, z), (28, -22, z)], DETAIL)
    for x in (-22, 22):
        s.line([(x, 23, 3), (x, 23, 31)], EDGE)
    s.box(-29, 21, 31, 58, 4, 4, 1)
