from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import screen_point

DESCRIPTION = "A desktop globe shows its latitude and longitude lines with a location pin over the grid."


def draw(s):
    s.disk(0, 0, 0, 18, 15, 4)
    s.box(-4, -4, 4, 8, 8, 13, 2)
    center = (0, 0, 44)
    radius = 29
    # The lengths of the projection's two screen axes define the apparent rim.
    rim = oval(0, 0, radius * 1.22474487, radius * 1.06066017)
    s.face([screen_point(*center, u, v) for u, v in rim[:-1]], EDGE)

    # Keep the near half of the spherical grid above the globe's silhouette.
    for points in (
        *[[(latitude, longitude) for longitude in range(-135, 226, 3)]
          for latitude in (-35, 0, 35)],
        *[[(latitude, longitude) for latitude in range(-90, 91, 3)]
          for longitude in (-21, 45, 111)],
    ):
        visible = []
        for latitude, longitude in points:
            a, b = radians(latitude), radians(longitude)
            x, y, z = cos(a) * cos(b), cos(a) * sin(b), sin(a)
            if x + y + z > .15:
                visible.append((radius * x, radius * y, center[2] + radius * z))
            elif visible:
                s.line(visible, DETAIL)
                visible = []
        if visible:
            s.line(visible, DETAIL)

    tip = (17, 2)
    head = oval(17, 20, 9, 9, 215, -35, 30)
    hole = oval(17, 20, 3.2, 3.2, count=24)[:-1]
    s.face([screen_point(*center, u, v) for u, v in [tip, *head]], EDGE,
           openings=[[screen_point(*center, u, v) for u, v in hole]])
