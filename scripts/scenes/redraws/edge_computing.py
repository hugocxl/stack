from geometry import DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A remote sensor housing has a side lens and a cutaway front that reveals its processor."


def draw(s):
    # A lens on the closed end identifies the housing as a sensor.
    s.face([(-35, -26, 0), (35, -26, 0), (35, -26, 54), (-35, -26, 54)], EDGE)
    s.face([(35, -26, 0), (35, 0, 0), (35, 0, 54), (35, -26, 54)], EDGE)
    for radius in (9, 5):
        s.line([(35, y, z) for y, z in oval(-13, 30, radius, radius, count=32)], EDGE)
    s.face([(-35, -26, 54), (35, -26, 54), (35, 0, 54), (-35, 0, 54)], EDGE)
    s.face([(-24, -12, 8), (24, -12, 8), (24, 0, 8), (-24, 0, 8)], DETAIL)

    bezel(s, -20, -7, 14, 30, 27, EDGE, 2)
    bezel(s, -15, -7, 19, 20, 17, DETAIL, 1)
    for x in (-15, -8, -1, 6):
        s.line([(x, -7, 10), (x, -7, 14)], EDGE)
        s.line([(x, -7, 41), (x, -7, 45)], EDGE)
    for z in (19, 28, 37):
        s.line([(-24, -7, z), (-20, -7, z)], EDGE)
        s.line([(10, -7, z), (15, -7, z)], EDGE)

    opening = [(-27, 0, 8), (25, 0, 8), (25, 0, 46), (-27, 0, 46)]
    front = [(-35, 0, 0), (35, 0, 0), (35, 0, 54), (-35, 0, 54)]
    s.face(front, EDGE, openings=[opening])
    s.disk(-22, -17, 54, 4, 4, 2, EDGE)
    s.tube([(-22, -17, 56), (-22, -17, 71)], 1.5, EDGE)
