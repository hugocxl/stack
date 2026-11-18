from math import cos, radians, sin

from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A curved return arrow wraps around the lower right corner of a restored document."


def draw(s):
    ruled_file(s)
    path = [(45 + 14*cos(radians(a)), 2, 10 + 14*sin(radians(a)))
            for a in range(-142, 104, 7)]
    arrow(s, path, BOLD, head=7.6)
