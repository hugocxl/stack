from geometry import DETAIL, EDGE
from scenes.redraws._w1 import software_package
from scenes.systems_shapes import bezel

DESCRIPTION = "A taped parcel rests on a shelf inside the open door of a locker bank."


def draw(s):
    left, right, back, front, roof = -35, 35, -25, 11, 77
    # Line the recess and seat the parcel before adding the front frame.
    s.face([(left, back, 0), (right, back, 0), (right, back, roof), (left, back, roof)], DETAIL)
    s.face([(-30, back, 35), (1, back, 35), (1, front, 35), (-30, front, 35)], EDGE)
    s.face([(-30, back, 35), (-30, front, 35), (-30, front, 71), (-30, back, 71)], DETAIL)
    software_package(s, -14, -2, 35, .43, show_code=False)
    s.face([(left, back, roof), (right, back, roof), (right, front, roof), (left, front, roof)], EDGE)
    s.face([(right, back, 0), (right, front, 0), (right, front, roof), (right, back, roof)], EDGE)
    opening = [(-30, 35), (1, 35), (1, 71), (-30, 71)]
    frame = [(left, 0), (right, 0), (right, roof), (left, roof)]
    s.face([(x, front, z) for x, z in frame], EDGE,
           openings=([(x, front, z) for x, z in opening],))

    for x, z, w, h in ((-30, 5, 31, 25), (5, 5, 25, 20), (5, 28, 25, 20), (5, 51, 25, 20)):
        bezel(s, x, front, z, w, h, EDGE, 1.3)
        s.line([(x + w - 6, front, z + h * .42), (x + w - 6, front, z + h * .64)], DETAIL)

    s.face([(-30, front, 35), (-30, front, 71),
            (-34, front + 26, 71), (-34, front + 26, 35)], EDGE)
    s.line([(-33, front + 21, 50), (-33, front + 21, 56)], DETAIL)
