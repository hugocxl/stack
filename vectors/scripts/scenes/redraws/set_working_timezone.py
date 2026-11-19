from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import screen_point

DESCRIPTION = "A desktop globe has a clock badge over one side of its latitude and longitude grid."


def draw(s):
    s.disk(0, 0, 0, 18, 15, 4)
    s.box(-4, -4, 4, 8, 8, 13, 2)
    z, radius = 44, 29
    rim = oval(0, 0, radius * 1.22474487, radius * 1.06066017)
    s.face([screen_point(0, 0, z, u, v) for u, v in rim[:-1]], EDGE)
    parallels = ([(lat, lon) for lon in range(-135, 226, 3)] for lat in (-32, 0, 32))
    meridians = ([(lat, lon) for lat in range(-90, 91, 3)] for lon in (-15, 45, 105))
    for points in (*parallels, *meridians):
        visible = []
        for latitude, longitude in points:
            a, b = radians(latitude), radians(longitude)
            x, y, height = cos(a) * cos(b), cos(a) * sin(b), sin(a)
            if x + y + height > .15:
                visible.append((radius * x, radius * y, z + radius * height))
            else:
                s.line(visible, DETAIL)
                visible = []
        s.line(visible, DETAIL)
    badge(s, "clock", *screen_point(0, 0, z, 31, 15), 14)
