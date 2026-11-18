from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A load-testing press compresses a bowing specimen between two platens."


def draw(s):
    s.box(-41, -26, 0, 82, 49, 9, 4)
    for x in (-35, 29):
        s.box(x, -19, 9, 7, 8, 70, 2)
    s.box(-41, -23, 79, 82, 28, 9, 4)
    s.disk(0, -9, 52, 6, 6, 27, EDGE)
    s.box(-21, -21, 46, 42, 29, 6, 3)
    s.box(-21, -21, 9, 42, 29, 6, 3)
    s.tube([(-11, -6, 15), (-5, -6, 21), (4, -6, 27),
            (8, -6, 32), (6, -6, 38), (-3, -6, 46)], 4.2, BOLD)
    for z in (25, 31, 37):
        s.line([(31, -11, z), (35, -11, z)], DETAIL)
