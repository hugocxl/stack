from math import cos, pi, sin

from geometry import EDGE, oval
from scenes.redraws._w5 import desk_calendar, plane_mark

DESCRIPTION = "A standing travel calendar divides the year into quadrants marked by a flower, sun, leaf, and snowflake."


def draw(s):
    face = desk_calendar(s)
    plane_mark(s, face, 31, 47.3, .34)
    s.line([face(31, 4), face(31, 38)], EDGE)
    s.line([face(5, 21), face(57, 21)], EDGE)

    def mark(x, z, points):
        s.line([face(x + u, z + v) for u, v in points], EDGE)

    for i in range(6):
        a = i*pi/3
        mark(16, 30, oval(3*cos(a), 3*sin(a), 1.9, 1.9, count=15))
    mark(46, 30, oval(0, 0, 3.2, 3.2, count=24))
    for i in range(8):
        a = i*pi/4
        mark(46, 30, [(4.9*cos(a), 4.9*sin(a)), (7.2*cos(a), 7.2*sin(a))])
    mark(16, 11, [(-5, -4), (-6, 1), (-3, 4), (6, 6), (5, -1), (2, -5), (-5, -4)])
    mark(16, 11, [(-7, -6), (3, 3)])
    for i in range(6):
        a = i*pi/3
        u, v = cos(a), sin(a)
        mark(46, 11, [(0, 0), (7*u, 7*v)])
        mark(46, 11, [(4*u - 2*v, 4*v + 2*u), (5.2*u, 5.2*v), (4*u + 2*v, 4*v - 2*u)])
