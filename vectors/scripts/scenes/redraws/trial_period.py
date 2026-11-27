from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A tall turned hourglass with sand settling in its lower bulb carries a play badge."

TOP = 112


def post(s, angle, r=24):
    x, y = r*cos(radians(angle)), r*sin(radians(angle))
    s.tube([(x, y, 7), (x, y, TOP)], 2, EDGE)


def draw(s):
    turned(s, [(29, 0), (29, 7)], steps=1)
    post(s, 225)
    turned(s, [(.5, 7), (15, 9), (18, 20), (16, 36), (6, 54), (2.4, 59.5), (6, 65), (16, 83), (18, 99), (15, 110), (.5, TOP)], steps=5)
    lip(s, 0, 0, 19, 17, DETAIL, -30, 120)
    s.line([(0, 0, 58), (0, 0, 21)], DETAIL)
    turned(s, [(29, TOP), (29, TOP + 7)], steps=1)
    post(s, 120)
    post(s, 330)
    badge(s, "play", *_screen(0, 0, 0, 38, 10), 13)
