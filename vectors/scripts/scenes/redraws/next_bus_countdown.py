from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A city bus with a wide windshield and destination panel carries a clock badge."


def side_window(s, x, y, z, w, h):
    s.face([(a, y, b) for a, b in rounded(x, z, w, h, 1.8)], EDGE)


def windscreen(s, x, y, z, w, h):
    s.face([(x, a, b) for a, b in rounded(y, z, w, h, 2.7)], EDGE)


def wheel_side(s, x, y, r, *, center=None):
    center = r if center is None else center
    s.face([(a, y, b) for a, b in oval(x, center, r, r)[:-1]])
    s.line([(a, y, b) for a, b in oval(x, center, r * .38, r * .38)], DETAIL)


def draw(s):
    for x, y in ((-24, 7), (18, 7), (-24, 52), (18, 52)):
        wheel_side(s, x, y, 7)

    s.box(-35, 5, 8, 62, 50, 50, 5)
    for x in (-28, -10):
        side_window(s, x, 55, 31, 15, 15)
    side_window(s, 9, 55, 15, 13, 31)
    s.line([(15.5, 55.01, 15), (15.5, 55.01, 46)], DETAIL)

    windscreen(s, 27, 10, 25, 40, 20)
    windscreen(s, 26.99, 16, 49, 28, 5)
    for y in (14, 46):
        s.face([(27, a, b) for a, b in oval(y, 17, 4, 2.5)[:-1]])
    s.line([(27, 22, 15), (27, 38, 15)], DETAIL)
    s.line([(27, 31, 25), (27, 31, 45)], DETAIL)
    badge(s, "clock", 32, 4, 56, 13)
