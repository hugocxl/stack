from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import pipe_section

DESCRIPTION = "A sprinkler head on a supply pipe sends out curved water jets and carries a Wi-Fi badge."


def draw(s):
    pipe_section(s, 0, 68, 17, 7, 5, bore=3)
    pipe_section(s, 27, 41, 17, 7, 7)
    s.disk(34, 17, 10, 4.5, 4.5, 15)
    s.disk(34, 17, 24, 9, 8, 5)
    s.tube([(38, 17, 27), (43, 17, 30), (47, 17, 30)], 2.4)
    for reach, lift, shift in ((48, 21, -15), (37, 13, -9)):
        points = []
        for i in range(21):
            t = i / 20
            points.append((47 + reach*t, 17 + shift*t, 30*(1-t) + 4*lift*t*(1-t)))
        s.line(points, EDGE if reach == 48 else DETAIL, dashed=reach != 48)
    badge(s, "wifi", 15, 20, 23, 10)
