from geometry import DETAIL, EDGE

DESCRIPTION = "A sloped ramp and continuous handrail meet the raised threshold of a residential doorway."


def draw(s):
    s.box(-27, -15, 0, 54, 15, 65, 1)
    s.face([(-17, .1, 11), (17, .1, 11), (17, .1, 54), (-17, .1, 54)], EDGE)
    s.line([(-12, .2, 13), (-12, .2, 49), (12, .2, 49), (12, .2, 13)], DETAIL)
    s.tube([(7, 1.1, 33), (11, 1.1, 33)], 1, EDGE)
    s.line([(-25, .15, 50), (-20, .15, 50)], DETAIL)
    s.line([(20, .15, 50), (25, .15, 50)], DETAIL)

    landing = [(-19, 0, 11), (19, 0, 11), (19, 13, 11), (-19, 13, 11)]
    s.face([(19, 0, 0), (19, 57, 0), (19, 13, 11), (19, 0, 11)])
    s.face(landing)
    s.face([(-19, 13, 11), (19, 13, 11), (19, 57, 0), (-19, 57, 0)])
    for y in (8, 27, 49):
        z = 11 if y <= 13 else 11*(57 - y)/44
        s.tube([(-18, y, z), (-18, y, z + 14)], 1.1)
    s.tube([(-18, 4, 25), (-18, 13, 25), (-18, 52, 15.25)], 1.5, EDGE)
