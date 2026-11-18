from geometry import DETAIL, EDGE
from scenes.redraws._w1 import caliper

DESCRIPTION = "A caliper grips the outer edge of a machined bearing with a visible central bore."


def draw(s):
    s.disk(0, 0, 0, 21, 19, 7)
    s.ring(0, 0, 7, 21, 19, 14, wall=7, ink=EDGE)
    s.ellipse(0, 0, 21, 17.5, 16, DETAIL, 0, 360)
    caliper(s, -21, 21, 0, 35, 17)
