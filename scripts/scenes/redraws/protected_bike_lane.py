from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A bicycle pavement marking identifies the lane behind a raised curb that separates it from traffic."


def draw(s):
    s.box(-50, -33, 0, 100, 71, 5, 1.8)
    for x in (-42, -15, 12, 39):
        s.line([(x - 6, -16, 5), (x + 6, -16, 5)], DETAIL)
    s.box(-50, -3, 5, 100, 5, 5, 1)
    s.line([(-48, 35, 5), (48, 35, 5)], DETAIL)
    for x in (-21, 21):
        s.ellipse(x, 25, 5, 10.5, 10.5, EDGE)
    z = 5
    s.line([(-21, 25, z), (-12, 13, z), (8, 13, z), (-3, 25, z), (-21, 25, z)], BOLD)
    s.line([(-3, 25, z), (-14, 9, z)], EDGE)
    s.line([(-18, 9, z), (-10, 9, z)], EDGE)
    s.line([(21, 25, z), (10, 11, z), (10, 6, z), (16, 6, z)], BOLD)
    s.line([(8, 13, z), (11, 13, z)], EDGE)
