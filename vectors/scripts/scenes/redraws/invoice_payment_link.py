from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._w5 import currency_mark, invoice, printed_stroke

DESCRIPTION = "Two interlocking links overlap an itemized invoice beside its total."


def draw(s):
    face = invoice(s)
    currency_mark(s, face, 15, 10, 5)
    printed_stroke(s, face, [(23, 10), (40, 10)], EDGE)

    def link(x, y, z, pitch, turn):
        c, t = cos(radians(turn)), sin(radians(turn))

        def point(u, v):
            along, across = c * u - t * v, t * u + c * v
            return (x + .75 * along + .42 * across,
                    y - .15 * along + pitch * across,
                    z + .74 * along - .6 * across)

        outer = rounded(-13.5, -6, 27, 12, 6)
        inner = rounded(-10.2, -3, 20.4, 6, 3)
        s.face([point(u, v) for u, v in outer], EDGE,
               openings=[[point(u, v) for u, v in inner]])

    link(51, 3, 3, .16, 8)
    link(63, .6, 14.8, -.3, -15)
