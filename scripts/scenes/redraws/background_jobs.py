from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import upright_profile
from scenes.systems_shapes import bezel

DESCRIPTION = "Two meshing gears sit behind a monitor bezel with a moon badge on its corner."


def draw(s):
    s.box(-17, -20, 0, 34, 26, 4, 3)
    s.box(-5, -15, 4, 10, 9, 16, 2)
    s.box(-38, -10, 13, 76, 10, 54, 4)
    bezel(s, -33, 0, 18, 66, 44, EDGE, 3)
    for x, z, radius, phase in ((-15, 37, 15, 0), (10, 43, 11, 20)):
        outline = []
        for tooth in range(8):
            for step, scale in ((0, .8), (11, 1), (25, 1), (36, .8)):
                angle = radians(phase - tooth * 45 - step)
                outline.append((x + radius * scale * cos(angle), z + radius * scale * sin(angle)))
        upright_profile(s, outline, 0, 2, DETAIL)
        s.line([(a, 0, b) for a, b in oval(x, z, radius * .34, radius * .34)], EDGE)
    badge(s, "moon", 37, 0, 60, 14)
