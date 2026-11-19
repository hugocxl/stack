from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import screen_point

DESCRIPTION = "A reset arrow curls around the flared lip of a notification bell."


def draw(s):
    def point(u, v):
        return screen_point(0, 0, 35, u, v)

    s.face([point(u, v) for u, v in oval(0, 31, 5.5, 7, count=32)[:-1]], EDGE)
    s.face([point(u, v) for u, v in oval(0, -13, 6.5, 8, count=32)[:-1]], EDGE)
    bell = [(-30, -10), (-30, -6), (-24, -3), (-20, 3), (-18, 14),
            (-15, 21), (-11, 26), (-5, 29), (0, 30), (5, 29),
            (11, 26), (15, 21), (18, 14), (20, 3), (24, -3),
            (30, -6), (30, -10), (24, -12), (14, -14), (0, -15),
            (-14, -14), (-24, -12)]
    s.face([point(u + 4, v + 2.7) for u, v in bell], EDGE)
    s.face([point(u, v) for u, v in bell], EDGE)
    s.line([point(u, v) for u, v in ((-26, -6), (-17, -8), (0, -9),
                                    (17, -8), (26, -6))], DETAIL)
    path = oval(0, -10, 37, 17, 179, 363, 36)
    arrow(s, [point(u, v) for u, v in path], BOLD, head=9)
