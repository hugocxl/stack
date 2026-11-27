from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import turned

DESCRIPTION = "A sprinkler head on a supply pipe throws two arcs of water and carries a Wi-Fi badge."


def draw(s):
    s.tube([(-70, 0, 4), (60, 0, 4)], 3.6, EDGE)
    turned(s, [(7, 4), (7, 16), (4, 18), (4, 26), (6, 28), (6, 32)], 0, 0, 0, steps=2)
    for sgn in (1, -1):
        s.line([(sgn*t*.7, -sgn*t*.7*.0 + t*.0, 32 + t*1.4 - t*t*.02) for t in range(0, 72, 3)], DETAIL, dashed=True)
    badge(s, "wifi", 40, -26, 52, 11)
