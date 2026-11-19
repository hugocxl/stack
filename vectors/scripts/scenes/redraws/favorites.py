from math import cos, radians, sin

from geometry import BOLD
from scenes.redraws._w4 import upright

DESCRIPTION = "A five-point favorite star has one clean silhouette and a shallow side wall."


def draw(s):
    outline = []
    for i in range(10):
        a = radians(90 + 36*i)
        radius = 44 if i % 2 == 0 else 19
        outline.append((radius*cos(a), 42 + radius*sin(a)))
    upright(s, outline, 0, 8, BOLD, angle=-17)
