from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import bezier_path, upright

DESCRIPTION = "A lifted drape exposes the lens and controls of a compact camera."


def draw(s):
    rear_corner = (1, -12, 48)
    rear_flap = bezier_path((-6, 5, 11), ((-6, -12, 32), (-3, -15, 42), rear_corner))
    rear = bezier_path(rear_corner,
                       ((6, -14, 54), (12, -14, 56), (16, -13, 58)),
                       ((34, -12, 75), (49, -6, 68), (61, -3, 53)),
                       ((69, -2, 41), (69, 0, 23), (76, -3, 12)))
    s.face([*rear_flap[:-1], *rear, (63, 6, 9)], EDGE)
    s.box(0, 0, 0, 68, 31, 42, 5)
    s.box(11, 6, 42, 15, 12, 4, 2, DETAIL)
    upright(s, oval(37, 21, 16, 16)[:-1], 43, 13)
    s.line([(x, 43, z) for x, z in oval(37, 21, 11, 11)], EDGE)
    s.line([(x, 43, z) for x, z in oval(37, 21, 7.5, 7.5)], DETAIL)
    s.face([(7, 31, 31), (17, 31, 31), (17, 31, 36), (7, 31, 36)], DETAIL)

    hem = bezier_path((3, 9, 44), ((16, 16, 47), (25, 19, 51), (42, 24, 53)),
                      ((56, 27, 51), (59, 19, 41), (68, 15, 32)),
                      ((72, 10, 24), (79, 5, 15), (76, -3, 12)))
    s.face([*hem, *reversed(rear[:-1])])
    s.line([(27, -13, 61), (34, 0, 58), (42, 17, 55)], DETAIL)
    s.line([(59, -3, 53), (60, 7, 47), (64, 13, 37)], DETAIL)
