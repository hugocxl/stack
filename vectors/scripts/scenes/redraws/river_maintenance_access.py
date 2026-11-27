from geometry import DETAIL, EDGE

DESCRIPTION = "A railed ramp runs from the top of a riverbank down to the water."


def draw(s):
    H = 30
    s.box(-70, -40, 0, 140, 34, H, 2)
    s.face([(-20, -6, H), (20, -6, H), (20, 60, 0), (-20, 60, 0)], EDGE)
    s.face([(20, -6, H), (20, -6, 0), (20, 60, 0)], EDGE)
    for x in (-18, 18):
        s.tube([(x, -6, H + 10), (x, 60, 10)], 1.4, EDGE)
        for t in (0, .5, 1):
            y, z = -6 + 66*t, H*(1 - t)
            s.tube([(x, y, z), (x, y, z + 10)], 1.2, EDGE)
    import math
    for y in (66, 76):
        s.line([(x, y + 2*math.sin(x/7), 0) for x in range(-70, 72, 3)], DETAIL)
