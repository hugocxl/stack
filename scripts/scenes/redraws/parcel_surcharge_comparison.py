from geometry import DETAIL, EDGE
from scenes.redraws._w1 import panel_coin
from scenes.systems_shapes import bezel

DESCRIPTION = "A standing parcel rate card compares a standard box with one coin and an oversized box with three coins."


def carton_mark(s, x, z, size):
    def line(points):
        s.line([(x + a * size, 0, z + b * size) for a, b in points], EDGE)

    line([(0, .24), (.53, 0), (1, .21), (1, .75), (.51, 1), (0, .77), (0, .24)])
    line([(0, .77), (.53, .52), (1, .75)])
    line([(.53, .52), (.53, 0)])
    line([(.25, .89), (.78, .64), (.78, .47)])


def draw(s):
    s.face([(-33, -6, 30), (33, -6, 30), (33, -23, 0), (-33, -23, 0)], EDGE)
    s.box(-39, -6, 0, 78, 6, 66, 3)
    bezel(s, -33, 0, 6, 66, 54, DETAIL, 2)
    s.line([(-33, 0, 34), (33, 0, 34)], DETAIL)
    s.line([(-5, 0, 6), (-5, 0, 60)], DETAIL)

    carton_mark(s, -27, 40, 15)
    carton_mark(s, -30, 9, 22)
    panel_coin(s, 4, 0, 47, 4.4)
    for x in (4, 15, 26):
        panel_coin(s, x, 0, 20, 4.4)
