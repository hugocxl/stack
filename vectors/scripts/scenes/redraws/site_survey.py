from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import coin

DESCRIPTION = "A survey total station with an optical lens and sighting handle stands on its three telescoping tripod legs."


def draw(s):
    for x, y in ((-26, -17), (-21, 27), (31, 0)):
        s.tube([(x, y, 0), (.48 * x, .48 * y, 26)], 1.35, EDGE)
        s.tube([(.57 * x, .57 * y, 21), (.14 * x, .14 * y, 47)], 2.25, EDGE)
    s.disk(0, 0, 46, 11, 10, 4)
    s.disk(0, 0, 50, 7.5, 7.5, 5)
    s.box(-13, -8, 55, 26, 19, 6, 1.8)
    s.tube([(-12, -4, 75), (-12, -4, 87), (-7, -4, 92),
            (7, -4, 92), (12, -4, 87), (12, -4, 75)], 2.05, EDGE)
    s.box(-13, -8, 60, 6, 18, 23, 1.8)
    s.box(7, -8, 60, 6, 18, 23, 1.8)
    s.box(-8, -9, 63, 16, 18, 16, 2)
    coin(s, 0, 13, 71, 8, depth=4.5)
    s.line([(x, 13, z) for x, z in oval(0, 71, 5.2, 5.2)], DETAIL)
    s.face([(-9, 11, 60), (9, 11, 60), (9, 16, 54), (-9, 16, 54)], EDGE)
    s.line([(-5, 12, 58.8), (5, 12, 58.8), (5, 14.7, 55.6),
            (-5, 14.7, 55.6), (-5, 12, 58.8)], DETAIL)
