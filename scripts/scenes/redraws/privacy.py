from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import lens_outline, panel

DESCRIPTION = "A desktop webcam has a closed privacy shutter across the center of its circular lens."


def draw(s):
    s.box(17, -17, 0, 34, 25, 4, 5)
    s.tube([(34, -8, 4), (34, -8, 21)], 4, EDGE)
    face = lambda x, z: (x, 0, z)
    panel(s, rounded(0, 17, 68, 33, 13), face, 13)
    lens_outline(s, face, 32, 33, 12.8)
    lens_outline(s, face, 32, 33, 9.6, DETAIL)
    shutter = lambda x, z: (x, 1.2, z)
    panel(s, rounded(18.4, 26.2, 27.2, 13.6, 2.1), shutter, 1.2)
    for x in (28, 32, 36):
        s.line([shutter(x, 30.2), shutter(x, 35.8)], DETAIL)
    lens_outline(s, face, 55, 33, 1.35, DETAIL)
