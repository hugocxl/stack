from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import dashboard_chart, product_laptop

DESCRIPTION = "A desk spotlight casts a diagonal beam across an implemented chart in a laptop window."


def draw(s):
    screen = product_laptop(s)
    dashboard_chart(screen, 31, 15, 40, 29)
    for v in (22, 34):
        screen.rows(11, v, (13,))

    s.line([(-14, 7, 66), screen.at(64, 46)], DETAIL)
    s.line([(-8, 7, 53), screen.at(29, 14)], DETAIL)

    s.disk(-23, 15, 0, 11, 10, 4)
    s.tube([(-23, 15, 4), (-23, 15, 47), (-26, 10, 60), (-27, 4, 65)], 1.9)
    s.face([(-34, 4, 70), (-29, 4, 76), (-25, 4, 76), (-14, 7, 68),
            (-8, 7, 52), (-26, 4, 60), (-34, 4, 66)], EDGE)
    s.line([(-11 + .38*u, 7, 60 + v) for u, v in oval(0, 0, 5, 7, 0, 185)], EDGE)
