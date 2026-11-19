from math import cos, radians, sin

from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A prescription bottle rests on the sill of an open pharmacy service hatch."


def prescription_bottle(s, x, y, z, scale=1):
    """Build a prescription bottle with a wraparound label and ribbed cap."""
    def disk(radius, elevation, height, ink=EDGE):
        s.disk(x, y, z + elevation*scale, radius*scale, radius*scale, height*scale, ink)

    disk(14, 0, 38)
    disk(12, 38, 4, DETAIL)
    disk(15, 42, 9)
    for lift in (10, 28):
        s.ellipse(x, y, z + lift*scale, 14*scale, 14*scale, DETAIL, -37, 127)
    for start in (13, 29, 45, 61, 77):
        a = x + 15*scale*cos(radians(start))
        b = y + 15*scale*sin(radians(start))
        s.line([(a, b, z + 43*scale), (a, b, z + 47.2*scale)], DETAIL)

    front = Surface(s, lambda u, v: (x + (.707*u + 9.8)*scale,
                                      y + (9.8 - .707*u)*scale, z + v*scale))
    medical_cross(front, 0, 19, 6.8)


def draw(s):
    back = Surface(s, lambda u, v: (u, 0, v))
    front = Surface(s, lambda u, v: (u, 14, v))
    outer = rounded(0, 0, 106, 94, 2)
    hole = rounded(13, 30, 80, 41, 1)
    for plane in (back, front):
        s.face([plane.at(u, v) for u, v in outer],
               openings=[[plane.at(u, v) for u, v in hole]])
    s.face([(0, 0, 94), (106, 0, 94), (106, 14, 94), (0, 14, 94)])
    s.face([(106, 0, 0), (106, 0, 94), (106, 14, 94), (106, 14, 0)])
    s.face([(13, 0, 30), (13, 14, 30), (13, 14, 71), (13, 0, 71)], DETAIL)
    front.line([(0, 25), (106, 25)], DETAIL)
    medical_cross(front, 53, 83, 8, EDGE)
    s.box(7, 9, 26, 92, 28, 5, 2)
    prescription_bottle(s, 69, 24, 31, .73)
